#!/usr/bin/env python3
"""Build a chapter page from source/chNN.md and source/pack.yml.

The teaching body is an HTML fragment under YAML front matter (J-2).
Headings ``## N.M Title`` become sections. A ``see:`` line becomes the
shared see-also strip. Packs with no source/ folder are skipped, so this
can ship before any live pack is wired.

Master Design, 2026-10-15:
  MD-1  body carries data-pack, data-page="chapter", and data-chapter.
  MD-2  the see: shorthand uses the classes in _shared/see-also.css
        (those rules use --t1-fw, --t3-arm-fw, and --t2-fw).
  MD-3  a chapter with no visual omits the map frame. The build warns
        and does not fail.

Usage:
  python3 tools/build-chapter.py --check
  python3 tools/build-chapter.py --all
  python3 tools/build-chapter.py ias-16/source/ch08.md
"""

import argparse
import difflib
import hashlib
import html as html_lib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIVE_PACKS = ("ias-16", "ias-2", "ifrs-18", "cf-2018")
FOOTER_NAV_STAMP = "footer-nav-20261010"
SHARED_ASSETS = (
    ("link", "tokens.css"),
    ("script", "chrome-include.js"),
    ("script", "last-update.js"),
    ("link", "cite.css"),
    ("link", "teaching.css"),
)
DISCLAIMER = (
    '<!-- disclaimer:start -->'
    '<aside class="callout pack-disclaimer" id="pack-disclaimer"></aside>'
    "<!-- disclaimer:end -->"
)
HEADING_RE = re.compile(r"^## (\d+(?:\.\d+)*) (.+)$")
HTML_HEADING_RE = re.compile(r"^## html (s-\d+(?:-\d+)*)$")
H3_RE = re.compile(r"<h3\b([^>]*)>(.*?)</h3>", re.S)
TOP_RE = re.compile(r'<a class="sec-top" href="[^"]*">top</a>')
SEE_LINE_RE = re.compile(r"^see:\s*(\S.*)$")
ASIDE_RE = re.compile(
    r'^<aside class="callout see-also"><span class="see-also-strip">'
    r'<span class="see-label">See also</span> '
    r"(.*?)</span></aside>$"
)
BIT_RE = re.compile(r'<span class="see-bit"><a href="([^"]*)">(.*?)</a></span>')
NOTE_RE = re.compile(r'<span class="see-strip-note">(.*?)</span>')
ROW_RE = re.compile(
    r'\{\s*href:\s*"((?:\\.|[^"\\])*)"\s*,\s*label:\s*"((?:\\.|[^"\\])*)"\s*\}'
)
V_QUERY = re.compile(r"\?v=[A-Za-z0-9._~%-]*")


class ChapterError(Exception):
    """A chapter source failed a check. The build stops."""


def file_stamp(path):
    if not path.is_file():
        return "000000000000"
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def esc(text):
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def attr(text, name):
    match = re.search(rf'\b{name}="([^"]*)"', text)
    if not match:
        return ""
    return match.group(1)


def js_escape(text):
    return text.replace("\\", "\\\\").replace('"', '\\"')


def js_unescape(text):
    out = []
    index = 0
    while index < len(text):
        if text[index] == "\\" and index + 1 < len(text):
            out.append(text[index + 1])
            index += 2
        else:
            out.append(text[index])
            index += 1
    return "".join(out)


def parse_scalar(raw):
    raw = raw.strip()
    if raw.startswith('"'):
        if len(raw) < 2 or not raw.endswith('"'):
            raise ChapterError(f"unclosed quote: {raw}")
        body = raw[1:-1]
        out = []
        index = 0
        while index < len(body):
            if body[index] == "\\" and index + 1 < len(body):
                code = body[index + 1]
                out.append({"n": "\n", "t": "\t", '"': '"', "\\": "\\"}.get(code, code))
                index += 2
            else:
                out.append(body[index])
                index += 1
        return "".join(out)
    if raw.startswith("'"):
        if len(raw) < 2 or not raw.endswith("'"):
            raise ChapterError(f"unclosed quote: {raw}")
        return raw[1:-1].replace("''", "'")
    if " #" in raw:
        raw = raw.split(" #", 1)[0].rstrip()
    if raw == "true":
        return True
    if raw == "false":
        return False
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    return raw


