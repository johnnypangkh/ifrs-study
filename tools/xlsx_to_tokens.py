#!/usr/bin/env python3
"""Generate _shared/tokens.css from design/MASTER-STYLES.xlsx.

The Text, Colour, Spacing and Grid sheets are emitted. Box, Components and
Top bar are read and emit nothing. ChangeLog is ignored. Grid rows marked
LEGACY-PR1 are not emitted.

Day (the :root block) is the default. Dark is the override, in the same
two-block shape as main: prefers-color-scheme, then [data-theme="dark"].
The four type-scale tokens stay in _shared/type-scale.css and are mirrored
inside the mobile @media. --check fails if those two copies differ, or if
either differs from the workbook.

Usage:
  python3 tools/xlsx_to_tokens.py            # write _shared/tokens.css
  python3 tools/xlsx_to_tokens.py --check    # MATCH or a diff, exit 1 on drift
  python3 tools/xlsx_to_tokens.py --owned    # report-only baseline comparison
  python3 tools/xlsx_to_tokens.py --map-lint # report-only hardcoded-value counts
  python3 tools/xlsx_to_tokens.py --repo-grep
"""
import difflib
import re
import subprocess
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
XLSX = ROOT / "design" / "MASTER-STYLES.xlsx"
TOKENS = ROOT / "_shared" / "tokens.css"
TYPE_SCALE = ROOT / "_shared" / "type-scale.css"
READ_SHEETS = ("Text", "Colour", "Box", "Spacing", "Grid", "Components", "Top bar")
EXTRA = re.compile(r"(\w+)=([\d.]+rem)/([\d.]+rem)")
DECL = re.compile(r"(--[\w-]+)\s*:\s*([^;]+);")
PROP = re.compile(r"(--[\w-]+)\s*:")


def n(value):
    """rem number format from the box draft: no leading zero."""
    text = "%g" % float(value)
    return text[1:] if text.startswith("0.") else text


def rem(value):
    return n(value) + "rem"


def line(name, value, indent):
    return (" " * indent) + f"{name}: {value};"


def extras(notes):
    return EXTRA.findall(str(notes or ""))


def load_workbook():
    wb = openpyxl.load_workbook(XLSX, data_only=True)
    missing = [name for name in READ_SHEETS if name not in wb.sheetnames]
    if missing:
        raise SystemExit("missing sheet: " + ", ".join(missing))
    # Read, then emit nothing. ChangeLog is ignored.
    for name in ("Box", "Components", "Top bar"):
        wb[name].max_row
    return wb


def sheet_rows(wb, name):
    ws = wb[name]
    header = [cell.value for cell in ws[1]]
    rows = []
    for cells in ws.iter_rows(min_row=2):
        if cells[0].value is None and all(cell.value is None for cell in cells):
            continue
        rows.append(dict(zip(header, [cell.value for cell in cells])))
    return rows


def type_scale_lines(text_rows):
    lines = []
    for row in text_rows:
        if row.get("Group") != "type-scale":
            continue
        notes = str(row.get("Notes") or "")
        if "mobile " not in notes:
            raise SystemExit(f"type-scale row {row.get('Token prefix')} has no mobile note")
        value = notes.split("mobile ", 1)[1]
        lines.append(line(row["Token prefix"], value, 4))
    if len(lines) != 4:
        raise SystemExit(f"expected 4 type-scale rows, found {len(lines)}")
    return lines


def emit_map_row(row, bucket, indent, mobile):
    prefix = row["Token prefix"]
    if mobile:
        if float(row["Mobile rem"]) != float(row["Desktop rem"]):
            bucket.append(line(f"{prefix}-fs", rem(row["Mobile rem"]), indent))
        for key, desktop, mobile_value in extras(row.get("Notes")):
            if desktop != mobile_value:
                bucket.append(line(f"{prefix}-{key}", mobile_value, indent))
        return
    bucket.append(line(f"{prefix}-fs", rem(row["Desktop rem"]), indent))
    if row["Weight"] is not None:
        bucket.append(line(f"{prefix}-fw", str(int(row["Weight"])), indent))
    if row["Line height"] is not None:
        bucket.append(line(f"{prefix}-lh", n(row["Line height"]), indent))
    for key, desktop, _mobile_value in extras(row.get("Notes")):
        bucket.append(line(f"{prefix}-{key}", desktop, indent))


