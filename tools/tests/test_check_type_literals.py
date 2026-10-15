#!/usr/bin/env python3
"""Fixture checks for the type-literal guard."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "check_type_literals", TOOLS / "check-type-literals.py"
)
guard = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(guard)


def write_pack_css(root, text):
    path = root / "ias-2" / "draft-v1-linked" / "assets" / "sample.css"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path.relative_to(root).as_posix()


class TypeLiteralTests(unittest.TestCase):
    def test_new_literal_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_pack_css(root, ".title {\n  font-weight: 700;\n}\n")
            hits = guard.scan_tree(root)
            new_rows, stale = guard.evaluate(hits, [])
            self.assertEqual(len(new_rows), 1)
            self.assertEqual(new_rows[0]["value"], "700")
            self.assertEqual(stale, [])

    def test_fixed_row_still_listed_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rel = write_pack_css(root, ".title {\n  font-weight: var(--t1-fw);\n}\n")
            baseline = [
                {
                    "path": rel,
                    "selector": ".title",
                    "property": "font-weight",
                    "value": "700",
                    "occurrence": "1",
                    "class": "DRIFT",
                    "line": "2",
                }
            ]
            hits = guard.scan_tree(root)
            new_rows, stale = guard.evaluate(hits, baseline)
            self.assertEqual(new_rows, [])
            self.assertEqual(len(stale), 1)
            self.assertEqual(stale[0]["class"], "DRIFT")

    def test_var_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_pack_css(
                root,
                ".title {\n  font-weight: var(--t1-fw);\n  line-height: calc(var(--t1-lh) * var(--scale));\n}\n",
            )
            hits = guard.scan_tree(root)
            new_rows, stale = guard.evaluate(hits, [])
            self.assertEqual(hits, [])
            self.assertEqual(new_rows, [])
            self.assertEqual(stale, [])

    def test_exception_passes_when_absent(self):
        baseline = [
            {
                "path": "ias-2/draft-v1-linked/assets/sample.css",
                "selector": ".kept",
                "property": "line-height",
                "value": "1.15",
                "occurrence": "1",
                "class": "EXCEPTION",
                "line": "4",
            }
        ]
        new_rows, stale = guard.evaluate([], baseline)
        self.assertEqual(new_rows, [])
        self.assertEqual(stale, [])

    def test_comment_is_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_pack_css(
                root,
                "/* font-weight: 700; */\n.title {\n  font-weight: var(--t2-fw);\n}\n",
            )
            self.assertEqual(guard.scan_tree(root), [])

    def test_line_shift_still_matches(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rel = write_pack_css(root, ".title {\n  font-weight: 700;\n}\n")
            before = guard.scan_tree(root)
            self.assertEqual(before[0]["line"], "2")
            write_pack_css(root, "\n\n.title {\n  font-weight: 700;\n}\n")
            after = guard.scan_tree(root)
            self.assertNotEqual(after[0]["line"], before[0]["line"])
            self.assertEqual(guard.row_key(after[0]), guard.row_key(before[0]))
            baseline = [{**before[0], "class": "DRIFT"}]
            new_rows, stale = guard.evaluate(after, baseline)
            self.assertEqual(new_rows, [])
            self.assertEqual(stale, [])
            self.assertEqual(rel, before[0]["path"])


class HomepageExcludeTests(unittest.TestCase):
    def test_excluded_wireframe_is_ignored_and_live_homepage_is_scanned(self):
        style = "<style>\nbody { line-height: 1.4; }\n</style>\n"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            homepage = root / "homepage"
            homepage.mkdir()
            for name in (
                "_shot-search-demo.html",
                "homepage-wireframe-v0.html",
                "homepage-wireframe-v0.1.before-7c.html",
            ):
                (homepage / name).write_text(style, encoding="utf-8")
            (homepage / "homepage-wireframe-v0.1.html").write_text(style, encoding="utf-8")
            (homepage / "how-these-notes-are-made.html").write_text(style, encoding="utf-8")
            hits = guard.scan_tree(root)
            paths = {hit["path"] for hit in hits}
            self.assertEqual(
                paths,
                {
                    "homepage/homepage-wireframe-v0.1.html",
                    "homepage/how-these-notes-are-made.html",
                },
            )


if __name__ == "__main__":
    unittest.main()
