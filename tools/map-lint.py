#!/usr/bin/env python3
"""Fail Concept Map markup that breaks Pick A.

IAS 16 already has 34 cite chips on the master map. That count may stay.
A new cite on any of the four Concept Maps fails. Glyph arrows fail.
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


def selector_blocks(text):
    text = strip_comments(text)
    blocks = []
    for match in re.finditer(r"([^{}]+)\{([^{}]*)\}", text):
        blocks.append((match.group(1).strip(), match.group(2)))
    return blocks


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
        if not found or found.group(1) != digest:
            errors.append(f"map-box import stamp mismatch in {rel}")
        if re.search(r"var\(--tb-|var\(--t-meta\)", strip_comments(text)):
            errors.append(f"teaching type token in map scope: {rel}")
        for selector, body in selector_blocks(text):
            if ".m-" in selector and re.search(
                r"\b(?:border|background|font-size)\s*:", body
            ):
                errors.append(f"pack look on .m-* in {rel}: {selector[:80]}")
            if "dashed" in body and ".m-see" not in selector and "matrix" not in selector and "n-a" not in selector and "na " not in selector:
                errors.append(f"dashed outside .m-see in {rel}: {selector[:80]}")
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
