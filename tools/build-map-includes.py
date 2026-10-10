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
from pathlib import Path

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


def splice(path):
    text = path.read_text(encoding="utf-8")
    if "<!-- include:" not in text:
        return False
    pieces = []
    cursor = 0
    changed = False
    for include in iter_includes(text):
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
        pieces.append(text[cursor:include["start_end"]])
        pieces.append(interior)
        if text[include["start_end"]:include["end_start"]] != interior:
            changed = True
            print(
                f"splice {path.relative_to(PACK.parent.parent)} "
                f"<= {include['file']}#{include['id']}"
            )
        else:
            print(
                f"unchanged {path.relative_to(PACK.parent.parent)} "
                f"{include['file']}#{include['id']}"
            )
        cursor = include["end_start"]
    pieces.append(text[cursor:])
    updated = "".join(pieces)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        changed = True
    return changed


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
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    sys.exit(main())