def parse_yaml(text):
    """A small YAML reader for pack.yml and chapter front matter.

    Maps and lists are one level deep. Values are scalars.
    """
    root = {}
    lines = text.replace("\r\n", "\n").split("\n")
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        if line[0] in " \t":
            raise ChapterError(f"unexpected indent: {line}")
        key, sep, raw = line.partition(":")
        if not sep or not key.strip():
            raise ChapterError(f"expected key: value, got {line}")
        key = key.strip()
        raw = raw.strip()
        if raw == "":
            index += 1
            block = []
            while index < len(lines):
                nxt = lines[index]
                if not nxt.strip() or nxt.lstrip().startswith("#"):
                    index += 1
                    continue
                if nxt[0] not in " \t":
                    break
                block.append(nxt)
                index += 1
            if not block:
                root[key] = ""
            elif block[0].strip().startswith("-"):
                root[key] = [_list_item(item) for item in block]
            else:
                nested = {}
                for item in block:
                    stripped = item.strip()
                    nkey, nsep, nraw = stripped.partition(":")
                    if not nsep:
                        raise ChapterError(f"expected key: value, got {stripped}")
                    nested[nkey.strip()] = parse_scalar(nraw)
                root[key] = nested
            continue
        root[key] = parse_scalar(raw)
        index += 1
    return root


def _list_item(line):
    stripped = line.strip()
    if not stripped.startswith("-"):
        raise ChapterError(f"expected a list item, got {stripped}")
    return parse_scalar(stripped[1:].strip())


def split_front_matter(text, where):
    text = text.replace("\r\n", "\n")
    if text.startswith("\ufeff"):
        text = text[1:]
    if not text.startswith("---\n"):
        raise ChapterError(f"{where}: chapter source must open with ---")
    end = text.find("\n---\n", 3)
    if end < 0:
        raise ChapterError(f"{where}: front matter is not closed with ---")
    meta = parse_yaml(text[4:end])
    body = text[end + 5 :]
    return meta, body


def require_text(data, key, where):
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ChapterError(f"{where}: missing {key}")
    return value.strip()


def load_profile(pack_dir):
    path = pack_dir / "source" / "pack.yml"
    if not path.is_file():
        raise ChapterError(f"missing {path}")
    data = parse_yaml(path.read_text(encoding="utf-8"))
    profile = {
        "id": require_text(data, "id", path),
        "standard": require_text(data, "standard", path),
        "noindex": data.get("noindex"),
        "css": data.get("css"),
        "path": path,
    }
    if not isinstance(profile["noindex"], bool):
        raise ChapterError(f"{path}: noindex must be true or false")
    css = profile["css"]
    if not isinstance(css, list) or not css:
        raise ChapterError(f"{path}: css must list at least one stylesheet")
    for item in css:
        if not isinstance(item, str) or not item or item.startswith("/") or ".." in item:
            raise ChapterError(f"{path}: css entry is not a pack-relative path: {item}")
    return profile


def is_see_shorthand(line):
    stripped = line.strip()
    return bool(SEE_LINE_RE.match(stripped)) and "<" not in stripped


def parse_see_line(line):
    match = SEE_LINE_RE.match(line.strip())
    if not match:
        raise ChapterError(f"not a see: line: {line}")
    rest = match.group(1).strip()
    note = ""
    if " :: " in rest:
        rest, note = rest.rsplit(" :: ", 1)
        note = note.strip()
    bits = []
    for part in rest.split(";"):
        part = part.strip()
        if not part:
            continue
        if " — " in part:
            href, label = part.split(" — ", 1)
            href, label = href.strip(), label.strip()
        else:
            href = label = part.strip()
        if not href or not label:
            raise ChapterError(f"empty see: target in {line}")
        bits.append({"href": href, "label": label})
    if not bits:
        raise ChapterError(f"see: line has no targets: {line}")
    return {"type": "see", "bits": bits, "note": note}


