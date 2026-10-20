#!/usr/bin/env python3
"""Fail a pull request that removes or rewrites teaching text without approval.

Compares visible teaching items at the merge-base with main (base) to the
PR head. Each item is counted at its own location: kind, normalised text,
file, and locator. A lower count at a location is a removal there, even
when the same text still exists somewhere else. A move is only a matched
pair: the count falls at one location and rises by the same amount at
another location that did not already hold that copy. A removal and an
addition of the same kind are one change only when they are in the same
file and they share a location, or their text is at least 0.6 similar.
A cross-file match is a move only when the text is identical. Similar
text in two files stays a removal and an addition.

Approval lives in changes/<pr-number>.yml on a pull request, or
changes/<branch-name>.yml when git has no pull-request number. A removed
entry matches the file and the normalised text, and the locator when the
entry has one. A removal or a change with no entry fails, an entry that
matches nothing fails, and a missing file fails when anything was removed
or changed. Additions without an entry are warnings unless --strict-added.

Included copies (<!-- include:... -->) are not a second owned copy. The
source file owns that text. A hand copy that the head replaces with an
include is compared only to the multiset that section renders: the items
between its map-section start and end, at the hand-copy region that
include replaced. A line elsewhere in the source file does not cover the
including file. The same normalised text is kept when the source already
had it, or moved when a different file newly owns it (moved_from is the
hand copy, moved_to is source#section). It is not a removal. Unchanged
text that stays in the same file is kept when only its locator changes.

The books have to balance. At each location the base count equals kept
plus moved out plus removed plus the old side of a change. Across the
run, base items equal kept plus moved plus changed plus removed, and
head items equal kept plus moved plus changed plus added. A miss exits
non-zero with a reconciliation error that names the items. Nothing can
disappear without a row.
"""

import csv
import os
import re
import subprocess
import sys
from collections import Counter
from difflib import SequenceMatcher
from html.parser import HTMLParser
from pathlib import Path

from map_sections import DATA_PHASE, V_QUERY, extract_map_section

ROOT = Path(__file__).resolve().parents[1]
HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
    "meta", "source", "track", "wbr",
}
SKIP_TAGS = {"script", "style", "noscript", "svg", "template"}
BLOCK_TAGS = HEADING_TAGS | {
    "p", "div", "ul", "ol", "li", "table", "thead", "tbody", "tfoot", "tr",
    "section", "article", "aside", "header", "footer", "nav", "figure",
    "blockquote", "dl", "form", "fieldset",
}
LAST_UPDATE = re.compile(
    r"Last update\s*(?:·|\u00b7)\s*\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}\s+HKT"
)
MAP_SECTION = re.compile(r"\s*map-section:([A-Za-z0-9_-]+):(start|end)\s*$")
INCLUDE_TOKEN = re.compile(
    r"^[ \t]*<!-- include:(?P<file>[^#\s>]+)#(?P<id>[A-Za-z0-9_-]+):(?P<which>start|end)(?P<opts>.*?)-->[ \t]*$",
    re.M,
)
ACTIONS = ("removed", "changed", "added")
SIMILARITY = 0.6
DETAIL_STATUSES = ("moved", "changed", "removed", "added")


class Node:
    def __init__(self, tag, attrs):
        self.tag = tag
        self.attrs = attrs
        self.children = []
        self.parent = None
        self.map_section = ""
        self.heading_path = ""
        self.heading_id = ""


class Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("document", {})
        self.stack = [self.root]
        self.section_stack = []
        self.heading_stack = []
        self.current_heading_path = ""
        self.current_heading_id = ""

    def handle_starttag(self, tag, attrs):
        self._open(tag, attrs, tag in VOID_TAGS)

    def handle_startendtag(self, tag, attrs):
        self._open(tag, attrs, True)

    def _open(self, tag, attrs, void):
        node = Node(tag, dict(attrs))
        node.pos = self.getpos()
        node.map_section = self.section_stack[-1] if self.section_stack else ""
        node.heading_path = self.current_heading_path
        node.heading_id = self.current_heading_id
        parent = self.stack[-1]
        node.parent = parent
        parent.children.append(node)
        if tag == "br":
            parent.children.append(" ")
        if not void:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag != tag:
                continue
            node = self.stack[index]
            del self.stack[index:]
            if tag in HEADING_TAGS:
                self._close_heading(node)
            return

    def _close_heading(self, node):
        text = collapse(text_of(node, "heading"))
        level = int(node.tag[1])
        while self.heading_stack and self.heading_stack[-1][0] >= level:
            self.heading_stack.pop()
        heading_id = node.attrs.get("id", "")
        self.heading_stack.append((level, text, heading_id))
        self.current_heading_path = " / ".join(
            item[1] for item in self.heading_stack if item[1]
        )
        self.current_heading_id = ""
        for item in reversed(self.heading_stack):
            if item[2]:
                self.current_heading_id = item[2]
                break
        node.heading_path = self.current_heading_path
        node.heading_id = heading_id or self.current_heading_id

    def handle_data(self, data):
        self.stack[-1].children.append(data)

    def handle_comment(self, data):
        match = MAP_SECTION.match(data)
        if not match:
            return
        if match.group(2) == "start":
            self.section_stack.append(match.group(1))
        elif self.section_stack:
            self.section_stack.pop()


def collapse(text):
    return re.sub(r"\s+", " ", text).strip()


def normalise_key(text):
    """Whitespace, cache stamps, phase hooks, and generated stamps only.

    Hyphens, non-breaking hyphens, and capitals all stay, so they still
    count as different teaching text.
    """
    text = V_QUERY.sub("", text)
    text = DATA_PHASE.sub("", text)
    text = LAST_UPDATE.sub("", text)
    return collapse(text)