def emit_teaching_row(row, bucket):
    prefix = row["Token prefix"]
    if prefix == "--cite" or row.get("Style name") == "Cite":
        bucket.append(line("--cite-size", rem(row["Desktop rem"]), 2))
        bucket.append(line("--cite-weight", str(int(row["Weight"])), 2))
        return
    emit_map_row(row, bucket, 2, mobile=False)


def build_parts(wb):
    text_rows = sheet_rows(wb, "Text")
    colour_rows = sheet_rows(wb, "Colour")
    spacing_rows = sheet_rows(wb, "Spacing")
    grid_rows = sheet_rows(wb, "Grid")

    day = []
    map_mobile = []
    grid_mobile = []
    night = []

    for row in colour_rows:
        token = row.get("Token")
        if not token or not str(token).startswith("--"):
            continue
        day.append(line(token, str(row["Day value (default :root)"]).strip(), 2))
        night_value = row.get("Night value (dark override: prefers-color-scheme + [data-theme=dark])")
        if night_value is None or str(night_value).strip() == "(same as day)":
            continue
        night.append(line(token, str(night_value).strip(), 4))

    for row in text_rows:
        if row.get("Group") != "site":
            continue
        day.append(line(row["Token prefix"], rem(row["Desktop rem"]), 2))

    for row in spacing_rows:
        token = row.get("Token")
        if not token or not str(token).startswith("--"):
            continue
        if row.get("Desktop") is None:
            continue
        day.append(line(str(token), str(row["Desktop"]).strip(), 2))

    for row in grid_rows:
        if row.get("Status") == "LEGACY-PR1":
            continue
        token = row.get("Token")
        if not token or not str(token).startswith("--"):
            continue
        if row.get("Desktop") is None:
            continue
        day.append(line(str(token), str(row["Desktop"]).strip(), 2))
        mobile_value = row.get("Mobile")
        if mobile_value is None:
            continue
        mobile_text = str(mobile_value).strip()
        if mobile_text in ("", "same"):
            continue
        if mobile_text != str(row["Desktop"]).strip():
            grid_mobile.append(line(str(token), mobile_text, 4))

    for row in text_rows:
        if row.get("Group") != "map":
            continue
        emit_map_row(row, day, 2, mobile=False)
        emit_map_row(row, map_mobile, 4, mobile=True)

    for row in text_rows:
        if row.get("Group") != "teaching":
            continue
        emit_teaching_row(row, day)

    scale = type_scale_lines(text_rows)
    # Text sheet (map overrides, then the type-scale mirror), then Grid.
    mobile = map_mobile + scale + grid_mobile

    if len(night) != 43:
        raise SystemExit(f"expected 43 night colours, found {len(night)}")
    return day, mobile, night, scale


def render(day, mobile, night):
    def block(selector, decls, indent):
        pad = " " * indent
        body = "\n".join(decls)
        return f"{pad}{selector} {{\n{body}\n{pad}}}"

    # Night declarations sit at indent 4 inside the media :root and at indent 2
    # in the data-theme block. build_parts stored them at indent 4; restamp
    # the data-theme copy at indent 2 so both blocks carry the same values.
    night_inner = night
    night_root = [line(name, value, 2) for name, value in parse_decl_lines(night)]
    parts = [
        "/* GENERATED — do not edit. tools/xlsx_to_tokens.py reads design/MASTER-STYLES.xlsx. */",
        block(":root", day, 0),
        "@media (max-width:560px) {\n" + block(":root", mobile, 2) + "\n}",
        "@media (prefers-color-scheme: dark) {\n"
        + block(':root:not([data-theme="light"])', night_inner, 2)
        + "\n}",
        block(':root[data-theme="dark"]', night_root, 0),
    ]
    return "\n".join(parts) + "\n"


def parse_decl_lines(lines):
    found = []
    for item in lines:
        match = DECL.search(item)
        if not match:
            raise SystemExit(f"declaration did not parse: {item}")
        found.append((match.group(1), match.group(2).strip()))
    return found