def parse_aside_line(line):
    match = ASIDE_RE.match(line.strip())
    if not match:
        return None
    body = match.group(1)
    note = ""
    note_match = NOTE_RE.search(body)
    if note_match:
        note = html_lib.unescape(note_match.group(1))
        body = body[: note_match.start()] + body[note_match.end() :]
    bits = []
    for href, label in BIT_RE.findall(body):
        bits.append(
            {"href": html_lib.unescape(href), "label": html_lib.unescape(label)}
        )
    if not bits or BIT_RE.sub("", body).strip():
        return None
    return {"type": "see", "bits": bits, "note": note}


def split_blocks(text):
    if not text:
        return []
    blocks = []
    buf = []

    def flush():
        if not buf:
            return
        chunk = "\n".join(buf)
        buf.clear()
        if chunk.strip() == "":
            if blocks:
                blocks.append({"type": "html", "text": chunk})
            return
        blocks.append({"type": "html", "text": chunk})

    for line in text.split("\n"):
        aside = parse_aside_line(line)
        if aside is not None:
            flush()
            blocks.append(aside)
            continue
        if is_see_shorthand(line):
            flush()
            blocks.append(parse_see_line(line))
            continue
        buf.append(line)
    flush()
    while blocks and blocks[0]["type"] == "html" and blocks[0]["text"].strip() == "":
        blocks.pop(0)
    while blocks and blocks[-1]["type"] == "html" and blocks[-1]["text"].strip() == "":
        blocks.pop()
    return blocks


def parse_sections(body, where):
    lines = body.replace("\r\n", "\n").split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    sections = []
    tail = []
    after = []
    mode = "seek"
    current = None
    buf = []

    def flush():
        nonlocal current
        if current is None:
            return
        current["blocks"] = split_blocks("\n".join(buf).strip("\n"))
        sections.append(current)
        current = None
        buf.clear()

    index = 0
    while index < len(lines):
        line = lines[index]
        if line == "<!-- tail -->":
            flush()
            mode = "tail"
            index += 1
            continue
        if line == "<!-- after -->":
            flush()
            mode = "after"
            index += 1
            continue
        if mode == "tail":
            tail.append(line)
            index += 1
            continue
        if mode == "after":
            after.append(line)
            index += 1
            continue
        plain = HEADING_RE.match(line)
        rich = HTML_HEADING_RE.match(line)
        if plain or rich:
            flush()
            if plain:
                number = plain.group(1)
                current = {
                    "kind": "plain",
                    "number": number,
                    "title": plain.group(2).strip(),
                    "id": "s-" + number.replace(".", "-"),
                }
                index += 1
            else:
                if index + 1 >= len(lines) or not lines[index + 1].strip():
                    raise ChapterError(f"{where}: {line} needs the heading HTML on the next line")
                current = {
                    "kind": "html",
                    "id": rich.group(1),
                    "html": lines[index + 1],
                }
                index += 2
            mode = "section"
            continue
        if mode == "seek":
            if line.strip():
                raise ChapterError(f"{where}: content before the first heading: {line[:60]}")
            index += 1
            continue
        buf.append(line)
        index += 1
    flush()
    if not sections:
        raise ChapterError(f"{where}: a chapter needs at least one ## heading")
    return sections, "\n".join(tail).strip("\n"), "\n".join(after).strip("\n")


def chapter_number_of(section):
    if section["kind"] == "plain":
        return int(section["number"].split(".", 1)[0])
    match = re.match(r"s-(\d+)", section["id"])
    if not match:
        raise ChapterError(f"section id {section['id']} is not s-N-M")
    return int(match.group(1))


