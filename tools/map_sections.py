"""Shared rules for IAS 16 map includes and local ?v= stamps.

build-map-includes.py, stamp-assets.py, and check-duplicates.py all use
these helpers so a stamp or a normalised plate cannot mean one thing in
the builder and another in CI.
"""

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "ias-16" / "draft-v1-linked"

# Cache-bust queries the site already uses. The value charset matches
# tools/build-last-update.py so a stamp rewrite strips the same way.
V_QUERY = re.compile(r"\?v=[A-Za-z0-9._~%-]*")
DATA_PHASE = re.compile(
    r"\s+data-phase-[A-Za-z0-9_-]+(?:=\"[^\"]*\"|='[^']*')?"
)
HEX12 = re.compile(r"^[0-9a-f]{12}$")

# These two files are stamped by their own generators. stamp-assets.py
# must not rewrite them, and check-duplicates.py must not demand that
# their ?v= equal a hash this script would have chosen.
SKIP_STAMP_NAMES = {"search-index.js", "last-update.js"}

LOCAL_SUFFIXES = {".css", ".js", ".html"}

INCLUDE_START = re.compile(
    r"^(?P<indent>[ \t]*)<!-- include:(?P<file>[^#\s>]+)#(?P<id>[A-Za-z0-9_-]+):start(?P<opts>.*?)-->[ \t]*$",
    re.M,
)
OPT_PAIR = re.compile(r"\s+([A-Za-z0-9_-]+)=\"([^\"]*)\"")
ALLOWED_OPTS = {"inject-class", "inject-attr"}

ATTR_URL = re.compile(
    r"""(?P<pre>(?:\b(?:href|src)\s*=\s*))(?P<q>["'])(?P<url>[^"']*)(?P=q)""",
    re.I,
)
CSS_URL = re.compile(
    r"""url\(\s*(?P<q>["']?)(?P<url>[^"')]+)(?P=q)\s*\)""",
    re.I,
)


