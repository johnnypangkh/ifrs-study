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


if __name__ == "__main__":
    unittest.main()