def parse_chapter(text, where):
    meta, body = split_front_matter(text, where)
    chapter_no = meta.get("chapter")
    if not isinstance(chapter_no, int) or chapter_no < 1:
        raise ChapterError(f"{where}: chapter must be a positive integer")
    file_name = require_text(meta, "file", where)
    expected = f"ch{chapter_no:02d}.html"
    if file_name != expected:
        raise ChapterError(f"{where}: file {file_name} does not match chapter {chapter_no} ({expected})")
    title = require_text(meta, "title", where)
    pill = require_text(meta, "pill", where)
    purpose = meta.get("purpose")
    if purpose is not None and not isinstance(purpose, str):
        raise ChapterError(f"{where}: purpose must be a string")
    if isinstance(purpose, str):
        purpose = purpose.strip() or None
    map_info = meta.get("map")
    if map_info in ("", None):
        map_info = None
    elif not isinstance(map_info, dict):
        raise ChapterError(f"{where}: map must be a src/title block")
    else:
        src = map_info.get("src") or ""
        title_attr = map_info.get("title") or ""
        if not isinstance(src, str) or not isinstance(title_attr, str):
            raise ChapterError(f"{where}: map src and title must be strings")
        map_info = {"src": src.strip(), "title": title_attr.strip()}
        if map_info["src"] and (".." in map_info["src"] or map_info["src"].startswith("/")):
            raise ChapterError(f"{where}: map src must stay inside the pack")
    sections, tail, after = parse_sections(body, where)
    ids = []
    for section in sections:
        number = chapter_number_of(section)
        if number != chapter_no:
            raise ChapterError(
                f"{where}: heading {section['id']} is not in chapter {chapter_no}"
            )
        if section["id"] in ids:
            raise ChapterError(f"{where}: duplicate section id {section['id']}")
        ids.append(section["id"])
    return {
        "pack": require_text(meta, "pack", where),
        "chapter": chapter_no,
        "file": file_name,
        "title": title,
        "pill": pill,
        "purpose": purpose,
        "map": map_info,
        "sections": sections,
        "tail": tail,
        "after": after,
        "where": str(where),
    }


def see_hrefs(chapter):
    hrefs = []
    for section in chapter["sections"]:
        for block in section["blocks"]:
            if block["type"] == "see":
                for bit in block["bits"]:
                    hrefs.append(bit["href"])
    return hrefs


def render_see(block):
    bits = []
    for bit in block["bits"]:
        bits.append(
            '<span class="see-bit"><a href="'
            + esc(bit["href"])
            + '">'
            + esc(bit["label"])
            + "</a></span>"
        )
    note = ""
    if block.get("note"):
        note = '<span class="see-strip-note">' + esc(block["note"]) + "</span>"
    return (
        '<aside class="callout see-also"><span class="see-also-strip">'
        '<span class="see-label">See also</span> '
        + "".join(bits)
        + note
        + "</span></aside>"
    )


def blocks_html(blocks):
    parts = []
    for block in blocks:
        if block["type"] == "html":
            parts.append(block["text"])
        elif block["type"] == "see":
            parts.append(render_see(block))
        else:
            raise ChapterError(f"unknown block {block['type']}")
    return "\n".join(parts)


def render_heading(section, top_href):
    top = f'<a class="sec-top" href="{esc(top_href)}">top</a>'
    if section["kind"] == "plain":
        text = esc(f"{section['number']} {section['title']}")
    else:
        text = section["html"]
    return f'<h3 id="{esc(section["id"])}">{text}{top}</h3>'


def document_title(title, standard):
    match = re.match(r"^Chapter (\d+) — (.+)$", title)
    if match:
        short = f"Ch{match.group(1)} {match.group(2)}"
    else:
        short = title
    return esc(f"{short} — {standard}")


def shared_tag(kind, name, repo_root):
    href = f"../../_shared/{name}?v={file_stamp(repo_root / '_shared' / name)}"
    if kind == "link":
        return f'<link rel="stylesheet" href="{href}">'
    return f'<script src="{href}"></script>'


def map_frame(chapter, out_dir, warnings):
    info = chapter.get("map")
    label = f"{chapter['pack']} {chapter['file']}"
    if not info or not info.get("src"):
        warnings.append(f"{label}: no concept map; map frame omitted")
        return None, "#chapter-title"
    src = info["src"]
    visual = out_dir / src
    if not visual.is_file():
        warnings.append(
            f"{label}: no concept map ({src} is not on disk); map frame omitted"
        )
        return None, "#chapter-title"
    if not info.get("title"):
        raise ChapterError(f"{chapter['where']}: map.title is required when the visual exists")
    stamped = esc(src) + "?v=" + file_stamp(visual)
    frame = "\n".join(
        [
            '<section class="visual-section">',
            '  <fieldset class="visual-fieldset" id="page-map">',
            '    <legend class="visual-legend">Concept Map</legend>',
            f'    <iframe src="{stamped}" title="{esc(info["title"])}" scrolling="no"></iframe>',
            "  </fieldset>",
            "</section>",
        ]
    )
    return frame, "#page-map"