def class_set(node):
    return set(node.attrs.get("class", "").split())


def is_see_chip(classes):
    return "see" in classes or "see-also" in classes


def ancestor_has(node, predicate):
    current = node.parent
    while current is not None and current.tag != "document":
        if predicate(current):
            return True
        current = current.parent
    return False


def text_of(node, mode):
    """Visible text. Cites and see-chips stay their own items."""
    parts = []

    def walk(current, root):
        if isinstance(current, str):
            parts.append(current)
            return
        if current.tag in SKIP_TAGS:
            return
        if current.attrs.get("aria-hidden") == "true":
            return
        classes = class_set(current)
        if "sec-top" in classes or "chrome-last-update" in classes:
            return
        if not root and "cite" in classes and mode != "raw":
            return
        if not root and is_see_chip(classes) and mode not in {"raw", "see"}:
            return
        if not root and classes & {"spare-split", "spare-bit"} and mode != "raw":
            return
        if not root and mode == "li" and current.tag == "li":
            return
        if not root and mode == "cell" and current.tag == "table":
            return
        if not root and mode == "div" and current.tag in BLOCK_TAGS:
            return
        if current.tag == "br":
            parts.append(" ")
            return
        for child in current.children:
            if isinstance(child, Node) and parts and not parts[-1][-1:].isspace():
                parts.append(" ")
            walk(child, False)

    walk(node, True)
    return "".join(parts)


def locator(node):
    """Nearest id, else the section heading id, else data-section / map-section, else the heading path."""
    current = node
    while current is not None and current.tag != "document":
        if current.attrs.get("id"):
            return current.attrs["id"]
        current = current.parent
    if node.heading_id:
        return node.heading_id
    current = node
    while current is not None and current.tag != "document":
        section = current.attrs.get("data-section") or current.map_section
        if section:
            return "section:" + section
        current = current.parent
    return node.heading_path or ""


def link_target(href):
    href = V_QUERY.sub("", href or "")
    fragment = ""
    if "#" in href:
        href, fragment = href.split("#", 1)
    path = href.split("?", 1)[0]
    if fragment:
        return fragment
    return path


def link_label(node):
    return collapse(text_of(node, "raw"))


class Item:
    def __init__(self, kind, exact, key, file, locator, line=0):
        self.kind = kind
        self.exact = exact
        self.key = key
        self.file = file
        self.locator = locator
        self.line = line


def add_item(items, kind, raw, file, node):
    exact = collapse(LAST_UPDATE.sub("", raw))
    key = normalise_key(exact)
    if not key:
        return
    line = node.pos[0] if getattr(node, "pos", None) else 0
    items.append(Item(kind, exact, key, file, locator(node), line))


def extract_html(html, file):
    html = strip_include_bodies(html, file)
    builder = Builder()
    builder.feed(html)
    builder.close()
    items = []
    walk(builder.root, file, items)
    return items


def walk(node, file, items):
    if node.tag in SKIP_TAGS:
        return
    # Johnny 2026-10-15 20:46 J4. The pack disclaimer is chrome (SR §6.2),
    # not teaching. Its wording lives in chrome-packs.js.
    if node.tag == "aside" and node.attrs.get("id") == "pack-disclaimer":
        return
    if node.attrs.get("aria-hidden") == "true":
        return
    classes = class_set(node)
    if "sec-top" in classes or "chrome-last-update" in classes:
        return
    if node.attrs.get("aria-label"):
        add_item(items, "aria-label", node.attrs["aria-label"], file, node)
    if node.attrs.get("title"):
        add_item(items, "title", node.attrs["title"], file, node)
    if node.tag in HEADING_TAGS:
        add_item(items, "heading", text_of(node, "heading"), file, node)
    elif node.tag == "li":
        add_item(items, "li", text_of(node, "li"), file, node)
    elif node.tag in {"td", "th"}:
        add_item(items, "cell", text_of(node, "cell"), file, node)
    elif "cite" in classes and not ancestor_has(node, lambda n: "cite" in class_set(n)):
        add_item(items, "cite", text_of(node, "raw"), file, node)
    elif is_see_chip(classes) and not ancestor_has(node, lambda n: is_see_chip(class_set(n))):
        add_item(items, "see", text_of(node, "see"), file, node)
    elif node.tag == "p":
        add_item(items, "text", text_of(node, "p"), file, node)
    elif node.tag == "div":
        # Inline text only. Block children are their own items, so a layout
        # wrapper does not repeat the plate. The same run is taken outside a
        # plate as inside one, so a copy that is not wrapped in .plate is
        # still the same teaching item.
        add_item(items, "text", text_of(node, "div"), file, node)
    if node.tag == "a" and node.attrs.get("href"):
        label = link_label(node)
        target = link_target(node.attrs.get("href", ""))
        rendered = (label + " #" + target).strip() if target else label
        add_item(items, "link", rendered, file, node)
    for child in node.children:
        if isinstance(child, Node):
            walk(child, file, items)


def include_spans(html, origin):
    """Matched include bodies, outermost first in the returned list.

    Nesting is legal: the revaluation plate includes the during-use axis.
    Each tuple is (source name, section id, body start, body end, depth).
    """
    tokens = list(INCLUDE_TOKEN.finditer(html))
    if not tokens:
        return []
    stack = []
    spans = []
    for token in tokens:
        key = (token.group("file"), token.group("id"))
        if token.group("which") == "start":
            stack.append((key, token))
            continue
        if not stack or stack[-1][0] != key:
            raise SystemExit(
                f"{origin}: include end {key[0]}#{key[1]} does not match the open include"
            )
        start = stack.pop()[1]
        spans.append((
            key[0], key[1], start.end(), token.start(), len(stack),
        ))
    if stack:
        key = stack[-1][0]
        raise SystemExit(f"{origin}: missing end marker for include:{key[0]}#{key[1]}")
    return spans


