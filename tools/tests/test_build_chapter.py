#!/usr/bin/env python3
"""Chapter template: fixtures, live-page round trip, and the --check gate."""

import importlib.util
import io
import shutil
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "build-chapter"
_spec = importlib.util.spec_from_file_location("build_chapter", TOOLS / "build-chapter.py")
build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build)

LIVE = (
    ("ias-16", "ias16", "IAS 16", "ch01.html"),
    ("ias-2", "ias2", "IAS 2", "ch01.html"),
    ("ifrs-18", "ifrs18", "IFRS 18", "ch01.html"),
    ("cf-2018", "cf2018", "Conceptual Framework 2018", "ch01.html"),
)
SEE_CSS = ROOT / "_shared" / "see-also.css"


def section_slices(page):
    article = build.re.search(
        r'<article class="teaching">(.*)</article>', page, build.re.S
    ).group(1)
    found = list(build.H3_RE.finditer(article))
    bodies = []
    for index, h3 in enumerate(found):
        end = found[index + 1].start() if index + 1 < len(found) else len(article)
        bodies.append(article[h3.end() : end].strip("\n"))
    return bodies


class BuildChapterTests(unittest.TestCase):
    def render_fixture(self, pack_dir, warnings=None):
        warnings = [] if warnings is None else warnings
        profile = build.load_profile(pack_dir)
        chapters = build.read_sources(pack_dir)
        rendered = build.render_pack(pack_dir, profile, chapters, pack_dir, warnings)
        return profile, {chapter["file"]: page for chapter, page in rendered}

    def test_new_chapter_matches_golden_and_chrome_row(self):
        pack = FIXTURES / "new-chapter"
        warnings = []
        _profile, pages = self.render_fixture(pack, warnings)
        html = pages["ch08.html"]
        golden = (pack / "expected" / "ch08.golden").read_text(encoding="utf-8")
        self.assertEqual(html, golden)
        self.assertIn('data-pack="ias16"', html)
        self.assertIn('data-page="chapter"', html)
        self.assertIn('data-chapter="ch08"', html)
        self.assertIn('id="page-map"', html)
        self.assertIn('id="s-8-0"', html)
        self.assertIn('href="#page-map"', html)
        self.assertIn("revaluation model", html)
        self.assertIn('href="ch05.html#s-5-2"', html)
        self.assertIn('class="see-strip-note"', html)
        self.assertIn("<!-- disclaimer:start -->", html)
        self.assertIn('id="pack-disclaimer"', html)
        self.assertIn("footer-nav-20261010", html)
        self.assertNotIn("style=", html.lower())
        self.assertNotIn("font-weight", html)
        self.assertEqual(
            [warning for warning in warnings if "ch08.html" in warning],
            [],
        )
        chrome = (pack / "chrome-packs.js").read_text(encoding="utf-8")
        updated = build.apply_chrome(chrome, build.read_sources(pack), "ias16")
        self.assertIn('{ href: "ch08.html", label: "8 Transition" }', updated)
        self.assertIn('{ href: "ch09.html", label: "9 Held for sale" }', updated)
        self.assertLess(
            updated.index("ch07.html"),
            updated.index("ch08.html"),
        )
        self.assertLess(
            updated.index("ch08.html"),
            updated.index("ch09.html"),
        )
        self.assertIn("personal study notes.", updated)
        self.assertEqual(build.apply_chrome(updated, build.read_sources(pack), "ias16"), updated)

    def test_round_trip_fixtures_one_per_pack(self):
        for name in ("ias16", "ias2", "ifrs18", "cf2018"):
            with self.subTest(pack=name):
                pack = FIXTURES / "roundtrip" / name
                warnings = []
                profile, pages = self.render_fixture(pack, warnings)
                html = pages["ch01.html"]
                again = build.extract_chapter(html, "ch01.html")
                second = build.render_chapter(
                    {**again, "pill": "ignored", "where": "round trip"},
                    profile,
                    pack / "draft-v1-linked",
                    pack,
                    [],
                )
                self.assertEqual(second, html)
                self.assertEqual(build.comparable(again), build.comparable(build.read_sources(pack)[0]))
                self.assertNotIn("style=", html.lower())
                self.assertIn('data-page="chapter"', html)
                self.assertIn('data-chapter="ch01"', html)
                if name == "ifrs18":
                    self.assertNotIn('name="robots"', html)
                    self.assertIn("assets/map.css?v=", html)
                if name == "cf2018":
                    self.assertIn("assets/map.css?v=", html)
                    self.assertIn('class="see-strip-note"', html)
                    self.assertIn('class="sec-no"', html)
                if name == "ias2":
                    self.assertIn('id="key-terms"', html)
                    self.assertIn('id="pack-stamp"', html)
                    self.assertNotIn('class="purpose"', html)

    def test_live_pages_round_trip_teaching_body(self):
        for folder, pack_id, standard, file_name in LIVE:
            with self.subTest(pack=folder):
                path = ROOT / folder / "draft-v1-linked" / file_name
                original = path.read_text(encoding="utf-8")
                chapter = build.extract_chapter(original, file_name)
                self.assertEqual(chapter["pack"], pack_id)
                self.assertEqual(chapter["file"], file_name)
                bodies = section_slices(original)
                self.assertEqual(len(bodies), len(chapter["sections"]))
                for body, section in zip(bodies, chapter["sections"]):
                    self.assertEqual(build.blocks_html(section["blocks"]), body)
                profile = {
                    "id": pack_id,
                    "standard": standard,
                    "noindex": 'content="noindex"' in original,
                    "css": build.re.findall(r'href="(assets/[^"?]+)', original),
                }
                warnings = []
                rendered = build.render_chapter(
                    chapter,
                    profile,
                    path.parent,
                    ROOT,
                    warnings,
                )
                self.assertEqual(path.read_text(encoding="utf-8"), original)
                again = build.extract_chapter(rendered, file_name)
                self.assertEqual(build.comparable(again), build.comparable(chapter))
                self.assertIn(
                    f'data-pack="{pack_id}" data-page="chapter" data-chapter="{file_name[:-5]}"',
                    rendered,
                )
                self.assertNotIn("style=", rendered.lower())
                second = build.render_chapter(again, profile, path.parent, ROOT, [])
                self.assertEqual(second, rendered)

    def test_duplicate_section_id_fails(self):
        text = (FIXTURES / "new-chapter" / "source" / "ch08.md").read_text(encoding="utf-8")
        text = text.replace("## 8.1 Proceeds before intended use", "## 8.0 Again")
        with self.assertRaises(build.ChapterError) as caught:
            build.parse_chapter(text, "ch08.md")
        self.assertIn("duplicate section id s-8-0", str(caught.exception))

    def test_broken_see_target_fails(self):
        pack = FIXTURES / "new-chapter"
        text = (pack / "source" / "ch08.md").read_text(encoding="utf-8")
        text = text.replace(
            "see: ch04.html#s-4-1 — revaluation model; ch05.html#s-5-2",
            "see: ch04.html#s-4-9 — missing section",
        )
        chapter = build.parse_chapter(text, "ch08.md")
        profile = build.load_profile(pack)
        page = build.render_chapter(
            chapter, profile, pack / "draft-v1-linked", pack, []
        )
        with self.assertRaises(build.ChapterError) as caught:
            build.check_see_target(
                "ch04.html#s-4-9",
                page,
                pack / "draft-v1-linked",
                {},
                "ch08.md",
            )
        self.assertIn("broken see:", str(caught.exception))
        with self.assertRaises(build.ChapterError):
            build.check_see_target("#s-8-9", page, pack / "draft-v1-linked", {}, "ch08.md")

    def test_missing_visual_omits_the_frame_and_warns(self):
        pack = FIXTURES / "new-chapter"
        warnings = []
        _profile, pages = self.render_fixture(pack, warnings)
        html = pages["ch09.html"]
        self.assertNotIn("visual-section", html)
        self.assertNotIn("visual-fieldset", html)
        self.assertNotIn('id="page-map"', html)
        self.assertIn('href="#chapter-title"', html)
        self.assertTrue(any("ch09.html" in warning and "map frame omitted" in warning for warning in warnings))
        self.assertNotIn("\n\n\n", html)

    def test_no_map_key_omits_the_frame(self):
        pack = FIXTURES / "roundtrip" / "ias2"
        text = (pack / "source" / "ch01.md").read_text(encoding="utf-8")
        text = text.replace("map:\n  src: visuals/ch01-scope.html\n  title: \"IAS 2 scope\"\n", "")
        chapter = build.parse_chapter(text, "ch01.md")
        warnings = []
        html = build.render_chapter(
            chapter,
            build.load_profile(pack),
            pack / "draft-v1-linked",
            pack,
            warnings,
        )
        self.assertEqual(len(warnings), 1)
        self.assertIn("map frame omitted", warnings[0])
        self.assertNotIn("visual-section", html)
        self.assertNotIn('id="page-map"', html)

    def test_second_run_writes_nothing(self):
        with self._copied_repo() as root:
            warnings = []
            first = build.build_pack(
                root / "ias-16",
                root / "_shared" / "chrome-packs.js",
                root,
                True,
                warnings,
            )
            self.assertTrue(first["changed"])
            html = (root / "ias-16" / "draft-v1-linked" / "ch08.html").read_bytes()
            chrome = (root / "_shared" / "chrome-packs.js").read_bytes()
            second = build.build_pack(
                root / "ias-16",
                root / "_shared" / "chrome-packs.js",
                root,
                True,
                [],
            )
            self.assertEqual(second["changed"], [])
            self.assertEqual(second["diffs"], [])
            self.assertEqual((root / "ias-16" / "draft-v1-linked" / "ch08.html").read_bytes(), html)
            self.assertEqual((root / "_shared" / "chrome-packs.js").read_bytes(), chrome)

    def test_check_fails_when_the_page_drifts(self):
        with self._copied_repo() as root:
            build.build_pack(
                root / "ias-16",
                root / "_shared" / "chrome-packs.js",
                root,
                True,
                [],
            )
            page = root / "ias-16" / "draft-v1-linked" / "ch08.html"
            page.write_text(page.read_text(encoding="utf-8").replace("Overview", "Overview EDITED"), encoding="utf-8")
            code, out = self._run_main(["--check", "--root", str(root)])
            self.assertEqual(code, 1)
            self.assertIn("Overview", out)
            self.assertIn("drifted", out)

    def test_check_skips_a_tree_with_no_source(self):
        code, out = self._run_main(["--check", "--root", str(ROOT)])
        self.assertEqual(code, 0)
        self.assertIn("no source/", out)
        code, out = self._run_main(["--all", "--root", str(ROOT)])
        self.assertEqual(code, 0)
        self.assertIn("no source/", out)

    def test_see_shorthand_uses_only_see_also_classes(self):
        css = SEE_CSS.read_text(encoding="utf-8")
        for token in ("--t1-fw", "--t3-arm-fw", "--t2-fw"):
            self.assertIn(token, css)
        pack = FIXTURES / "new-chapter"
        _profile, pages = self.render_fixture(pack)
        html = pages["ch08.html"]
        self.assertIn('class="see-also-strip"', html)
        self.assertIn('class="see-label"', html)
        self.assertIn('class="see-bit"', html)
        self.assertIn('class="see-strip-note"', html)
        self.assertNotRegex(html, r"font-weight\s*:")
        self.assertNotIn("style=", html.lower())

    def test_existing_chrome_row_is_left_byte_for_byte(self):
        text = (ROOT / "_shared" / "chrome-packs.js").read_text(encoding="utf-8")
        updated = build.upsert_chapter_row(text, "ias16", "ch01.html", "1 Scope")
        self.assertEqual(updated, text)
        inserted = build.upsert_chapter_row(text, "ias16", "ch08.html", "8 Transition")
        self.assertNotEqual(inserted, text)
        self.assertIn('{ href: "ch08.html", label: "8 Transition" }', inserted)
        self.assertLess(inserted.index('"7 Disclosure"'), inserted.index('"8 Transition"'))
        self.assertIn(text.split("disclaimer:", 1)[1], inserted)
        again = build.upsert_chapter_row(inserted, "ias16", "ch08.html", "8 Transition")
        self.assertEqual(again, inserted)

    def _copied_repo(self):
        return _CopiedRepo()

    def _run_main(self, argv):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = build.main(argv)
        return code, stdout.getvalue() + stderr.getvalue()


class _CopiedRepo:
    """A temp repo whose only sourced pack is a copy of the new-chapter fixture."""

    def __enter__(self):
        import tempfile

        self._handle = tempfile.TemporaryDirectory()
        root = Path(self._handle.name)
        pack = root / "ias-16"
        shutil.copytree(FIXTURES / "new-chapter", pack)
        shared = root / "_shared"
        shared.mkdir()
        shutil.copy(pack / "chrome-packs.js", shared / "chrome-packs.js")
        return root

    def __exit__(self, *args):
        self._handle.cleanup()


if __name__ == "__main__":
    unittest.main()