def render_chapter(chapter, profile, out_dir, repo_root, warnings):
    if chapter["pack"] != profile["id"]:
        raise ChapterError(
            f"{chapter['where']}: pack {chapter['pack']} does not match {profile['id']}"
        )
    frame, top_href = map_frame(chapter, out_dir, warnings)
    head = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
    ]
    if profile["noindex"]:
        head.append('<meta name="robots" content="noindex">')
    head.extend(
        [
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=1280">',
            f"<title>{document_title(chapter['title'], profile['standard'])}</title>",
        ]
    )
    for kind, name in SHARED_ASSETS:
        head.append(shared_tag(kind, name, repo_root))
    for rel in profile["css"]:
        head.append(
            f'<link rel="stylesheet" href="{esc(rel)}?v={file_stamp(out_dir / rel)}">'
        )
    head.append("</head>")
    file_stem = chapter["file"][:-5]
    body = (
        f'<body data-pack="{esc(profile["id"])}" '
        f'data-page="chapter" data-chapter="{esc(file_stem)}">'
    )
    header_lines = [
        '<div class="page-header">',
        f'  <h1 id="chapter-title">{esc(chapter["title"])}</h1>',
    ]
    if chapter.get("purpose"):
        header_lines.append(f'  <p class="purpose">{esc(chapter["purpose"])}</p>')
    header_lines.append("</div>")
    article = ["<article class=\"teaching\">", ""]
    for section in chapter["sections"]:
        article.append(render_heading(section, top_href))
        body_html = blocks_html(section["blocks"])
        if body_html:
            article.append(body_html)
        article.append("")
    article.append("</article>")
    parts = head + [
        body,
        "<!-- chrome:start -->",
        '<header class="chrome-bar"></header>',
        "<!-- chrome:end -->",
        '<main class="page">',
        "\n".join(header_lines),
        "",
    ]
    if frame:
        parts.extend([frame, ""])
    parts.append("\n".join(article))
    if chapter.get("tail"):
        parts.extend(["", chapter["tail"]])
    parts.extend(["", DISCLAIMER, "", "<!-- footer-nav:start -->"])
    parts.append('<nav class="footer-nav"></nav>')
    parts.append(
        f'<script src="../../_shared/footer-nav.js?v={FOOTER_NAV_STAMP}"></script>'
    )
    parts.append("<!-- footer-nav:end -->")
    if chapter.get("after"):
        parts.extend([chapter["after"]])
    parts.extend(["</main>", "", "</body>", "</html>", ""])
    page = "\n".join(parts)
    if "style=" in page.lower():
        raise ChapterError(f"{chapter['where']}: output contains style=, which is not allowed")
    info = chapter.get("map") or {}
    src = info.get("src") or ""
    has_frame = bool(src) and (out_dir / src).is_file()
    assert_page_map(page, has_frame, chapter["where"])
    assert_unique_ids(page, chapter["where"])
    return page


def ids_in(page):
    return set(re.findall(r'\bid="([^"]*)"', page))


def assert_unique_ids(page, where):
    found = re.findall(r'\bid="([^"]*)"', page)
    seen = set()
    for ident in found:
        if ident in seen:
            raise ChapterError(f"{where}: duplicate id {ident}")
        seen.add(ident)


def assert_page_map(page, has_frame, where):
    present = 'id="page-map"' in page
    tops = re.findall(r'class="sec-top" href="([^"]+)"', page)
    if has_frame:
        if not present:
            raise ChapterError(f"{where}: missing #page-map")
        if any(href != "#page-map" for href in tops):
            raise ChapterError(f"{where}: a top pill does not point at #page-map")
    else:
        if present or 'class="visual-section"' in page or 'class="visual-fieldset"' in page:
            raise ChapterError(f"{where}: map frame was emitted without a visual")
        if any(href != "#chapter-title" for href in tops):
            raise ChapterError(
                f"{where}: a top pill should point at #chapter-title when the map is omitted"
            )