def strip_include_bodies(html, origin):
    """Drop included copies, including an include nested inside another.

    The source file is parsed on its own. The outer body is skipped, so the
    inner copy is skipped with it.
    """
    spans = include_spans(html, origin)
    if not spans:
        return html
    parts = []
    cursor = 0
    for _name, _section, begin, end, _depth in sorted(spans, key=lambda item: item[2]):
        if begin < cursor:
            continue
        parts.append(html[cursor:begin])
        cursor = end
    parts.append(html[cursor:])
    return "".join(parts)


def resolve_include(including_file, name):
    return (Path(including_file).parent / name).as_posix()


def outermost_includes(files):
    """(including file, source file, section id) for includes that are not nested."""
    found = []
    for path in sorted(files):
        for name, section, _begin, _end, depth in include_spans(files[path], path):
            if depth != 0:
                continue
            found.append((path, resolve_include(path, name), section))
    return found


def section_items(files, source, section, seen):
    """Items the source section renders, with nested includes expanded."""
    if (source, section) in seen:
        return []
    seen.add((source, section))
    html = files.get(source, "")
    if not html:
        return []
    try:
        body = extract_map_section(html, section, source)
    except SystemExit:
        return []
    items = extract_html(body, source)
    for name, nested, _begin, _end, depth in include_spans(body, source):
        if depth != 0:
            continue
        items.extend(section_items(
            files, resolve_include(source, name), nested, seen,
        ))
    return items


class Books:
    """Where every compared item went. Reconciliation reads these lists."""

    def __init__(self):
        self.kept_base = []
        self.kept_head = []
        self.moved_out = []
        self.moved_in = []
        self.removed = []
        self.added = []
        self.changed_old = []
        self.changed_new = []


def clone_item(item):
    return Item(item.kind, item.exact, item.key, item.file, item.locator, item.line)


def describe_item(item):
    place_label = item.file + (" :: " + item.locator if item.locator else "")
    return f"{item.kind} {place_label}: {item.exact}"


def _marker_positions(html, name, section):
    needle = f"<!-- include:{name}#{section}:start -->"
    found = []
    start = 0
    while True:
        index = html.find(needle, start)
        if index < 0:
            return found
        found.append(index)
        start = index + len(needle)


def find_replaced_region(base_html, head_html, include_line):
    """Base line bounds (exclusive) of the hand copy this include replaced.

    `include_line` is the 1-based line of the include in `head_html`. Both
    strings are the include bodies already stripped, which is the same text
    `extract_html` numbers. The bounds are a unique line before the include
    and a unique line after it, each present once in both files. When the
    include is the whole file, the region is the whole base file. Otherwise
    a missing anchor means the spot is unknown and nothing is covered.
    """
    base_lines = base_html.splitlines()
    head_lines = head_html.splitlines()
    base_counts = Counter(base_lines)
    head_counts = Counter(head_lines)
    base_at = {}
    for number, line in enumerate(base_lines, 1):
        if base_counts[line] == 1:
            base_at[line] = number

    def unique_base_line(line):
        if not line.strip():
            return None
        if head_counts[line] != 1 or base_counts.get(line) != 1:
            return None
        return base_at.get(line)

    before = None
    saw_before = False
    for number in range(include_line - 1, 0, -1):
        line = head_lines[number - 1]
        if not line.strip():
            continue
        saw_before = True
        found = unique_base_line(line)
        if found is not None:
            before = found
            break

    after = None
    saw_after = False
    for number in range(include_line + 1, len(head_lines) + 1):
        line = head_lines[number - 1]
        if not line.strip():
            continue
        saw_after = True
        found = unique_base_line(line)
        if found is not None:
            after = found
            break

    if before is None and after is None and not saw_before and not saw_after:
        return (0, len(base_lines) + 1)
    if before is None or after is None or before >= after:
        return None
    return (before, after)


def _strip_cache(files):
    return {path: strip_include_bodies(html, path) for path, html in files.items()}


def _new_include_refs(base_files, head_files):
    """Outermost includes present in head and absent from base, in file order."""
    base_left = Counter(outermost_includes(base_files))
    found = []
    for path in sorted(head_files):
        for name, section, _begin, _end, depth in include_spans(head_files[path], path):
            if depth != 0:
                continue
            key = (path, resolve_include(path, name), section)
            if base_left[key] > 0:
                base_left[key] -= 1
                continue
            found.append((path, key[1], section, name))
    return found


def extract_tree(files):
    items = []
    for path in sorted(files):
        items.extend(extract_html(files[path], path))
    return items


class Row:
    def __init__(self, status, kind, file, locator, old, new, old_key, new_key):
        self.status = status
        self.kind = kind
        self.file = file
        self.locator = locator
        self.old = old
        self.new = new
        self.old_key = old_key
        self.new_key = new_key
        self.source = ""
        self.approved = False
        self.moved_from = ""
        self.moved_to = ""
        self.base_item = None
        self.head_item = None
        self.old_file = file
        self.old_locator = locator


def place(file, locator):
    if locator:
        return file + " :: " + locator
    return file


def location_groups(items):
    groups = {}
    for item in items:
        key = (item.kind, item.key, item.file, item.locator)
        groups.setdefault(key, []).append(item)
    return groups


