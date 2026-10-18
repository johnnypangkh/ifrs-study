#!/usr/bin/env python3
"""Fail Concept Map markup that breaks Pick A or the #86 arrow / L0 locks.

IAS 16 already has 34 cite chips on the master map. That count may stay.
A new cite on any of the four Concept Maps fails. Glyph arrows fail.
Sibling .stem-head / .m-arrow / .st-h-head fail on every live pack page.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPS = (
    "cf-2018/draft-v1-linked/index.html",
    "ias-16/draft-v1-linked/visuals/master-concept-map.html",
    "ias-2/draft-v1-linked/visuals/map-formula-board.html",
    "ifrs-18/draft-v1-linked/index.html",
)
MAP_CSS = (
    "cf-2018/draft-v1-linked/assets/map.css",
    "ifrs-18/draft-v1-linked/assets/map.css",
    "ias-16/draft-v1-linked/visuals/ias16.css",
    "ias-2/draft-v1-linked/visuals/ias2.css",
    "ifrs-18/draft-v1-linked/visuals/map-jumpboard.css",
)
# Index maps import map-box themselves. Chapter kits load visuals.css,
# which already imports it, so those files are not required to repeat it.
MAP_CSS_IMPORT = (
    "cf-2018/draft-v1-linked/assets/map.css",
    "ifrs-18/draft-v1-linked/assets/map.css",
)
# Timeline, N/A, and event marks. Not see-also chips. TOP 4 stays out.
DASH_OK = (
    ".m-see",
    "matrix",
    "n-a",
    "na ",
    ".day",
    ".incidental",
    ".cmp-na",
    ".cost-out",
    ".period-fade",
    ".v-lead",
    ".v-tail",
    ".reval-event",
)
OWNED_SUBJECT = {
    "plate",
    "peer",
    "inner-rail",
    "item-rows",
    "inner-detail",
    "soft-note",
    "thin-tip",
    "see",
    "disc-band",
    "pack-stop",
}
L4_SUBJECT = {"soft-note", "thin-tip"}
LOOK_PROP = re.compile(
    r"(?:^|[;{\s])(?P<name>border(?:-(?:top|right|bottom|left))?(?:-(?:width|style|color))?"
    r"|background(?:-color|-image)?|font-size)\s*:"
)
PICK_A_CLASS = re.compile(
    r"\.m-(?:l[0-4]|see|stop|warn|result|strip|rule|pill|flow|link|visit)\b"
)
SIBLING_HEAD_RE = re.compile(
    r"""class=["'][^"']*\b(?:stem-head|m-arrow|st-h-head)\b"""
)
HEAD_CLASS_RE = re.compile(r"\.(?:stem-head|m-arrow|st-h-head)\b")
MAP_PARENTS = (
    "ias-16/draft-v1-linked/index.html",
    "ias-2/draft-v1-linked/index.html",
)
INLINE_MAPS = (
    "cf-2018/draft-v1-linked/index.html",
    "ifrs-18/draft-v1-linked/index.html",
)
# Base counts at c488600. IAS 16's 34 stay until Content marks destinations.
# CF's one cite is the page-header purpose chip, not a new map cite.
CITE_ALLOW = {
    "cf-2018/draft-v1-linked/index.html": 1,
    "ias-16/draft-v1-linked/visuals/master-concept-map.html": 34,
    "ias-2/draft-v1-linked/visuals/map-formula-board.html": 0,
    "ifrs-18/draft-v1-linked/index.html": 0,
}
GLYPHS = ("→", "↓", "▶")
COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)
IMPORT_RE = re.compile(
    r'@import\s+url\("(?:\.\./)+_shared/modules/visuals/map-box\.css\?v=([0-9a-f]{12})"\)'
)


def strip_comments(text):
    return COMMENT_RE.sub("", text)


def cite_count(text):
    return len(re.findall(r'class="[^"]*\bcite(?:-official)?\b', text))


def split_selectors(selector):
    parts, buf, depth = [], "", 0
    for ch in selector:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(buf)
            buf = ""
        else:
            buf += ch
    parts.append(buf)
    return parts