def check_see_target(href, page, out_dir, siblings, where):
    if href.startswith("#"):
        ident = href[1:]
        if not ident or ident not in ids_in(page):
            raise ChapterError(f"{where}: broken see: {href}")
        return
    if href.startswith(("http:", "https:", "//", "/")):
        raise ChapterError(f"{where}: broken see: {href}")
    path, _, frag = href.partition("#")
    if not path or ".." in path:
        raise ChapterError(f"{where}: broken see: {href}")
    if path in siblings:
        target = siblings[path]
    else:
        file = out_dir / path
        if not file.is_file():
            raise ChapterError(f"{where}: broken see: {href} (missing {path})")
        target = file.read_text(encoding="utf-8")
    if frag and frag not in ids_in(target):
        raise ChapterError(f"{where}: broken see: {href} (no id {frag})")


def chapter_sort_key(href):
    match = re.fullmatch(r"ch(\d+)\.html", href)
    if not match:
        return (10**6, href)
    return (int(match.group(1)), href)


def parse_chapter_rows(inner):
    return [
        {"href": js_unescape(match.group(1)), "label": js_unescape(match.group(2))}
        for match in ROW_RE.finditer(inner)
    ]


def format_rows(rows):
    lines = []
    last = len(rows) - 1
    for index, row in enumerate(rows):
        comma = "," if index != last else ""
        lines.append(
            '      { href: "'
            + js_escape(row["href"])
            + '", label: "'
            + js_escape(row["label"])
            + '" }'
            + comma
        )
    return "\n" + "\n".join(lines) + "\n    "


def upsert_chapter_row(text, pack_id, href, label):
    marker = f"  {pack_id}: {{"
    start = text.find(marker)
    if start < 0:
        raise ChapterError(f"chrome-packs.js has no pack {pack_id}")
    # Two spaces then a closing brace. Four-space lines inside the pack
    # also begin with a newline and two spaces, so a bare "\n  " search
    # would stop on the first property.
    region_end = text.find("\n  }", start + len(marker))
    if region_end < 0:
        region_end = len(text)
    chap = text.find("chapters:", start, region_end)
    if chap < 0:
        raise ChapterError(f"chrome-packs.js pack {pack_id} has no chapters array")
    bracket = text.find("[", chap, region_end)
    if bracket < 0:
        raise ChapterError(f"chrome-packs.js pack {pack_id} chapters array is unclosed")
    depth = 0
    end = None
    for index in range(bracket, len(text)):
        if text[index] == "[":
            depth += 1
        elif text[index] == "]":
            depth -= 1
            if depth == 0:
                end = index
                break
    if end is None:
        raise ChapterError(f"chrome-packs.js pack {pack_id} chapters array is unclosed")
    rows = parse_chapter_rows(text[bracket + 1 : end])
    replaced = False
    for row in rows:
        if row["href"] == href:
            row["label"] = label
            replaced = True
            break
    if not replaced:
        rows.append({"href": href, "label": label})
    rows.sort(key=lambda row: chapter_sort_key(row["href"]))
    desired = format_rows(rows)
    current = text[bracket + 1 : end]
    if current == desired:
        return text
    return text[: bracket + 1] + desired + text[end:]