def diff_items(base_items, head_items, base_files=None, head_files=None):
    """Per-location multiset. A surviving copy in another file is not a keep.

    A new include absorbs a hand copy only when that copy sits in the region
    the include replaced and the section renders the same text. Unchanged
    text that only gained a map-section locator in the same file stays kept.
    Anything left over is still a removal. Every base and head item is kept,
    moved, changed, removed, or added; `books` is that accounting.
    """
    books = Books()
    base_groups = location_groups(base_items)
    head_groups = location_groups(head_items)
    down = []
    up = []
    for key in sorted(set(base_groups) | set(head_groups)):
        base = base_groups.get(key, [])
        head = head_groups.get(key, [])
        matched = min(len(base), len(head))
        books.kept_base.extend(base[:matched])
        books.kept_head.extend(head[:matched])
        if len(base) > matched:
            down.extend(base[matched:])
        elif len(head) > matched:
            up.extend(head[matched:])
    injections = []
    include_moved = []
    if base_files is not None and head_files is not None:
        down, up, include_moved = absorb_new_includes(
            down, up, base_files, head_files, base_items, head_items,
            books, injections,
        )
    same_base, same_head, down, up = pair_same_file(down, up)
    books.kept_base.extend(same_base)
    books.kept_head.extend(same_head)
    moved, removed, added = pair_moves(down, up)
    moved = include_moved + moved
    changed = pair_changes(removed, added)
    for row in moved:
        books.moved_out.append(row.base_item)
        books.moved_in.append(row.head_item)
    for row in changed:
        books.changed_old.append(row.base_item)
        books.changed_new.append(row.head_item)
    for row in removed:
        books.removed.append(row.base_item)
    for row in added:
        books.added.append(row.head_item)
    rows = moved + changed + removed + added
    head_cmp = list(head_items) + injections
    counts = {
        "kept": len(books.kept_base),
        "moved": len(moved),
        "changed": len(changed),
        "removed": len(removed),
        "added": len(added),
        "base": len(base_items),
        "head": len(head_cmp),
    }
    return rows, counts, books, head_cmp


def _discard(pool, target):
    for index, item in enumerate(pool):
        if item is target:
            del pool[index]
            return True
    return False


def absorb_new_includes(down, up, base_files, head_files, base_items, head_items, books, injections):
    """Match a disappeared hand copy to the section a new include renders.

    Coverage is that section's multiset, at the replaced region only. The
    rest of the source file does not cover the including file. A wording
    change the source itself lost is kept on the hand copy (no second row)
    only inside that same region, and only up to the number the source lost.
    """
    base_counts = Counter((item.kind, item.key, item.file) for item in base_items)
    head_counts = Counter((item.kind, item.key, item.file) for item in head_items)
    drop_left = Counter()
    gain_left = Counter()
    for key, count in base_counts.items():
        lost = count - head_counts.get(key, 0)
        if lost > 0:
            drop_left[key] = lost
    for key, count in head_counts.items():
        extra = count - base_counts.get(key, 0)
        if extra > 0:
            gain_left[key] = extra
    stripped_base = _strip_cache(base_files)
    stripped_head = _strip_cache(head_files)
    occurrence = Counter()
    claimed = set()
    moved = []
    for including, source, section, name in _new_include_refs(base_files, head_files):
        head_html = stripped_head.get(including, "")
        positions = _marker_positions(head_html, name, section)
        slot = occurrence[(including, name, section)]
        occurrence[(including, name, section)] += 1
        if slot >= len(positions):
            continue
        include_line = head_html.count("\n", 0, positions[slot]) + 1
        region = find_replaced_region(
            stripped_base.get(including, ""), head_html, include_line,
        )
        if region is None:
            continue
        lo, hi = region
        render_left = Counter(
            (item.kind, item.key)
            for item in section_items(head_files, source, section, set())
        )
        region_items = [
            item for item in down
            if id(item) not in claimed
            and item.file == including
            and lo < item.line < hi
        ]
        for item in region_items:
            render_key = (item.kind, item.key)
            if render_left.get(render_key, 0) <= 0:
                continue
            source_key = (item.kind, item.key, source)
            # A locator change on the source does not raise its count, so it
            # is not a move. Only a copy the source file did not already hold.
            gained = [
                other for other in up
                if other.file == source
                and other.kind == item.kind
                and other.key == item.key
            ]
            if source != item.file and gain_left.get(source_key, 0) > 0 and gained:
                dest = gained[0]
                _discard(up, dest)
                gain_left[source_key] -= 1
                render_left[render_key] -= 1
                claimed.add(id(item))
                row = Row(
                    "moved", item.kind, source, "section:" + section,
                    item.exact, item.exact, item.key, item.key,
                )
                row.moved_from = place(item.file, item.locator)
                row.moved_to = source + "#" + section
                row.base_item = item
                row.head_item = dest
                moved.append(row)
                continue
            render_left[render_key] -= 1
            claimed.add(id(item))
            _keep_counterpart(item, books, injections)
        for item in region_items:
            if id(item) in claimed or item.file == source:
                continue
            source_key = (item.kind, item.key, source)
            if drop_left.get(source_key, 0) <= 0:
                continue
            drop_left[source_key] -= 1
            claimed.add(id(item))
            _keep_counterpart(item, books, injections)
    rest = [item for item in down if id(item) not in claimed]
    return rest, up, moved


def _keep_counterpart(item, books, injections):
    """The include still shows this hand copy, so both sides of the books keep it."""
    counterpart = clone_item(item)
    injections.append(counterpart)
    books.kept_base.append(item)
    books.kept_head.append(counterpart)