def normalise(text):
    """Collapse whitespace and drop data-phase-* attributes and ?v=."""
    text = V_QUERY.sub("", text)
    text = DATA_PHASE.sub("", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_opts(raw):
    opts = {}
    rest = raw or ""
    for name, value in OPT_PAIR.findall(rest):
        if name not in ALLOWED_OPTS:
            raise SystemExit(f"unknown include option {name}")
        opts[name] = value
    consumed = OPT_PAIR.sub("", rest).strip()
    if consumed:
        raise SystemExit(f"could not parse include options: {raw.strip()}")
    classes = opts.get("inject-class", "").split()
    attrs = opts.get("inject-attr", "").split()
    return classes, attrs


def extract_map_section(html, section_id, origin):
    start = f"<!-- map-section:{section_id}:start -->"
    end = f"<!-- map-section:{section_id}:end -->"
    i = html.find(start)
    j = html.find(end)
    if i < 0 or j < 0 or j < i:
        raise SystemExit(
            f"{origin} is missing <!-- map-section:{section_id}:start/end -->"
        )
    if html.find(start, i + len(start)) != -1:
        raise SystemExit(f"{origin} repeats map-section:{section_id}")
    return html[i + len(start):j]


def reindent(body, indent):
    lines = body.replace("\r\n", "\n").strip("\n").split("\n")
    indents = []
    for line in lines:
        if line.strip():
            indents.append(len(line) - len(line.lstrip(" ")))
    common = min(indents) if indents else 0
    out = []
    for line in lines:
        if not line.strip():
            out.append("")
            continue
        if line.startswith(" " * common):
            stripped = line[common:]
        else:
            stripped = line.lstrip(" ")
        out.append(indent + stripped)
    return "\n".join(out)


def inject_root(html, classes, attrs):
    """Add master-only classes and boolean attributes to the first tag."""
    match = re.search(r"<[A-Za-z][^>]*>", html)
    if not match:
        raise SystemExit("included map section has no root tag")
    tag = match.group(0)
    if tag.endswith("/>"):
        raise SystemExit("included map section root is empty")
    class_match = re.search(r'\bclass="([^"]*)"', tag)
    have = class_match.group(1).split() if class_match else []
    for name in classes:
        if name not in have:
            have.append(name)
    if classes:
        if class_match:
            tag = tag[:class_match.start(1)] + " ".join(have) + tag[class_match.end(1):]
        else:
            tag = tag[:-1] + f' class="{" ".join(have)}">'
    for attr in attrs:
        if re.search(rf"(?:^|\s){re.escape(attr)}(?:\s|=|>)", tag) is None:
            tag = tag[:-1] + f" {attr}>"
    return html[:match.start()] + tag + html[match.end():]


def strip_injected(html, classes, attrs):
    """Undo inject_root on the first tag so a comparison matches the source."""
    match = re.search(r"<[A-Za-z][^>]*>", html)
    if not match:
        return html
    tag = match.group(0)
    class_match = re.search(r'\bclass="([^"]*)"', tag)
    if class_match and classes:
        kept = [name for name in class_match.group(1).split() if name not in classes]
        if kept:
            tag = tag[:class_match.start(1)] + " ".join(kept) + tag[class_match.end(1):]
        else:
            tag = tag[:class_match.start()] + tag[class_match.end():]
            tag = re.sub(r"\s+>", ">", tag)
            tag = re.sub(r"\s{2,}", " ", tag)
    for attr in attrs:
        tag = re.sub(rf"\s+{re.escape(attr)}(?:=\"[^\"]*\"|='[^']*')?", "", tag)
    return html[:match.start()] + tag + html[match.end():]


def include_end(html, file_name, section_id, search_from):
    pattern = re.compile(
        rf"^(?P<indent>[ \t]*)<!-- include:{re.escape(file_name)}#{re.escape(section_id)}:end -->[ \t]*$",
        re.M,
    )
    match = pattern.search(html, search_from)
    return match


def iter_includes(html):
    """Yield include regions in document order.

    body is the text between the start comment and the end comment,
    excluding the newline that follows the start comment when present.
    """
    cursor = 0
    while True:
        start = INCLUDE_START.search(html, cursor)
        if not start:
            return
        classes, attrs = parse_opts(start.group("opts"))
        end = include_end(html, start.group("file"), start.group("id"), start.end())
        if not end:
            raise SystemExit(
                f"missing end marker for include:{start.group('file')}#{start.group('id')}"
            )
        if INCLUDE_START.search(html, start.end(), end.start()):
            raise SystemExit("include regions overlap")
        yield {
            "file": start.group("file"),
            "id": start.group("id"),
            "classes": classes,
            "attrs": attrs,
            "indent": start.group("indent"),
            "start_end": start.end(),
            "end_start": end.start(),
            "body": html[start.end():end.start()],
        }
        cursor = end.end()


def rendered_body(source_body, indent, classes, attrs):
    """Interior between an include start comment and its end comment.

    The end comment keeps the indent already on its own line. The returned
    text ends with a newline so that indent stays put.
    """
    block = inject_root(reindent(source_body, indent), classes, attrs)
    return "\n" + block + "\n"


def resolve_local(from_file, url_path):
    """Return a pack file for a relative css/js/html URL, else None."""
    if not url_path or url_path.startswith(("#", "?", "data:", "mailto:")):
        return None
    if url_path.startswith(("http://", "https://", "//")):
        return None
    path = url_path.split("#", 1)[0].split("?", 1)[0]
    if not path or path.startswith("/"):
        return None
    candidate = (from_file.parent / path).resolve()
    try:
        candidate.relative_to(PACK.resolve())
    except ValueError:
        return None
    if candidate.suffix.lower() not in LOCAL_SUFFIXES:
        return None
    if not candidate.is_file():
        return None
    return candidate


def split_url(url):
    fragment = ""
    path = url
    if "#" in path:
        path, fragment = path.split("#", 1)
        fragment = "#" + fragment
    query = ""
    if "?" in path:
        path, query = path.split("?", 1)
        query = "?" + query
    return path, query, fragment


def query_v(query):
    match = re.search(r"[?&]v=([^&]*)", query)
    if not match:
        return None
    return match.group(1)


def set_query_v(query, value):
    if re.search(r"[?&]v=", query):
        return re.sub(r"([?&]v=)[^&]*", lambda match: match.group(1) + value, query, count=1)
    if query:
        return query + "&v=" + value
    return "?v=" + value


def file_stamp(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def iter_versioned_refs(text, from_file):
    """Yield local css/js/html references that already carry ?v=.

    search-index.js and last-update.js are yielded with skip=True so the
    stamper leaves them to their own scripts and the checker ignores them.
    """
    spans = []
    for match in ATTR_URL.finditer(text):
        spans.append((match.start("url"), match.end("url"), match.group("url")))
    for match in CSS_URL.finditer(text):
        spans.append((match.start("url"), match.end("url"), match.group("url")))
    spans.sort()
    for start, end, url in spans:
        path, query, fragment = split_url(url)
        version = query_v(query)
        if version is None:
            continue
        local = resolve_local(from_file, path)
        if local is None:
            continue
        yield {
            "start": start,
            "end": end,
            "url": url,
            "path": path,
            "query": query,
            "fragment": fragment,
            "version": version,
            "local": local,
            "skip": local.name in SKIP_STAMP_NAMES,
        }


CLASS_ATTR = re.compile(r'\bclass="([^"]*)"')
ARIA_ATTR = re.compile(r'\baria-label="([^"]*)"')
PLATE_TOKENS = {"plate", "disc-band"}


def class_tokens(tag):
    match = CLASS_ATTR.search(tag)
    if not match:
        return []
    return match.group(1).split()


def find_plate_sections(html):
    """Outermost elements whose class tokens include plate or disc-band."""
    token = re.compile(r"<(/?)([A-Za-z][\w:-]*)\b([^>]*)>")
    skip = 0
    stack = []
    found = []
    for match in token.finditer(html):
        closing, name, rest = match.group(1), match.group(2).lower(), match.group(3)
        if name in {"script", "style"}:
            if closing:
                skip = max(0, skip - 1)
            elif not rest.rstrip().endswith("/"):
                skip += 1
            continue
        if skip or rest.rstrip().endswith("/"):
            continue
        if name in {"meta", "link", "br", "hr", "img", "input", "wbr", "col", "source", "base", "area"}:
            continue
        if closing:
            for index in range(len(stack) - 1, -1, -1):
                if stack[index][0] != name:
                    continue
                opened = stack[index]
                del stack[index:]
                _name, start, tag, kind = opened
                if kind:
                    raw = html[start:match.end()]
                    aria = ARIA_ATTR.search(tag)
                    found.append({
                        "start": start,
                        "end": match.end(),
                        "raw": raw,
                        "aria": aria.group(1) if aria else "",
                        "kind": kind,
                    })
                break
            continue
        kind = None
        tokens = class_tokens(match.group(0))
        if "plate" in tokens:
            kind = "plate"
        elif "disc-band" in tokens:
            kind = "disc-band"
        stack.append((name, match.start(), match.group(0), kind))
    return found


def section_inside(span_start, regions):
    for begin, end in regions:
        if begin <= span_start < end:
            return True
    return False
