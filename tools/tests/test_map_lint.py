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

    def test_glyph_connector_fails(self):
        text = '<span class="mx-stem-arrow">▼</span>\n'
        errors = lint.glyph_connector_errors(text, "fixture.html", "")
        self.assertEqual(len(errors), 1)
        self.assertIn("glyph connector", errors[0])

    def test_held_measurement_glyph_needs_the_shaft_head(self):
        text = '<span class="mx-stem-arrow">▼</span>\n'
        box = ".mx-stem::after { border-top: var(--rail-bar-l) solid var(--link-semantic); }\n.mx-stem-arrow { color: transparent; }\n"
        self.assertEqual(
            lint.glyph_connector_errors(text, lint.STAMP_HELD_GLYPH, box),
            [],
        )
        self.assertEqual(len(lint.glyph_connector_errors(text, "other.html", box)), 1)
        self.assertEqual(len(lint.glyph_connector_errors(text, lint.STAMP_HELD_GLYPH, "")), 1)

    def test_bare_shaft_fails_role(self):
        text = '<span class="stem-shaft"></span>\n<span class="map-visit-arrow"></span>\n'
        errors = lint.shaft_role_errors(text, "fixture.html")
        self.assertEqual(len(errors), 2)

    def test_shaft_role_passes(self):
        text = (
            '<span class="stem-shaft m-flow"></span>\n'
            '<span class="m-shaft m-link"></span>\n'
            '<span class="map-visit-arrow m-visit"></span>\n'
            '<span class="stem-shaft m-flow mute"></span>\n'
        )
        self.assertEqual(lint.shaft_role_errors(text, "fixture.html"), [])

    def test_live_tree_passes(self):
        self.assertEqual(lint.lint(), [])


if __name__ == "__main__":
    unittest.main()
