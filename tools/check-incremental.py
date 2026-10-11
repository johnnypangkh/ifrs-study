#!/usr/bin/env python3
"""Fail a pull request that removes or rewrites teaching text without approval.

Compares visible teaching items at the merge-base with main (base) to the
PR head. Each item is counted at its own location: kind, normalised text,
file, and locator. A lower count at a location is a removal there, even
when the same text still exists somewhere else. A move is only a matched
pair: the count falls at one location and rises by the same amount at
another location that did not already hold that copy. A removal and an
addition of the same kind that share a location, or whose text is at least
0.6 similar, are one change.

Approval lives in changes/<pr-number>.yml on a pull request, or
changes/<branch-name>.yml when git has no pull-request number. A removed
entry matches the file and the normalised text, and the locator when the
entry has one. A removal or a change with no entry fails, an entry that
matches nothing fails, and a missing file fails when anything was removed
or changed. Additions without an entry are warnings unless --strict-added.

Included copies (<!-- include:... -->) are not a second owned copy. The
source file owns that text. A hand copy that the head replaces with an
include of the same normalised text is kept when the source already had
it, or moved when a different file newly owns it (moved_from is the hand
copy, moved_to is source#section). It is not a removal. Unchanged text
that stays in the same file is kept when only its locator changes.
"""

import csv
import os
import re
import subprocess
import sys
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
    def __init__(self, kind, exact, key, file, locator):
        self.kind = kind
        self.exact = exact
        self.key = key
        self.file = file
        self.locator = locator


def add_item(items, kind, raw, file, node):
    exact = collapse(LAST_UPDATE.sub("", raw))
    key = normalise_key(exact)
    if not key:
        return
    items.append(Item(kind, exact, key, file, locator(node)))


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


class Shadow:
    def __init__(self, item, source_file, section_id):
        self.item = item
        self.source_file = source_file
        self.section_id = section_id


def new_include_views(base_files, head_files):
    """Shadows for includes that are new in head, plus keys the base source already had.

    A shadow attributes the source section's text to the including file so a
    hand copy can match it. The owned copy stays on the source file.
    `covered` maps an including file to (kind, key) pairs that lived in the
    base source section, so a wording change is reported once, on the source.
    """
    base_set = set(outermost_includes(base_files))
    shadows = []
    covered = {}
    for including, source, section in outermost_includes(head_files):
        if (including, source, section) in base_set:
            continue
        for item in section_items(head_files, source, section, set()):
            item.file = including
            shadows.append(Shadow(item, source, section))
        # The map-section markers often arrive in the same diff as the include.
        # Before that, the source file itself is the section.
        base_html = base_files.get(source, "")
        if f"<!-- map-section:{section}:start -->" in base_html:
            base_section = section_items(base_files, source, section, set())
        else:
            base_section = extract_html(base_html, source) if base_html else []
        for item in base_section:
            covered.setdefault(including, set()).add((item.kind, item.key))
    return shadows, covered


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


def diff_items(base_items, head_items, shadows=None, covered=None):
    """Per-location multiset. A surviving copy in another file is not a keep.

    A new include that renders the same text absorbs the hand copy it
    replaced. Unchanged text that only gained a map-section locator in the
    same file stays kept. Anything left over is still a removal.
    """
    base_groups = location_groups(base_items)
    head_groups = location_groups(head_items)
    kept = 0
    down = []
    up = []
    for key in sorted(set(base_groups) | set(head_groups)):
        base = base_groups.get(key, [])
        head = head_groups.get(key, [])
        kept += min(len(base), len(head))
        if len(base) > len(head):
            down.extend(base[:len(base) - len(head)])
        elif len(head) > len(base):
            up.extend(head[:len(head) - len(base)])
    include_kept, include_moved, down, up = absorb_new_includes(
        down, up, shadows or [], covered or {}, base_items, head_items,
    )
    kept += include_kept
    same_kept, down, up = pair_same_file(down, up)
    kept += same_kept
    moved, removed, added = pair_moves(down, up)
    moved = include_moved + moved
    changed = pair_changes(removed, added)
    rows = moved + changed + removed + added
    counts = {
        "kept": kept,
        "moved": len(moved),
        "changed": len(changed),
        "removed": len(removed),
        "added": len(added),
    }
    return rows, counts


