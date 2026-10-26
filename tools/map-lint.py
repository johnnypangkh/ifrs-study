#!/usr/bin/env python3
"""Fail Concept Map markup that breaks Pick A or the #86 arrow / L0 locks.

IAS 16 master cite cap is 4 (Johnny SIGNED FINAL-B2 2026-10-20 19:31 / #98).
The three #98 plates cite 0. The remaining 4 are ch07 Disclosure. Do not trim them.
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
    ".m-tl-span",  # #104 Wave2a B16: MF timeline span (muted + dashed), ch05 only
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
# IAS 16 master: Johnny SIGNED FINAL-B2 2026-10-20 19:31 / #98.
# Three #98 plates cite 0. Remaining 4 are ch07 Disclosure (untouched).
# CF's one cite is the page-header purpose chip, not a new map cite.
CITE_ALLOW = {
    "cf-2018/draft-v1-linked/index.html": 1,
    "ias-16/draft-v1-linked/visuals/master-concept-map.html": 4,
    "ias-2/draft-v1-linked/visuals/map-formula-board.html": 0,
    "ifrs-18/draft-v1-linked/index.html": 0,
}
# #98 plates may reuse these bare shared classes. Any other collision fails.
# Catches a bare shared rule only (the tl-row failure). Not other width regressions.
# #109 adds bare `.m-tl` (timeline root). Child `.m-tl-*` rules are descendants,
# not bare selectors, so they are not in this set.
PLATE98_SHARED_OK = {"cap", "inner-board", "see-bit", "see-label", "m-tl"}
# #109 do-now #3. Map chrome paint must sit on an alias:
# L* / m-flow|link|visit / m-tl* (D4 .cell / .limb count as the alias names).
# A plate-parent override of .m-tl* is placement and stays. A new class shaped
# like timeline/map chrome (.foo-cell, .tl-axis, …) fails. Pre-#109 pack
# classes that already paint stay listed so the gate does not blank them.
MAP_CHROME_ALIAS = re.compile(
    r"^(?:m-l[0-4]|m-flow|m-link|m-visit|m-tl(?:-[\w-]+)?|cell|limb)$"
)
CHROME_SHAPED = re.compile(
    r"(?:timeline|(?:^|-)tl-(?:axis|shaft|line|ring|flag|pole|ribbon|span)$|-(?:cell|limb)$)"
)
PACK_CHROME_KNOWN = frozenset({
    "case-cell",
    "cmp-cell",
    "goes-cell",
    "impair-ca-cell",
    "impair-formula-cell",
    "lens-cell",
    "m-cell",
    "rev-cell",
    "rm-cell",
    "rmx-cell",
    "split-cell",
    "when-cell",
})
PLACEMENT_PARENT = re.compile(
    r"\.(?:plate|ppe-tl-row|ch04-reval|ch05-dep|ch04-impair)\b"
)
PAINT_DECL = re.compile(r"\b(?:border|background|font-size)\s*:")
PLATE98_SECTIONS = (
    ("ias-16/draft-v1-linked/visuals/ch05-depreciation.html", "ch05-dep"),
    ("ias-16/draft-v1-linked/visuals/ch04-models.html", "ch04-reval"),
    ("ias-16/draft-v1-linked/visuals/ch04-models.html", "ch04-impair"),
)
BARE_CLASS_RE = re.compile(
    r"\.([A-Za-z_][\w-]*)(?::(?::)?[\w-]+(?:\([^)]*\))?)*"
)
IMPORT_URL_RE = re.compile(r'@import\s+url\("([^"?]+)')
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


# L3: a ▼/▾ inside a stem or arrow class is a glyph connector.
# ch06-measurement.html still contains the character. The stamp gate folds
# → ↓ ▶ and not ▼, and this PR does not edit the stamp tool, so the span
# stays. It is not the connector once map-box paints .mx-stem::after and
# clears .mx-stem-arrow. Any other hit fails. If that head is removed, the
# held line fails too.
STAMP_HELD_GLYPH = "cf-2018/draft-v1-linked/visuals/ch06-measurement.html"
GLYPH_CONNECTOR_RE = re.compile(r"[▼▾]")
GLYPH_CLASS_RE = re.compile(r"""class=["'][^"']*(?:stem|arrow)""")
SHAFT_CLASS_RE = re.compile(r"""class=(["'])([^"']*)\1""")
SHAFT_TOKEN_RE = re.compile(
    r"\b(?:stem-shaft|st-h-shaft|m-shaft|pack-flow-shaft|map-visit-arrow)\b"
)
SHAFT_ROLE_RE = re.compile(r"\b(?:m-flow|m-link|m-visit)\b")


def measurement_stem_rewritten(box):
    return (
        re.search(r"\.mx-stem::after\s*\{[^}]*border-top\s*:", box) is not None
        and re.search(r"\.mx-stem-arrow\s*\{[^}]*color:\s*transparent", box) is not None
    )


def glyph_connector_errors(text, rel, box):
    errors = []
    held_ok = rel == STAMP_HELD_GLYPH and measurement_stem_rewritten(box)
    for line_no, line in enumerate(text.splitlines(), 1):
        if not GLYPH_CONNECTOR_RE.search(line) or not GLYPH_CLASS_RE.search(line):
            continue
        if held_ok and 'class="mx-stem-arrow"' in line:
            continue
        errors.append(f"glyph connector in {rel}:{line_no}")
    return errors


def shaft_role_errors(text, rel):
    """L4: a map shaft needs m-flow, m-link, or m-visit on the same element."""
    errors = []
    for line_no, line in enumerate(text.splitlines(), 1):
        for match in SHAFT_CLASS_RE.finditer(line):
            classes = match.group(2)
            if SHAFT_TOKEN_RE.search(classes) and not SHAFT_ROLE_RE.search(classes):
                errors.append(f"shaft missing semantic role in {rel}:{line_no}")
    return errors


# #121 Gap G2. Kit IDs B01–B21 only. An unknown data-brick value FAILs.
# Phase-1 loci record the Wave B files. Missing attrs do not fail:
# the 35 zero-brick maps stay untagged, and deferred IDs are not required.
BRICK_IDS = frozenset(f"B{n:02d}" for n in range(1, 22))
BRICK_PHASE1_LOCI = (
    "ias-16/draft-v1-linked/visuals/ch05-depreciation.html",
    "ias-16/draft-v1-linked/visuals/master-concept-map.html",
)
BRICK_ATTR_RE = re.compile(
    r"""data-brick\s*=\s*(?:(?P<q>["'])(?P<quoted>.*?)(?P=q)|(?P<bare>[^\s"'=<>`]+))"""
)


def data_brick_errors(text, rel):
    """#121: data-brick must be a kit ID B01–B21.

    Does not require an attr. BRICK_PHASE1_LOCI names the Wave B files
    (ch05 + master) and is not a force-tag. Zero-brick maps stay quiet.
    """
    errors = []
    for line_no, line in enumerate(text.splitlines(), 1):
        for match in BRICK_ATTR_RE.finditer(line):
            value = match.group("quoted")
            if value is None:
                value = match.group("bare")
            if value not in BRICK_IDS:
                errors.append(f"unknown data-brick {value!r} in {rel}:{line_no}")
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
        errors.extend(map_chrome_alias_errors(text, rel))
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
    box = (ROOT / "_shared/modules/visuals/map-box.css").read_text(encoding="utf-8")
    for path in html_scan_paths():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        errors.extend(sibling_head_errors(text, rel))
        errors.extend(glyph_connector_errors(text, rel, box))
        errors.extend(shaft_role_errors(text, rel))
        errors.extend(data_brick_errors(text, rel))
    if "body.embed .m-l0" not in box or not re.search(
        r"body\.embed \.m-l0[\s\S]{0,240}?border:\s*0", box
    ):
        errors.append("map-box missing embed L0 neutralize")
    if not re.search(r"\.cfmap\.m-l0 \.status-frame\s*\{[^}]*border:\s*0", box):
        errors.append("map-box missing CF status-frame L0 neutralize")
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
    errors.extend(field_errors(box))
    errors.extend(plate98_collision_errors())
    return errors


BOARD_HOST = re.compile(
    r"(?:\.m-l0|#conceptMap|\.cfmap\b|\.std-frame|\.ppe\.pack|\.ias2\.m-map)"
)
FIELD_IMAGE = re.compile(
    r"background-image\s*:[^;}]*(?:repeating-(?:linear|radial)-gradient|radial-gradient|linear-gradient)"
)
ML0_SUBJECT = re.compile(r"^\.m-l0(?:[:]{1,2}[\w-]+)*$")


def _selector_is_ml0(selector):
    """True when a selector part is the board host `.m-l0` itself."""
    for part in split_selectors(selector):
        if ML0_SUBJECT.fullmatch(part.strip()):
            return True
    return False


def field_errors(box):
    """#122: graph-paper field retired. Solid --bg only. Residual field FAILs."""
    errors = []
    for rel in MAPS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        if "m-l0" not in text:
            errors.append(f"Concept Map board lacks .m-l0: {rel}")
    for selector, body in selector_blocks(box):
        if _selector_is_ml0(selector) and FIELD_IMAGE.search(body):
            errors.append(
                f"residual graph-paper field on .m-l0: {selector.strip()[:80]}"
            )
    for rel in MAP_CSS:
        text = strip_comments((ROOT / rel).read_text(encoding="utf-8"))
        if "--map-field-" in text:
            errors.append(f"residual --map-field- token in {rel}")
        for selector, body in selector_blocks(text):
            if BOARD_HOST.search(selector) and FIELD_IMAGE.search(body):
                errors.append(f"pack-local field image in {rel}: {selector.strip()[:80]}")
    for path in ROOT.rglob("*.css"):
        rel = path.relative_to(ROOT).as_posix()
        if "_archive" in path.parts or "node_modules" in path.parts:
            continue
        if "--map-field-" in path.read_text(encoding="utf-8"):
            errors.append(f"residual --map-field- token in {rel}")
    return errors


def _shared_css_texts():
    """`_shared/visuals.css` (and its @import tree) plus `_shared/type-scale.css`."""
    texts = []
    seen = set()

    def walk(path):
        path = path.resolve()
        if path in seen or not path.is_file():
            return
        seen.add(path)
        text = path.read_text(encoding="utf-8")
        texts.append(text)
        for match in IMPORT_URL_RE.finditer(text):
            walk(path.parent / match.group(1))

    walk(ROOT / "_shared/visuals.css")
    walk(ROOT / "_shared/type-scale.css")
    return texts


def bare_shared_classes(css_texts):
    """Class names whose whole selector is `.name`, optional pseudos only."""
    names = set()
    for text in css_texts:
        stripped = COMMENT_RE.sub("", text)
        for selector in re.findall(r"([^{}@;]+)\{", stripped):
            for part in selector.split(","):
                part = part.strip()
                match = BARE_CLASS_RE.fullmatch(part)
                if match:
                    names.add(match.group(1))
    return names


def plate98_section_classes(html, section):
    match = re.search(
        rf"map-section:{re.escape(section)}:start(.*?)map-section:{re.escape(section)}:end",
        html,
        re.S,
    )
    if match is None:
        return set()
    classes = set()
    for chunk in re.findall(r'class="([^"]+)"', match.group(1)):
        classes.update(chunk.split())
    return classes


def map_chrome_alias_errors(css_text, rel="pack.css"):
    """#109: new map chrome must alias into L* / m-flow|link|visit / m-tl*.

    Placement overrides under a plate parent stay. Inventing a pack paint
    class (.foo-cell, a raw .tl-axis, an unscoped .m-tl* repaint) fails.
    """
    errors = []
    for selector, body in selector_blocks(css_text):
        if not PAINT_DECL.search(body):
            continue
        classes = set()
        for sel in split_selectors(selector):
            classes.update(re.findall(r"\.([A-Za-z0-9_-]+)", sel))
        placed = PLACEMENT_PARENT.search(selector) is not None
        for name in sorted(classes):
            if MAP_CHROME_ALIAS.match(name):
                if name.startswith("m-tl") and not placed:
                    errors.append(
                        "pack timeline paint without plate parent in "
                        f"{rel}: {selector.strip()[:80]}"
                    )
                    break
                continue
            if CHROME_SHAPED.search(name) and name not in PACK_CHROME_KNOWN:
                errors.append(
                    f"invented map chrome class in {rel}: .{name} "
                    f"({selector.strip()[:60]})"
                )
                break
    return errors


def plate98_shared_collisions(plate_classes, bare_classes):
    """Plate classes that hit a bare shared rule and are not allowlisted."""
    return sorted((set(plate_classes) & set(bare_classes)) - PLATE98_SHARED_OK)


def plate98_collision_errors():
    plate = set()
    for rel, section in PLATE98_SECTIONS:
        html = (ROOT / rel).read_text(encoding="utf-8")
        plate |= plate98_section_classes(html, section)
    hits = plate98_shared_collisions(plate, bare_shared_classes(_shared_css_texts()))
    return [
        "shared class collision on #98 plate: "
        f"{name} (not in PLATE98_SHARED_OK)"
        for name in hits
    ]


def main():
    errors = lint()
    if errors:
        for item in errors:
            print(item)
        raise SystemExit(1)
    print("map-lint: PASS")


if __name__ == "__main__":
    main()
