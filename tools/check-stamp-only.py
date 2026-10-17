#!/usr/bin/env python3
"""Existing pages may change only the Last update stamp text and ?v= restamps.

The homepage may also gain the one Settings link. Writes nothing unless
--csv is given.
"""
import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))
from map_sections import (  # noqa: E402
    ATTR_URL,
    CSS_URL,
    HEX12,
    SKIP_STAMP_NAMES,
    file_stamp,
    query_v,
    split_url,
)

V_QUERY = re.compile(r"\?v=[A-Za-z0-9._~%-]*")
PACK_PAGE = re.compile(
    r"^(?:ias-16|ias-2|ifrs-18|cf-2018)/draft-v1-linked/.+\.html$"
)
FOOTER_NAV_STAMP = "footer-nav-20261010"
IFRAME_TAG = re.compile(r"<iframe\b[^>]*>", re.I)
STAMP_PACKS = ("ias-16", "ias-2", "ifrs-18", "cf-2018")
STAMP = re.compile(r"Last update · \d{4}-\d{2}-\d{2} \d{2}:\d{2} HKT")
HOME = "homepage/homepage-wireframe-v0.1.html"
# site/settings/index.html and _shared/settings-rows.html are gated instead by check-settings-rows.py (276/276) and xlsx_to_tokens.py --check.
CONTENT_ALLOW = (
    "_shared/settings-rows.html",
)
# Settings may change ?v= only, and each new value must match the file hash.
SETTINGS_PAGE = "site/settings/index.html"
# W4 replaces these three style attributes with classes. The stamp gate
# treats that swap as non-content on the six IFRS 18 pages. Any other
# HTML change on those pages still fails.
UTILITY_PAGES = (
    "ifrs-18/draft-v1-linked/ch03.html",
    "ifrs-18/draft-v1-linked/ch04.html",
    "ifrs-18/draft-v1-linked/ch05.html",
    "ifrs-18/draft-v1-linked/ch06.html",
    "ifrs-18/draft-v1-linked/ch07.html",
    "ifrs-18/draft-v1-linked/references.html",
)
UTILITY_CLASS = {
    "text-align:right": "num",
    "flex:11auto": "grow",
    "color:var(--muted)": "muted",
}
LINK = (
    '    <p><a href="../site/settings/index.html" style="color:var(--blue)">Settings</a></p>\n'
)
STAMPS_OBJ = re.compile(r"var STAMPS = \{.*?\n  \};", re.S)
PATHS_OBJ = re.compile(r"var PACK_PATHS = \[.*?\n  \];", re.S)