def pair_same_file(down, up):
    """Unchanged text that stays in one file is kept when only the locator changes."""
    down_by = {}
    up_by = {}
    for item in down:
        down_by.setdefault((item.kind, item.key, item.file), []).append(item)
    for item in up:
        up_by.setdefault((item.kind, item.key, item.file), []).append(item)
    kept_base = []
    kept_head = []
    rest_down = []
    rest_up = []
    for key in sorted(set(down_by) | set(up_by)):
        sources = down_by.get(key, [])
        dests = up_by.get(key, [])
        pair_count = min(len(sources), len(dests))
        kept_base.extend(sources[:pair_count])
        kept_head.extend(dests[:pair_count])
        rest_down.extend(sources[pair_count:])
        rest_up.extend(dests[pair_count:])
    return kept_base, kept_head, rest_down, rest_up


def pair_moves(down, up):
    """Pair a decrease with an increase of the same text. A copy already in base does not increase, so it is not a move."""
    down_by = {}
    up_by = {}
    for item in down:
        down_by.setdefault((item.kind, item.key), []).append(item)
    for item in up:
        up_by.setdefault((item.kind, item.key), []).append(item)
    moved = []
    removed = []
    added = []
    for key in sorted(set(down_by) | set(up_by)):
        sources = down_by.get(key, [])
        dests = up_by.get(key, [])
        pair_count = min(len(sources), len(dests))
        kind, norm = key
        for index in range(pair_count):
            src = sources[index]
            dst = dests[index]
            row = Row(
                "moved", kind, dst.file, dst.locator,
                src.exact, dst.exact, norm, norm,
            )
            row.moved_from = place(src.file, src.locator)
            row.moved_to = place(dst.file, dst.locator)
            row.base_item = src
            row.head_item = dst
            moved.append(row)
        for item in sources[pair_count:]:
            row = Row(
                "removed", kind, item.file, item.locator,
                item.exact, "", norm, "",
            )
            row.base_item = item
            removed.append(row)
        for item in dests[pair_count:]:
            row = Row(
                "added", kind, item.file, item.locator,
                "", item.exact, "", norm,
            )
            row.head_item = item
            added.append(row)
    return moved, removed, added


def pair_changes(removed, added):
    """Pair a removal with an addition only inside one file.

    Cross-file text is a move when it is identical (see pair_moves) and
    stays removed plus added when it merely looks similar. PR 110 paired
    the abbreviations SOC cell with the chapter 4 OCI cell because the
    similarity test ignored the file.
    """
    candidates = []
    for i, old in enumerate(removed):
        for j, new in enumerate(added):
            if old.kind != new.kind or old.file != new.file:
                continue
            same = bool(old.locator) and old.locator == new.locator
            ratio = SequenceMatcher(None, old.old_key, new.new_key, autojunk=False).ratio()
            if same or ratio >= SIMILARITY:
                candidates.append((ratio, 1 if same else 0, i, j))
    candidates.sort(reverse=True)
    used_old = set()
    used_new = set()
    pairs = []
    for _ratio, _same, i, j in candidates:
        if i in used_old or j in used_new:
            continue
        used_old.add(i)
        used_new.add(j)
        pairs.append((i, j))
    return _rebuild_pairs(removed, added, pairs)


def _rebuild_pairs(removed, added, pairs):
    """Turn pair indexes into changed rows and drop those items from the lists.

    `pairs` indexes refer to the lists as they were before any pop. Apply
    from the highest index so each pop leaves the other indexes in `pairs`
    untouched — but the two lists have independent indexes, so pop each
    list on its own descending pass.
    """
    changed = []
    for i, j in pairs:
        old = removed[i]
        new = added[j]
        locator = old.locator if old.locator and old.locator == new.locator else (
            new.locator or old.locator
        )
        row = Row(
            "changed", old.kind, new.file or old.file, locator,
            old.old, new.new, old.old_key, new.new_key,
        )
        row.base_item = old.base_item
        row.head_item = new.head_item
        if old.base_item is not None:
            row.old_file = old.base_item.file
            row.old_locator = old.base_item.locator
        changed.append(row)
    for i in sorted({i for i, _j in pairs}, reverse=True):
        removed.pop(i)
    for j in sorted({j for _i, j in pairs}, reverse=True):
        added.pop(j)
    return changed


def parse_changes(text):
    entries = []
    current = None
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            index += 1
            continue
        if line.startswith("- "):
            if current is not None:
                entries.append(current)
            current = {}
            index = _store_field(current, line[2:], lines, index)
            continue
        if current is not None and (line.startswith(" ") or line.startswith("\t")):
            index = _store_field(current, stripped, lines, index)
            continue
        raise SystemExit(f"cannot parse changes YAML at line {index + 1}: {line}")
    if current is not None:
        entries.append(current)
    for entry in entries:
        entry.setdefault("action", "")
        entry.setdefault("file", "")
        entry.setdefault("old", "")
        entry.setdefault("new", "")
        entry.setdefault("source", "")
        entry["matched"] = False
    return entries


def _store_field(entry, text, lines, index):
    if ":" not in text:
        raise SystemExit(f"cannot parse changes YAML at line {index + 1}: {text}")
    key, _, raw = text.partition(":")
    key = key.strip()
    raw = raw.strip()
    if raw in {"|", ">", "|-", ">-", "|+", ">+"}:
        value, index = _read_block(lines, index, raw.startswith(">"))
    else:
        value = _parse_scalar(raw)
    entry[key] = value
    return index + 1


def _read_block(lines, index, folded):
    block = []
    indent = None
    index += 1
    while index < len(lines):
        line = lines[index]
        if line.strip() == "":
            block.append("")
            index += 1
            continue
        spaces = len(line) - len(line.lstrip(" "))
        if spaces == 0:
            break
        if indent is None:
            indent = spaces
        if spaces < indent:
            break
        block.append(line[indent:])
        index += 1
    body = "\n".join(block).strip("\n")
    if folded:
        body = collapse(body)
    return body, index - 1


def _parse_scalar(raw):
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in {'"', "'"}:
        quote = raw[0]
        inner = raw[1:-1]
        if quote == "'":
            return inner.replace("''", "'")
        return _unescape(inner)
    return raw


