#!/usr/bin/env python3
"""Fail the IAS 16 tree when a map plate is duplicated or a local ?v= is stale.

Four checks:

- DRIFT. The normalised body of an include region must match its chapter
  map-section. data-phase-* attributes, ?v=, and classes or attributes
  named by inject-class / inject-attr are ignored, and whitespace is
  collapsed. A hand edit of the generated copy fails here.
- DUPLICATE. A normalised plate or disc-band section must not appear
  twice outside a matching include region. A drifted include does not
  count as matching, so the edited master copy and the chapter source
  are both counted.
- AXIS. The during-use life-cycle block (map-section:ch05-axis, the
  5.4 Begins/Ceases axis) must not appear twice outside a matching
  include. Whitespace between tags is ignored, so a pretty-printed
  copy still counts. A copy inside .reval-plate or .impair-plate is
  deferred until those plates move to chapter 4: it must still match
  the chapter axis, and it is not itself a failure. Any other copy
  outside a matching include fails.
- STAMP. A local .css / .js / .html ?v= under ias-16/draft-v1-linked/
  must be 12 lowercase hex digits. search-index.js and last-update.js
  are owned by their own generators and are not checked here.
"""

import re
import sys

from map_sections import (
    HEX12,
    PACK,
    extract_map_section,
    find_plate_sections,
    iter_includes,
    iter_versioned_refs,
    normalise,
    section_inside,
    strip_injected,
)

# These master plates still draw the shared Begins/Ceases axis so the
# revaluation-date and impairment-date bands keep their scale. The plates
# move to ch04 in a later pass. Until then a matching copy inside them is
# listed, not failed. A drifted copy, or a copy anywhere else outside a
# matching include, fails.
AXIS_ID = "ch05-axis"
DEFERRED_AXIS_PLATES = ("reval-plate", "impair-plate")
TAG = re.compile(r"<(/?)([A-Za-z][\w:-]*)\b([^>]*)>")


def pack_html_files():
    files = []
    for path in sorted(PACK.rglob("*.html")):
        if path.is_symlink() or not path.is_file():
            continue
        files.append(path)
    return files


def pack_text_files():
    files = []
    for path in sorted(PACK.rglob("*")):
        if path.is_symlink() or not path.is_file():
            continue
        if path.suffix.lower() not in {".html", ".css", ".js"}:
            continue
        files.append(path)
    return files


def rel(path):
    return path.relative_to(PACK.parent.parent).as_posix()


def matching_body(include, source_html, origin):
    source = extract_map_section(source_html, include["id"], origin)
    body = strip_injected(include["body"], include["classes"], include["attrs"])
    return normalise(body) == normalise(source)


def check_includes(html_files):
    errors = []
    regions = {}
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        if "<!-- include:" not in text:
            regions[path] = []
            continue
        spans = []
        for include in iter_includes(text):
            source_path = (path.parent / include["file"]).resolve()
            try:
                source_path.relative_to(PACK.resolve())
            except ValueError:
                errors.append(f"DRIFT: {rel(path)} include escapes the pack: {include['file']}")
                spans.append((include["start_end"], include["end_start"], False, include))
                continue
            if not source_path.is_file():
                errors.append(f"DRIFT: {rel(path)} missing source {include['file']}")
                spans.append((include["start_end"], include["end_start"], False, include))
                continue
            source_html = source_path.read_text(encoding="utf-8")
            try:
                ok = matching_body(include, source_html, rel(source_path))
            except SystemExit as exc:
                errors.append(f"DRIFT: {exc}")
                ok = False
            if not ok:
                errors.append(
                    "DRIFT: "
                    f"{rel(path)} include {include['file']}#{include['id']} "
                    f"does not match {rel(source_path)} map-section {include['id']}"
                )
            spans.append((include["start_end"], include["end_start"], ok, include))
        regions[path] = spans
    return errors, regions


def inject_classes(regions):
    names = []
    seen = set()
    for spans in regions.values():
        for _begin, _end, _ok, include in spans:
            for name in include["classes"]:
                if name not in seen:
                    seen.add(name)
                    names.append(name)
    return names


def place_of(path, section, drifted):
    where = rel(path)
    for begin, end, include in drifted:
        if begin <= section["start"] < end:
            return where + f" (drifted include {include['file']}#{include['id']})"
    return where


