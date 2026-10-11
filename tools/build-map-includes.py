#!/usr/bin/env python3
"""Splice IAS 16 chapter map sections into the master concept map.

A chapter visual owns the section once:

    <!-- map-section:ch06:start -->
    <section class="plate">...</section>
    <!-- map-section:ch06:end -->

The master names that block. A master-owned wrapper around the comments
keeps data-phase-start / data-phase-end and any spine class. Optional
inject-class and inject-attr on the start comment are copied onto the
included root tag, because some selectors match the plate itself:

    <div class="map-include" data-phase-start data-phase-end>
      <!-- include:ch06-derecognition.html#ch06:start inject-class="ch06-map" -->
      ...generated section...
      <!-- include:ch06-derecognition.html#ch06:end -->
    </div>

The script rewrites only the generated span. It does not fetch at
runtime and does not add an iframe. A second run rewrites nothing.
Master blocks with no include comment are left untouched.
"""

import sys

from map_sections import (
    PACK,
    extract_map_section,
    iter_includes,
    rendered_body,
)


def pack_html_files():
    files = []
    for path in sorted(PACK.rglob("*.html")):
        if path.is_symlink() or not path.is_file():
            continue
        files.append(path)
    return files


def outermost_includes(text):
    """Includes that are not nested inside another include."""
    includes = list(iter_includes(text))
    outers = []
    for include in includes:
        inside = False
        for other in includes:
            if (
                other["start_end"] < include["start_end"]
                and include["end_start"] <= other["end_start"]
            ):
                inside = True
                break
        if not inside:
            outers.append(include)
    return outers


def fill_include(text, include, path):
    source_path = (path.parent / include["file"]).resolve()
    try:
        source_path.relative_to(PACK.resolve())
    except ValueError:
        raise SystemExit(f"{path}: include escapes the IAS 16 pack: {include['file']}")
    if not source_path.is_file():
        raise SystemExit(f"{path}: missing include source {include['file']}")
    source_html = source_path.read_text(encoding="utf-8")
    source_body = extract_map_section(
        source_html,
        include["id"],
        source_path.relative_to(PACK.parent.parent),
    )
    interior = rendered_body(
        source_body,
        include["indent"],
        include["classes"],
        include["attrs"],
    )
    same = text[include["start_end"]:include["end_start"]] == interior
    updated = text[:include["start_end"]] + interior + text[include["end_start"]:]
    return updated, not same


def splice(path):
    text = path.read_text(encoding="utf-8")
    if "<!-- include:" not in text:
        return False
    original = text
    # Outermost first, from the end of the file so earlier offsets stay
    # valid. A nested include (the chapter 5 axis inside a chapter 4
    # section) is filled when its own file is spliced; the outer copy
    # then takes that already-filled section. Repeating until the
    # outermost bodies match keeps a second run from rewriting.
    for _round in range(8):
        outers = outermost_includes(text)
        if not outers:
            break
        delta = False
        for include in reversed(outers):
            text, changed = fill_include(text, include, path)
            rel = path.relative_to(PACK.parent.parent)
            if changed:
                delta = True
                print(f"splice {rel} <= {include['file']}#{include['id']}")
            else:
                print(f"unchanged {rel} {include['file']}#{include['id']}")
        if not delta:
            break
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    if not PACK.is_dir():
        raise SystemExit(f"missing pack {PACK}")
    seen = False
    for path in pack_html_files():
        text = path.read_text(encoding="utf-8")
        if "<!-- include:" not in text:
            continue
        seen = True
        splice(path)
    if not seen:
        raise SystemExit("no <!-- include: --> markers under ias-16/draft-v1-linked/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