def _unescape(text):
    out = []
    index = 0
    while index < len(text):
        if text[index] == "\\" and index + 1 < len(text):
            code = text[index + 1]
            out.append({"n": "\n", "t": "\t", '"': '"', "\\": "\\"}.get(code, code))
            index += 2
            continue
        out.append(text[index])
        index += 1
    return "".join(out)


def yaml_quote(text):
    escaped = (
        text.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
    )
    return '"' + escaped + '"'


def dump_changes(rows):
    lines = []
    wanted = [row for row in rows if row.status in {"changed", "removed", "added"}]
    for row in wanted:
        lines.append("- action: " + row.status)
        lines.append("  file: " + yaml_quote(row.file))
        if row.locator:
            lines.append("  locator: " + yaml_quote(row.locator))
        if row.status in {"removed", "changed"}:
            lines.append("  old: " + yaml_quote(row.old))
        if row.status in {"changed", "added"}:
            lines.append("  new: " + yaml_quote(row.new))
        lines.append('  source: "TODO"')
    return "\n".join(lines) + ("\n" if lines else "")


def _side_locator(row, action):
    """Locator of the old item, or of the new item, on a tool-paired change."""
    if action == "removed":
        if row.base_item is not None:
            return row.base_item.locator or ""
        return row.old_locator or ""
    if row.head_item is not None:
        return row.head_item.locator or ""
    return row.locator or ""


def _entry_matches_changed_side(entry, row, action):
    """True when a yml half names this changed row's old or new side.

    Same file. Same locator only when the entry gives one, compared to that
    side's own locator. Pairing is not consulted again.
    """
    if entry.get("action") != action or entry.get("file", "") != row.file:
        return False
    wanted = (entry.get("locator") or "").strip()
    if wanted and wanted != _side_locator(row, action):
        return False
    if action == "removed":
        return normalise_key(entry.get("old", "")) == row.old_key
    return normalise_key(entry.get("new", "")) == row.new_key


def split_explicit_pairs(rows, entries, books, counts):
    """Unpair a tool-paired change when the YAML names both halves.

    A changed row becomes one removed row and one added row only when one
    removed entry matches the old side and one added entry matches the new
    side. A lone half stays changed. Each new row is approved later by its
    own entry. Books move with the items so the balance is unchanged.
    """
    if not entries:
        return rows
    used = set()
    out = []
    for row in rows:
        if row.status != "changed" or row.base_item is None or row.head_item is None:
            out.append(row)
            continue
        removed_at = None
        added_at = None
        for index, entry in enumerate(entries):
            if index in used:
                continue
            if removed_at is None and _entry_matches_changed_side(entry, row, "removed"):
                removed_at = index
                continue
            if added_at is None and _entry_matches_changed_side(entry, row, "added"):
                added_at = index
        if removed_at is None or added_at is None:
            out.append(row)
            continue
        if not _discard(books.changed_old, row.base_item):
            out.append(row)
            continue
        if not _discard(books.changed_new, row.head_item):
            books.changed_old.append(row.base_item)
            out.append(row)
            continue
        used.add(removed_at)
        used.add(added_at)
        old_row = Row(
            "removed", row.kind, row.file, _side_locator(row, "removed"),
            row.old, "", row.old_key, "",
        )
        old_row.base_item = row.base_item
        old_row.old_file = row.old_file
        old_row.old_locator = row.old_locator
        new_row = Row(
            "added", row.kind, row.file, _side_locator(row, "added"),
            "", row.new, "", row.new_key,
        )
        new_row.head_item = row.head_item
        books.removed.append(row.base_item)
        books.added.append(row.head_item)
        counts["changed"] -= 1
        counts["removed"] += 1
        counts["added"] += 1
        out.append(old_row)
        out.append(new_row)
    return out


def match_entries(rows, entries):
    if not entries:
        return
    for entry in entries:
        action = entry.get("action", "")
        if action not in ACTIONS:
            continue
        old_key = normalise_key(entry.get("old", ""))
        new_key = normalise_key(entry.get("new", ""))
        file_name = entry.get("file", "")
        source = (entry.get("source") or "").strip()
        wanted_locator = (entry.get("locator") or "").strip()
        for row in rows:
            if row.approved or row.status != action:
                continue
            if row.file != file_name:
                continue
            if wanted_locator and row.locator != wanted_locator:
                continue
            if action == "removed" and row.old_key == old_key:
                _take(row, entry, source)
                break
            if action == "added" and row.new_key == new_key:
                _take(row, entry, source)
                break
            if action == "changed" and row.old_key == old_key and row.new_key == new_key:
                _take(row, entry, source)
                break


def _take(row, entry, source):
    entry["matched"] = True
    if source:
        row.approved = True
        row.source = source
    else:
        row.source = ""


def problems(rows, entries, approval_missing, strict_added):
    issues = []
    removals = [row for row in rows if row.status == "removed"]
    changes = [row for row in rows if row.status == "changed"]
    additions = [row for row in rows if row.status == "added"]
    if approval_missing and (removals or changes):
        issues.append(
            "approval YAML is missing and this diff removes or changes teaching text"
        )
    for row in removals + changes:
        if not row.approved:
            issues.append(
                f"UNAPPROVED {row.status}: {row.file}: {row.old}"
                + (f" → {row.new}" if row.new else "")
            )
    if strict_added:
        for row in additions:
            if not row.approved:
                issues.append(f"UNAPPROVED added: {row.file}: {row.new}")
    for entry in entries or []:
        source = (entry.get("source") or "").strip()
        action = entry.get("action", "")
        if not source:
            issues.append(
                f"empty source on {action or 'entry'} {entry.get('file', '')}"
            )
        if action not in ACTIONS:
            issues.append(f"bad action {action!r} in {entry.get('file', '')}")
            continue
        if not entry.get("matched"):
            shown = entry.get("old") or entry.get("new") or ""
            issues.append(
                f"stale approval matches nothing: {action} {entry.get('file', '')}: {shown}"
            )
    return issues