def check_duplicates(html_files, regions):
    errors = []
    classes = inject_classes(regions)
    groups = {}
    by_aria = {}
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        spans = regions.get(path, [])
        matching = [(begin, end) for begin, end, ok, _include in spans if ok]
        drifted = [(begin, end, include) for begin, end, ok, include in spans if not ok]
        any_include = [(begin, end) for begin, end, _ok, _include in spans]
        for section in find_plate_sections(text):
            if section_inside(section["start"], matching):
                continue
            raw = strip_injected(section["raw"], classes, [])
            key = normalise(raw)
            groups.setdefault(key, []).append((path, section, drifted))
            if section["aria"]:
                identity = (section["kind"], section["aria"])
                by_aria.setdefault(identity, []).append(
                    (path, section, drifted, section_inside(section["start"], any_include))
                )
    reported = set()
    for key, hits in groups.items():
        if len(hits) < 2:
            continue
        aria = hits[0][1]["aria"] or key[:80]
        places = [place_of(path, section, drifted) for path, section, drifted in hits]
        reported.add(tuple(places))
        lines = "\n".join(f"  - {place}" for place in places)
        errors.append(
            f'DUPLICATE: normalised {hits[0][1]["kind"]} "{aria}" appears '
            f"{len(hits)} times outside a matching include\n{lines}"
        )
    for (kind, aria), hits in by_aria.items():
        drifted_hits = [hit for hit in hits if hit[2] and section_inside(hit[1]["start"], [(b, e) for b, e, _inc in hit[2]])]
        outside_hits = [hit for hit in hits if not hit[3]]
        if not drifted_hits or not outside_hits:
            continue
        places = []
        for path, section, drifted, _inside in drifted_hits + outside_hits:
            places.append(place_of(path, section, drifted))
        marker = tuple(places)
        if marker in reported:
            continue
        reported.add(marker)
        lines = "\n".join(f"  - {place}" for place in places)
        errors.append(
            f'DUPLICATE: {kind} "{aria}" appears {len(places)} times '
            f"outside a matching include\n{lines}"
        )
    return errors


def axis_key(text):
    """Normalise an axis block, including whitespace between tags."""
    return re.sub(r">\s+<", "><", normalise(text))


def element_end(html, start):
    match = re.match(r"<([A-Za-z][\w:-]*)\b([^>]*)>", html[start:])
    if not match:
        return None
    name = match.group(1).lower()
    if match.group(2).rstrip().endswith("/"):
        return start + match.end()
    depth = 1
    i = start + match.end()
    while depth and i < len(html):
        token = TAG.search(html, i)
        if not token:
            return None
        closing = bool(token.group(1))
        same = token.group(2).lower() == name
        self_close = (not closing) and token.group(3).rstrip().endswith("/")
        if same and not self_close:
            depth += -1 if closing else 1
        i = token.end()
    return i if depth == 0 else None


def iter_axis_blocks(html):
    """Yield (start, end, raw) for each 5.4 During use + Begins/Ceases pair."""
    cursor = 0
    needle = '<div class="lc-head-k">'
    while True:
        start = html.find(needle, cursor)
        if start < 0:
            return
        cursor = start + len(needle)
        first_end = element_end(html, start)
        if first_end is None:
            continue
        second = first_end
        while second < len(html) and html[second].isspace():
            second += 1
        if not html.startswith('<div class="lc-head-axis">', second):
            continue
        end = element_end(html, second)
        if end is None:
            continue
        yield start, end, html[start:end]


def plate_name(start, sections):
    for section in sections:
        if section["start"] <= start < section["end"]:
            for name in DEFERRED_AXIS_PLATES:
                if name in section["raw"][:160]:
                    return name
    return ""


def axis_source(html_files):
    marker = f"<!-- map-section:{AXIS_ID}:start -->"
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        if marker not in text:
            continue
        body = extract_map_section(text, AXIS_ID, rel(path))
        return axis_key(body), path
    return None, None


def check_axis(html_files, regions):
    """Fail when the during-use axis is copied outside a matching include.

    The chapter section is the one allowed copy. The master Depreciation
    include holds the same block and is skipped. Copies inside the
    Revaluation and Impairment plates are deferred: they must still match
    the chapter axis, and any other copy is a failure.
    """
    errors = []
    canonical, source = axis_source(html_files)
    if canonical is None:
        errors.append(f"AXIS: no map-section:{AXIS_ID} in the IAS 16 pack")
        return errors
    kept = []
    deferred = []
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        spans = regions.get(path, [])
        matching = [(begin, end) for begin, end, ok, _include in spans if ok]
        sections = find_plate_sections(text)
        for start, _end, raw in iter_axis_blocks(text):
            if section_inside(start, matching):
                continue
            key = axis_key(raw)
            where = plate_name(start, sections)
            place = rel(path) + (f" {where}" if where else "")
            if key != canonical:
                errors.append(
                    "AXIS: "
                    f"{place} during-use axis does not match "
                    f"{rel(source)} map-section:{AXIS_ID}"
                )
                continue
            if where:
                deferred.append(place)
            else:
                kept.append(place)
    if len(kept) != 1:
        lines = "\n".join(f"  - {place}" for place in kept) or "  - (none)"
        errors.append(
            f"AXIS: map-section:{AXIS_ID} appears {len(kept)} times "
            f"outside a matching include (expected the chapter source once)\n{lines}"
        )
    for place in deferred:
        print(f"deferred axis (PR 4): {place}")
    return errors


def check_stamps(files):
    errors = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for ref in iter_versioned_refs(text, path):
            if ref["skip"]:
                continue
            if HEX12.fullmatch(ref["version"]):
                continue
            errors.append(
                f"STAMP: {rel(path)} local ?v={ref['version']} "
                f"on {ref['path']} is not 12 hex"
            )
    return errors


def main():
    if not PACK.is_dir():
        raise SystemExit(f"missing pack {PACK}")
    html_files = pack_html_files()
    errors, regions = check_includes(html_files)
    errors.extend(check_duplicates(html_files, regions))
    errors.extend(check_axis(html_files, regions))
    errors.extend(check_stamps(pack_text_files()))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
