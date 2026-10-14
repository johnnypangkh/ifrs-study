#!/usr/bin/env python3
"""Fail on new or stale font-weight / line-height literals.

A value is a literal unless it is var(...), a calc() of vars only, or one of
inherit, normal, initial, unset. Comments are stripped before the scan.

The baseline is keyed by path, normalised selector, property, value, and
occurrence, so a line shift does not retire a row. DRIFT and GAP rows must
still match a live hit (the allowlist only shrinks). EXCEPTION rows may stay
after the literal is gone. A hit with no baseline row is a new literal.
"""
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = Path(__file__).resolve().parent / "type-literals-baseline.tsv"
KEYWORDS = {"inherit", "normal", "initial", "unset"}
SKIP_REL = {"_shared/tokens.css", "_shared/tokens-core.css"}
PACKS = ("ifrs-18", "ias-2", "ias-16", "cf-2018")
KEY_FIELDS = ("path", "selector", "property", "value", "occurrence")

PROP_RE = re.compile(
    r"(font-weight|line-height)\s*:\s*([^;!}]+)",
    re.I,
)
VAR_RE = re.compile(r"var\((?:[^()]|\([^()]*\))*\)")
STYLE_BLOCK_RE = re.compile(r"<style\b[^>]*>(.*?)</style>", re.I | re.S)
STYLE_ATTR_RE = re.compile(
    r"<([a-zA-Z][\w:-]*)\b([^>]*?)\sstyle\s*=\s*([\"'])(.*?)\3",
    re.I | re.S,
)
CLASS_RE = re.compile(r"""class\s*=\s*(['"])(.*?)\1""", re.I | re.S)


def strip_comments(text):
    def repl(match):
        return re.sub(r"[^\n]", " ", match.group(0))

    return re.sub(r"/\*.*?\*/", repl, text, flags=re.S)


def norm_space(text):
    return re.sub(r"\s+", " ", text).strip()


def norm_selector(text):
    text = norm_space(text)
    text = re.sub(r"\s*([>+~])\s*", r" \1 ", text)
    text = re.sub(r"\s*,\s*", ", ", text)
    return text


def norm_value(raw):
    value = norm_space(raw)
    value = re.sub(r"\s*!important$", "", value, flags=re.I).strip()
    return value


def is_allowed(raw):
    value = norm_value(raw)
    if value.lower() in KEYWORDS:
        return True
    if re.fullmatch(r"var\((?:[^()]|\([^()]*\))*\)", value):
        return True
    if re.fullmatch(r"calc\((?:[^()]|\([^()]*\))*\)", value, flags=re.I):
        inner = value[5:-1]
        leftover = VAR_RE.sub("", inner)
        if re.search(r"\d", leftover):
            return False
        return True
    return False