def absorb_new_includes(down, up, shadows, covered, base_items, head_items):
    """Match a disappeared hand copy to a new include that renders it."""
    buckets = {}
    for shadow in shadows:
        item = shadow.item
        buckets.setdefault((item.kind, item.key, item.file), []).append(shadow)
    base_counts = {}
    head_counts = {}
    for item in base_items:
        key = (item.kind, item.key, item.file)
        base_counts[key] = base_counts.get(key, 0) + 1
    for item in head_items:
        key = (item.kind, item.key, item.file)
        head_counts[key] = head_counts.get(key, 0) + 1
    gain = {}
    for key, count in head_counts.items():
        extra = count - base_counts.get(key, 0)
        if extra > 0:
            gain[key] = extra
    kept = 0
    moved = []
    rest = []
    consumed = {}
    for item in down:
        bucket = buckets.get((item.kind, item.key, item.file))
        if bucket:
            shadow = bucket.pop()
            source_key = (item.kind, item.key, shadow.source_file)
            if shadow.source_file != item.file and gain.get(source_key, 0) > 0:
                gain[source_key] -= 1
                consumed[source_key] = consumed.get(source_key, 0) + 1
                row = Row(
                    "moved", item.kind, shadow.source_file,
                    "section:" + shadow.section_id,
                    item.exact, item.exact, item.key, item.key,
                )
                row.moved_from = place(item.file, item.locator)
                row.moved_to = shadow.source_file + "#" + shadow.section_id
                moved.append(row)
            else:
                kept += 1
            continue
        if (item.kind, item.key) in covered.get(item.file, ()):
            # The source already owned this wording. Its own diff is the row.
            continue
        rest.append(item)
    if consumed:
        kept_up = []
        for item in up:
            key = (item.kind, item.key, item.file)
            if consumed.get(key, 0) > 0:
                consumed[key] -= 1
                continue
            kept_up.append(item)
        up = kept_up
    return kept, moved, rest, up


def pair_same_file(down, up):
    """Unchanged text that stays in one file is kept when only the locator changes."""
    down_by = {}
    up_by = {}
    for item in down:
        down_by.setdefault((item.kind, item.key, item.file), []).append(item)
    for item in up:
        up_by.setdefault((item.kind, item.key, item.file), []).append(item)
    kept = 0
    rest_down = []
    rest_up = []
    for key in sorted(set(down_by) | set(up_by)):
        sources = down_by.get(key, [])
        dests = up_by.get(key, [])
        pair_count = min(len(sources), len(dests))
        kept += pair_count
        rest_down.extend(sources[pair_count:])
        rest_up.extend(dests[pair_count:])
    return kept, rest_down, rest_up


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
            moved.append(row)
        for item in sources[pair_count:]:
            removed.append(Row(
                "removed", kind, item.file, item.locator,
                item.exact, "", norm, "",
            ))
        for item in dests[pair_count:]:
            added.append(Row(
                "added", kind, item.file, item.locator,
                "", item.exact, "", norm,
            ))
    return moved, removed, added


def pair_changes(removed, added):
    candidates = []
    for i, old in enumerate(removed):
        for j, new in enumerate(added):
            if old.kind != new.kind:
                continue
            same = bool(old.locator) and old.file == new.file and old.locator == new.locator
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
        changed.append(Row(
            "changed", old.kind, new.file or old.file, locator,
            old.old, new.new, old.old_key, new.new_key,
        ))
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


def evaluate(base_files, head_files, approval=None, strict_added=False):
    """approval is None when the YAML file is absent, otherwise its text."""
    base_items = extract_tree(base_files)
    head_items = extract_tree(head_files)
    shadows, covered = new_include_views(base_files, head_files)
    rows, counts = diff_items(base_items, head_items, shadows, covered)
    entries = None
    missing = approval is None
    if not missing:
        entries = parse_changes(approval)
        match_entries(rows, entries)
    issues = problems(rows, entries, missing, strict_added)
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
