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
V_QUERY = re.compile(r"\?v=[A-Za-z0-9._~%-]*")
STAMP = re.compile(r"Last update · \d{4}-\d{2}-\d{2} \d{2}:\d{2} HKT")
HOME = "homepage/homepage-wireframe-v0.1.html"
# site/settings/index.html and _shared/settings-rows.html are gated instead by check-settings-rows.py (276/276) and xlsx_to_tokens.py --check.
CONTENT_ALLOW = (
    "site/settings/index.html",
    "_shared/settings-rows.html",
)
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--csv")
    args = parser.parse_args()
    failed = False
    rows = []
    for path in git_paths(args.base):
        base = git_text(args.base, path)
        file = ROOT / path
        if base is None or not file.is_file():
            print(f"missing existing page {path}")
            failed = True
            continue
        head = file.read_text(encoding="utf-8")
        base_n = fold_style_media(fold_viewport(norm(base)))
        head_n = fold_style_media(fold_viewport(norm(head)))
        if path == MAP_NARROW:
            base_n = fold_map_narrow(base_n)
            head_n = fold_map_narrow(head_n)
        if path in UTILITY_PAGES:
            base_n = fold_utility_styles(base_n)
            head_n = fold_utility_styles(head_n)
        if path == HOME:
            if LINK not in head:
                print("homepage is missing the Settings link")
                failed = True
            # The Settings link is already on main. Strip it on both sides so an
            # unchanged homepage is not reported as an edit, and a new link on
            # an older base still compares equal.
            head_n = head_n.replace(LINK, "", 1)
            base_n = base_n.replace(LINK, "", 1)
        if head_n != base_n and path not in CONTENT_ALLOW:
            print(f"HTML changed outside ?v= and the homepage link: {path}")
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
    if failed:
        return 1
    print("stamp-only: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