def git_text(rev, path):
    result = subprocess.run(
        ["git", "show", f"{rev}:{path}"],
        cwd=ROOT,
        capture_output=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.decode("utf-8")


def git_paths(rev):
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", rev],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return [line for line in result.stdout.splitlines() if line.endswith(".html")]


def norm(text):
    return V_QUERY.sub("?v=", text)


def _stamp_target(from_file, url_path, root):
    """A local css/js/html file under _shared or a pack draft tree."""
    if not url_path or url_path.startswith(("#", "?", "data:", "mailto:")):
        return None
    if url_path.startswith(("http://", "https://", "//", "/")):
        return None
    path = url_path.split("#", 1)[0].split("?", 1)[0]
    if not path:
        return None
    candidate = (from_file.parent / path).resolve()
    if candidate.suffix.lower() not in {".css", ".js", ".html"} or not candidate.is_file():
        return None
    try:
        rel = candidate.relative_to(root.resolve())
    except ValueError:
        return None
    if rel.parts[0] == "_shared":
        return candidate
    if (
        len(rel.parts) >= 2
        and rel.parts[0] in STAMP_PACKS
        and rel.parts[1] == "draft-v1-linked"
    ):
        return candidate
    return None


def iter_checked_stamps(text, from_file, root, iframe_only=False):
    """Versioned local targets this gate checks against the file hash."""
    chunks = [match.group(0) for match in IFRAME_TAG.finditer(text)] if iframe_only else [text]
    seen = set()
    for chunk in chunks:
        urls = []
        for match in ATTR_URL.finditer(chunk):
            urls.append(match.group("url"))
        for match in CSS_URL.finditer(chunk):
            urls.append(match.group("url"))
        for url in urls:
            path, query, _fragment = split_url(url)
            version = query_v(query)
            if version is None:
                continue
            local = _stamp_target(from_file, path, root)
            if local is None:
                continue
            key = (path, str(local))
            if key in seen:
                continue
            seen.add(key)
            yield path, version, local


def stamp_value_failure(text, path, root, from_file=None, iframe_only=False):
    """Fail when ?v= is not the target sha256[:12].

    footer-nav.js keeps its name stamp. search-index.js and last-update.js
    stay with their own generators. A non-hash token on any other file is
    a hand token. A 12-hex value that is not the current file hash is a
    mismatch, including a stale hash left over from an older file.
    """
    origin = from_file or (root / path)
    for url_path, version, local in iter_checked_stamps(
        text, origin, root, iframe_only=iframe_only
    ):
        if local.name in SKIP_STAMP_NAMES:
            continue
        if local.name == "footer-nav.js" and version == FOOTER_NAV_STAMP:
            continue
        digest = file_stamp(local)
        if version == digest:
            continue
        if HEX12.fullmatch(version):
            return (
                f"stamp hash mismatch: {path} {url_path} "
                f"?v={version} disk={digest}"
            )
        return f"stamp hand token: {path} {url_path} ?v={version}"
    return None


# Johnny 2026-10-17 11:15 — theme.js?v= may be added only on these 22 visuals.
THEME_JS_PAGES = (
    "cf-2018/draft-v1-linked/visuals/ch01-objective-users.html",
    "cf-2018/draft-v1-linked/visuals/ch02-qualitative-characteristics.html",
    "cf-2018/draft-v1-linked/visuals/ch03-reporting-entity.html",
    "cf-2018/draft-v1-linked/visuals/ch04-elements.html",
    "cf-2018/draft-v1-linked/visuals/ch05-recognition-derecognition.html",
    "cf-2018/draft-v1-linked/visuals/ch06-measurement.html",
    "cf-2018/draft-v1-linked/visuals/ch07-presentation-disclosure.html",
    "cf-2018/draft-v1-linked/visuals/ch08-capital.html",
    "cf-2018/draft-v1-linked/visuals/ch09-combined.html",
    "cf-2018/draft-v1-linked/visuals/ch10-carve.html",
    "cf-2018/draft-v1-linked/visuals/ch11-status.html",
    "ifrs-18/draft-v1-linked/visuals/ch01-whats-new.html",
    "ifrs-18/draft-v1-linked/visuals/ch02-pfs-aggregation.html",
    "ifrs-18/draft-v1-linked/visuals/ch03-classification-path.html",
    "ifrs-18/draft-v1-linked/visuals/ch03-mba-nest.html",
    "ifrs-18/draft-v1-linked/visuals/ch03-pnl-categories.html",
    "ifrs-18/draft-v1-linked/visuals/ch04-totals-subtotals.html",
    "ifrs-18/draft-v1-linked/visuals/ch05-operating-expenses.html",
    "ifrs-18/draft-v1-linked/visuals/ch06-mpms.html",
    "ifrs-18/draft-v1-linked/visuals/ch07-other-fs.html",
    "ifrs-18/draft-v1-linked/visuals/ch08-transition.html",
    "ifrs-18/draft-v1-linked/visuals/map-jumpboard.html",
)
INNER_STAMP_CSS = ("_shared/chrome.css", "_shared/teaching.css")
CHROME_INCLUDE = "_shared/chrome-include.js"
CHROME_ASSETS = (
    "chrome.css",
    "theme.js",
    "iframe-fit.js",
    "chrome-packs.js",
    "disclaimer.js",
    "chrome-bar.js",
    "search.js",
)
CHROME_V_OBJECT = re.compile(r"var V = \{.*?\};", re.S)
CHROME_V_STRING = re.compile(r'var V = "[0-9a-f]{12}";')
CHROME_INDEX = re.compile(r'var INDEX = "([0-9a-f]{12})";')
CHROME_MAP_COMMENT = (
    "\n   Map values are sha256[:12]. stamp-assets.py rewrites them."
)


def stamp_added_failure(base, head, path, root):
    """A ?v= on a URL the base page did not version is off the allowlist.

    The one exception is theme.js?v= on the 22 CF and IFRS 18 visual pages.
    """
    if not PACK_PAGE.fullmatch(path):
        return None
    origin = root / path
    base_paths = {
        url_path
        for url_path, _version, _local in iter_checked_stamps(base, origin, root)
    }
    for url_path, version, local in iter_checked_stamps(head, origin, root):
        if url_path in base_paths:
            continue
        if (
            path in THEME_JS_PAGES
            and local.name == "theme.js"
            and version == file_stamp(local)
        ):
            continue
        return f"stamp ?v= added off the allowlist: {path} {url_path}"
    return None


def inner_css_stamp_errors(root):
    """@import ?v= inside chrome.css and teaching.css must match the file.

    A parent page's chrome.css?v= or teaching.css?v= only proves the parent
    file's own hash. It does not prove an import inside that file. This
    check is what catches a stale or hand-token inner stamp.
    """
    errors = []
    for rel in INNER_STAMP_CSS:
        path = root / rel
        if not path.is_file():
            continue
        error = stamp_value_failure(path.read_text(encoding="utf-8"), rel, root)
        if error:
            errors.append(error)
    return errors


def parse_chrome_v_map(text):
    """Ordered (name, hash) pairs from var V = { ... }, or None."""
    match = CHROME_V_OBJECT.search(text)
    if not match:
        return None
    pairs = re.findall(r'"([^"]+)": "([0-9a-f]{12})"', match.group(0))
    return pairs


def _mask_chrome_include(text):
    """Hide the V map, the string-V migration, and INDEX."""
    text = text.replace(CHROME_MAP_COMMENT, "")
    text = CHROME_V_OBJECT.sub("var V = {};", text)
    text = CHROME_V_STRING.sub("var V = {};", text)
    text = text.replace('"?v=" + V;', '"?v=" + V[file];')
    text = CHROME_INDEX.sub('var INDEX = "";', text)
    return text


def chrome_include_failure(base, head, root):
    """Each V map entry must be that asset's sha256[:12].

    The one-time string-V to object migration is allowed. INDEX may differ
    only when the new value is homepage/search-index.js's hash.
    asset(), the document.write list, and any other logic still fail.
    """
    pairs = parse_chrome_v_map(head)
    if not pairs:
        return "chrome-include.js V map missing"
    keys = [name for name, _value in pairs]
    unknown = [name for name in keys if name not in CHROME_ASSETS]
    if unknown:
        return f"chrome-include.js V map has an extra key: {unknown[0]}"
    missing = [name for name in CHROME_ASSETS if name not in keys]
    if missing:
        return f"chrome-include.js V map missing a key: {missing[0]}"
    if keys != list(CHROME_ASSETS):
        return "chrome-include.js V map key order changed"
    for name, value in pairs:
        asset = root / "_shared" / name
        if not asset.is_file():
            return f"chrome-include.js missing asset {name}"
        digest = file_stamp(asset)
        if value != digest:
            return f"chrome-include.js V[{name}]={value} disk={digest}"
    index = CHROME_INDEX.search(head)
    if not index:
        return "chrome-include.js INDEX missing"
    search = root / "homepage" / "search-index.js"
    if search.is_file() and index.group(1) != file_stamp(search):
        return (
            f"chrome-include.js INDEX={index.group(1)} "
            f"disk={file_stamp(search)}"
        )
    if _mask_chrome_include(base) != _mask_chrome_include(head):
        return "chrome-include.js changed outside the V map"
    return None


def settings_stamp_failure(base, head, root):
    """Settings may change ?v= only, and the new value must match disk."""
    base_lines = base.splitlines()
    head_lines = head.splitlines()
    if len(base_lines) != len(head_lines):
        return f"settings stamp: line count changed: {SETTINGS_PAGE}"
    origin = root / SETTINGS_PAGE
    for line_no, (old, new) in enumerate(zip(base_lines, head_lines), 1):
        if old == new:
            continue
        if V_QUERY.sub("", old) != V_QUERY.sub("", new):
            return f"settings stamp: diff outside the allowlist: {SETTINGS_PAGE}:{line_no}"
        urls = [match.group("url") for match in ATTR_URL.finditer(new)]
        checked = False
        for url in urls:
            path, query, _fragment = split_url(url)
            version = query_v(query)
            if version is None:
                continue
            local = _stamp_target(origin, path, root)
            if local is None:
                continue
            if local.name == "footer-nav.js" and version == FOOTER_NAV_STAMP:
                checked = True
                continue
            digest = file_stamp(local)
            if version != digest:
                return (
                    f"settings stamp hash mismatch: {SETTINGS_PAGE}:{line_no} "
                    f"?v={version} disk={digest}"
                )
            checked = True
        if not checked:
            return f"settings stamp: diff outside the allowlist: {SETTINGS_PAGE}:{line_no}"
    return None


def fold_settings_stamps(base_html, head_html, path):
    """?v=-only settings edits compare equal after norm()."""
    return base_html


def fold_theme_js(base_html, head_html, path):
    """Accept the theme.js?v= addition on the 22 listed visuals. Base only."""
    if path not in THEME_JS_PAGES:
        return base_html
    theme = ROOT / "_shared" / "theme.js"
    if not theme.is_file():
        return base_html
    old = 'src="../../../_shared/theme.js"'
    new = 'src="../../../_shared/theme.js?v=' + file_stamp(theme) + '"'
    if old in base_html and new in head_html:
        return base_html.replace(old, new, 1)
    return base_html


def check_source_iframe_stamps(root):
    """In-body source iframes must carry the visual file's current hash."""
    errors = []
    for name in STAMP_PACKS:
        src = root / name / "source"
        if not src.is_dir():
            continue
        origin = root / name / "draft-v1-linked" / "chapter.html"
        for md in sorted(src.glob("*.md")):
            rel = md.relative_to(root).as_posix()
            error = stamp_value_failure(
                md.read_text(encoding="utf-8"),
                rel,
                root,
                from_file=origin,
                iframe_only=True,
            )
            if error:
                errors.append(error)
    return errors


# Johnny 2026-10-16 20:14 — shared visual stamp cleanup.
# Only these ?v= lines may differ. A byte change, or a ?v= change on any
# other line, fails the gate.
SHARED_VISUAL_CSS = "_shared/visuals.css"
SHARED_VISUAL_IMPORTS = {
    13: "tokens-core.css?v=",
    14: "see-also.css?v=",
    # #82: visuals twin of teaching-layout-1 and box-1. ?v= only.
    16: "modules/visuals/teaching-layout-1.css?v=",
    17: "modules/visuals/box-1.css?v=",
    # #83: leftover visual body type. ?v= only.
    20: "modules/visuals/components-2.css?v=",
    24: "modules/visuals/components-4.css?v=",
    27: "modules/visuals/components-5.css?v=",
    28: "modules/visuals/cite-1.css?v=",
    29: "modules/visuals/components-6.css?v=",
}
SHARED_VISUAL_PAGES = (
    "cf-2018/draft-v1-linked/visuals/ch01-objective-users.html",
    "cf-2018/draft-v1-linked/visuals/ch02-qualitative-characteristics.html",
    "cf-2018/draft-v1-linked/visuals/ch03-reporting-entity.html",
    "cf-2018/draft-v1-linked/visuals/ch04-elements.html",
    "cf-2018/draft-v1-linked/visuals/ch05-recognition-derecognition.html",
    "cf-2018/draft-v1-linked/visuals/ch06-measurement.html",
    "cf-2018/draft-v1-linked/visuals/ch07-presentation-disclosure.html",
    "cf-2018/draft-v1-linked/visuals/ch08-capital.html",
    "cf-2018/draft-v1-linked/visuals/ch09-combined.html",
    "cf-2018/draft-v1-linked/visuals/ch10-carve.html",
    "cf-2018/draft-v1-linked/visuals/ch11-status.html",
    "ias-2/draft-v1-linked/visuals/ch01-scope.html",
    "ias-2/draft-v1-linked/visuals/ch02-recognition.html",
    "ias-2/draft-v1-linked/visuals/ch03-initial.html",
    "ias-2/draft-v1-linked/visuals/ch04-subsequent.html",
    "ias-2/draft-v1-linked/visuals/ch05-derecognition.html",
    "ias-2/draft-v1-linked/visuals/ch06-disclosure.html",
    "ias-2/draft-v1-linked/visuals/map-formula-board.html",
    "ifrs-18/draft-v1-linked/visuals/ch01-whats-new.html",
    "ifrs-18/draft-v1-linked/visuals/ch02-pfs-aggregation.html",
    "ifrs-18/draft-v1-linked/visuals/ch03-classification-path.html",
    "ifrs-18/draft-v1-linked/visuals/ch03-mba-nest.html",
    "ifrs-18/draft-v1-linked/visuals/ch03-pnl-categories.html",
    "ifrs-18/draft-v1-linked/visuals/ch04-totals-subtotals.html",
    "ifrs-18/draft-v1-linked/visuals/ch05-operating-expenses.html",
    "ifrs-18/draft-v1-linked/visuals/ch06-mpms.html",
    "ifrs-18/draft-v1-linked/visuals/ch07-other-fs.html",
    "ifrs-18/draft-v1-linked/visuals/ch08-transition.html",
    "ifrs-18/draft-v1-linked/visuals/map-jumpboard.html",
    "ias-16/draft-v1-linked/visuals/ch01-scope.html",
    "ias-16/draft-v1-linked/visuals/ch02-recognition.html",
    "ias-16/draft-v1-linked/visuals/ch03-initial.html",
    "ias-16/draft-v1-linked/visuals/ch04-models.html",
    "ias-16/draft-v1-linked/visuals/ch05-depreciation.html",
    "ias-16/draft-v1-linked/visuals/ch06-derecognition.html",
    "ias-16/draft-v1-linked/visuals/ch07-disclosure.html",
    "ias-16/draft-v1-linked/visuals/master-concept-map.html",
)
# In-body iframes in the IFRS 18 ch03 source. ?v= only. Johnny 2026-10-16 21:14.
IFRS18_CH03 = "ifrs-18/draft-v1-linked/ch03.html"
IFRS18_CH03_IFRAMES = (
    "visuals/ch03-mba-nest.html?v=",
    "visuals/ch03-classification-path.html?v=",
)


def _v_only(old, new):
    return V_QUERY.sub("?v=", old) == V_QUERY.sub("?v=", new) and old != new


def shared_visual_stamp_failure(base, head, path):
    """Return an error when path differs outside the shared-visual allowlist.

    visuals.css may change ?v= only on lines 13, 14, 16, 17, 20, 24, 27, 28, and 29.
    Each listed visual page may change ?v= only on its visuals.css link.
    Identical text is not a failure. None means this path is not in the
    allowlist, or the difference is allowed.
    """
    if path == SHARED_VISUAL_CSS:
        allowed = SHARED_VISUAL_IMPORTS
        def listed(line_no, old):
            needle = allowed.get(line_no)
            return needle is not None and needle in old
    elif path in SHARED_VISUAL_PAGES:
        def listed(line_no, old):
            return "visuals.css?v=" in old
    elif path == IFRS18_CH03:
        def listed(line_no, old):
            return any(needle in old for needle in IFRS18_CH03_IFRAMES)
    else:
        return None
    # ch03 also carries the accepted map-iframe cascade. Only the two
    # in-body iframe lines are judged here; other lines stay on the
    # normal stamp gate.
    strict = path != IFRS18_CH03
    base_lines = base.splitlines()
    head_lines = head.splitlines()
    if len(base_lines) != len(head_lines):
        if not strict:
            return None
        return f"shared visual stamp: line count changed: {path}"
    for line_no, (old, new) in enumerate(zip(base_lines, head_lines), 1):
        if old == new:
            continue
        theme = ROOT / "_shared" / "theme.js"
        if (
            path in THEME_JS_PAGES
            and theme.is_file()
            and 'src="../../../_shared/theme.js"' in old
            and old.replace(
                'src="../../../_shared/theme.js"',
                'src="../../../_shared/theme.js?v=' + file_stamp(theme) + '"',
                1,
            )
            == new
        ):
            continue
        if not listed(line_no, old):
            if strict:
                return f"shared visual stamp: diff outside the allowlist: {path}"
            continue
        if not _v_only(old, new):
            return f"shared visual stamp: diff outside the allowlist: {path}"
    return None


def fold_viewport(html):
    """width=device-width, initial-scale=1 and width=1280 are the same page."""
    return html.replace(
        'content="width=device-width, initial-scale=1"',
        'content="width=1280"',
    )


def _brace_end(text, brace):
    depth = 0
    k = brace
    n = len(text)
    while k < n:
        if text.startswith("/*", k):
            end = text.find("*/", k + 2)
            k = n if end < 0 else end + 2
            continue
        char = text[k]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return k + 1
        k += 1
    return n


def strip_width_media(text):
    """Drop @media rules whose condition contains width. Other at-rules stay."""
    out = []
    i = 0
    n = len(text)
    while i < n:
        if text.startswith("/*", i):
            end = text.find("*/", i + 2)
            end = n if end < 0 else end + 2
            out.append(text[i:end])
            i = end
            continue
        if text.startswith("@media", i):
            brace = text.find("{", i)
            if brace < 0:
                out.append(text[i])
                i += 1
                continue
            if re.search(r"width", text[i:brace], re.I):
                i = _brace_end(text, brace)
                continue
        out.append(text[i])
        i += 1
    return "".join(out)


def _drop_style_indent_blanks(style):
    """A removed width query leaves its indent as a whitespace-only line."""
    lines = style.split("\n")
    kept = []
    for line in lines:
        if line != "" and line.strip() == "":
            continue
        kept.append(line)
    return "\n".join(kept)


def fold_style_media(html):
    """Inline style width queries are the W6 removal, not teaching text."""
    return re.sub(
        r"<style\b[^>]*>.*?</style>",
        lambda match: _drop_style_indent_blanks(strip_width_media(match.group(0))),
        html,
        flags=re.S | re.I,
    )


# F2 hard-wires master-concept-map.html to the not-narrow branch. The
# comparison treats base and head as that same branch. Each pair is applied
# once and is a no-op once the branch is already gone.
MAP_NARROW = "ias-16/draft-v1-linked/visuals/master-concept-map.html"
MAP_NARROW_FOLDS = (
    (
        '    if (window.matchMedia("(max-width: 800px)").matches) {\n'
        '      flow.style.removeProperty("--shaft-x");\n'
        "      return;\n"
        "    }\n",
        "",
    ),
    (
        '    if (window.matchMedia("(max-width: 800px)").matches) {\n'
        '      if (name.style.minHeight) name.style.minHeight = "";\n'
        '      if (rule && rule.style.marginTop) rule.style.marginTop = "";\n'
        "      return;\n"
        "    }\n",
        "",
    ),
    (
        '    var narrow = window.matchMedia("(max-width: 800px)").matches;\n'
        "    for (var g = 0; g < terms.length; g++) {\n",
        "    for (var g = 0; g < terms.length; g++) {\n",
    ),
    (
        "    if (narrow || terms.length < 2) return;\n",
        "    if (terms.length < 2) return;\n",
    ),
    (
        '    var narrow = window.matchMedia("(max-width: 800px)").matches;\n'
        "    var specs = [];\n",
        "    var specs = [];\n",
    ),
    (
        '      if (narrow) placeLabel(lab, x - em(0.55), (y1 + y2) / 2, "left");\n'
        '      else placeLabel(lab, x + em(0.55), (y1 + y2) / 2, "right");\n',
        '      placeLabel(lab, x + em(0.55), (y1 + y2) / 2, "right");\n',
    ),
    (
        '      if (narrow) hFlow(leaf1.cy, q1.cx, leaf1.l, noLab, "mute");\n'
        '      else hFlow(q1.cy, q1.r, leaf1.l, noLab, "mute");\n',
        '      hFlow(q1.cy, q1.r, leaf1.l, noLab, "mute");\n',
    ),
    (
        '      if (narrow) hFlow(leaf3.cy, q3.cx, leaf3.l, yesLab, "stop");\n'
        '      else hFlow(q3.cy, q3.r, leaf3.l, yesLab, "stop");\n',
        '      hFlow(q3.cy, q3.r, leaf3.l, yesLab, "stop");\n',
    ),
    (
        "    var recogRail = root.querySelector('.rail-link[data-phase=\"recog\"]');\n"
        '    var scopeNext = root.querySelector(".scope-tip");\n',
        '    var scopeNext = root.querySelector(".scope-tip");\n',
    ),
    (
        "    if (narrow && shown(recogRail) && shown(capQ)) {\n"
        "      var railB = boxOf(recogRail);\n"
        "      var q2 = boxOf(capQ);\n"
        "      vFlow(railB.cx, railB.b, q2.t, null);\n"
        "    }\n",
        "",
    ),
    (
        '      if (narrow) hFlow(leafY.cy, qY.cx, leafY.l, capNo, "mute");\n'
        '      else hFlow(qY.cy, qY.r, leafY.l, capNo, "mute");\n',
        '      hFlow(qY.cy, qY.r, leafY.l, capNo, "mute");\n',
    ),
    (
        "      if (narrow || Math.abs(qYes.cx - plate.cx) <= 3) {\n",
        "      if (Math.abs(qYes.cx - plate.cx) <= 3) {\n",
    ),
    (
        "    if (!narrow) {\n"
        '      linkStem(root.querySelector(".cost-result"), root.querySelector(".nature-nest > .port-tab"));\n'
        '      linkStem(root.querySelector(".da-col"), root.querySelector(".ready-axis > .axis-port"));\n'
        "    }\n",
        '    linkStem(root.querySelector(".cost-result"), root.querySelector(".nature-nest > .port-tab"));\n'
        '    linkStem(root.querySelector(".da-col"), root.querySelector(".ready-axis > .axis-port"));\n',
    ),
    (
        '      if (narrow && shown(rail) && rail.classList.contains("rail-link")) {\n'
        "        var R = boxOf(rail);\n"
        "        vFlow(S.cx, S.b, R.t, flowLab);\n"
        "        vFlow(R.cx, R.b, T.t, null);\n"
        "      } else {\n"
        "        vFlow(S.cx, S.b, T.t, flowLab);\n"
        "      }\n",
        "      vFlow(S.cx, S.b, T.t, flowLab);\n",
    ),
    (
        "    if (!narrow && shown(parent) && heads.length >= 2 && shown(heads[0]) && shown(heads[1])) {\n",
        "    if (shown(parent) && heads.length >= 2 && shown(heads[0]) && shown(heads[1])) {\n",
    ),
    (
        '    var narrow = window.matchMedia("(max-width: 800px)").matches;\n'
        '    var rails = root.querySelectorAll(".rail-link[data-phase]");\n'
        "    for (var i = 0; i < rails.length; i++) {\n"
        "      var rail = rails[i];\n"
        "      if (narrow) {\n"
        "        if (rail.style.marginTop || rail.style.height) {\n"
        '          rail.style.marginTop = "";\n'
        '          rail.style.height = "";\n'
        "        }\n"
        "        continue;\n"
        "      }\n",
        '    var rails = root.querySelectorAll(".rail-link[data-phase]");\n'
        "    for (var i = 0; i < rails.length; i++) {\n"
        "      var rail = rails[i];\n",
    ),
)


def fold_map_narrow(html):
    for old, new in MAP_NARROW_FOLDS:
        html = html.replace(old, new, 1)
    return html


# PR5 removes the five IAS 2 inline style blocks and turns the seven
# note-box style attributes into class="note-box". The stamp gate treats
# that swap as non-content. Any other HTML change on these pages still fails.
IAS2_NOTE_PAGES = (
    "ias-2/draft-v1-linked/index.html",
    "ias-2/draft-v1-linked/ch01.html",
    "ias-2/draft-v1-linked/ch02.html",
    "ias-2/draft-v1-linked/ch03.html",
    "ias-2/draft-v1-linked/ch04.html",
    "ias-2/draft-v1-linked/ch05.html",
    "ias-2/draft-v1-linked/ch06.html",
)
IAS2_NOTE_ATTR = (
    ' style="margin:0.75rem 0;padding:0.85rem 1rem;border:1px solid var(--line);'
    'border-radius:8px;background:var(--band);font-size:12.5px;line-height:1.55;'
    'color:var(--muted)"'
)


def fold_ias2_pr5(html):
    """Drop the archived inline style block and the note-box style attribute."""
    html = re.sub(r"\n<style>.*?</style>", "", html, count=1, flags=re.S)
    return html.replace(
        'class="callout pack-disclaimer" id="pack-disclaimer"' + IAS2_NOTE_ATTR,
        'class="callout pack-disclaimer note-box" id="pack-disclaimer"',
        1,
    )


# PR7 archives then deletes these HTML pages. They are not published notes.
# The stamp gate treats the absence as the approved deletion, not a missing page.
PR7_DELETED_HTML = (
    "cf-2018/chapter-visuals/_archive/ch01-overview.html",
    "cf-2018/chapter-visuals/ch01-objective-users.html",
    "cf-2018/chapter-visuals/ch02-qualitative-characteristics.html",
    "cf-2018/chapter-visuals/ch03-reporting-entity.html",
    "cf-2018/chapter-visuals/ch04-elements.html",
    "cf-2018/chapter-visuals/ch05-recognition-derecognition.html",
    "cf-2018/chapter-visuals/ch06-measurement.html",
    "cf-2018/chapter-visuals/ch07-presentation-disclosure.html",
    "cf-2018/chapter-visuals/ch08-capital.html",
    "cf-2018/chapter-visuals/ch09-status.html",
    "cf-2018/draft-v1-linked/_archive-index-stub.html",
    "cf-2018/draft-v1-linked/_archive/ch01-overview-redirect.html",
    "cf-2018/draft-v1-linked/_archive/ch01-overview.html",
    "cf-2018/draft-v1-linked/_archive/visuals-ch01-overview.html",
    "cf-2018/draft-v1-linked/_archive/visuals/ch09-status.html",
)
CF_FLOOR_PAGES = (
    "cf-2018/draft-v1-linked/ch03.html",
    "cf-2018/draft-v1-linked/ch09.html",
    "cf-2018/draft-v1-linked/ch10.html",
)
# Row #74 THEME removes data-theme="dark" from the eleven CF 2018 visual
# roots (T2). The stamp gate treats that attribute as non-content. Any
# other HTML change on those pages still fails.
CF_THEME_VISUALS = (
    "cf-2018/draft-v1-linked/visuals/ch01-objective-users.html",
    "cf-2018/draft-v1-linked/visuals/ch02-qualitative-characteristics.html",
    "cf-2018/draft-v1-linked/visuals/ch03-reporting-entity.html",
    "cf-2018/draft-v1-linked/visuals/ch04-elements.html",
    "cf-2018/draft-v1-linked/visuals/ch05-recognition-derecognition.html",
    "cf-2018/draft-v1-linked/visuals/ch06-measurement.html",
    "cf-2018/draft-v1-linked/visuals/ch07-presentation-disclosure.html",
    "cf-2018/draft-v1-linked/visuals/ch08-capital.html",
    "cf-2018/draft-v1-linked/visuals/ch09-combined.html",
    "cf-2018/draft-v1-linked/visuals/ch10-carve.html",
    "cf-2018/draft-v1-linked/visuals/ch11-status.html",
)


def fold_cf_theme(html):
    """Drop the forced night attribute on a CF visual root. Idempotent."""
    return html.replace('<html lang="en" data-theme="dark">', '<html lang="en">', 1)


# Johnny 2026-10-14 Option S / PR #124 — stamp gate ignores cite DOM order; check-incremental owns teaching.
CITE_HOUSE_RANK = (
    ("cite-official", 0),
    ("cite-pwc", 1),
    ("cite-dtt", 2),
    ("cite-ey", 3),
    ("cite-kpmg", 4),
)


def _is_span_open(html, index):
    if not html.startswith("<span", index):
        return False
    if index + 5 >= len(html):
        return True
    return html[index + 5] in " \t\r\n>/"


def _tag_end(html, index):
    """Index just after the '>' of the tag that starts at index."""
    quote = None
    cursor = index
    length = len(html)
    while cursor < length:
        char = html[cursor]
        if quote:
            if char == quote:
                quote = None
            cursor += 1
            continue
        if char in "\"'":
            quote = char
            cursor += 1
            continue
        if char == ">":
            return cursor + 1
        cursor += 1
    return length


def _span_close(html, open_end):
    """Exclusive end of the span whose opening tag ended at open_end."""
    depth = 1
    cursor = open_end
    length = len(html)
    while cursor < length and depth:
        if _is_span_open(html, cursor):
            cursor = _tag_end(html, cursor)
            depth += 1
            continue
        if html.startswith("</span>", cursor):
            depth -= 1
            cursor += len("</span>")
            continue
        cursor += 1
    return cursor


def _class_tokens(open_tag):
    match = re.search(r"""\bclass\s*=\s*(?:"([^"]*)"|'([^']*)')""", open_tag)
    if not match:
        return []
    return (match.group(1) if match.group(1) is not None else match.group(2)).split()


def _cite_house_rank(classes):
    """Rank of a .cite chip. None when the span is not a chip."""
    if "cite" not in classes:
        return None
    for name, rank in CITE_HOUSE_RANK:
        if name in classes:
            return rank
    return 5


def fold_cite_order(html):
    """Sort each run of adjacent .cite spans by house. Idempotent.

    Johnny 2026-10-14 Option S / PR #124 — stamp gate ignores cite DOM order; check-incremental owns teaching.
    Official, then PwC, DTT, EY, KPMG, then any other cite-* class.
    Chips of the same house keep their relative order. Whitespace between
    chips in a run becomes one space. A chip's own text and classes stay.
    """
    parts = []
    index = 0
    length = len(html)
    while index < length:
        if not _is_span_open(html, index):
            parts.append(html[index])
            index += 1
            continue
        open_end = _tag_end(html, index)
        rank = _cite_house_rank(_class_tokens(html[index:open_end]))
        if rank is None:
            parts.append(html[index])
            index += 1
            continue
        chips = []
        cursor = index
        run_end = index
        while cursor < length and _is_span_open(html, cursor):
            chip_open_end = _tag_end(html, cursor)
            chip_rank = _cite_house_rank(_class_tokens(html[cursor:chip_open_end]))
            if chip_rank is None:
                break
            chip_end = _span_close(html, chip_open_end)
            chips.append((chip_rank, html[cursor:chip_end]))
            run_end = chip_end
            gap = chip_end
            while gap < length and html[gap] in " \t\r\n":
                gap += 1
            if gap >= length or not _is_span_open(html, gap):
                break
            next_open_end = _tag_end(html, gap)
            if _cite_house_rank(_class_tokens(html[gap:next_open_end])) is None:
                break
            cursor = gap
        ordered = [raw for _, raw in sorted(chips, key=lambda item: item[0])]
        parts.append(" ".join(ordered))
        index = run_end
    return "".join(parts)


# Row #42 A1–A6, Johnny 2026-10-14 21:39
# Exact approved <li> lines, cite chips included. Not a general addition rule.
ROW42_A1_A6_LINES = {
    'ias-16/draft-v1-linked/ch03.html': (
        '  <li><strong>Start-up of a new network (PwC).</strong> When an operator builds a new mobile network in a new territory, costs of setting up the new business as a whole are not part of the cost of the network assets, even if they are incurred while the network is being built. Only costs of constructing the physical assets, such as transmitter towers, are capitalised. <span class="cite cite-official">IAS 16 · para 20</span> <span class="cite cite-pwc"><span class="cite-house">PwC</span> MOA 2020 Ch22 · FAQ 22.22.5</span></li>',
        '  <li><strong>Share-based payment (KPMG).</strong> The cost of employee benefits incurred for employees working directly on constructing or acquiring the asset includes share-based payment transactions, so that cost is directly attributable to the asset. <span class="cite cite-official">IAS 16 · para 17(a)</span> <span class="cite cite-kpmg"><span class="cite-house">KPMG</span> Insights 2019/20 · 3.2 · 3.2.30.40</span></li>',
        '  <li><strong>Foreign currency decommissioning liability (KPMG).</strong> IFRS is not clear on foreign exchange gains and losses from retranslating a decommissioning provision. In KPMG\'s view the liability is monetary to the extent it will be settled in a fixed or determinable number of currency units, and only that part is retranslated. An entity chooses a policy, applied consistently, to recognise those gains and losses either in P&amp;L or as an adjustment to the cost of the related asset. <span class="cite cite-official">IAS 21 · para 23</span> <span class="cite cite-official">IFRIC 1 · para 5–6</span> <span class="cite cite-kpmg"><span class="cite-house">KPMG</span> Insights 2019/20 · 3.2 · 3.2.80.25–40</span></li>',
    ),
    'ias-16/draft-v1-linked/ch02.html': (
        '  <li><strong>Surface mine stripping (IFRIC 20 see-also).</strong> Production stripping costs that improve access to a specific part of an ore body are added as a component of an existing asset; other routine stripping costs are inventory production costs. Detail is outside this pack. <span class="cite cite-official">IFRIC 20 · para 10</span> <span class="cite cite-official">IAS 16 · para 43</span> <span class="cite cite-ey"><span class="cite-house">EY</span> iGAAP 2026 Ch19 · section 3.1.6</span></li>',
    ),
    'ias-16/draft-v1-linked/ch04.html': (
        '  <li><strong>Business combination (PwC).</strong> Measuring an acquired subsidiary\'s PPE at FV in a business combination is not a revaluation, because that FV is the cost to the group. The group\'s existing assets in the same class therefore do not need to be revalued. <span class="cite cite-official">IAS 16 · para 38</span> <span class="cite cite-pwc"><span class="cite-house">PwC</span> MOA 2020 Ch22 · FAQ 22.71.2</span></li>',
        '  <li><strong>Right-of-use assets (IFRS 16 see-also).</strong> A lessee that applies the revaluation model to a class of PPE may choose to apply it to all ROU assets that relate to that class. Lessee measurement is in IFRS 16. <span class="cite cite-official">IFRS 16 · para 35</span> <span class="cite cite-ey"><span class="cite-house">EY</span> iGAAP 2026 Ch19 · section 6.5</span></li>',
    ),
}


def fold_row42_a1_a6(base_html, head_html, path):
    """Ignore only the six approved Row #42 additions on their three pages.

    Row #42 A1–A6, Johnny 2026-10-14 21:39
    Drop an exact <li> from head only when base does not already contain
    that same line. Any other byte, a second copy, or removal of the line
    still differs.
    """
    for item in ROW42_A1_A6_LINES.get(path, ()):
        needle = "\n" + item
        if needle in head_html and needle not in base_html:
            head_html = head_html.replace(needle, "", 1)
    return base_html, head_html


# Johnny 00:22 via PM 4 (Q-e). One-time deletion of the three CF iframe-floor
# <style> blocks. The id and the rule text both have to match. Any other
# edit on those pages, and any other <style> removal, still fails.
CF_IFRAME_FLOOR_BLOCKS = {
    "cf-2018/draft-v1-linked/ch03.html": (
        '<style id="ch03-iframe-floor">\n'
        '.visual-section iframe[src*="ch03-reporting-entity"]'
        "{min-height: calc(15 * var(--space-6));}\n"
        "</style>\n"
    ),
    "cf-2018/draft-v1-linked/ch09.html": (
        '<style id="ch09-iframe-floor">\n'
        '.visual-section iframe[src*="ch09-combined"]'
        "{min-height: calc(17 * var(--space-6) + var(--space-4));}\n"
        "</style>\n"
    ),
    "cf-2018/draft-v1-linked/ch10.html": (
        '<style id="ch10-iframe-floor">\n'
        '.visual-section iframe[src*="ch10-carve"]'
        "{min-height: calc(17 * var(--space-6) + var(--space-4));}\n"
        "</style>\n"
    ),
}


def fold_cf_iframe_floors(html, path):
    """Drop one approved floor block. Idempotent, and only on an exact match."""
    block = CF_IFRAME_FLOOR_BLOCKS.get(path)
    if block and block in html:
        return html.replace(block, "", 1)
    return html


def fold_cf2018_pr7(html, path):
    """P7: cost-sum style moved to draft.css; iframe floors became token sums."""
    if path == "cf-2018/draft-v1-linked/ch05.html":
        html = re.sub(
            r"\n<style>\s*article\.teaching \.cost-sum \{.*?</style>",
            "",
            html,
            count=1,
            flags=re.S,
        )
    if path in CF_FLOOR_PAGES:
        html = re.sub(
            r'(<style id="ch\d+-iframe-floor">\s*'
            r'\.visual-section iframe\[src\*="[^"]+"\]\{min-height:)[^;]+;',
            r"\1TOKEN;",
            html,
            count=1,
        )
    return html


IAS16_REFERENCES = "ias-16/draft-v1-linked/references.html"
IAS16_MUTED_SPAN = (
    '<span style="color:var(--muted)">'
    "(studied via HKAS 16 on box inputs; site label IAS 16 only)</span>"
)
IAS16_MUTED_CLASS = (
    '<span class="muted">'
    "(studied via HKAS 16 on box inputs; site label IAS 16 only)</span>"
)


def fold_ias16_references_muted(html, path):
    """Treat the one approved references span as class=muted.

    Only that exact span is folded. Any other edit on the page still fails.
    """
    if path != IAS16_REFERENCES:
        return html
    if IAS16_MUTED_SPAN not in html:
        return html
    return html.replace(IAS16_MUTED_SPAN, IAS16_MUTED_CLASS, 1)


# Johnny 18:36 J1 (a): exactly these eight IAS 2 inline-style edits.
IAS2_DISCLAIMER_STRONG = (
    '<strong style="color:var(--ink)">Disclaimer — personal study pack.</strong>'
)
IAS2_DISCLAIMER_PLAIN = "<strong>Disclaimer — personal study pack.</strong>"
IAS2_DISCLAIMER_PAGES = (
    "ias-2/draft-v1-linked/index.html",
    "ias-2/draft-v1-linked/ch01.html",
    "ias-2/draft-v1-linked/ch02.html",
    "ias-2/draft-v1-linked/ch03.html",
    "ias-2/draft-v1-linked/ch04.html",
    "ias-2/draft-v1-linked/ch05.html",
    "ias-2/draft-v1-linked/ch06.html",
)
IAS2_REFERENCES = "ias-2/draft-v1-linked/references.html"
IAS2_MUTED_SPAN = '<span style="color:var(--muted)">(HKAS 2 on box inputs)</span>'
IAS2_MUTED_CLASS = '<span class="muted">(HKAS 2 on box inputs)</span>'


# Johnny 2026-10-15 23:59 — PR-6 clean-up. Only the noindex line on nine
# IFRS 18 pages, and the MD-1 body attributes on the fourteen IAS 16 / IAS 2 pages.
PR6_NOINDEX = '<meta name="robots" content="noindex">'
PR6_NOINDEX_PAGES = tuple(
    f"ifrs-18/draft-v1-linked/ch0{n}.html" for n in range(1, 9)
) + ("ifrs-18/draft-v1-linked/abbreviations.html",)
PR6_IAS16_CHAPTERS = tuple(
    f"ias-16/draft-v1-linked/ch0{n}.html" for n in range(1, 8)
)
PR6_IAS2_CHAPTERS = tuple(
    f"ias-2/draft-v1-linked/ch0{n}.html" for n in range(1, 7)
)
PR6_IAS2_INDEX = "ias-2/draft-v1-linked/index.html"


# Johnny 2026-10-16 09:21 named these nine gaps. Johnny 2026-10-16 09:57
# (QC r1 item 7, option a) limited the stamp fold to this allow-list.
# Each marker is the next heading, or the article close after 5.11.
IAS16_SECTION_GAPS = {
    "ias-16/draft-v1-linked/ch04.html": (
        '<h3 id="s-4-4"',
        '<h3 id="s-4-6"',
    ),
    "ias-16/draft-v1-linked/ch05.html": (
        '<h3 id="s-5-3"',
        '<h3 id="s-5-4"',
        '<h3 id="s-5-5"',
        '<h3 id="s-5-6"',
        '<h3 id="s-5-8"',
        '<h3 id="s-5-9"',
        "</article>",
    ),
}


def _newline_run_before(html, marker):
    """Span of newlines sitting immediately before marker, or None.

    The article close is the last </article>. Heading markers occur once.
    """
    idx = html.rfind(marker) if marker == "</article>" else html.find(marker)
    if idx < 0:
        return None
    start = idx
    while start > 0 and html[start - 1] == "\n":
        start -= 1
    return start, idx


def fold_ias16_section_gap(base_html, head_html, path):
    """Drop extra blank lines at the nine approved spots. Nothing else.

    Johnny 2026-10-16 09:57. Where base has more newlines immediately before
    an allow-listed marker than head does, those extra newlines are removed
    from base. A longer run on head is left alone, so an added blank line
    still fails the stamp gate. A gap before any other heading is not folded.
    """
    markers = IAS16_SECTION_GAPS.get(path)
    if not markers:
        return base_html, head_html
    for marker in markers:
        base_span = _newline_run_before(base_html, marker)
        head_span = _newline_run_before(head_html, marker)
        if base_span is None or head_span is None:
            continue
        extra = (base_span[1] - base_span[0]) - (head_span[1] - head_span[0])
        if extra > 0:
            end = base_span[1]
            base_html = base_html[: end - extra] + base_html[end:]
    return base_html, head_html


# Johnny 2026-10-16 15:00 — CF chapters use the shared shell.
# Title moves to the line after the viewport meta. Each marker gains
# exactly one blank line. No other gap on these pages is folded.
CF2018_CHAPTERS = tuple(
    f"cf-2018/draft-v1-linked/ch{n:02d}.html" for n in range(1, 12)
)
CF2018_VIEWPORT = '<meta name="viewport" content="width=1280">\n'
CF2018_TITLE = re.compile(r"<title>.*?</title>\n", re.S)
CF2018_BLANK_ADDS = {
    f"cf-2018/draft-v1-linked/ch{n:02d}.html": (
        '<section class="visual-section">',
        '<article class="teaching">',
        "</article>",
        '<section class="key-terms">',
    )
    for n in range(1, 12)
    if n != 7
}
CF2018_BLANK_ADDS["cf-2018/draft-v1-linked/ch07.html"] = (
    '<section class="visual-section">',
    '<article class="teaching">',
    '<section class="key-terms">',
)
CF2018_BLANK_ADDS["cf-2018/draft-v1-linked/ch03.html"] = (
    '<section class="visual-section">',
    '<article class="teaching">',
    '<h3 id="s-3-0"',
    "</article>",
    '<section class="key-terms">',
)
CF2018_BLANK_ADDS["cf-2018/draft-v1-linked/ch04.html"] = (
    '<section class="visual-section">',
    '<article class="teaching">',
    '<h3 id="s-4-0"',
    "</article>",
    '<section class="key-terms">',
)


def _move_title_after_viewport(html):
    """Put the one title element on the line after the viewport meta."""
    match = CF2018_TITLE.search(html)
    if not match:
        return html
    title = match.group(0)
    without = html[: match.start()] + html[match.end() :]
    idx = without.find(CF2018_VIEWPORT)
    if idx < 0:
        return html
    at = idx + len(CF2018_VIEWPORT)
    if without[at : at + len(title)] == title:
        return without
    return without[:at] + title + without[at:]


def fold_cf2018_shell(base_html, head_html, path):
    """Fold the approved CF title move and the listed one-line blank adds.

    Johnny 2026-10-16 15:32. The title element is moved to the line after
    the viewport meta on the base page only. Head must already have its
    title on that line; any other head position still fails. At each listed
    marker, one newline is inserted into base only when head has exactly
    one more newline there. A second extra newline, or a gap before any
    other marker, still fails.
    """
    if path not in CF2018_CHAPTERS:
        return base_html, head_html
    base_html = _move_title_after_viewport(base_html)
    for marker in CF2018_BLANK_ADDS[path]:
        base_span = _newline_run_before(base_html, marker)
        head_span = _newline_run_before(head_html, marker)
        if base_span is None or head_span is None:
            continue
        base_len = base_span[1] - base_span[0]
        head_len = head_span[1] - head_span[0]
        if head_len - base_len == 1:
            end = base_span[1]
            base_html = base_html[:end] + "\n" + base_html[end:]
    return base_html, head_html


# Johnny 2026-10-16 17:11 — IAS 2 chapters use the same shell rules.
# Title moves on the base only. Blank deltas are exactly +1 or -1.
IAS2_CHAPTERS = tuple(
    f"ias-2/draft-v1-linked/ch0{n}.html" for n in range(1, 7)
)
IAS2_BLANK_DELTAS = {
    f"ias-2/draft-v1-linked/ch0{n}.html": (
        ('<section class="visual-section">', 1),
        ('<article class="teaching">', 1),
        (f'<h3 id="s-{n}-0"', 1),
        ("</main>", -1),
    )
    for n in range(1, 7)
}
for _rel in (
    "ias-2/draft-v1-linked/ch01.html",
    "ias-2/draft-v1-linked/ch02.html",
    "ias-2/draft-v1-linked/ch05.html",
    "ias-2/draft-v1-linked/ch06.html",
):
    IAS2_BLANK_DELTAS[_rel] = IAS2_BLANK_DELTAS[_rel] + (("</article>", 1),)
IAS2_BLANK_DELTAS["ias-2/draft-v1-linked/ch03.html"] = (
    IAS2_BLANK_DELTAS["ias-2/draft-v1-linked/ch03.html"]
    + (('<h3 id="s-3-3"', -1),)
)


def fold_ias2_shell(base_html, head_html, path):
    """Fold the IAS 2 title position and the listed one-line blank changes.

    Johnny 2026-10-16 17:11, using the 15:32 title rule. The title element
    is moved to the line after the viewport meta on the base page only.
    Head must already have its title on that line. At each listed marker,
    base gains or loses exactly one newline when that is the whole
    difference. Any other gap still fails.
    """
    if path not in IAS2_CHAPTERS:
        return base_html, head_html
    base_html = _move_title_after_viewport(base_html)
    for marker, delta in IAS2_BLANK_DELTAS[path]:
        base_span = _newline_run_before(base_html, marker)
        head_span = _newline_run_before(head_html, marker)
        if base_span is None or head_span is None:
            continue
        base_len = base_span[1] - base_span[0]
        head_len = head_span[1] - head_span[0]
        if head_len - base_len != delta:
            continue
        end = base_span[1]
        if delta == 1:
            base_html = base_html[:end] + "\n" + base_html[end:]
        elif delta == -1 and base_len > 0:
            base_html = base_html[: end - 1] + base_html[end:]
    return base_html, head_html


# Johnny 2026-10-16 19:02 option (b) — IFRS 18 chapters use the shared shell.
# Title text changes only on ch06 and ch08, and only on the base page.
# Shell indent (h1 and the map frame) is rewritten on the base page only.
# Blank deltas are exactly +1 or -1 at the listed markers.
IFRS18_CHAPTERS = tuple(
    f"ifrs-18/draft-v1-linked/ch{n:02d}.html" for n in range(1, 9)
)
IFRS18_TITLES = {
    "ifrs-18/draft-v1-linked/ch06.html": (
        "<title>Ch6 MPMs — IFRS 18</title>",
        "<title>Ch6 Management-defined performance measures (MPMs) — IFRS 18</title>",
    ),
    "ifrs-18/draft-v1-linked/ch08.html": (
        "<title>Ch8 Transition — IFRS 18</title>",
        "<title>Ch8 Transition &amp; effective date — IFRS 18</title>",
    ),
}
IFRS18_INDENT_PREFIXES = (
    (' <h1 id="chapter-title">', '  <h1 id="chapter-title">'),
    (
        ' <fieldset class="visual-fieldset" id="page-map">',
        '  <fieldset class="visual-fieldset" id="page-map">',
    ),
    (' <legend class="visual-legend">', "    <legend class=\"visual-legend\">"),
    (" <iframe ", "    <iframe "),
    (" </fieldset>", "  </fieldset>"),
)
IFRS18_BLANK_DELTAS = {
    f"ifrs-18/draft-v1-linked/ch{n:02d}.html": (
        ('<section class="visual-section">', 1),
        ('<article class="teaching">', 1),
    )
    for n in range(1, 9)
}
for _n in (1, 2, 3, 4, 5):
    _rel = f"ifrs-18/draft-v1-linked/ch{_n:02d}.html"
    IFRS18_BLANK_DELTAS[_rel] = IFRS18_BLANK_DELTAS[_rel] + (
        ('<section class="key-terms">', 1),
    )
for _n in (4, 5, 6):
    _rel = f"ifrs-18/draft-v1-linked/ch{_n:02d}.html"
    IFRS18_BLANK_DELTAS[_rel] = IFRS18_BLANK_DELTAS[_rel] + (("</article>", -1),)


def _reindent_ifrs18_shell(base_html, head_html):
    """Give base the head indent on the h1 and map-frame lines. Nothing else."""
    head_lines = set(head_html.splitlines())
    for old_prefix, new_prefix in IFRS18_INDENT_PREFIXES:
        lines = base_html.splitlines(keepends=True)
        replaced = False
        out = []
        for line in lines:
            body = line[:-1] if line.endswith("\n") else line
            ending = "\n" if line.endswith("\n") else ""
            new_body = new_prefix + body[len(old_prefix) :]
            if (
                not replaced
                and body.startswith(old_prefix)
                and body not in head_lines
                and new_body in head_lines
            ):
                out.append(new_prefix + body[len(old_prefix) :] + ending)
                replaced = True
            else:
                out.append(line)
        base_html = "".join(out)
    return base_html


def fold_ifrs18_shell(base_html, head_html, path):
    """Fold the approved IFRS 18 title text, shell indent, and blank lines.

    Johnny 2026-10-16 19:02 option (b). The two title strings are replaced
    on the base page only, and only when head already has the new string.
    Head must already have its title on the line after the viewport meta.
    The h1 and map-frame indent is applied on base only when that exact
    line is already on head. At each listed marker, base gains or loses
    exactly one newline when that is the whole difference. A title-text
    change on any other page, or any other gap, still fails.
    """
    if path not in IFRS18_CHAPTERS:
        return base_html, head_html
    pair = IFRS18_TITLES.get(path)
    if pair is not None:
        old, new = pair
        if old in base_html and new in head_html and old not in head_html:
            base_html = base_html.replace(old, new, 1)
    base_html = _move_title_after_viewport(base_html)
    base_html = _reindent_ifrs18_shell(base_html, head_html)
    for marker, delta in IFRS18_BLANK_DELTAS[path]:
        base_span = _newline_run_before(base_html, marker)
        head_span = _newline_run_before(head_html, marker)
        if base_span is None or head_span is None:
            continue
        base_len = base_span[1] - base_span[0]
        head_len = head_span[1] - head_span[0]
        if head_len - base_len != delta:
            continue
        end = base_span[1]
        if delta == 1:
            base_html = base_html[:end] + "\n" + base_html[end:]
        elif delta == -1 and base_len > 0:
            base_html = base_html[: end - 1] + base_html[end:]
    return base_html, head_html


def fold_pr6_cleanup(html, path):
    """Fold the approved noindex insert and MD-1 body attributes. Nothing else."""
    if path in PR6_NOINDEX_PAGES:
        html = html.replace("<head>\n" + PR6_NOINDEX + "\n", "<head>\n", 1)
    if path in PR6_IAS16_CHAPTERS:
        chapter = Path(path).stem
        html = html.replace(
            f'data-pack="ias16" data-page="{chapter}"',
            f'data-pack="ias16" data-page="chapter" data-chapter="{chapter}"',
            1,
        )
    if path in PR6_IAS2_CHAPTERS:
        chapter = Path(path).stem
        old = 'data-pack="ias2"'
        new = f'data-pack="ias2" data-page="chapter" data-chapter="{chapter}"'
        # Already MD-1, or the pre-MD-1 tag. A third shape is left for the diff.
        if new not in html:
            html = html.replace(old, new, 1)
    if path == PR6_IAS2_INDEX:
        old = 'data-pack="ias2"'
        new = 'data-pack="ias2" data-page="map"'
        if new not in html:
            html = html.replace(old, new, 1)
    return html


def fold_ias2_inline_styles(html, path):
    """Fold the eight approved IAS 2 inline colour styles. Nothing else.

    Disclaimer <strong style="color:var(--ink)"> on seven pages, and the one
    references muted span. Any other teaching edit still fails.
    """
    if path in IAS2_DISCLAIMER_PAGES and IAS2_DISCLAIMER_STRONG in html:
        html = html.replace(IAS2_DISCLAIMER_STRONG, IAS2_DISCLAIMER_PLAIN, 1)
    if path == IAS2_REFERENCES and IAS2_MUTED_SPAN in html:
        html = html.replace(IAS2_MUTED_SPAN, IAS2_MUTED_CLASS, 1)
    return html


def fold_utility_styles(html):
    """Swap the three approved utility styles into classes. Idempotent."""

    def repl_tag(match):
        tag = match.group(0)
        style = re.search(r'\sstyle="([^"]*)"', tag)
        if not style:
            return tag
        compact = re.sub(r"\s+", "", style.group(1))
        class_name = UTILITY_CLASS.get(compact)
        if class_name is None:
            return tag
        tag = tag[:style.start()] + tag[style.end():]
        class_attr = re.search(r'\sclass="([^"]*)"', tag)
        if class_attr:
            classes = class_attr.group(1).split()
            if class_name not in classes:
                classes.append(class_name)
            replacement = ' class="' + " ".join(classes) + '"'
            tag = tag[:class_attr.start()] + replacement + tag[class_attr.end():]
        else:
            tag = re.sub(
                r"^<[A-Za-z0-9]+",
                lambda item: item.group(0) + f' class="{class_name}"',
                tag,
                count=1,
            )
        return tag

    return re.sub(r"<[^>]+>", repl_tag, html)


# Johnny 2026-10-15 20:46 J4, narrowed after QC r1 and QC r2 E10.
# On head, only the empty shell directly before <!-- footer-nav:start -->.
# A pasted aside folds only when it is the exact aside that page had at
# base, in that page's base slot: directly before the footer-nav comment,
# or, on the seven IAS 2 note pages, immediately before </footer>.
# Another wording from the same pack, a shell anywhere else, or a wording
# pasted mid-page is left untouched and the stamp gate fails.
DISCLAIMER_SHELL = (
    "<!-- disclaimer:start -->"
    '<aside class="callout pack-disclaimer" id="pack-disclaimer"></aside>'
    "<!-- disclaimer:end -->"
)
DISCLAIMER_NAV = "<!-- footer-nav:start -->"
DISCLAIMER_PAGES = (
    'cf-2018/draft-v1-linked/abbreviations.html',
    'cf-2018/draft-v1-linked/ch01.html',
    'cf-2018/draft-v1-linked/ch02.html',
    'cf-2018/draft-v1-linked/ch03.html',
    'cf-2018/draft-v1-linked/ch04.html',
    'cf-2018/draft-v1-linked/ch05.html',
    'cf-2018/draft-v1-linked/ch06.html',
    'cf-2018/draft-v1-linked/ch07.html',
    'cf-2018/draft-v1-linked/ch08.html',
    'cf-2018/draft-v1-linked/ch09.html',
    'cf-2018/draft-v1-linked/ch10.html',
    'cf-2018/draft-v1-linked/ch11.html',
    'cf-2018/draft-v1-linked/index.html',
    'cf-2018/draft-v1-linked/references.html',
    'ias-16/draft-v1-linked/abbreviations.html',
    'ias-16/draft-v1-linked/ch01.html',
    'ias-16/draft-v1-linked/ch02.html',
    'ias-16/draft-v1-linked/ch03.html',
    'ias-16/draft-v1-linked/ch04.html',
    'ias-16/draft-v1-linked/ch05.html',
    'ias-16/draft-v1-linked/ch06.html',
    'ias-16/draft-v1-linked/ch07.html',
    'ias-16/draft-v1-linked/index.html',
    'ias-16/draft-v1-linked/references.html',
    'ias-2/draft-v1-linked/abbreviations.html',
    'ias-2/draft-v1-linked/ch01.html',
    'ias-2/draft-v1-linked/ch02.html',
    'ias-2/draft-v1-linked/ch03.html',
    'ias-2/draft-v1-linked/ch04.html',
    'ias-2/draft-v1-linked/ch05.html',
    'ias-2/draft-v1-linked/ch06.html',
    'ias-2/draft-v1-linked/index.html',
    'ias-2/draft-v1-linked/references.html',
    'ifrs-18/draft-v1-linked/abbreviations.html',
    'ifrs-18/draft-v1-linked/ch01.html',
    'ifrs-18/draft-v1-linked/ch02.html',
    'ifrs-18/draft-v1-linked/ch03.html',
    'ifrs-18/draft-v1-linked/ch04.html',
    'ifrs-18/draft-v1-linked/ch05.html',
    'ifrs-18/draft-v1-linked/ch06.html',
    'ifrs-18/draft-v1-linked/ch07.html',
    'ifrs-18/draft-v1-linked/ch08.html',
    'ifrs-18/draft-v1-linked/index.html',
    'ifrs-18/draft-v1-linked/references.html',
)
DISCLAIMER_KNOWN_ASIDES = (
    '<aside class="callout pack-disclaimer" id="pack-disclaimer">\n  <strong>Disclaimer — personal study pack.</strong>\n  These Conceptual Framework 2018 pages are <strong>personal study notes</strong> for private learning. They are <strong>not</strong> accounting, legal, or professional advice, and are <strong>not</strong> for commercial or mass redistribution.\n  The Conceptual Framework does not override an applicable IFRS Standard. Official Standards remain authoritative. Big4 / firm-manual extracts and third-party financial-statement examples appear only as short teaching paraphrase or cited figures for private study; the pack owner has legal counsel.\n  Do not treat this site as a substitute for the Official text, firm manuals, or issuer financial statements.\n</aside>',
    '<aside class="callout pack-disclaimer" id="pack-disclaimer">\n  <strong>Disclaimer — personal study pack.</strong>\n  These Conceptual Framework 2018 pages are <strong>personal study notes</strong> for private learning. They are <strong>not</strong> accounting, legal, or professional advice, and are <strong>not</strong> for commercial or mass redistribution.\n  The Conceptual Framework does not override an applicable IFRS Standard. Official Standards remain authoritative. Big4 / firm-manual material appears only as short teaching paraphrase or cited extracts for private study.\n  Do not treat this site as a substitute for the Official text, firm manuals, or professional advice.\n</aside>',
    '<aside class="callout pack-disclaimer" id="pack-disclaimer">\n  <strong>Disclaimer — personal study pack.</strong>\n  These IAS 16 pages are <strong>personal study notes</strong> for private learning. They are <strong>not</strong> accounting, legal, or professional advice, and are <strong>not</strong> for commercial or mass redistribution.\n  Official Standards remain authoritative. Big4 / firm-manual extracts and third-party financial-statement examples appear only as short teaching paraphrase or cited figures for private study; the pack owner has legal counsel.\n  Do not treat this site as a substitute for the Official text, firm manuals, or issuer financial statements.\n</aside>',
    '<aside class="callout pack-disclaimer" id="pack-disclaimer">\n  <strong>Disclaimer — personal study pack.</strong>\n  These IAS 2 pages are <strong>personal study notes</strong> for private learning. They are <strong>not</strong> accounting, legal, or professional advice, and are <strong>not</strong> for commercial or mass redistribution.\n  Official Standards remain authoritative. Big4 / firm-manual extracts and third-party financial-statement examples appear only as short teaching paraphrase or cited figures for private study; the pack owner has legal counsel.\n  Do not treat this site as a substitute for the Official text, firm manuals, or issuer financial statements.\n</aside>',
    '<aside class="callout pack-disclaimer note-box" id="pack-disclaimer">\n    <strong>Disclaimer — personal study pack.</strong>\n    These IAS 2 pages are <strong>personal study notes</strong> for private learning. They are <strong>not</strong> accounting, legal, or professional advice, and are <strong>not</strong> for commercial or mass redistribution.\n    Official Standards remain authoritative. Big4 / firm-manual extracts and third-party financial-statement examples appear only as short teaching paraphrase or cited figures for private study; the pack owner has legal counsel.\n    Do not treat this site as a substitute for the Official text, firm manuals, or issuer financial statements.\n  </aside>',
    '<aside class="callout pack-disclaimer" id="pack-disclaimer">\n  <strong>Disclaimer — personal study pack.</strong>\n  These IFRS 18 Presentation and Disclosure pages are <strong>personal study notes</strong> for private learning. They are <strong>not</strong> accounting, legal, or professional advice, and are <strong>not</strong> for commercial or mass redistribution.\n  Official Standards remain authoritative. Big4 / firm-manual material appears only as short teaching paraphrase or cited extracts for private study.\n  Do not treat this site as a substitute for the Official text, firm manuals, or professional advice.\n</aside>',
    '<aside class="callout pack-disclaimer" id="pack-disclaimer">\n  <strong>Disclaimer — personal study pack.</strong>\n  These IFRS 18 pages are <strong>personal study notes</strong> for private learning. They are <strong>not</strong> accounting, legal, or professional advice, and are <strong>not</strong> for commercial or mass redistribution.\n  Official Standards remain authoritative. Big4 / firm-manual extracts and third-party financial-statement examples appear only as short teaching paraphrase or cited figures for private study; the pack owner has legal counsel.\n  Do not treat this site as a substitute for the Official text, firm manuals, or issuer financial statements.\n</aside>',
)


def _exact_base_aside(html):
    """The one known Disclaimer aside this base page contains, or None."""
    found = [block for block in DISCLAIMER_KNOWN_ASIDES if block in html]
    if len(found) == 1:
        return found[0]
    return None


def _find_all(html, block):
    spans = []
    start = 0
    while True:
        at = html.find(block, start)
        if at < 0:
            return spans
        spans.append((at, at + len(block), block))
        start = at + len(block)


def _only_whitespace_before_nav(html, end):
    """True when end is followed only by whitespace and the footer-nav comment."""
    nav = html.find(DISCLAIMER_NAV, end)
    if nav < 0:
        return False
    return html[end:nav].strip() == ""


def _approved_disclaimer(html, path, base_aside):
    """The one shell or this page's own base aside, or None.

    The shell counts only directly before <!-- footer-nav:start -->.
    A pasted aside counts only when it is the exact aside this page had
    at base, in that page's base slot. Another wording from the same pack
    does not count.
    """
    shells = _find_all(html, DISCLAIMER_SHELL)
    asides = _find_all(html, base_aside) if base_aside else []
    if len(shells) + len(asides) != 1:
        return None
    if shells:
        start, end, _block = shells[0]
        if _only_whitespace_before_nav(html, end):
            return start, end
        return None
    start, end, block = asides[0]
    if _only_whitespace_before_nav(html, end):
        return start, end
    if (
        path in IAS2_NOTE_PAGES
        and "note-box" in block
        and html.startswith("\n</footer>", end)
    ):
        return start, end
    return None


def _remove_disclaimer_block(html, start, end):
    """Drop the aside's lines, keeping the linebreak of the following line."""
    line = html.rfind("\n", 0, start) + 1
    if html[line:start].strip() == "":
        start = line
        if start > 0 and html[start - 1] == "\n":
            start -= 1
    return html[:start] + html[end:]


def _ensure_disclaimer_shell(html):
    idx = html.find(DISCLAIMER_NAV)
    if idx < 0:
        return html
    prefix = html[:idx]
    if prefix.rstrip("\n").endswith(DISCLAIMER_SHELL):
        prefix = prefix[:prefix.rfind(DISCLAIMER_SHELL)]
    return prefix.rstrip("\n") + "\n\n" + DISCLAIMER_SHELL + "\n\n" + html[idx:]


def fold_disclaimer_injector(html, path, base_aside=None):
    """Normalise one in-slot Disclaimer to the empty shell before footer-nav.

    The empty shell is accepted only directly before <!-- footer-nav:start -->.
    The old wording is accepted only when it is the exact aside this page
    had at base, in that page's base slot. Anything else, including another
    wording from the same pack, stays.
    """
    if path not in DISCLAIMER_PAGES:
        return html
    found = _approved_disclaimer(html, path, base_aside)
    if not found:
        return html
    start, end = found
    return _ensure_disclaimer_shell(_remove_disclaimer_block(html, start, end))


def load_stamps(text):
    match = re.search(r"var STAMPS = (\{.*?\n  \});", text, re.S)
    if not match:
        raise SystemExit("last-update.js has no STAMPS object")
    import json
    return json.loads(match.group(1))


def logic_same(base, head):
    def mask(text):
        text = STAMPS_OBJ.sub("var STAMPS = {};", text, count=1)
        text = PATHS_OBJ.sub("var PACK_PATHS = [];", text, count=1)
        return text
    return mask(base) == mask(head)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--csv")
    args = parser.parse_args(argv)
    failed = False
    rows = []
    for path in git_paths(args.base):
        base = git_text(args.base, path)
        file = ROOT / path
        if base is None or not file.is_file():
            if path in PR7_DELETED_HTML:
                continue
            print(f"missing existing page {path}")
            failed = True
            continue
        head = file.read_text(encoding="utf-8")
        if PACK_PAGE.fullmatch(path):
            hash_error = stamp_value_failure(head, path, ROOT)
            if hash_error:
                print(hash_error)
                failed = True
            added_error = stamp_added_failure(base, head, path, ROOT)
            if added_error:
                print(added_error)
                failed = True
        if path == SETTINGS_PAGE:
            settings_error = settings_stamp_failure(base, head, ROOT)
            if settings_error:
                print(settings_error)
                failed = True
        base = fold_settings_stamps(base, head, path)
        base = fold_theme_js(base, head, path)
        stamp_error = shared_visual_stamp_failure(base, head, path)
        if stamp_error:
            print(stamp_error)
            failed = True
            continue
        base_n = fold_cf_iframe_floors(norm(base), path)
        head_n = fold_cf_iframe_floors(norm(head), path)
        base_n = fold_cf2018_pr7(fold_style_media(fold_viewport(base_n)), path)
        head_n = fold_cf2018_pr7(fold_style_media(fold_viewport(head_n)), path)
        if path == MAP_NARROW:
            base_n = fold_map_narrow(base_n)
            head_n = fold_map_narrow(head_n)
        if path in UTILITY_PAGES:
            base_n = fold_utility_styles(base_n)
            head_n = fold_utility_styles(head_n)
        base_n = fold_ias16_references_muted(base_n, path)
        head_n = fold_ias16_references_muted(head_n, path)
        base_n = fold_ias2_inline_styles(base_n, path)
        head_n = fold_ias2_inline_styles(head_n, path)
        # Johnny 2026-10-15 23:59 — noindex on 9 IFRS 18 pages; MD-1 body on 14 pages.
        base_n = fold_pr6_cleanup(base_n, path)
        head_n = fold_pr6_cleanup(head_n, path)
        # Johnny 2026-10-16 09:57 — collapse only the nine approved IAS 16 gaps.
        base_n, head_n = fold_ias16_section_gap(base_n, head_n, path)
        # Johnny 2026-10-16 15:32 — move the CF title on base only.
        base_n, head_n = fold_cf2018_shell(base_n, head_n, path)
        # Johnny 2026-10-16 17:11 — IAS 2 title on base only, listed blanks.
        base_n, head_n = fold_ias2_shell(base_n, head_n, path)
        # Johnny 2026-10-16 19:02 — IFRS 18 title text, indent, listed blanks.
        base_n, head_n = fold_ifrs18_shell(base_n, head_n, path)
        if path in IAS2_NOTE_PAGES:
            base_n = fold_ias2_pr5(base_n)
            head_n = fold_ias2_pr5(head_n)
        # Johnny 2026-10-15 20:46 J4 — Disclaimer shell only, on the 44 pack pages.
        # QC r2 E10: the allowed aside is the one this page had at base.
        base_aside = _exact_base_aside(base_n) if path in DISCLAIMER_PAGES else None
        base_n = fold_disclaimer_injector(base_n, path, base_aside)
        head_n = fold_disclaimer_injector(head_n, path, base_aside)
        if path in CF_THEME_VISUALS:
            base_n = fold_cf_theme(base_n)
            head_n = fold_cf_theme(head_n)
        if path == HOME:
            if LINK not in head:
                print("homepage is missing the Settings link")
                failed = True
            # The Settings link is already on main. Strip it on both sides so an
            # unchanged homepage is not reported as an edit, and a new link on
            # an older base still compares equal.
            head_n = head_n.replace(LINK, "", 1)
            base_n = base_n.replace(LINK, "", 1)
        # Johnny 2026-10-14 Option S / PR #124 — stamp gate ignores cite DOM order; check-incremental owns teaching.
        base_n = fold_cite_order(base_n)
        head_n = fold_cite_order(head_n)
        # Row #42 A1–A6, Johnny 2026-10-14 21:39
        if path in ROW42_A1_A6_LINES:
            base_n, head_n = fold_row42_a1_a6(base_n, head_n, path)
        if head_n != base_n and path not in CONTENT_ALLOW:
            print(f"HTML changed outside ?v= and the homepage link: {path}")
            failed = True
    try:
        base_css = git_text(args.base, SHARED_VISUAL_CSS)
    except KeyError:
        base_css = None
    css_file = ROOT / SHARED_VISUAL_CSS
    if base_css is not None and css_file.is_file():
        stamp_error = shared_visual_stamp_failure(
            base_css, css_file.read_text(encoding="utf-8"), SHARED_VISUAL_CSS
        )
        if stamp_error:
            print(stamp_error)
            failed = True
    base_js = git_text(args.base, "_shared/last-update.js")
    head_js = (ROOT / "_shared" / "last-update.js").read_text(encoding="utf-8")
    if not logic_same(base_js, head_js):
        print("last-update.js changed more than stamp data")
        failed = True
    base_stamps = load_stamps(base_js)
    head_stamps = load_stamps(head_js)
    if "site" not in head_stamps:
        print("site stamp missing")
        failed = True
    for key, base_stamp in sorted(base_stamps.items()):
        head_stamp = head_stamps.get(key)
        if not head_stamp:
            print(f"stamp removed: {key}")
            failed = True
            continue
        only = STAMP.fullmatch(head_stamp["text"]) and set(head_stamp) == set(base_stamp)
        if not only:
            print(f"stamp shape changed: {key}")
            failed = True
        rows.append({
            "page": key,
            "base_stamp": base_stamp["text"],
            "head_stamp": head_stamp["text"],
            "only_stamp_changed": "yes" if only else "no",
        })
    if args.csv:
        with open(args.csv, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["page", "base_stamp", "head_stamp", "only_stamp_changed"],
            )
            writer.writeheader()
            writer.writerows(rows)
    for row in rows:
        print(
            f"{row['page']}\t{row['base_stamp']}\t{row['head_stamp']}\t{row['only_stamp_changed']}"
        )
    for error in check_source_iframe_stamps(ROOT):
        print(error)
        failed = True
    for error in inner_css_stamp_errors(ROOT):
        print(error)
        failed = True
    try:
        base_include = git_text(args.base, CHROME_INCLUDE)
    except KeyError:
        base_include = None
    include_path = ROOT / CHROME_INCLUDE
    if base_include is not None and include_path.is_file():
        include_error = chrome_include_failure(
            base_include,
            include_path.read_text(encoding="utf-8"),
            ROOT,
        )
        if include_error:
            print(include_error)
            failed = True
    if failed:
        return 1
    print("stamp-only: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