def _location_key(item):
    return (item.kind, item.key, item.file, item.locator)


def _tally(items):
    counts = Counter()
    for item in items:
        if item is None:
            continue
        counts[_location_key(item)] += 1
    return counts


def _unaccounted(items, *groups):
    """Items in `items` that no group claimed, by identity."""
    claimed = set()
    for group in groups:
        for item in group:
            if item is not None:
                claimed.add(id(item))
    return [item for item in items if id(item) not in claimed]


def reconciliation_errors(base_items, head_items, books):
    """Fail when an item vanishes or the location books do not add up.

    For every base location, count = kept + moved_out + removed + changed
    (old side). Across the run, base items = kept + moved + changed +
    removed, and head items = kept + moved + changed + added.
    """
    issues = []
    issues.extend(_location_errors(
        "base", base_items,
        (("kept", books.kept_base), ("moved_out", books.moved_out),
         ("removed", books.removed), ("changed", books.changed_old)),
    ))
    issues.extend(_location_errors(
        "head", head_items,
        (("kept", books.kept_head), ("moved_in", books.moved_in),
         ("added", books.added), ("changed", books.changed_new)),
    ))
    kept = len(books.kept_base)
    moved = len(books.moved_out)
    changed = len(books.changed_old)
    removed = len(books.removed)
    added = len(books.added)
    if (
        len(books.kept_head) != kept
        or len(books.moved_in) != moved
        or len(books.changed_new) != changed
    ):
        issues.append(
            "reconciliation error: pair counts differ "
            f"(kept {kept}/{len(books.kept_head)}, "
            f"moved {moved}/{len(books.moved_in)}, "
            f"changed {changed}/{len(books.changed_new)})"
        )
    base_sum = kept + moved + changed + removed
    if len(base_items) != base_sum:
        missing = _unaccounted(
            base_items, books.kept_base, books.moved_out,
            books.removed, books.changed_old,
        )
        issues.append(_equation_error(
            "base", len(base_items), kept, moved, changed, removed, "removed", missing,
        ))
    head_sum = len(books.kept_head) + len(books.moved_in) + len(books.changed_new) + added
    if len(head_items) != head_sum:
        missing = _unaccounted(
            head_items, books.kept_head, books.moved_in,
            books.added, books.changed_new,
        )
        issues.append(_equation_error(
            "head", len(head_items), len(books.kept_head), len(books.moved_in),
            len(books.changed_new), added, "added", missing,
        ))
    return issues


def _location_errors(side, items, parts):
    actual = _tally(items)
    tallies = [(name, _tally(group)) for name, group in parts]
    samples = {}
    for item in items:
        samples.setdefault(_location_key(item), item)
    for _name, group in parts:
        for item in group:
            if item is not None:
                samples.setdefault(_location_key(item), item)
    keys = set(actual)
    for _name, tally in tallies:
        keys.update(tally)
    issues = []
    for key in sorted(keys):
        have = actual.get(key, 0)
        got = sum(tally.get(key, 0) for _name, tally in tallies)
        if have == got:
            continue
        item = samples.get(key)
        label = describe_item(item) if item is not None else " ".join(str(part) for part in key)
        detail = ", ".join(
            f"{name} {tally.get(key, 0)}" for name, tally in tallies
        )
        issues.append(
            f"reconciliation error: {side} {label} count {have} != {detail}"
        )
    return issues


def _equation_error(side, have, kept, moved, changed, tail, tail_name, missing):
    message = (
        f"reconciliation error: {side} items {have} != "
        f"kept {kept} + moved {moved} + changed {changed} + {tail_name} {tail}"
    )
    if missing:
        message += ": " + "; ".join(describe_item(item) for item in missing[:30])
    return message


def evaluate(base_files, head_files, approval=None, strict_added=False):
    """approval is None when the YAML file is absent, otherwise its text."""
    base_items = extract_tree(base_files)
    head_items = extract_tree(head_files)
    rows, counts, books, head_cmp = diff_items(
        base_items, head_items, base_files, head_files,
    )
    entries = None
    missing = approval is None
    if not missing:
        entries = parse_changes(approval)
        rows = split_explicit_pairs(rows, entries, books, counts)
        match_entries(rows, entries)
    issues = problems(rows, entries, missing, strict_added)
    issues.extend(reconciliation_errors(base_items, head_cmp, books))
    return (1 if issues else 0), rows, counts, issues


def escape_cell(text):
    return (text or "").replace("|", "\\|").replace("\n", " ")


def source_cell(row):
    if row.status == "moved":
        return "—"
    if row.approved and row.source:
        return "approved: " + row.source
    return "UNAPPROVED"