def _close_brace(text, open_at):
    depth = 0
    for index in range(open_at, len(text)):
        char = text[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index
    return len(text) - 1


def _blank_nested(body):
    chars = []
    depth = 0
    for char in body:
        if char == "{":
            depth += 1
            chars.append(" ")
        elif char == "}":
            if depth:
                depth -= 1
            chars.append(" ")
        elif depth and char != "\n":
            chars.append(" ")
        else:
            chars.append(char)
    return "".join(chars)


def _nested_opens(body):
    opens = []
    depth = 0
    for index, char in enumerate(body):
        if char == "{":
            if depth == 0:
                opens.append(index)
            depth += 1
        elif char == "}" and depth:
            depth -= 1
    return opens


def _prelude_before(body, start, open_at):
    chars = []
    depth = 0
    for index in range(start, open_at):
        char = body[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth = max(0, depth - 1)
        elif depth == 0:
            chars.append(char)
    return "".join(chars)


def iter_rules(text, inherited="(root)", line=1):
    """Yield (selector, brace_line, declaration_text) for each style rule."""
    index = 0
    pending = []
    while index < len(text):
        char = text[index]
        if char != "{":
            if char == "\n":
                line += 1
            pending.append(char)
            index += 1
            continue
        prelude = norm_selector("".join(pending))
        pending = []
        close = _close_brace(text, index)
        body = text[index + 1 : close]
        brace_line = line
        at_rule = prelude.startswith("@")
        selector = inherited if at_rule or not prelude else prelude
        if not at_rule:
            yield selector or "(root)", brace_line, _blank_nested(body)
        search = 0
        for open_at in _nested_opens(body):
            nested_prelude = norm_selector(_prelude_before(body, search, open_at))
            nested_close = _close_brace(body, open_at)
            nested_body = body[open_at + 1 : nested_close]
            nested_at = nested_prelude.startswith("@")
            nested_sel = selector if nested_at or not nested_prelude else nested_prelude
            nested_line = brace_line + body[:open_at].count("\n")
            synthetic = nested_prelude + "{" + nested_body + "}"
            yield from iter_rules(synthetic, inherited=selector, line=nested_line)
            search = nested_close + 1
        line += text[index : close + 1].count("\n")
        index = close + 1


def declarations(selector, brace_line, body):
    found = []
    for match in PROP_RE.finditer(body):
        if is_allowed(match.group(2)):
            continue
        newlines = body[: match.start()].count("\n")
        found.append(
            {
                "selector": selector or "(root)",
                "property": match.group(1).lower(),
                "value": norm_value(match.group(2)),
                "line": brace_line + newlines,
            }
        )
    return found


def scan_css(text):
    text = strip_comments(text)
    hits = []
    for selector, brace_line, body in iter_rules(text):
        hits.extend(declarations(selector, brace_line, body))
    return hits


def element_selector(tag, attrs):
    classes = ""
    match = CLASS_RE.search(attrs)
    if match:
        names = match.group(2).split()
        if names:
            classes = "." + ".".join(names)
    return norm_selector(tag.lower() + classes) or tag.lower()


def scan_html(text):
    hits = []
    for match in STYLE_BLOCK_RE.finditer(text):
        block = match.group(1)
        # Line of the first character of the block.
        line = text[: match.start(1)].count("\n") + 1
        for hit in scan_css(block):
            # scan_css lines are relative to a file that starts at line 1.
            # Shift by the block's starting line.
            hit["line"] += line - 1
            hits.append(hit)
    for match in STYLE_ATTR_RE.finditer(text):
        tag, attrs, style = match.group(1), match.group(2), match.group(4)
        selector = element_selector(tag, attrs)
        line = text[: match.start(4)].count("\n") + 1
        hits.extend(declarations(selector, line, style))
    return hits


def iter_sources(root):
    root = Path(root)
    shared = root / "_shared"
    if shared.is_dir():
        for path in sorted(shared.rglob("*")):
            if path.suffix.lower() not in {".css", ".html"}:
                continue
            rel = path.relative_to(root).as_posix()
            if rel in SKIP_REL or "design/archive/" in rel:
                continue
            yield rel, path
    for pack in PACKS:
        draft = root / pack / "draft-v1-linked"
        if not draft.is_dir():
            continue
        for path in sorted(draft.rglob("*")):
            if path.suffix.lower() not in {".css", ".html"}:
                continue
            rel = path.relative_to(root).as_posix()
            if "design/archive/" in rel:
                continue
            yield rel, path
    homepage = root / "homepage"
    if homepage.is_dir():
        for path in sorted(homepage.glob("*.html")):
            yield path.relative_to(root).as_posix(), path
    site = root / "site"
    if site.is_dir():
        for path in sorted(site.rglob("*")):
            if path.suffix.lower() not in {".css", ".html"}:
                continue
            rel = path.relative_to(root).as_posix()
            if "design/archive/" in rel:
                continue
            yield rel, path


def scan_tree(root):
    grouped = {}
    for rel, path in iter_sources(root):
        text = path.read_text(encoding="utf-8")
        if path.suffix.lower() == ".css":
            found = scan_css(text)
        else:
            found = scan_html(text)
        if found:
            grouped.setdefault(rel, []).extend(found)
    rows = []
    for rel in sorted(grouped):
        found = sorted(
            grouped[rel],
            key=lambda hit: (hit["line"], hit["selector"], hit["property"], hit["value"]),
        )
        counts = Counter()
        for hit in found:
            tail = (hit["selector"], hit["property"], hit["value"])
            counts[tail] += 1
            rows.append(
                {
                    "path": rel,
                    "selector": hit["selector"],
                    "property": hit["property"],
                    "value": hit["value"],
                    "occurrence": str(counts[tail]),
                    "line": str(hit["line"]),
                }
            )
    return rows


def row_key(row):
    return tuple(row[field] for field in KEY_FIELDS)


def read_baseline(path):
    path = Path(path)
    if not path.is_file():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        return []
    header = lines[0].split("\t")
    rows = []
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.split("\t")
        rows.append(dict(zip(header, parts)))
    return rows


def write_baseline(path, rows):
    header = ["path", "selector", "property", "value", "occurrence", "class", "line"]
    body = ["\t".join(header)]
    for row in rows:
        body.append("\t".join(row.get(field, "") for field in header))
    Path(path).write_text("\n".join(body) + "\n", encoding="utf-8")


def pack_of(path):
    if path.startswith("_shared/"):
        return "_shared"
    if path.startswith("homepage/"):
        return "homepage"
    if path.startswith("site/"):
        return "site"
    return path.split("/", 1)[0]


def merge_baseline(hits, previous):
    previous_by_key = {row_key(row): row for row in previous}
    merged = []
    for hit in hits:
        old = previous_by_key.get(row_key(hit))
        merged.append({**hit, "class": (old or {}).get("class") or "DRIFT"})
    return merged


def evaluate(hits, baseline):
    hit_keys = {row_key(row) for row in hits}
    base_keys = {row_key(row) for row in baseline}
    new_rows = [row for row in hits if row_key(row) not in base_keys]
    stale = []
    for row in baseline:
        if row_key(row) in hit_keys:
            continue
        if row.get("class") == "EXCEPTION":
            continue
        stale.append(row)
    return new_rows, stale


def format_hit(row):
    line = row.get("line") or "?"
    return (
        f"{row['path']}:{line}\t{row['selector']}\t{row['property']}\t"
        f"{row['value']}\t#{row['occurrence']}\t{row.get('class', '')}"
    )


def report(hits, baseline):
    counts = Counter()
    for row in baseline:
        counts[(pack_of(row["path"]), row.get("class", ""))] += 1
    print("baseline rows", len(baseline), "live hits", len(hits))
    for pack, klass in sorted(counts):
        print(f"{pack}\t{klass}\t{counts[(pack, klass)]}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-baseline", action="store_true")
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--baseline", type=Path, default=BASELINE)
    args = parser.parse_args(argv)
    hits = scan_tree(args.root)
    if args.write_baseline:
        merged = merge_baseline(hits, read_baseline(args.baseline))
        write_baseline(args.baseline, merged)
        print(f"wrote {len(merged)} rows to {args.baseline}")
        return 0
    baseline = read_baseline(args.baseline)
    if args.report:
        report(hits, baseline)
    new_rows, stale = evaluate(hits, baseline)
    for row in new_rows:
        print("new\t" + format_hit(row))
    for row in stale:
        print("stale\t" + format_hit(row))
    if new_rows or stale:
        print(f"type literals: {len(new_rows)} new, {len(stale)} stale")
        return 1
    print(f"type literals: 0 new, 0 stale ({len(baseline)} baseline)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