def extract_chapter(page, file_hint=""):
    """Read a chapter page back into the source model.

    Plain headings and the see: strip this tool emits come back as source.
    Any other teaching HTML is kept as a pass-through block. The pill is not
    on the page; chrome-packs.js owns it.
    """
    body_tag = re.search(r"<body\b([^>]*)>", page)
    if not body_tag:
        raise ChapterError("page has no body tag")
    pack = attr(body_tag.group(1), "data-pack")
    data_chapter = attr(body_tag.group(1), "data-chapter")
    if not data_chapter and file_hint:
        data_chapter = Path(file_hint).stem
    match = re.fullmatch(r"ch(\d+)", data_chapter or "")
    if not pack or not match:
        raise ChapterError("page is missing data-pack or a chNN file name")
    chapter_no = int(match.group(1))
    file_name = f"ch{chapter_no:02d}.html"
    h1 = re.search(r'<h1 id="chapter-title">(.*?)</h1>', page, re.S)
    if not h1:
        raise ChapterError(f"{file_name}: missing h1#chapter-title")
    title = html_lib.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip()
    purpose = None
    purpose_match = re.search(r'<p class="purpose">(.*?)</p>', page, re.S)
    if purpose_match:
        raw = purpose_match.group(1).strip()
        purpose = raw if "<" in raw else html_lib.unescape(raw)
    map_match = re.search(
        r'<fieldset class="visual-fieldset" id="page-map">(.*?)</fieldset>',
        page,
        re.S,
    )
    map_info = None
    if map_match:
        iframe = re.search(r"<iframe\b([^>]*)>", map_match.group(1), re.S)
        if iframe:
            src = V_QUERY.sub("", html_lib.unescape(attr(iframe.group(1), "src")))
            map_title = html_lib.unescape(attr(iframe.group(1), "title"))
            map_info = {"src": src, "title": map_title}
    article = re.search(r'<article class="teaching">(.*)</article>', page, re.S)
    if not article:
        raise ChapterError(f"{file_name}: missing article.teaching")
    inner = article.group(1)
    found = list(H3_RE.finditer(inner))
    if not found:
        raise ChapterError(f"{file_name}: article has no h3 sections")
    sections = []
    for index, h3 in enumerate(found):
        ident = attr(h3.group(1), "id")
        raw = TOP_RE.sub("", h3.group(2))
        end = found[index + 1].start() if index + 1 < len(found) else len(inner)
        body = inner[h3.end() : end].strip("\n")
        if "<" in raw:
            section = {"kind": "html", "id": ident, "html": raw}
        else:
            text = html_lib.unescape(raw).strip()
            plain = re.match(r"^(\d+(?:\.\d+)*)\s+(.+)$", text)
            derived = "s-" + plain.group(1).replace(".", "-") if plain else ""
            if plain and derived == ident:
                section = {
                    "kind": "plain",
                    "number": plain.group(1),
                    "title": plain.group(2),
                    "id": ident,
                }
            else:
                section = {"kind": "html", "id": ident, "html": raw}
        section["blocks"] = split_blocks(body)
        sections.append(section)
    after_article = page.split("</article>", 1)[1]
    tail = after_article.partition("<!-- disclaimer:start -->")[0].strip("\n")
    post = page.partition("<!-- footer-nav:end -->")[2]
    after = post.split("</main>", 1)[0].strip("\n")
    return {
        "pack": pack,
        "chapter": chapter_no,
        "file": file_name,
        "title": title,
        "pill": None,
        "purpose": purpose,
        "map": map_info,
        "sections": sections,
        "tail": tail,
        "after": after,
        "where": file_name,
    }


def comparable(chapter):
    """Fields a page can reproduce. The pill lives only in chrome-packs.js."""
    sections = []
    for section in chapter["sections"]:
        item = {
            "kind": section["kind"],
            "id": section["id"],
            "blocks": section["blocks"],
        }
        if section["kind"] == "plain":
            item["number"] = section["number"]
            item["title"] = section["title"]
        else:
            item["html"] = section["html"]
        sections.append(item)
    return {
        "pack": chapter["pack"],
        "chapter": chapter["chapter"],
        "file": chapter["file"],
        "title": chapter["title"],
        "purpose": chapter.get("purpose"),
        "map": chapter.get("map"),
        "sections": sections,
        "tail": chapter.get("tail") or "",
        "after": chapter.get("after") or "",
    }


def read_sources(pack_dir):
    source = pack_dir / "source"
    paths = sorted(source.glob("ch*.md"))
    chapters = []
    for path in paths:
        if not re.fullmatch(r"ch\d+\.md", path.name):
            continue
        chapters.append(parse_chapter(path.read_text(encoding="utf-8"), path))
    return chapters


def render_pack(pack_dir, profile, chapters, repo_root, warnings):
    out_dir = pack_dir / "draft-v1-linked"
    rendered = []
    for chapter in chapters:
        page = render_chapter(chapter, profile, out_dir, repo_root, warnings)
        rendered.append((chapter, page))
    siblings = {chapter["file"]: page for chapter, page in rendered}
    for chapter, page in rendered:
        for href in see_hrefs(chapter):
            check_see_target(href, page, out_dir, siblings, chapter["where"])
    return rendered


def unified(path, old, new):
    diff = difflib.unified_diff(
        old.splitlines(True),
        new.splitlines(True),
        fromfile=f"a/{path}",
        tofile=f"b/{path}",
    )
    return "".join(diff)