def format_markdown(counts, rows):
    lines = [
        "## Incremental teaching diff",
        "",
        "| status | count |",
        "| --- | --- |",
    ]
    for status in ("kept", "moved", "changed", "removed", "added"):
        lines.append(f"| {status} | {counts[status]} |")
    lines.append("")
    detail = [row for row in rows if row.status in DETAIL_STATUSES]
    if not detail:
        lines.append("No moved, changed, removed, or added teaching items.")
        lines.append("")
        return "\n".join(lines)
    lines.extend([
        "| status | kind | file | locator | old | new | approval | moved_from | moved_to |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ])
    order = {name: index for index, name in enumerate(DETAIL_STATUSES)}
    detail.sort(key=lambda row: (order[row.status], row.file, row.locator, row.old, row.new))
    for row in detail:
        lines.append("| " + " | ".join([
            escape_cell(row.status),
            escape_cell(row.kind),
            escape_cell(row.file),
            escape_cell(row.locator),
            escape_cell(row.old),
            escape_cell(row.new),
            escape_cell(source_cell(row)),
            escape_cell(row.moved_from),
            escape_cell(row.moved_to),
        ]) + " |")
    lines.append("")
    warns = [row for row in detail if row.status == "added" and not row.approved]
    if warns:
        lines.append(
            f"{len(warns)} added item(s) have no approval entry (warning only, unless --strict-added)."
        )
        lines.append("")
    return "\n".join(lines)


def write_csv(path, rows):
    detail = [row for row in rows if row.status in DETAIL_STATUSES]
    order = {name: index for index, name in enumerate(DETAIL_STATUSES)}
    detail.sort(key=lambda row: (order[row.status], row.file, row.locator, row.old, row.new))
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow([
            "status", "kind", "file", "locator", "old", "new",
            "approval", "moved_from", "moved_to",
        ])
        for row in detail:
            writer.writerow([
                row.status, row.kind, row.file, row.locator,
                row.old, row.new, source_cell(row),
                row.moved_from, row.moved_to,
            ])


def in_scope(path):
    """Every teaching HTML file, except a retired `_archive/` snapshot."""
    if not path.endswith(".html"):
        return False
    return "_archive" not in path.split("/")


def git_bytes(*args):
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
    )
    return result.returncode, result.stdout, result.stderr


def git_text(*args):
    code, out, err = git_bytes(*args)
    if code != 0:
        message = err.decode("utf-8", "replace").strip()
        raise SystemExit(message or f"git {' '.join(args)} failed")
    return out.decode("utf-8")


def resolve_commitish(name):
    for candidate in (name, "origin/" + name):
        code, _out, _err = git_bytes("rev-parse", "--verify", "--quiet", candidate)
        if code == 0:
            return candidate
    raise SystemExit(f"unknown ref {name}")


def merge_base(head, base):
    return git_text("merge-base", resolve_commitish(head), resolve_commitish(base)).strip()


def list_html(rev):
    out = git_text("ls-tree", "-r", "--name-only", rev)
    return [line for line in out.splitlines() if in_scope(line)]


def read_rev(rev, path):
    code, out, _err = git_bytes("show", f"{rev}:{path}")
    if code != 0:
        return ""
    return out.decode("utf-8")


def load_rev(rev):
    files = {}
    for path in list_html(rev):
        files[path] = read_rev(rev, path)
    return files


def pull_request_number():
    ref = os.environ.get("GITHUB_REF", "")
    match = re.search(r"refs/pull/(\d+)(?:/|$)", ref)
    if match:
        return match.group(1)
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path and Path(event_path).is_file():
        import json
        try:
            payload = json.loads(Path(event_path).read_text(encoding="utf-8"))
        except ValueError:
            payload = {}
        number = (payload.get("pull_request") or {}).get("number")
        if number:
            return str(number)
    return ""


def branch_name():
    head_ref = os.environ.get("GITHUB_HEAD_REF", "").strip()
    if head_ref:
        return head_ref
    name = git_text("rev-parse", "--abbrev-ref", "HEAD").strip()
    if name == "HEAD":
        return os.environ.get("GITHUB_REF_NAME", "HEAD")
    return name


def default_approval(root, pr_number):
    number = pr_number or pull_request_number()
    if number:
        return root / "changes" / f"{number}.yml"
    branch = branch_name()
    return root / "changes" / f"{branch}.yml"


def parse_args(argv):
    args = {
        "base": None,
        "head": "HEAD",
        "strict_added": False,
        "approval": None,
        "pr": None,
        "report": "incremental-report.csv",
        "markdown": None,
        "emit_draft": None,
    }
    index = 0
    while index < len(argv):
        token = argv[index]
        if token == "--strict-added":
            args["strict_added"] = True
            index += 1
            continue
        if token in {"--base", "--head", "--approval", "--pr", "--report", "--markdown", "--emit-draft"}:
            if index + 1 >= len(argv):
                raise SystemExit(f"{token} needs a value")
            key = token[2:].replace("-", "_")
            args[key] = argv[index + 1]
            index += 2
            continue
        raise SystemExit(f"unknown argument {token}")
    return args


def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)
    base_name = args["base"] or os.environ.get("GITHUB_BASE_REF") or "main"
    head = resolve_commitish(args["head"])
    base = merge_base(head, base_name)
    approval_path = (
        Path(args["approval"]) if args["approval"]
        else default_approval(ROOT, args["pr"])
    )
    if not approval_path.is_absolute():
        approval_path = ROOT / approval_path
    approval = None
    if approval_path.is_file():
        approval = approval_path.read_text(encoding="utf-8")
    code, rows, counts, issues = evaluate(
        load_rev(base), load_rev(head), approval, strict_added=args["strict_added"]
    )
    markdown = format_markdown(counts, rows)
    sys.stdout.write(markdown)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(markdown)
    if args["markdown"]:
        Path(args["markdown"]).write_text(markdown, encoding="utf-8")
    report = Path(args["report"])
    if not report.is_absolute():
        report = Path.cwd() / report
    write_csv(report, rows)
    if args["emit_draft"]:
        Path(args["emit_draft"]).write_text(dump_changes(rows), encoding="utf-8")
    if issues:
        for issue in issues:
            print(issue, file=sys.stderr)
        print(
            f"base {base} head {head} approval {approval_path}",
            file=sys.stderr,
        )
    else:
        print(f"ok base {base} head {head}", file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(main())
