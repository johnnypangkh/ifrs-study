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

    def test_plate_class_colliding_with_bare_shared_rule_fails(self):
        css = ".tl-row { display: flex; max-width: var(--legacy-w-17); }\n.cap { }\n"
        bare = lint.bare_shared_classes([css])
        hits = lint.plate98_shared_collisions({"tl-row", "cap"}, bare)
        self.assertEqual(hits, ["tl-row"])
        self.assertNotIn("tl-row", lint.bare_shared_classes([
            ".plate .tl-row { max-width: none; }\n",
        ]))

    def test_allowlist_only_plate_classes_pass(self):
        css = ".cap{}\n.inner-board{}\n.see-bit{}\n.see-label{}\n.m-tl{}\n.tl-row{}\n"
        bare = lint.bare_shared_classes([css])
        hits = lint.plate98_shared_collisions(set(lint.PLATE98_SHARED_OK), bare)
        self.assertEqual(hits, [])

    def test_invented_map_chrome_class_fails(self):
        css = ".foo-cell { border: var(--stroke-1) solid var(--line); background: var(--surface); }\n"
        errors = lint.map_chrome_alias_errors(css, "fixture.css")
        self.assertEqual(len(errors), 1)
        self.assertIn("invented map chrome class", errors[0])
        self.assertIn(".foo-cell", errors[0])

    def test_unscoped_timeline_paint_fails(self):
        css = ".m-tl-line { background: var(--muted); border: 0; }\n"
        errors = lint.map_chrome_alias_errors(css, "fixture.css")
        self.assertEqual(len(errors), 1)
        self.assertIn("without plate parent", errors[0])

    def test_plate_timeline_placement_passes(self):
        css = (
            ".plate.ch05-dep .m-tl-line { background: var(--accent); }\n"
            ".ppe-tl-row .m-tl { display: flex; }\n"
            ".lens-cell { border: var(--stroke-1) solid var(--line); background: var(--band); }\n"
        )
        self.assertEqual(lint.map_chrome_alias_errors(css, "fixture.css"), [])

    def test_unknown_data_brick_fails(self):
        """#121: B22 / B00 / B9 / b09 / free text FAIL. B01–B21 and a missing attr pass."""
        for value in ("B22", "B00", "B9", "b09", "see-also"):
            text = f'<p data-brick="{value}">x</p>\n'
            errors = lint.data_brick_errors(text, "fixture.html")
            self.assertEqual(len(errors), 1, value)
            self.assertIn("unknown data-brick", errors[0])
            self.assertIn(repr(value), errors[0])
        self.assertEqual(len(lint.data_brick_errors("<p data-brick='B9'>x</p>\n", "fixture.html")), 1)
        self.assertEqual(len(lint.data_brick_errors("<p data-brick=B22>x</p>\n", "fixture.html")), 1)
        self.assertEqual(lint.data_brick_errors("<p>no brick</p>\n", "zero-map.html"), [])
        for value in ("B01", "B09", "B21"):
            self.assertEqual(
                lint.data_brick_errors(f'<p data-brick="{value}"></p>\n', "fixture.html"),
                [],
                value,
            )

    def test_phase1_loci_are_not_force_tagged(self):
        self.assertEqual(
            lint.BRICK_PHASE1_LOCI,
            (
                "ias-16/draft-v1-linked/visuals/ch05-depreciation.html",
                "ias-16/draft-v1-linked/visuals/master-concept-map.html",
            ),
        )
        for rel in lint.BRICK_PHASE1_LOCI:
            text = (lint.ROOT / rel).read_text(encoding="utf-8")
            self.assertEqual(lint.data_brick_errors(text, rel), [])
        self.assertEqual(
            lint.data_brick_errors(
                "<div class='m-l0'></div>\n",
                "ias-2/draft-v1-linked/visuals/ch01-scope.html",
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()