def apply_chrome(text, chapters, pack_id):
    for chapter in chapters:
        if not chapter.get("pill"):
            raise ChapterError(f"{chapter['where']}: missing pill")
        text = upsert_chapter_row(text, pack_id, chapter["file"], chapter["pill"])
    return text


def build_pack(pack_dir, chrome_path, repo_root, write, warnings):
    profile = load_profile(pack_dir)
    chapters = read_sources(pack_dir)
    if not chapters:
        raise ChapterError(f"{pack_dir}/source has pack.yml but no chNN.md")
    rendered = render_pack(pack_dir, profile, chapters, repo_root, warnings)
    out_dir = pack_dir / "draft-v1-linked"
    chrome_text = chrome_path.read_text(encoding="utf-8")
    updated = apply_chrome(chrome_text, chapters, profile["id"])
    diffs = []
    changed = []
    for chapter, page in rendered:
        dest = out_dir / chapter["file"]
        try:
            rel = dest.relative_to(repo_root)
        except ValueError:
            rel = dest
        current = dest.read_text(encoding="utf-8") if dest.is_file() else ""
        if current != page:
            diffs.append(unified(rel.as_posix(), current, page))
            if write:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(page, encoding="utf-8")
                changed.append(rel.as_posix())
    chrome_rel = chrome_path.name
    try:
        chrome_rel = chrome_path.relative_to(repo_root).as_posix()
    except ValueError:
        chrome_rel = chrome_path.as_posix()
    if updated != chrome_text:
        diffs.append(unified(chrome_rel, chrome_text, updated))
        if write:
            chrome_path.write_text(updated, encoding="utf-8")
            changed.append(chrome_rel)
    return {"diffs": diffs, "changed": changed, "count": len(rendered)}


def packs_with_source(root):
    found = []
    for name in LIVE_PACKS:
        pack = root / name
        if (pack / "source" / "pack.yml").is_file():
            found.append(pack)
    return found


def run_root(root, write):
    root = root.resolve()
    packs = packs_with_source(root)
    if not packs:
        print("build-chapter: no source/ folders; nothing to do")
        return 0
    chrome_path = root / "_shared" / "chrome-packs.js"
    if not chrome_path.is_file():
        raise ChapterError(f"missing {chrome_path}")
    warnings = []
    diffs = []
    changed = []
    count = 0
    for pack in packs:
        result = build_pack(pack, chrome_path, root, write, warnings)
        diffs.extend(result["diffs"])
        changed.extend(result["changed"])
        count += result["count"]
    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    if write:
        if changed:
            print("build-chapter: wrote " + ", ".join(changed))
        else:
            print(f"build-chapter: up to date ({count} chapter(s))")
        return 0
    if diffs:
        sys.stdout.write("".join(diffs))
        print(
            "build-chapter: chapter pages drifted from source. "
            "Run python3 tools/build-chapter.py --all and commit the result.",
            file=sys.stderr,
        )
        return 1
    print(f"build-chapter: {count} chapter(s) match source")
    return 0


def run_paths(root, paths):
    warnings = []
    chrome_path = root / "_shared" / "chrome-packs.js"
    changed = []
    seen = set()
    for raw in paths:
        path = Path(raw)
        if not path.is_absolute():
            path = root / path
        pack_dir = path.resolve().parent.parent
        if pack_dir in seen:
            continue
        seen.add(pack_dir)
        result = build_pack(pack_dir, chrome_path, root, True, warnings)
        changed.extend(result["changed"])
    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    if changed:
        print("build-chapter: wrote " + ", ".join(changed))
    else:
        print("build-chapter: up to date")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build chapter pages from source/chNN.md")
    parser.add_argument("--check", action="store_true", help="fail if a sourced chapter differs")
    parser.add_argument("--all", action="store_true", help="rebuild every pack that has source/")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args(argv)
    try:
        if args.check and (args.all or args.paths):
            print("use --check on its own", file=sys.stderr)
            return 2
        if args.check:
            return run_root(args.root, write=False)
        if args.paths:
            return run_paths(args.root, args.paths)
        if args.all:
            return run_root(args.root, write=True)
    except ChapterError as exc:
        print(f"build-chapter: {exc}", file=sys.stderr)
        return 1
    parser.print_help(sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