def subject_classes(selector):
    selector = selector.strip()
    depth = 0
    last = 0
    i = 0
    while i < len(selector):
        ch = selector[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif depth == 0 and ch in ">+~":
            last = i + 1
        elif depth == 0 and ch.isspace():
            j = i
            while j < len(selector) and selector[j].isspace():
                j += 1
            if j < len(selector):
                last = j
            i = j
            continue
        i += 1
    subject = re.sub(r"::?[a-zA-Z-]+(?:\([^)]*\))?", "", selector[last:])
    return set(re.findall(r"\.([A-Za-z0-9_-]+)", subject))


def selector_blocks(text):
    text = strip_comments(text)
    blocks = []
    for match in re.finditer(r"([^{}]+)\{([^{}]*)\}", text):
        blocks.append((match.group(1).strip(), match.group(2)))
    return blocks


def sibling_head_errors(text, rel):
    errors = []
    for line_no, line in enumerate(text.splitlines(), 1):
        if SIBLING_HEAD_RE.search(line):
            errors.append(f"sibling arrow head in {rel}:{line_no}")
    return errors


def html_scan_paths():
    paths = []
    for pack in ("cf-2018", "ias-16", "ias-2", "ifrs-18"):
        root = ROOT / pack / "draft-v1-linked"
        paths.extend(sorted(path for path in root.rglob("*.html") if path.is_file()))
    return paths


def lint():
    errors = []
    for rel in MAPS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for glyph in GLYPHS:
            if glyph in text:
                errors.append(f"glyph {glyph} in {rel}")
        count = cite_count(text)
        allowed = CITE_ALLOW.get(rel, 0)
        if count != allowed:
            errors.append(f"cite count {count} != {allowed} in {rel}")
    module = ROOT / "_shared/modules/visuals/map-box.css"
    digest = __import__("hashlib").sha256(module.read_bytes()).hexdigest()[:12]
    for rel in MAP_CSS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        found = IMPORT_RE.search(text)
        if rel in MAP_CSS_IMPORT and (not found or found.group(1) != digest):
            errors.append(f"map-box import stamp mismatch in {rel}")
        elif found and found.group(1) != digest:
            errors.append(f"map-box import stamp mismatch in {rel}")
        if re.search(r"var\(--tb-|var\(--t-meta\)", strip_comments(text)):
            errors.append(f"teaching type token in map scope: {rel}")
        for selector, body in selector_blocks(text):
            pick = PICK_A_CLASS.sub(
                "",
                re.sub(r":not\(\.m-(?:l[0-4]|see)\)", "", selector),
            )
            if PICK_A_CLASS.search(pick) and re.search(
                r"\b(?:border|background|font-size)\s*:", body
            ):
                errors.append(f"pack look on .m-* in {rel}: {selector[:80]}")
            if "dashed" in body and not any(token in selector for token in DASH_OK):
                errors.append(f"dashed outside .m-see in {rel}: {selector[:80]}")
            sels = split_selectors(selector)
            classes = [subject_classes(sel) for sel in sels]
            owned = [cls for cls in classes if cls & OWNED_SUBJECT]
            if owned and ":hover" not in selector:
                look = [
                    item.group("name")
                    for item in LOOK_PROP.finditer(body)
                    if item.group("name") != "font-size"
                    or (
                        owned
                        and all((cls & L4_SUBJECT) and cls <= L4_SUBJECT for cls in owned)
                        and not any(cls - OWNED_SUBJECT for cls in classes)
                    )
                ]
                if look:
                    errors.append(
                        f"pack look on map-box role in {rel}: {selector.strip()[:80]}"
                    )
            for sel, cls in zip(sels, classes):
                if ":hover" in sel:
                    continue
                if "close" in cls and "contain" in cls and re.search(
                    r"\b(?:border|background)\b", body
                ):
                    errors.append(f"pack close look in {rel}: {sel.strip()[:80]}")
                if (
                    rel.endswith("ias2.css")
                    and "q" in cls
                    and ":not(.m-l1)" not in sel
                    and re.search(r"\b(?:border|background)\s*:", body)
                ):
                    errors.append(f"pack .q look in {rel}: {sel.strip()[:80]}")
                if "tip-note" in cls and ".m-see" not in sel and ":not(.m-see)" not in sel:
                    if re.search(r"\bborder(?:-width|-style|-color)?\s*:", body):
                        errors.append(f"pack tip-note border in {rel}: {sel.strip()[:80]}")
            if HEAD_CLASS_RE.search(selector) and re.search(
                r"\b(?:border|background)\b", body
            ):
                errors.append(f"pack arrow-head look in {rel}: {selector.strip()[:80]}")
    for path in html_scan_paths():
        rel = path.relative_to(ROOT).as_posix()
        errors.extend(sibling_head_errors(path.read_text(encoding="utf-8"), rel))
    box = (ROOT / "_shared/modules/visuals/map-box.css").read_text(encoding="utf-8")
    if "body.embed .m-l0" not in box or not re.search(
        r"body\.embed \.m-l0[\s\S]{0,240}?border:\s*0", box
    ):
        errors.append("map-box missing embed L0 neutralize")
    if ".stem-shaft::after" not in box or ".st-h-shaft::after" not in box or ".m-shaft::after" not in box:
        errors.append("map-box missing canonical shaft ::after head")
    chrome = (ROOT / "_shared/modules/teaching/chrome-1.css").read_text(encoding="utf-8")
    if not re.search(
        r"\.visual-fieldset\.board-l0-onlabel\s*\{[^}]*--stroke-2[^}]*--ink",
        chrome,
    ):
        errors.append("chrome-1 missing B′ fieldset L0")
    for rel in MAP_PARENTS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        if "board-l0-onlabel" not in text or ">Concept Map<" not in text:
            errors.append(f"Map page missing B′ fieldset: {rel}")
    for rel in INLINE_MAPS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        if "board-legend-abs" not in text or ">Concept Map<" not in text:
            errors.append(f"Map page missing B′ on-border label: {rel}")
        if "visual-fieldset" in text:
            errors.append(f"inline Map gained a second frame: {rel}")
    return errors


def main():
    errors = lint()
    if errors:
        for item in errors:
            print(item)
        raise SystemExit(1)
    print("map-lint: PASS")


if __name__ == "__main__":
    main()
