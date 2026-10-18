#!/usr/bin/env python3
"""#86: sibling arrow heads fail, and the live tree passes."""

import importlib.util
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("map_lint", TOOLS / "map-lint.py")
lint = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lint)


class MapLintRow86Tests(unittest.TestCase):
    def test_sibling_head_fixture_fails(self):
        text = '<div class="st-down"><span class="stem-head"></span></div>\n'
        errors = lint.sibling_head_errors(text, "fixture.html")
        self.assertEqual(len(errors), 1)
        self.assertIn("sibling arrow head", errors[0])

    def test_continuous_shaft_passes(self):
        text = '<div class="st-down"><span class="stem-shaft"></span></div>\n'
        self.assertEqual(lint.sibling_head_errors(text, "fixture.html"), [])

    def test_live_tree_passes(self):
        self.assertEqual(lint.lint(), [])


if __name__ == "__main__":
    unittest.main()
