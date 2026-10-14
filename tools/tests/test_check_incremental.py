#!/usr/bin/env python3
"""Fixture checks for the incremental teaching-text guard."""

import importlib.util
import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
_spec = importlib.util.spec_from_file_location(
    "check_incremental", TOOLS / "check-incremental.py"
)
guard = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(guard)


def judge(base, head, approval=None, strict=False):
    return guard.evaluate(base, head, approval, strict_added=strict)


def read_repo(path):
    return (guard.ROOT / path).read_text(encoding="utf-8")


def drop_once(html, sentence):
    if sentence not in html:
        raise AssertionError("sentence missing from fixture: " + sentence)
    return html.replace(sentence, "", 1)


def approval_removed(file, old, source, locator=""):
    lines = [
        "- action: removed",
        "  file: " + guard.yaml_quote(file),
    ]
    if locator:
        lines.append("  locator: " + guard.yaml_quote(locator))
    lines.append("  old: " + guard.yaml_quote(old))
    lines.append("  source: " + guard.yaml_quote(source))
    return "\n".join(lines) + "\n"


class IncrementalTests(unittest.TestCase):
    def test_unapproved_removal_fails(self):
        base = {"a.html": "<p>This paragraph leaves the notes.</p>"}
        head = {"a.html": "<p>Unrelated replacement copy.</p>"}
        code, rows, _counts, issues = judge(base, head)
        self.assertNotEqual(code, 0)
        self.assertTrue(any(row.status == "removed" for row in rows))
        self.assertTrue(any("UNAPPROVED" in issue or "missing" in issue for issue in issues))

    def test_approved_change_passes(self):
        base = {"chapter.html": '<h2 id="t">Useful life is reviewed each year.</h2>'}
        head = {"chapter.html": '<h2 id="t">Useful life is reviewed each year-end.</h2>'}
        approval = "\n".join([
            "- action: changed",
            "  file: chapter.html",
            '  old: "Useful life is reviewed each year."',
            '  new: "Useful life is reviewed each year-end."',
            '  source: "Content item 1"',
            "",
        ])
        code, rows, _counts, issues = judge(base, head, approval)
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        changed = [row for row in rows if row.status == "changed"]
        self.assertEqual(len(changed), 1)
        self.assertEqual(changed[0].source, "Content item 1")

    def test_move_between_files_passes(self):
        base = {"a.html": "<p>Spare parts that meet the definition are PPE.</p>"}
        head = {"b.html": "<p>Spare parts that meet the definition are PPE.</p>"}
        code, rows, counts, issues = judge(base, head)
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        self.assertEqual(counts["moved"], 1)
        self.assertEqual(counts["removed"], 0)
        self.assertEqual(rows[0].status, "moved")

    def test_include_copy_is_not_double_counted(self):
        source = "<p>Alpha sentence owned by the source.</p>\n"
        axis = "<p>Gamma sentence owned by the axis.</p>\n"
        master = "\n".join([
            "<div>",
            "<!-- include:source.html#sec:start -->",
            "<p>Beta sentence that exists only in the include copy.</p>",
            "<!-- include:axis.html#axis:start -->",
            "<p>Delta sentence that exists only in the nested include.</p>",
            "<!-- include:axis.html#axis:end -->",
            "<!-- include:source.html#sec:end -->",
            "</div>",
            "",
        ])
        files = {"source.html": source, "axis.html": axis, "master.html": master}
        items = guard.extract_tree(files)
        texts = [item.exact for item in items if item.kind == "text"]
        self.assertEqual(texts.count("Alpha sentence owned by the source."), 1)
        self.assertEqual(texts.count("Gamma sentence owned by the axis."), 1)
        self.assertNotIn("Beta sentence that exists only in the include copy.", texts)
        self.assertNotIn("Delta sentence that exists only in the nested include.", texts)
        code, rows, counts, _issues = judge(files, files)
        self.assertEqual(code, 0)
        self.assertEqual(counts["moved"], 0)
        self.assertEqual(counts["added"], 0)
        self.assertEqual(counts["removed"], 0)
        self.assertEqual(rows, [])

    def test_version_or_phase_only_diff_passes(self):
        base = {
            "plate.html": (
                '<section class="plate" data-phase-start>'
                '<p>Same teaching sentence.</p>'
                '<a href="chapter.html?v=aaa111#s1">Open</a>'
                "</section>"
            )
        }
        head = {
            "plate.html": (
                '<section class="plate" data-phase-end="late">'
                '<p>Same teaching sentence.</p>'
                '<a href="chapter.html?v=bbb222#s1">Open</a>'
                "</section>"
            )
        }
        code, rows, counts, issues = judge(base, head)
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        self.assertEqual(rows, [])
        self.assertGreater(counts["kept"], 0)

    def test_nonbreaking_hyphen_is_a_change(self):
        base = {"a.html": "<p>Use a non\u2011breaking hyphen here.</p>"}
        head = {"a.html": "<p>Use a non-breaking hyphen here.</p>"}
        code, rows, _counts, _issues = judge(base, head)
        self.assertNotEqual(code, 0)
        changed = [row for row in rows if row.status == "changed"]
        self.assertEqual(len(changed), 1)
        self.assertIn("\u2011", changed[0].old)
        self.assertIn("-", changed[0].new)
        self.assertNotIn("\u2011", changed[0].new)

    def test_stale_entry_fails(self):
        files = {"a.html": "<p>Nothing moved.</p>"}
        approval = "\n".join([
            "- action: removed",
            "  file: a.html",
            '  old: "This sentence was never here."',
            '  source: "ruling example"',
            "",
        ])
        code, _rows, _counts, issues = judge(files, files, approval)
        self.assertNotEqual(code, 0)
        self.assertTrue(any("stale" in issue for issue in issues))

    def test_capital_letter_is_a_change(self):
        base = {"a.html": "<p>The Asset is recognised.</p>"}
        head = {"a.html": "<p>The asset is recognised.</p>"}
        code, rows, _counts, _issues = judge(base, head)
        self.assertNotEqual(code, 0)
        changed = [row for row in rows if row.status == "changed"]
        self.assertEqual(len(changed), 1)
        self.assertEqual(changed[0].old, "The Asset is recognised.")
        self.assertEqual(changed[0].new, "The asset is recognised.")

    def _removal(self, rows, file, sentence):
        hits = [
            row for row in rows
            if row.status == "removed" and row.file == file and row.old == sentence
        ]
        self.assertEqual(len(hits), 1, rows)
        return hits[0]

    def test_expC_crossfile_duplicate_is_a_removal(self):
        """QC expC: deleting the ch06 fire sentence must fail even though ch07 still has it."""
        sentence = "Company W\u2019s main operating plant is destroyed in a fire."
        ch06 = "ias-16/draft-v1-linked/ch06.html"
        ch07 = "ias-16/draft-v1-linked/ch07.html"
        base = {ch06: read_repo(ch06), ch07: read_repo(ch07)}
        head = {ch06: drop_once(base[ch06], sentence), ch07: base[ch07]}
        self.assertIn(sentence, head[ch07])

        code, rows, counts, issues = judge(base, head)
        self.assertNotEqual(code, 0)
        self.assertEqual(counts["moved"], 0)
        self.assertEqual(counts["removed"], 1)
        row = self._removal(rows, ch06, sentence)
        self.assertEqual(guard.source_cell(row), "UNAPPROVED")
        self.assertEqual(row.moved_from, "")
        self.assertTrue(any("UNAPPROVED removed" in issue for issue in issues))
        self.assertNotIn(ch07, row.file)

        wrong = approval_removed(ch07, sentence, "QC FAIL PR r1 item 1")
        code, rows, _counts, issues = judge(base, head, wrong)
        self.assertNotEqual(code, 0)
        self.assertFalse(self._removal(rows, ch06, sentence).approved)
        self.assertTrue(any("stale" in issue for issue in issues))

        ok = approval_removed(ch06, sentence, "QC FAIL PR r1 item 1")
        code, rows, counts, issues = judge(base, head, ok)
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        row = self._removal(rows, ch06, sentence)
        self.assertEqual(row.source, "QC FAIL PR r1 item 1")
        self.assertEqual(guard.source_cell(row), "approved: QC FAIL PR r1 item 1")

        located = approval_removed(
            ch06, sentence, "QC FAIL PR r1 item 1", locator=row.locator
        )
        code, _rows, _counts, issues = judge(base, head, located)
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)

    def test_expE_every_teaching_html_path_is_in_scope(self):
        """QC expE: every live HTML path is scanned. chapter-visuals was deleted in PR7."""
        listed = guard.git_text("ls-tree", "-r", "--name-only", "HEAD").splitlines()
        html = [path for path in listed if path.endswith(".html")]
        scoped = set(guard.list_html("HEAD"))
        for path in html:
            if "_archive" in path.split("/"):
                self.assertNotIn(path, scoped)
                self.assertFalse(guard.in_scope(path))
            else:
                self.assertIn(path, scoped)
                self.assertTrue(guard.in_scope(path))
        self.assertNotIn("cf-2018/chapter-visuals/ch09-status.html", scoped)
        self.assertIn("homepage/how-these-notes-are-made.html", scoped)
        self.assertIn("cf-2018/draft-v1-linked/ch01.html", scoped)
        self.assertNotIn("cf-2018/draft-v1-linked/_archive-index-stub.html", scoped)
        self.assertFalse(guard.in_scope("cf-2018/chapter-visuals/_archive/ch01-overview.html"))
        self.assertFalse(guard.in_scope("cf-2018/draft-v1-linked/_archive/ch01-overview.html"))
        self.assertTrue(guard.in_scope("_shared/example.html"))
        self.assertFalse(guard.in_scope("tools/README.md"))

        path = "cf-2018/draft-v1-linked/ch01.html"
        sentence = "Concepts + objective \u2014 not a Standard"
        base = {path: "<p>" + sentence + "</p>"}
        head = {path: drop_once(base[path], sentence)}
        code, rows, counts, issues = judge(base, head)
        self.assertNotEqual(code, 0)
        self.assertEqual(counts["moved"], 0)
        row = self._removal(rows, path, sentence)
        self.assertEqual(guard.source_cell(row), "UNAPPROVED")
        self.assertTrue(any("missing" in issue or "UNAPPROVED" in issue for issue in issues))

        code, rows, _counts, issues = judge(
            base, head, approval_removed(path, sentence, "QC FAIL PR r1 item 2")
        )
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        self.assertEqual(self._removal(rows, path, sentence).source, "QC FAIL PR r1 item 2")

    def test_expF_hand_copy_does_not_hide_source_removal(self):
        """QC expF: 'When the asset is available for use' still sits on the master outside the include."""
        sentence = "When the asset is available for use"
        ch05 = "ias-16/draft-v1-linked/visuals/ch05-depreciation.html"
        master = "ias-16/draft-v1-linked/visuals/master-concept-map.html"
        base = {ch05: read_repo(ch05), master: read_repo(master)}
        head = {ch05: drop_once(base[ch05], sentence), master: base[master]}
        self.assertGreaterEqual(head[master].count(sentence), 2)
        self.assertIn("<!-- include:ch05-depreciation.html#ch05-dep:start -->", head[master])

        code, rows, counts, issues = judge(base, head)
        self.assertNotEqual(code, 0)
        self.assertEqual(counts["moved"], 0)
        self.assertEqual(counts["removed"], 1)
        row = self._removal(rows, ch05, sentence)
        self.assertEqual(row.kind, "text")
        self.assertEqual(guard.source_cell(row), "UNAPPROVED")
        self.assertNotEqual(row.file, master)
        self.assertTrue(any("UNAPPROVED removed" in issue for issue in issues))

        code, rows, _counts, issues = judge(
            base, head, approval_removed(ch05, sentence, "QC FAIL PR r1 item 3")
        )
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        self.assertEqual(
            guard.source_cell(self._removal(rows, ch05, sentence)),
            "approved: QC FAIL PR r1 item 3",
        )

    def test_expF2_include_body_does_not_hide_source_removal(self):
        """QC expF2: the residual-value bullet survives only inside the master include."""
        sentence = (
            "If residual value rises to or above carrying amount, the depreciation "
            "charge is zero until it falls back below carrying amount."
        )
        ch05 = "ias-16/draft-v1-linked/visuals/ch05-depreciation.html"
        master = "ias-16/draft-v1-linked/visuals/master-concept-map.html"
        base = {ch05: read_repo(ch05), master: read_repo(master)}
        head = {ch05: drop_once(base[ch05], sentence), master: base[master]}
        self.assertIn(sentence, head[master])
        include_at = head[master].index("<!-- include:ch05-depreciation.html#ch05-dep:start -->")
        include_end = head[master].index("<!-- include:ch05-depreciation.html#ch05-dep:end -->")
        self.assertLess(include_at, head[master].index(sentence))
        self.assertLess(head[master].index(sentence), include_end)

        code, rows, counts, issues = judge(base, head)
        self.assertNotEqual(code, 0)
        self.assertEqual(counts["moved"], 0)
        self.assertEqual(counts["removed"], 1)
        row = self._removal(rows, ch05, sentence)
        self.assertEqual(row.kind, "li")
        self.assertEqual(row.locator, "section:ch05-dep")
        self.assertEqual(guard.source_cell(row), "UNAPPROVED")

        code, rows, _counts, issues = judge(
            base,
            head,
            approval_removed(
                ch05, sentence, "QC FAIL PR r1 item 4", locator="section:ch05-dep"
            ),
        )
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        row = self._removal(rows, ch05, sentence)
        self.assertEqual(row.source, "QC FAIL PR r1 item 4")
        self.assertTrue(guard.source_cell(row).startswith("approved:"))

    def test_true_move_reports_from_and_to(self):
        sentence = "Spare parts that meet the definition are PPE."
        base = {"a.html": '<p id="from-here">' + sentence + "</p>"}
        head = {"b.html": '<p id="to-here">' + sentence + "</p>"}
        code, rows, counts, issues = judge(base, head)
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        self.assertEqual(counts["moved"], 1)
        self.assertEqual(counts["removed"], 0)
        self.assertEqual(counts["added"], 0)
        row = rows[0]
        self.assertEqual(row.status, "moved")
        self.assertEqual(row.moved_from, "a.html :: from-here")
        self.assertEqual(row.moved_to, "b.html :: to-here")
        self.assertEqual(guard.source_cell(row), "\u2014")
        markdown = guard.format_markdown(counts, rows)
        self.assertIn("moved_from", markdown)
        self.assertIn("a.html :: from-here", markdown)
        self.assertIn("b.html :: to-here", markdown)

    def test_copy_already_in_base_is_still_a_removal(self):
        """A right-of-use line deleted from ch02 stays a removal: ch03 already had it, and the master copy is an include."""
        sentence = (
            "Depreciation of right-of-use assets used to construct, add to, "
            "replace part of or service PPE may form part of cost."
        )
        ch02 = "ias-16/draft-v1-linked/visuals/ch02-recognition.html"
        ch03 = "ias-16/draft-v1-linked/visuals/ch03-initial.html"
        master = "ias-16/draft-v1-linked/visuals/master-concept-map.html"

        def tip(section):
            return (
                f"<!-- map-section:{section}:start -->\n"
                f'<p class="thin-tip">{sentence}</p>\n'
                f"<!-- map-section:{section}:end -->\n"
            )

        base = {
            ch02: tip("ch02-recog"),
            ch03: tip("ch03-cost"),
            master: (
                "<!-- include:ch03-initial.html#ch03-cost:start -->\n"
                f'<p class="thin-tip">{sentence}</p>\n'
                "<!-- include:ch03-initial.html#ch03-cost:end -->\n"
            ),
        }
        head = {
            ch02: "<!-- map-section:ch02-recog:start -->\n<!-- map-section:ch02-recog:end -->\n",
            ch03: base[ch03],
            master: base[master],
        }
        code, rows, counts, issues = judge(base, head)
        self.assertNotEqual(code, 0)
        self.assertEqual(counts["moved"], 0)
        self.assertEqual(counts["removed"], 1)
        self.assertEqual(counts["added"], 0)
        row = self._removal(rows, ch02, sentence)
        self.assertEqual(row.locator, "section:ch02-recog")
        self.assertEqual(guard.source_cell(row), "UNAPPROVED")
        self.assertTrue(any("UNAPPROVED removed" in issue for issue in issues))

        code, rows, _counts, issues = judge(
            base,
            head,
            approval_removed(ch02, sentence, "ruling 2.4", locator="section:ch02-recog"),
        )
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        row = self._removal(rows, ch02, sentence)
        self.assertEqual(row.source, "ruling 2.4")
        self.assertEqual(guard.source_cell(row), "approved: ruling 2.4")

        missed = approval_removed(ch02, sentence, "ruling 2.4", locator="section:other")
        code, rows, _counts, issues = judge(base, head, missed)
        self.assertNotEqual(code, 0)
        self.assertFalse(self._removal(rows, ch02, sentence).approved)
        self.assertTrue(any("stale" in issue for issue in issues))

    def test_equivalent_include_keeps_hand_copy(self):
        sentence = "Alpha sentence stays on the plate."
        section = (
            "<!-- map-section:sec:start -->\n<p>" + sentence + "</p>\n"
            "<!-- map-section:sec:end -->\n"
        )
        base = {"master.html": "<p>" + sentence + "</p>\n", "source.html": section}
        head = {
            "master.html": (
                "<!-- include:source.html#sec:start -->\n"
                "<p>stale pasted body that must not count</p>\n"
                "<!-- include:source.html#sec:end -->\n"
            ),
            "source.html": section,
        }
        code, rows, counts, issues = judge(base, head)
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        self.assertEqual(rows, [])
        self.assertEqual(counts["removed"], 0)
        self.assertEqual(counts["moved"], 0)
        self.assertGreater(counts["kept"], 0)

    def test_include_of_new_source_is_a_move(self):
        sentence = "Alpha sentence moves into the source."
        base = {
            "master.html": '<p id="plate">' + sentence + "</p>\n",
            "source.html": (
                "<!-- map-section:sec:start -->\n<!-- map-section:sec:end -->\n"
            ),
        }
        head = {
            "master.html": (
                "<!-- include:source.html#sec:start -->\n"
                "<!-- include:source.html#sec:end -->\n"
            ),
            "source.html": (
                "<!-- map-section:sec:start -->\n<p>" + sentence + "</p>\n"
                "<!-- map-section:sec:end -->\n"
            ),
        }
        code, rows, counts, issues = judge(base, head)
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        self.assertEqual(counts["moved"], 1)
        self.assertEqual(counts["removed"], 0)
        self.assertEqual(counts["added"], 0)
        row = rows[0]
        self.assertEqual(row.status, "moved")
        self.assertEqual(row.moved_from, "master.html :: plate")
        self.assertEqual(row.moved_to, "source.html#sec")

    def test_include_of_different_text_is_not_kept(self):
        old = "The plate previously described residual value as scrap proceeds."
        new = "Zebra quantities are counted only on Tuesdays in the annex."
        base = {
            "master.html": "<p>" + old + "</p>\n",
            "source.html": (
                "<!-- map-section:sec:start -->\n<p>" + old + "</p>\n"
                "<!-- map-section:sec:end -->\n"
            ),
        }
        head = {
            "master.html": (
                "<!-- include:source.html#sec:start -->\n"
                "<!-- include:source.html#sec:end -->\n"
            ),
            "source.html": (
                "<!-- map-section:sec:start -->\n<p>" + new + "</p>\n"
                "<!-- map-section:sec:end -->\n"
            ),
        }
        code, rows, counts, issues = judge(base, head)
        self.assertNotEqual(code, 0)
        self.assertEqual(counts["moved"], 0)
        carriers = [
            row for row in rows
            if row.old == old and row.status in {"removed", "changed"}
        ]
        self.assertEqual(len(carriers), 1)
        self.assertEqual(carriers[0].file, "source.html")
        self.assertNotEqual(carriers[0].status, "moved")
        self.assertTrue(any("UNAPPROVED" in issue or "missing" in issue for issue in issues))
        self.assertFalse(any(row.file == "master.html" and row.old == old for row in rows))

    def test_old_include_does_not_hide_hand_copy_removal(self):
        sentence = "Hand copy beside an include that already existed."
        section = (
            "<!-- map-section:sec:start -->\n<p>" + sentence + "</p>\n"
            "<!-- map-section:sec:end -->\n"
        )
        include = (
            "<!-- include:source.html#sec:start -->\n"
            "<!-- include:source.html#sec:end -->\n"
        )
        base = {
            "master.html": "<p>" + sentence + "</p>\n" + include,
            "source.html": section,
        }
        head = {"master.html": include, "source.html": section}
        code, rows, counts, _issues = judge(base, head)
        self.assertNotEqual(code, 0)
        self.assertEqual(counts["moved"], 0)
        self.assertEqual(counts["removed"], 1)
        self._removal(rows, "master.html", sentence)

    def test_pr105_shaped_retro_is_only_real_edits(self):
        """61b01f69 → cc6a701f: include replacement and map-section wrappers stay quiet."""
        base = guard.load_rev("61b01f6992f48c96b927266a4a8508337e594dcd")
        head = guard.load_rev("cc6a701fbab57e6cc1efb1a54e47709aa566b567")
        code, rows, counts, _issues = judge(base, head)
        self.assertNotEqual(code, 0)
        self.assertEqual(counts["moved"], 0)
        self.assertEqual(counts["changed"], 3)
        self.assertEqual(counts["removed"], 3)
        self.assertEqual(counts["added"], 4)
        ch02 = "ias-16/draft-v1-linked/visuals/ch02-recognition.html"
        ch07 = "ias-16/draft-v1-linked/visuals/ch07-disclosure.html"
        expected = {
            (
                "changed", ch02,
                "2.2 Spare parts, stand-by and servicing equipment are PPE if they meet the definition; otherwise they are inventory (IAS 2).",
                "2.2 Spare parts, stand-by and servicing equipment are PPE if they meet the definition; otherwise they are inventory.",
            ),
            (
                "changed", ch07,
                "20A proceeds before intended use \u2014 measurement home on Initial measurement (see Initial).",
                "Proceeds before intended use \u2014 measured on Initial measurement",
            ),
            (
                "changed", ch07,
                "Class continuum \u2014 same grain as the entity\u2019s Models classes (see Models).",
                "Classes \u2014 same as the entity's Models classes",
            ),
            (
                "removed", ch02,
                "Depreciation of right-of-use assets used to construct, add to, replace part of or service PPE may form part of cost.",
                "",
            ),
            ("removed", ch02, "See also IAS 2 \u2014 otherwise inventory", ""),
            (
                "removed", ch07,
                "Split additions \u00b7 present disposals as a single line when useful for users.",
                "",
            ),
            ("added", ch02, "", "See also IAS 2"),
            ("added", ch07, "", "IAS 16 \u00b7 para 73(e)"),
            ("added", ch07, "", "KPMG Insights 2019/20 \u00b7 3.2 \u00b7 3.2.400.20"),
            (
                "added", ch07, "",
                "Show additions and acquisitions through business combinations as separate lines; show all disposals as one line.",
            ),
        }
        got = {(row.status, row.file, row.old, row.new) for row in rows}
        self.assertEqual(got, expected)

    def _assert_balanced(self, counts, issues):
        self.assertEqual(
            counts["base"],
            counts["kept"] + counts["moved"] + counts["changed"] + counts["removed"],
            counts,
        )
        self.assertEqual(
            counts["head"],
            counts["kept"] + counts["moved"] + counts["changed"] + counts["added"],
            counts,
        )
        self.assertFalse(any("reconciliation error" in issue for issue in issues), issues)

    def test_edge1_control_no_include(self):
        """Deleting a master hand line is a removal when no new include is added."""
        master = "ias-16/draft-v1-linked/visuals/master-concept-map.html"
        ch03 = "ias-16/draft-v1-linked/visuals/ch03-initial.html"
        sentence = "After recognition"
        needle = '<p class="pack-flow-label"><span class="onward">After recognition</span></p>'
        base = {master: read_repo(master), ch03: read_repo(ch03)}
        self.assertIn(sentence, base[ch03])
        head = {master: drop_once(base[master], needle), ch03: base[ch03]}
        code, rows, counts, issues = judge(base, head)
        self.assertNotEqual(code, 0)
        self.assertEqual(counts["removed"], 1)
        self.assertEqual(counts["moved"], 0)
        self.assertEqual(counts["changed"], 0)
        self.assertEqual(counts["added"], 0)
        row = self._removal(rows, master, sentence)
        self.assertEqual(row.kind, "text")
        self.assertEqual(row.locator, "")
        self.assertEqual(guard.source_cell(row), "UNAPPROVED")
        self.assertTrue(any("UNAPPROVED removed" in issue for issue in issues))
        self._assert_balanced(counts, issues)

    def test_edge2_new_include_does_not_hide_unrelated_hand_loss(self):
        """A new include covers only its section, not every line of the source file.

        "After recognition" sits on the master and also in ch03, outside
        map-section:ch03-cost. Adding a section the base file does not mark
        must not treat the whole ch03 file as covering that master line.
        """
        master = "ias-16/draft-v1-linked/visuals/master-concept-map.html"
        ch03 = "ias-16/draft-v1-linked/visuals/ch03-initial.html"
        sentence = "After recognition"
        needle = '<p class="pack-flow-label"><span class="onward">After recognition</span></p>'
        note = "A note that the new section renders on its own."
        anchor = (
            '<a class="rail-link" data-phase="models" '
            'href="../ch04.html#s-4-0" target="_parent">Measurement after recognition</a>'
        )
        base = {master: read_repo(master), ch03: read_repo(ch03)}
        self.assertIn(sentence, base[ch03])
        self.assertNotIn("map-section:ch03-note", base[ch03])
        self.assertEqual(base[master].count(anchor), 1)
        ch03_head = base[ch03].replace(
            "<!-- map-section:ch03-cost:end -->",
            "\n".join([
                "<!-- map-section:ch03-cost:end -->",
                "<!-- map-section:ch03-note:start -->",
                "<p>" + note + "</p>",
                "<!-- map-section:ch03-note:end -->",
            ]),
            1,
        )
        include = "\n".join([
            "<!-- include:ch03-initial.html#ch03-note:start -->",
            "<!-- include:ch03-initial.html#ch03-note:end -->",
            anchor,
        ])
        master_head = drop_once(base[master], needle).replace(anchor, include, 1)
        head = {master: master_head, ch03: ch03_head}

        code, rows, counts, issues = judge(base, head)
        self.assertNotEqual(code, 0)
        row = self._removal(rows, master, sentence)
        self.assertEqual(row.kind, "text")
        self.assertEqual(row.locator, "")
        self.assertEqual(guard.source_cell(row), "UNAPPROVED")
        self.assertEqual(counts["removed"], 1)
        self.assertTrue(any("UNAPPROVED removed" in issue and sentence in issue for issue in issues))
        self.assertFalse(any("reconciliation error" in issue for issue in issues), issues)
        self._assert_balanced(counts, issues)
        self.assertTrue(any(item.status == "added" and item.new == note for item in rows))

        code, rows, counts, issues = judge(
            base, head, approval_removed(master, sentence, "QC edge2")
        )
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        approved = self._removal(rows, master, sentence)
        self.assertEqual(approved.source, "QC edge2")
        self.assertEqual(guard.source_cell(approved), "approved: QC edge2")
        self._assert_balanced(counts, issues)

    def test_reconciliation_flags_a_vanished_item(self):
        gone = guard.Item("text", "Gone", "Gone", "a.html", "")
        errors = guard.reconciliation_errors([gone], [], guard.Books())
        self.assertTrue(errors)
        self.assertTrue(
            any(error.startswith("reconciliation error") and "Gone" in error for error in errors),
            errors,
        )

        base = {"a.html": "<p>Spare parts that meet the definition are PPE.</p>"}
        head = {"b.html": "<p>Spare parts that meet the definition are PPE.</p>"}
        code, _rows, counts, issues = judge(base, head)
        self.assertEqual(code, 0)
        self._assert_balanced(counts, issues)

        base_rev = "61b01f6992f48c96b927266a4a8508337e594dcd"
        head_rev = "cc6a701fbab57e6cc1efb1a54e47709aa566b567"
        code, _rows, counts, issues = judge(guard.load_rev(base_rev), guard.load_rev(head_rev))
        self.assertNotEqual(code, 0)
        self._assert_balanced(counts, issues)
        self.assertFalse(any(issue.startswith("reconciliation error") for issue in issues))


    def test_pr110_soc_cell_does_not_pair_with_ch04_oci(self):
        """Changed rows pair only inside one file.

        PR 110 paired the abbreviations SOC cell with the chapter 4 OCI
        cell. Those strings are similar and live in different files, so
        they are not one change. Identical text across files is still a move.
        """
        base = {
            "ias-16/draft-v1-linked/abbreviations.html": "<table><tr><td>SOC</td></tr></table>",
            "ias-16/draft-v1-linked/ch04.html": "<td id=\"s-4-5-impair\">P&amp;L</td>",
            "a.html": "<p>Spare parts that meet the definition are PPE.</p>",
        }
        head = {
            "ias-16/draft-v1-linked/abbreviations.html": "<table><tr><td>SCI</td></tr></table>",
            "ias-16/draft-v1-linked/ch04.html": "<td id=\"s-4-5-impair\">OCI</td>",
            "b.html": "<p>Spare parts that meet the definition are PPE.</p>",
        }
        approval = "\n".join([
            "- action: changed",
            "  file: ias-16/draft-v1-linked/abbreviations.html",
            '  old: "SOC"',
            '  new: "SCI"',
            '  source: "same-file abbreviations cell"',
            "- action: changed",
            "  file: ias-16/draft-v1-linked/ch04.html",
            '  locator: "s-4-5-impair"',
            '  old: "P&L"',
            '  new: "OCI"',
            '  source: "same-file chapter cell"',
            "",
        ])
        code, rows, counts, issues = judge(base, head, approval)
        self.assertEqual(issues, [])
        self.assertEqual(code, 0)
        self.assertFalse(any(
            row.status == "changed" and row.old == "SOC" and row.new == "OCI"
            for row in rows
        ))
        soc = [row for row in rows if row.status == "changed" and row.old == "SOC"]
        self.assertEqual(len(soc), 1)
        self.assertEqual(soc[0].new, "SCI")
        self.assertEqual(soc[0].file, "ias-16/draft-v1-linked/abbreviations.html")
        oci = [row for row in rows if row.status == "changed" and row.new == "OCI"]
        self.assertEqual(len(oci), 1)
        self.assertEqual(oci[0].old, "P&L")
        self.assertEqual(oci[0].file, "ias-16/draft-v1-linked/ch04.html")
        moved = [row for row in rows if row.status == "moved"]
        self.assertEqual(len(moved), 1)
        self.assertEqual(moved[0].old, "Spare parts that meet the definition are PPE.")
        self.assertEqual(counts["changed"], 2)
        self.assertEqual(counts["moved"], 1)
        self.assertEqual(counts["removed"], 0)
        self.assertEqual(counts["added"], 0)
        self._assert_balanced(counts, issues)

    def test_pr110_soc_cell_removed_and_oci_cell_added_stay_unpaired(self):
        """Cross-file SOC removal and OCI addition are not one change.

        PR 110 removed the abbreviations SOC cell and added the chapter 4
        OCI cell. The strings are similar and the files differ, so the
        guard keeps one removed row and one added row.
        """
        base = {
            "ias-16/draft-v1-linked/abbreviations.html": "<table><tr><td>SOC</td></tr></table>",
            "ias-16/draft-v1-linked/ch04.html": "<table><tr><td id=\"s-4-5-impair\">Kept cell</td></tr></table>",
        }
        head = {
            "ias-16/draft-v1-linked/abbreviations.html": "<table><tr></tr></table>",
            "ias-16/draft-v1-linked/ch04.html": "<table><tr><td id=\"s-4-5-impair\">Kept cell</td><td>OCI</td></tr></table>",
        }
        code, rows, counts, issues = judge(base, head)
        self.assertNotEqual(code, 0)
        self.assertTrue(any("UNAPPROVED removed" in issue for issue in issues))
        self.assertFalse(any(row.status == "changed" for row in rows))
        self.assertEqual(counts["removed"], 1)
        self.assertEqual(counts["added"], 1)
        self.assertEqual(counts["changed"], 0)
        self.assertEqual(counts["moved"], 0)
        removed = [row for row in rows if row.status == "removed"]
        added = [row for row in rows if row.status == "added"]
        self.assertEqual(removed[0].old, "SOC")
        self.assertEqual(removed[0].file, "ias-16/draft-v1-linked/abbreviations.html")
        self.assertEqual(added[0].new, "OCI")
        self.assertEqual(added[0].file, "ias-16/draft-v1-linked/ch04.html")
        self._assert_balanced(counts, issues)


if __name__ == "__main__":
    unittest.main()