def git_text(rel):
    import os
    refs = ["origin/main", "main"]
    base = os.environ.get("GITHUB_BASE_REF", "")
    if base:
        refs.extend([f"origin/{base}", base])
    for ref in refs:
        try:
            return subprocess.check_output(
                ["git", "show", f"{ref}:{rel}"],
                cwd=ROOT,
                text=True,
                stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            continue
    raise SystemExit(f"cannot read {rel} from main")


def slice_blocks(css):
    root_at = css.index(":root {")
    media_at = css.index("@media (prefers-color-scheme")
    dark_at = css.index(':root[data-theme="dark"]')
    return {
        "root": DECL.findall(css[root_at:media_at]),
        "mq": DECL.findall(css[media_at:dark_at]),
        "dark": DECL.findall(css[dark_at:]),
    }


def baseline_stop(day, night, scale):
    """STOP if a main token would change value. Additions are allowed."""
    base = slice_blocks(git_text("_shared/tokens.css"))
    generated_root = dict(parse_decl_lines(day))
    generated_night = dict(parse_decl_lines(night))
    problems = []
    for name, value in base["root"]:
        got = generated_root.get(name)
        if got is None or got.strip() != value.strip():
            problems.append(f":root {name} main={value!r} generated={got!r}")
    for block_name in ("mq", "dark"):
        for name, value in base[block_name]:
            got = generated_night.get(name)
            if got is None or got.strip() != value.strip():
                problems.append(f"{block_name} {name} main={value!r} generated={got!r}")
    current = TYPE_SCALE.read_text(encoding="utf-8")
    expected = "\n".join(scale)
    if expected not in current:
        problems.append("type-scale.css 4-token block is not the verbatim mirror")
    if problems:
        print("STOP: token value would change, or the type-scale mirror does not match.")
        for item in problems:
            print(item)
        raise SystemExit(1)


def type_scale_mirror_ok(css, scale):
    expected = "\n".join(scale)
    file_text = TYPE_SCALE.read_text(encoding="utf-8")
    in_tokens = expected in css
    in_file = expected in file_text
    return in_tokens and in_file, expected, file_text


def command_check():
    wb = load_workbook()
    day, mobile, night, scale = build_parts(wb)
    css = render(day, mobile, night)
    current = TOKENS.read_text(encoding="utf-8") if TOKENS.exists() else ""
    ok, expected, file_text = type_scale_mirror_ok(css, scale)
    failed = False
    if current != css:
        failed = True
        diff = difflib.unified_diff(
            current.splitlines(keepends=True),
            css.splitlines(keepends=True),
            fromfile="_shared/tokens.css",
            tofile="generated",
        )
        sys.stdout.writelines(diff)
    if not ok:
        failed = True
        print("TYPE-SCALE MIRROR MISMATCH")
        if expected not in file_text:
            print("--- type-scale.css is missing the verbatim block:")
            print(expected)
        if expected not in css:
            print("--- tokens.css mirror is missing the verbatim block:")
            print(expected)
    if failed:
        raise SystemExit(1)
    print("MATCH")


def command_write():
    wb = load_workbook()
    day, mobile, night, scale = build_parts(wb)
    baseline_stop(day, night, scale)
    css = render(day, mobile, night)
    ok, expected, file_text = type_scale_mirror_ok(css, scale)
    if not ok:
        print("STOP: refusing to change type-scale.css.")
        print("The 4-token block must stay byte-identical to main.")
        raise SystemExit(1)
    # The generator owns the block. Writing is a no-op when the bytes match,
    # which is the only legal outcome. Do not touch the file.
    if expected not in file_text:
        raise SystemExit(1)
    TOKENS.write_text(css, encoding="utf-8")
    second = render(*build_parts(load_workbook())[:3])
    if second != css:
        print("STOP: generator output is not deterministic.")
        raise SystemExit(1)
    print(f"written {TOKENS.relative_to(ROOT)}")


def command_owned():
    """Report-only. Does not gate."""
    wb = load_workbook()
    day, mobile, night, scale = build_parts(wb)
    css = render(day, mobile, night)
    base = slice_blocks(git_text("_shared/tokens.css"))
    base_ts = DECL.findall(git_text("_shared/type-scale.css"))
    generated_root = dict(parse_decl_lines(day))
    generated_mobile = dict(parse_decl_lines(mobile))
    generated_night = dict(parse_decl_lines(night))
    print("owned-token check (report-only)")
    print("baseline counts: "
          f":root {len(base['root'])}, "
          f"prefers-color-scheme {len(base['mq'])}, "
          f"data-theme=dark {len(base['dark'])}, "
          f"type-scale {len(base_ts)}")
    rows = []
    for name, value in base["root"]:
        rows.append((":root", name, value.strip(), generated_root.get(name)))
    for name, value in base["mq"]:
        rows.append(("prefers-color-scheme", name, value.strip(), generated_night.get(name)))
    for name, value in base["dark"]:
        rows.append(("data-theme=dark", name, value.strip(), generated_night.get(name)))
    scale_values = dict(parse_decl_lines(scale))
    for name, value in base_ts:
        got = scale_values.get(name)
        if got is None:
            got = generated_mobile.get(name)
        rows.append(("type-scale", name, value.strip(), got))
    same = 0
    for block, name, main_value, generated in rows:
        status = "EQUAL" if generated is not None and generated.strip() == main_value else "DIFF"
        if status == "EQUAL":
            same += 1
        print(f"{status}\t{block}\t{name}\t{main_value}\t{generated}")
    pack_hits = []
    for path in sorted(ROOT.glob("*/*")):
        if not path.is_dir():
            continue
        for name in ("shared.css", "draft.css"):
            for candidate in path.rglob(name):
                if "_archive" in candidate.parts:
                    continue
                text = candidate.read_text(encoding="utf-8", errors="replace")
                count = len(re.findall(r":root\b", text))
                if count:
                    pack_hits.append(f"{candidate.relative_to(ROOT)} {count}")
    print(f"pack shared/draft :root blocks: {len(pack_hits)}")
    for hit in pack_hits:
        print(f"PACK-ROOT\t{hit}")
    print(f"baseline declarations {len(rows)}; equal {same}; diff {len(rows) - same}")
    print(f"generated mobile declarations {len(generated_mobile)}")


def command_map_lint():
    """Report-only counts. Not a failure in PR1."""
    px = re.compile(r"(?<![\w-])\d+(?:\.\d+)?px\b")
    hex_colour = re.compile(r"#[0-9A-Fa-f]{3,8}\b")
    print("map-lint (report-only, not gating in PR1)")
    totals = {"files": 0, "px": 0, "hex": 0}
    for draft in sorted(ROOT.glob("*/draft-v1-linked")):
        pack = draft.parent.name
        files = px_count = hex_count = 0
        for path in sorted(draft.rglob("*")):
            if not path.is_file() or "_archive" in path.parts:
                continue
            if path.suffix.lower() not in {".css", ".html"}:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            files += 1
            px_count += len(px.findall(text))
            hex_count += len(hex_colour.findall(text))
        totals["files"] += files
        totals["px"] += px_count
        totals["hex"] += hex_count
        print(f"{pack}\tfiles {files}\tpx {px_count}\thex {hex_count}")
    print(f"total\tfiles {totals['files']}\tpx {totals['px']}\thex {totals['hex']}")
    print("PR1 does not fail on these counts. Hard fail is PR8.")


def owned_names(wb):
    day, mobile, night, scale = build_parts(wb)
    names = []
    for bucket in (day, mobile, night, scale):
        for name, _value in parse_decl_lines(bucket):
            if name not in names:
                names.append(name)
    return names


def command_repo_grep():
    wb = load_workbook()
    names = owned_names(wb)
    print("repo grep: other files that define a tokens.css-owned name (report-only)")
    print(f"owned names {len(names)}")
    hits = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".css", ".html"}:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel == "_shared/tokens.css":
            continue
        if "_archive" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        found = sorted(set(PROP.findall(text)))
        owned = [name for name in found if name in names]
        if not owned:
            continue
        hits.append(rel)
        print(f"{rel}\t{len(owned)}\t{', '.join(owned)}")
    print(f"files {len(hits)}")


def main():
    args = set(sys.argv[1:])
    if args == {"--check"}:
        command_check()
        return
    if args == {"--owned"}:
        command_owned()
        return
    if args == {"--map-lint"}:
        command_map_lint()
        return
    if args == {"--repo-grep"}:
        command_repo_grep()
        return
    if args:
        raise SystemExit("usage: xlsx_to_tokens.py [--check|--owned|--map-lint|--repo-grep]")
    command_write()


if __name__ == "__main__":
    main()
