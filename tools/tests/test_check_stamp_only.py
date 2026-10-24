#!/usr/bin/env python3
"""Q-e: the stamp gate allows only the three approved CF iframe-floor deletions."""

import importlib.util
import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "check_stamp_only", TOOLS / "check-stamp-only.py"
)
stamp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(stamp)

LAST_UPDATE = """/* fixture */
(function () {
  var STAMPS = {
    "cf2018": {
      "text": "Last update · 2026-10-14 23:27 HKT",
      "iso": "2026-10-14T23:27:00+08:00",
      "fingerprint": "abc"
    },
    "site": {
      "text": "Last update · 2026-10-14 17:15 HKT",
      "iso": "2026-10-14T17:15:00+08:00",
      "fingerprint": "def"
    }
  };

  var PACK_PATHS = [
    ["/cf-2018/", "cf2018"]
  ];
})();
"""

FOURTH = "cf-2018/draft-v1-linked/ch01.html"
FOURTH_STYLE = '<style id="not-a-floor">.x{color:red}</style>\n'


def page(body, block=""):
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<title>Chapter</title>\n"
        f"{block}"
        "</head>\n<body>\n"
        f"{body}\n"
        "</body>\n</html>\n"
    )


class IframeFloorFoldTests(unittest.TestCase):
    def run_gate(self, root, base_files):
        def git_text(rev, path):
            if path == "_shared/last-update.js":
                return LAST_UPDATE
            return base_files[path]

        def git_paths(rev):
            return list(base_files)

        original_root = stamp.ROOT
        original_text = stamp.git_text
        original_paths = stamp.git_paths
        stamp.ROOT = root
        stamp.git_text = git_text
        stamp.git_paths = git_paths
        buffer = io.StringIO()
        try:
            with redirect_stdout(buffer):
                code = stamp.main(["--base", "fixture"])
        finally:
            stamp.ROOT = original_root
            stamp.git_text = original_text
            stamp.git_paths = original_paths
        return code, buffer.getvalue()

    def write_tree(self, root, files):
        for rel, text in files.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        last = root / "_shared" / "last-update.js"
        last.parent.mkdir(parents=True, exist_ok=True)
        last.write_text(LAST_UPDATE, encoding="utf-8")

    def base_files(self):
        files = {}
        for rel, block in stamp.CF_IFRAME_FLOOR_BLOCKS.items():
            files[rel] = page("Teaching.", block)
        files[FOURTH] = page("Teaching.", FOURTH_STYLE)
        return files

    def test_ias16_extra_section_blank_is_folded(self):
        import tempfile

        ch04 = "ias-16/draft-v1-linked/ch04.html"
        ch05 = "ias-16/draft-v1-linked/ch05.html"
        # s-4-4 loses one blank line. s-4-6 keeps two on both sides.
        # The article close on ch04 is not an approved spot, so it stays equal.
        base_ch04 = (
            '<article class="teaching">\n'
            '<h3 id="s-4-3">4.3</h3>\n<p>Kept.</p>\n\n\n'
            '<h3 id="s-4-4">4.4</h3>\n<p>Kept.</p>\n\n\n'
            '<h3 id="s-4-6">4.6</h3>\n<p>Kept.</p>\n\n</article>'
        )
        head_ch04 = (
            '<article class="teaching">\n'
            '<h3 id="s-4-3">4.3</h3>\n<p>Kept.</p>\n\n'
            '<h3 id="s-4-4">4.4</h3>\n<p>Kept.</p>\n\n\n'
            '<h3 id="s-4-6">4.6</h3>\n<p>Kept.</p>\n\n</article>'
        )
        base_ch05 = (
            '<article class="teaching">\n'
            '<h3 id="s-5-11">5.11</h3>\n<p>Kept.</p>\n\n\n</article>'
        )
        head_ch05 = (
            '<article class="teaching">\n'
            '<h3 id="s-5-11">5.11</h3>\n<p>Kept.</p>\n\n</article>'
        )
        base = {ch04: page(base_ch04), ch05: page(base_ch05)}
        head = {ch04: page(head_ch04), ch05: page(head_ch05)}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_n6_ias16_section_gap_widen_fails(self):
        """N6 widen: a blank line removed outside the nine spots fails."""
        import tempfile

        cases = {
            "unlisted heading on ch04": (
                "ias-16/draft-v1-linked/ch04.html",
                '<h3 id="s-4-5">4.5</h3>',
            ),
            "article close on ch04": (
                "ias-16/draft-v1-linked/ch04.html",
                "</article>",
            ),
            "heading on ch06": (
                "ias-16/draft-v1-linked/ch06.html",
                '<h3 id="s-6-1">6.1</h3>',
            ),
        }
        for label, (rel, marker) in cases.items():
            base_body = f'<article class="teaching">\n<p>Kept.</p>\n\n\n{marker}'
            head_body = f'<article class="teaching">\n<p>Kept.</p>\n\n{marker}'
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.write_tree(root, {rel: page(head_body)})
                code, output = self.run_gate(root, {rel: page(base_body)})
            self.assertEqual(code, 1, f"{label}\n{output}")
            self.assertIn(Path(rel).name, output)
            self.assertNotIn("stamp-only: PASS", output)

    def test_n13_ias16_section_gap_addition_fails(self):
        """N13 addition: a blank line added at an approved spot fails."""
        import tempfile

        rel = "ias-16/draft-v1-linked/ch04.html"
        base_body = (
            '<article class="teaching">\n'
            '<h3 id="s-4-3">4.3</h3>\n<p>Kept.</p>\n\n'
            '<h3 id="s-4-4">4.4</h3>\n<p>Kept.</p>\n\n</article>'
        )
        head_body = (
            '<article class="teaching">\n'
            '<h3 id="s-4-3">4.3</h3>\n<p>Kept.</p>\n\n\n'
            '<h3 id="s-4-4">4.4</h3>\n<p>Kept.</p>\n\n</article>'
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: page(head_body)})
            code, output = self.run_gate(root, {rel: page(base_body)})
        self.assertEqual(code, 1, output)
        self.assertIn("ch04.html", output)
        self.assertNotIn("stamp-only: PASS", output)

    def _cf_shell(self, title_after_css=True, extra_at=None, blanks=()):
        title = "<title>Ch1 Objective</title>\n"
        head = [
            "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n",
            '<meta name="viewport" content="width=1280">\n',
        ]
        if not title_after_css:
            head.append(title)
        head.append('<link rel="stylesheet" href="assets/draft.css?v=abc">\n')
        if title_after_css:
            head.append(title)
        head.append("</head>\n<body>\n<div class=\"page-header\">\n</div>\n")
        gap = {name: "\n" for name in blanks}
        if extra_at:
            gap[extra_at] = gap.get(extra_at, "\n") + "\n"
        head.append(gap.get("map", "") + '<section class="visual-section">\n</section>\n')
        head.append(gap.get("article", "") + '<article class="teaching">\n')
        head.append('<h3 id="s-1-1">1.1</h3>\n<p>Kept.</p>\n')
        head.append(gap.get("close", "") + "</article>\n")
        head.append(gap.get("terms", "") + '<section class="key-terms">\n</section>\n')
        head.append("</body>\n</html>\n")
        return "".join(head)

    def test_cf2018_shell_allowlist_is_folded(self):
        import tempfile

        rel = "cf-2018/draft-v1-linked/ch01.html"
        base = self._cf_shell(title_after_css=True)
        head = self._cf_shell(
            title_after_css=False,
            blanks=("map", "article", "close", "terms"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_cf2018_unlisted_blank_add_fails(self):
        """Unlisted CF gap: a blank line before s-1-1 is not on the allow-list."""
        import tempfile

        rel = "cf-2018/draft-v1-linked/ch01.html"
        base = self._cf_shell(title_after_css=False, blanks=("map", "article", "close", "terms"))
        head = base.replace('<h3 id="s-1-1">', '\n<h3 id="s-1-1">', 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertIn("ch01.html", output)
        self.assertNotIn("stamp-only: PASS", output)

    def test_n10_cf_title_just_before_head_close_fails(self):
        """N10: a head title sitting just before </head> on ch02 fails."""
        import tempfile

        rel = "cf-2018/draft-v1-linked/ch02.html"
        base = self._cf_shell(title_after_css=False)
        title = "<title>Ch1 Objective</title>\n"
        head = base.replace(
            '<meta name="viewport" content="width=1280">\n' + title,
            '<meta name="viewport" content="width=1280">\n',
            1,
        ).replace("</head>\n", title + "</head>\n", 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertIn("ch02.html", output)
        self.assertNotIn("stamp-only: PASS", output)

    def test_n12_cf_title_inside_body_fails(self):
        """N12: a head title sitting inside <body> on ch09 fails."""
        import tempfile

        rel = "cf-2018/draft-v1-linked/ch09.html"
        base = self._cf_shell(title_after_css=False)
        title = "<title>Ch1 Objective</title>\n"
        head = base.replace(
            '<meta name="viewport" content="width=1280">\n' + title,
            '<meta name="viewport" content="width=1280">\n',
            1,
        ).replace("<body>\n", "<body>\n" + title, 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertIn("ch09.html", output)
        self.assertNotIn("stamp-only: PASS", output)

    def test_cf2018_extra_blank_add_fails(self):
        """Extra add: two new blank lines at an approved one-line spot fail."""
        import tempfile

        rel = "cf-2018/draft-v1-linked/ch01.html"
        base = self._cf_shell(title_after_css=False)
        head = self._cf_shell(
            title_after_css=False,
            blanks=("map",),
            extra_at="map",
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertIn("ch01.html", output)
        self.assertNotIn("stamp-only: PASS", output)

    def test_ias2_shell_allowlist_is_folded(self):
        import tempfile

        rel = "ias-2/draft-v1-linked/ch01.html"
        base = self._cf_shell(title_after_css=False).replace(
            "</body>\n",
            "<!-- pack-stamp:end -->\n\n</main>\n</body>\n",
            1,
        )
        head = self._cf_shell(
            title_after_css=False,
            blanks=("map", "article"),
        ).replace(
            '<article class="teaching">\n',
            '<article class="teaching">\n\n',
            1,
        ).replace(
            "</article>\n",
            "\n</article>\n",
            1,
        ).replace(
            "</body>\n",
            "<!-- pack-stamp:end -->\n</main>\n</body>\n",
            1,
        )
        # First heading in the fixture is s-1-1, not s-1-0. Point the
        # allow-list check at the real ch01 marker by renaming it.
        base = base.replace('id="s-1-1"', 'id="s-1-0"', 1)
        head = head.replace('id="s-1-1"', 'id="s-1-0"', 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_ias2_unlisted_blank_and_wrong_title_fail(self):
        """An unlisted IAS 2 gap, and a head title before </head>, fail."""
        import tempfile

        rel = "ias-2/draft-v1-linked/ch02.html"
        base = self._cf_shell(title_after_css=False)
        head = base.replace('<h3 id="s-1-1">', '\n<h3 id="s-1-1">', 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertIn("ch02.html", output)

        title = "<title>Ch1 Objective</title>\n"
        head = base.replace(
            '<meta name="viewport" content="width=1280">\n' + title,
            '<meta name="viewport" content="width=1280">\n',
            1,
        ).replace("</head>\n", title + "</head>\n", 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertNotIn("stamp-only: PASS", output)

    def test_ifrs18_title_and_blank_allowlist_is_folded(self):
        import tempfile

        rel = "ifrs-18/draft-v1-linked/ch06.html"
        old = "<title>Ch6 MPMs — IFRS 18</title>\n"
        new = (
            "<title>Ch6 Management-defined performance measures (MPMs) — "
            "IFRS 18</title>\n"
        )
        base = self._cf_shell(title_after_css=False).replace(
            "<title>Ch1 Objective</title>\n", old, 1
        )
        head = base.replace(old, new, 1).replace(
            '<section class="visual-section">',
            '\n<section class="visual-section">',
            1,
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_ifrs18_unlisted_blank_and_other_title_fail(self):
        """An unlisted IFRS 18 gap, a ch01 title rewrite, and a stale ch06 title fail."""
        import tempfile

        rel = "ifrs-18/draft-v1-linked/ch01.html"
        base = self._cf_shell(title_after_css=False)
        head = base.replace('<h3 id="s-1-1">', '\n<h3 id="s-1-1">', 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertIn("ch01.html", output)

        head = base.replace(
            "<title>Ch1 Objective</title>",
            "<title>Ch1 Something else — IFRS 18</title>",
            1,
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertNotIn("stamp-only: PASS", output)

        rel = "ifrs-18/draft-v1-linked/ch06.html"
        old = "<title>Ch6 MPMs — IFRS 18</title>"
        new = (
            "<title>Ch6 Management-defined performance measures (MPMs) — "
            "IFRS 18</title>"
        )
        base = self._cf_shell(title_after_css=False).replace(
            "<title>Ch1 Objective</title>", old, 1
        )
        head = base.replace(old, new, 1)
        stale = head.replace(new, old, 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: stale})
            code, output = self.run_gate(root, {rel: base.replace(old, new, 1)})
        self.assertEqual(code, 1, output)
        self.assertIn("ch06.html", output)

    def test_shared_visual_stamp_allowlist(self):
        import tempfile

        css = "\n".join(
            [f"/* line {n} */" for n in range(1, 13)]
            + [
                '@import url("tokens-core.css?v=aaaaaaaaaaaa");',
                '@import url("see-also.css?v=bbbbbbbbbbbb");',
            ]
            + [f"/* line {n} */" for n in range(15, 28)]
            + [
                '@import url("modules/visuals/cite-1.css?v=cccccccccccc");',
                '@import url("modules/visuals/components-6.css?v=dddddddddddd");',
                "",
            ]
        )
        head_css = (
            css.replace("aaaaaaaaaaaa", "111111111111")
            .replace("bbbbbbbbbbbb", "222222222222")
            .replace("cccccccccccc", "333333333333")
            .replace("dddddddddddd", "444444444444")
        )
        rel = "cf-2018/draft-v1-linked/visuals/ch01-objective-users.html"
        import hashlib
        digest = hashlib.sha256(head_css.encode("utf-8")).hexdigest()[:12]
        base_page = page(
            '<link rel="stylesheet" href="../../../_shared/visuals.css?v=49cc6a8eed7b">'
        )
        head_page = base_page.replace("49cc6a8eed7b", digest)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head_page, stamp.SHARED_VISUAL_CSS: head_css})
            code, output = self.run_gate(
                root, {rel: base_page, stamp.SHARED_VISUAL_CSS: css}
            )
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

        bad = head_css.replace("/* line 15 */", "/* line 15 edited */", 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head_page, stamp.SHARED_VISUAL_CSS: bad})
            code, output = self.run_gate(
                root, {rel: base_page, stamp.SHARED_VISUAL_CSS: css}
            )
        self.assertEqual(code, 1, output)
        self.assertIn("_shared/visuals.css", output)

        other = head_page.replace(
            "</head>",
            '<link rel="stylesheet" href="x.css?v=new">\n</head>',
            1,
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: other, stamp.SHARED_VISUAL_CSS: head_css})
            code, output = self.run_gate(
                root, {rel: base_page, stamp.SHARED_VISUAL_CSS: css}
            )
        self.assertEqual(code, 1, output)
        self.assertIn(rel, output)

    def test_visuals_layout_and_box_imports_are_stamp_only(self):
        """#82: visuals.css lines 16 and 17 may change ?v= and nothing else."""
        import tempfile

        lines = [f"/* line {n} */" for n in range(1, 30)]
        lines[15] = '@import url("modules/visuals/teaching-layout-1.css?v=500fdee144ef");'
        lines[16] = '@import url("modules/visuals/box-1.css?v=3a5ee9c19f38");'
        base = "\n".join(lines) + "\n"
        head = base.replace("500fdee144ef", "4a3e121b59ef").replace(
            "3a5ee9c19f38", "5a8e0e214e01"
        )
        rel = stamp.SHARED_VISUAL_CSS
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)
        bad = head.replace("teaching-layout-1.css", "teaching-layout-9.css", 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: bad})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertIn("_shared/visuals.css", output)

    def test_visuals_map_box_import_is_stamp_only(self):
        """#85: visuals.css line 30 may change ?v= and nothing else."""
        import tempfile

        lines = [f"/* line {n} */" for n in range(1, 32)]
        lines[29] = '@import url("modules/visuals/map-box.css?v=56bb56b4cee7");'
        base = "\n".join(lines) + "\n"
        head = base.replace("56bb56b4cee7", "aaaaaaaaaaaa")
        rel = stamp.SHARED_VISUAL_CSS
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)
        bad = head.replace("map-box.css", "map-box-2.css", 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: bad})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertIn("_shared/visuals.css", output)

    def test_visuals_timeline_import_may_be_one_trailing_line(self):
        """#109: one trailing timeline-1.css import is allowed when the hash matches."""
        import hashlib
        import tempfile

        lines = [f"/* line {n} */" for n in range(1, 31)]
        lines[29] = '@import url("modules/visuals/map-box.css?v=c28589dc13b6");'
        base = "\n".join(lines) + "\n"
        module = "/* timeline */\n.m-tl{position:relative}\n"
        digest = hashlib.sha256(module.encode("utf-8")).hexdigest()[:12]
        head = base + f'@import url("modules/visuals/timeline-1.css?v={digest}");\n'
        bad = base + '@import url("modules/visuals/timeline-1.css?v=000000000000");\n'
        mod = "_shared/modules/visuals/timeline-1.css"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {mod: module})
            original = stamp.ROOT
            stamp.ROOT = root
            try:
                ok = stamp.shared_visual_stamp_failure(base, head, stamp.SHARED_VISUAL_CSS)
                mismatch = stamp.shared_visual_stamp_failure(base, bad, stamp.SHARED_VISUAL_CSS)
            finally:
                stamp.ROOT = original
        self.assertIsNone(ok)
        self.assertIn("line count changed", mismatch)

    def test_visuals_component_imports_are_stamp_only(self):
        """#83: visuals.css lines 20, 24, 27, and 29 may change ?v= only."""
        import tempfile

        lines = [f"/* line {n} */" for n in range(1, 30)]
        lines[19] = '@import url("modules/visuals/components-2.css?v=63e62dc677fa");'
        lines[23] = '@import url("modules/visuals/components-4.css?v=d1bf3c1fee98");'
        lines[26] = '@import url("modules/visuals/components-5.css?v=634afd689584");'
        lines[28] = '@import url("modules/visuals/components-6.css?v=18232257839c");'
        base = "\n".join(lines) + "\n"
        head = (
            base.replace("63e62dc677fa", "aaaaaaaaaaaa")
            .replace("d1bf3c1fee98", "bbbbbbbbbbbb")
            .replace("634afd689584", "cccccccccccc")
            .replace("18232257839c", "dddddddddddd")
        )
        rel = stamp.SHARED_VISUAL_CSS
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)
        bad = head.replace("components-2.css", "components-9.css", 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: bad})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertIn("_shared/visuals.css", output)

    def test_ifrs18_ch03_inbody_iframes_are_allowlisted(self):
        import tempfile

        rel = stamp.IFRS18_CH03
        base = page(
            '<iframe src="visuals/ch03-mba-nest.html?v=c6b520c6ecf8"></iframe>\n'
            '<iframe src="visuals/ch03-classification-path.html?v=deba6c7fa271"></iframe>'
        )
        head = page(
            '<iframe src="visuals/ch03-mba-nest.html?v=da47600ecc21"></iframe>\n'
            '<iframe src="visuals/ch03-classification-path.html?v=628ac37c2497"></iframe>'
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

        bad = head.replace("scrolling", "scrolling", 1)
        bad = head.replace(
            "ch03-mba-nest.html?v=da47600ecc21",
            "ch03-mba-nest.html?v=da47600ecc21&amp;x",
            1,
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: bad})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertIn(rel, output)

    def test_ias16_section_word_change_still_fails(self):
        import tempfile

        rel = "ias-16/draft-v1-linked/ch05.html"
        base_body = '<article class="teaching">\n<h3 id="s-5-3">5.3</h3>\n<p>Kept.</p>\n\n</article>'
        head_body = base_body.replace("Kept.", "Edited.")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: page(head_body)})
            code, output = self.run_gate(root, {rel: page(base_body)})
        self.assertEqual(code, 1, output)
        self.assertIn("ch05.html", output)

    def test_deleting_the_three_approved_blocks_passes(self):
        import tempfile

        base = self.base_files()
        head = dict(base)
        for rel in stamp.CF_IFRAME_FLOOR_BLOCKS:
            head[rel] = page("Teaching.")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_extra_character_in_ch03_fails(self):
        import tempfile

        base = self.base_files()
        head = dict(base)
        for rel in stamp.CF_IFRAME_FLOOR_BLOCKS:
            head[rel] = page("Teaching.")
        head["cf-2018/draft-v1-linked/ch03.html"] = page("Teachinx.")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn("ch03.html", output)

    def test_fourth_style_removal_fails(self):
        import tempfile

        base = self.base_files()
        head = dict(base)
        for rel in stamp.CF_IFRAME_FLOOR_BLOCKS:
            head[rel] = page("Teaching.")
        head[FOURTH] = page("Teaching.")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn("ch01.html", output)


class Ias16ReferencesMutedFoldTests(unittest.TestCase):
    SPAN = stamp.IAS16_MUTED_SPAN
    CLASS = stamp.IAS16_MUTED_CLASS
    PAGE = stamp.IAS16_REFERENCES

    def run_gate(self, root, base_files):
        def git_text(rev, path):
            if path == "_shared/last-update.js":
                return LAST_UPDATE
            return base_files[path]

        def git_paths(rev):
            return list(base_files)

        original_root = stamp.ROOT
        original_text = stamp.git_text
        original_paths = stamp.git_paths
        stamp.ROOT = root
        stamp.git_text = git_text
        stamp.git_paths = git_paths
        buffer = io.StringIO()
        try:
            with redirect_stdout(buffer):
                code = stamp.main(["--base", "fixture"])
        finally:
            stamp.ROOT = original_root
            stamp.git_text = original_text
            stamp.git_paths = original_paths
        return code, buffer.getvalue()

    def write_tree(self, root, files):
        for rel, text in files.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        last = root / "_shared" / "last-update.js"
        last.parent.mkdir(parents=True, exist_ok=True)
        last.write_text(LAST_UPDATE, encoding="utf-8")

    def test_the_one_span_swap_passes(self):
        import tempfile

        base = {self.PAGE: page(f"Teaching. {self.SPAN}")}
        head = {self.PAGE: page(f"Teaching. {self.CLASS}")}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_any_other_teaching_edit_fails(self):
        import tempfile

        base = {self.PAGE: page(f"Teaching. {self.SPAN}")}
        head = {self.PAGE: page(f"Teachinx. {self.CLASS}")}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn("references.html", output)


class Ias2InlineStyleFoldTests(unittest.TestCase):
    """J1 (a): only the eight approved IAS 2 inline-style edits fold."""

    def run_gate(self, root, base_files):
        def git_text(rev, path):
            if path == "_shared/last-update.js":
                return LAST_UPDATE
            return base_files[path]

        def git_paths(rev):
            return list(base_files)

        original_root = stamp.ROOT
        original_text = stamp.git_text
        original_paths = stamp.git_paths
        stamp.ROOT = root
        stamp.git_text = git_text
        stamp.git_paths = git_paths
        buffer = io.StringIO()
        try:
            with redirect_stdout(buffer):
                code = stamp.main(["--base", "fixture"])
        finally:
            stamp.ROOT = original_root
            stamp.git_text = original_text
            stamp.git_paths = original_paths
        return code, buffer.getvalue()

    def write_tree(self, root, files):
        for rel, text in files.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        last = root / "_shared" / "last-update.js"
        last.parent.mkdir(parents=True, exist_ok=True)
        last.write_text(LAST_UPDATE, encoding="utf-8")

    def approved_base(self):
        files = {}
        for rel in stamp.IAS2_DISCLAIMER_PAGES:
            files[rel] = page(f"Teaching. {stamp.IAS2_DISCLAIMER_STRONG}")
        files[stamp.IAS2_REFERENCES] = page(f"Teaching. {stamp.IAS2_MUTED_SPAN}")
        return files

    def approved_head(self, base):
        head = {}
        for rel in stamp.IAS2_DISCLAIMER_PAGES:
            head[rel] = page(f"Teaching. {stamp.IAS2_DISCLAIMER_PLAIN}")
        head[stamp.IAS2_REFERENCES] = page(f"Teaching. {stamp.IAS2_MUTED_CLASS}")
        return head

    def test_the_eight_edits_pass(self):
        import tempfile

        base = self.approved_base()
        head = self.approved_head(base)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_any_other_teaching_edit_fails(self):
        import tempfile

        base = self.approved_base()
        head = self.approved_head(base)
        head["ias-2/draft-v1-linked/ch03.html"] = page(
            f"Teachinx. {stamp.IAS2_DISCLAIMER_PLAIN}"
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn("ch03.html", output)


class DisclaimerInjectorFoldTests(unittest.TestCase):
    """J4: only the empty Disclaimer shell on the 44 pack pages folds."""

    PAGE = "ias-16/draft-v1-linked/ch01.html"
    MOVED = "ias-2/draft-v1-linked/ch01.html"

    def run_gate(self, root, base_files):
        def git_text(rev, path):
            if path == "_shared/last-update.js":
                return LAST_UPDATE
            return base_files[path]

        def git_paths(rev):
            return list(base_files)

        original_root = stamp.ROOT
        original_text = stamp.git_text
        original_paths = stamp.git_paths
        stamp.ROOT = root
        stamp.git_text = git_text
        stamp.git_paths = git_paths
        buffer = io.StringIO()
        try:
            with redirect_stdout(buffer):
                code = stamp.main(["--base", "fixture"])
        finally:
            stamp.ROOT = original_root
            stamp.git_text = original_text
            stamp.git_paths = original_paths
        return code, buffer.getvalue()

    def write_tree(self, root, files):
        for rel, text in files.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        last = root / "_shared" / "last-update.js"
        last.parent.mkdir(parents=True, exist_ok=True)
        last.write_text(LAST_UPDATE, encoding="utf-8")

    def aside(self, note_box=False):
        for block in stamp.DISCLAIMER_KNOWN_ASIDES:
            has_note = "note-box" in block
            if has_note != note_box:
                continue
            # PAGE is an IAS 16 chapter. A CF or IFRS 18 wording is a
            # cross-pack swap and must not fold there.
            if not note_box and "IAS 16 pages" not in block:
                continue
            return block
        raise AssertionError("missing known aside")

    def shell_page(self, body):
        return page(
            body
            + "\n\n"
            + stamp.DISCLAIMER_SHELL
            + "\n\n"
            + "<!-- footer-nav:start -->\n"
        )

    def test_shell_replacing_the_pasted_aside_passes(self):
        import tempfile

        base = {self.PAGE: page("Teaching.\n\n" + self.aside() + "\n\n<!-- footer-nav:start -->\n")}
        head = {self.PAGE: self.shell_page("Teaching.")}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_ias2_aside_move_before_footer_nav_passes(self):
        import tempfile

        pasted = (
            "Teaching.\n\n<!-- footer-nav:start -->\n"
            "<footer>\n  <p>References stay.</p>\n  "
            + self.aside(note_box=True)
            + "\n</footer>\n"
        )
        base = {self.MOVED: page(pasted)}
        head = {
            self.MOVED: page(
                "Teaching.\n\n"
                + stamp.DISCLAIMER_SHELL
                + "\n\n<!-- footer-nav:start -->\n"
                "<footer>\n  <p>References stay.</p>\n</footer>\n"
            )
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_other_edit_inside_the_aside_fails(self):
        import tempfile

        pasted = self.aside().replace("personal study notes", "personal study noteX", 1)
        base = {self.PAGE: page("Teaching.\n\n" + self.aside() + "\n\n<!-- footer-nav:start -->\n")}
        head = {self.PAGE: page("Teaching.\n\n" + pasted + "\n\n<!-- footer-nav:start -->\n")}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn("ch01.html", output)

    def test_other_edit_on_the_page_fails(self):
        import tempfile

        base = {self.PAGE: page("Teaching.\n\n" + self.aside() + "\n\n<!-- footer-nav:start -->\n")}
        head = {self.PAGE: self.shell_page("Teachinx.")}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn("ch01.html", output)

    def test_same_swap_on_an_unlisted_page_fails(self):
        import tempfile

        other = "notes/extra.html"
        base = {other: page("Teaching.\n\n" + self.aside() + "\n\n<!-- footer-nav:start -->\n")}
        head = {other: self.shell_page("Teaching.")}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn("extra.html", output)

    def test_n6_shell_moved_after_footer_nav(self):
        """N6 shell moved after footer-nav"""
        import tempfile

        base = {
            self.PAGE: page(
                "Teaching.\n\n" + self.aside() + "\n\n<!-- footer-nav:start -->\n"
            )
        }
        head = {
            self.PAGE: page(
                "Teaching.\n\n<!-- footer-nav:start -->\n"
                + stamp.DISCLAIMER_SHELL
                + "\n"
            )
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn(
            "HTML changed outside ?v= and the homepage link: " + self.PAGE,
            output,
        )
        self.assertNotIn("stamp-only: PASS", output)

    def test_n6b_shell_moved_to_top_of_main(self):
        """N6b shell moved to top of <main> (mid-page, before teaching)"""
        import tempfile

        base = {self.PAGE: self.shell_page("<main>\n<p>Teaching.</p>\n</main>")}
        head = {
            self.PAGE: page(
                "<main>\n"
                + stamp.DISCLAIMER_SHELL
                + "\n<p>Teaching.</p>\n</main>\n\n<!-- footer-nav:start -->\n"
            )
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn(
            "HTML changed outside ?v= and the homepage link: " + self.PAGE,
            output,
        )
        self.assertNotIn("stamp-only: PASS", output)

    def test_n6c_known_aside_pasted_mid_page(self):
        """N6c known base aside text pasted mid-page on head (in place of shell)"""
        import tempfile

        aside = self.aside()
        base = {
            self.PAGE: page(
                "Before.\n\nAfter.\n\n" + aside + "\n\n<!-- footer-nav:start -->\n"
            )
        }
        head = {
            self.PAGE: page(
                "Before.\n\n" + aside + "\n\nAfter.\n\n<!-- footer-nav:start -->\n"
            )
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn(
            "HTML changed outside ?v= and the homepage link: " + self.PAGE,
            output,
        )
        self.assertNotIn("stamp-only: PASS", output)

    def test_n6d_cf_page_carrying_ias2_aside(self):
        """N6d CF page carrying IAS 2 base aside text (cross-pack swap)"""
        import tempfile

        cf_page = "cf-2018/draft-v1-linked/ch01.html"
        cf_aside = next(
            block
            for block in stamp.DISCLAIMER_KNOWN_ASIDES
            if "Conceptual Framework 2018" in block and "firm-manual material" in block
        )
        ias2_aside = next(
            block
            for block in stamp.DISCLAIMER_KNOWN_ASIDES
            if "IAS 2 pages" in block and "note-box" not in block
        )
        base = {
            cf_page: page(
                "Teaching.\n\n" + cf_aside + "\n\n<!-- footer-nav:start -->\n"
            )
        }
        head = {
            cf_page: page(
                "Teaching.\n\n" + ias2_aside + "\n\n<!-- footer-nav:start -->\n"
            )
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn(
            "HTML changed outside ?v= and the homepage link: " + cf_page,
            output,
        )
        self.assertNotIn("stamp-only: PASS", output)

    def test_e10_cf_minority_wording_on_ch05(self):
        """E10 CF minority wording in the shell slot on CF ch05 must FAIL"""
        import tempfile

        cf_page = "cf-2018/draft-v1-linked/ch05.html"
        majority = next(
            block
            for block in stamp.DISCLAIMER_KNOWN_ASIDES
            if "Conceptual Framework 2018" in block and "firm-manual material" in block
        )
        minority = next(
            block
            for block in stamp.DISCLAIMER_KNOWN_ASIDES
            if "Conceptual Framework 2018" in block and "issuer financial statements" in block
        )
        base = {
            cf_page: page(
                "Teaching.\n\n" + majority + "\n\n<!-- footer-nav:start -->\n"
            )
        }
        head = {
            cf_page: page(
                "Teaching.\n\n" + minority + "\n\n<!-- footer-nav:start -->\n"
            )
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn(
            "HTML changed outside ?v= and the homepage link: " + cf_page,
            output,
        )
        self.assertNotIn("stamp-only: PASS", output)


class Pr6CleanupFoldTests(unittest.TestCase):
    """PR-6: noindex on 9 IFRS 18 pages and MD-1 body tags on 14 pages."""

    def run_gate(self, root, base_files):
        def git_text(rev, path):
            if path == "_shared/last-update.js":
                return LAST_UPDATE
            return base_files[path]

        def git_paths(rev):
            return list(base_files)

        original_root = stamp.ROOT
        original_text = stamp.git_text
        original_paths = stamp.git_paths
        stamp.ROOT = root
        stamp.git_text = git_text
        stamp.git_paths = git_paths
        buffer = io.StringIO()
        try:
            with redirect_stdout(buffer):
                code = stamp.main(["--base", "fixture"])
        finally:
            stamp.ROOT = original_root
            stamp.git_text = original_text
            stamp.git_paths = original_paths
        return code, buffer.getvalue()

    def write_tree(self, root, files):
        for rel, text in files.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        last = root / "_shared" / "last-update.js"
        last.parent.mkdir(parents=True, exist_ok=True)
        last.write_text(LAST_UPDATE, encoding="utf-8")

    def base_files(self):
        files = {}
        for rel in stamp.PR6_NOINDEX_PAGES:
            files[rel] = page("Teaching.")
        for rel in stamp.PR6_IAS16_CHAPTERS:
            chapter = Path(rel).stem
            files[rel] = page("Teaching.").replace(
                "<body>",
                f'<body data-pack="ias16" data-page="{chapter}">',
                1,
            )
        for rel in stamp.PR6_IAS2_CHAPTERS:
            files[rel] = page("Teaching.").replace(
                "<body>",
                '<body data-pack="ias2">',
                1,
            )
        files[stamp.PR6_IAS2_INDEX] = page("Teaching.").replace(
            "<body>",
            '<body data-pack="ias2">',
            1,
        )
        return files

    def approved_head(self, base):
        head = dict(base)
        for rel in stamp.PR6_NOINDEX_PAGES:
            head[rel] = head[rel].replace(
                "<head>\n",
                '<head>\n<meta name="robots" content="noindex">\n',
                1,
            )
        for rel in stamp.PR6_IAS16_CHAPTERS:
            chapter = Path(rel).stem
            head[rel] = head[rel].replace(
                f'data-pack="ias16" data-page="{chapter}"',
                f'data-pack="ias16" data-page="chapter" data-chapter="{chapter}"',
                1,
            )
        for rel in stamp.PR6_IAS2_CHAPTERS:
            chapter = Path(rel).stem
            head[rel] = head[rel].replace(
                'data-pack="ias2"',
                f'data-pack="ias2" data-page="chapter" data-chapter="{chapter}"',
                1,
            )
        head[stamp.PR6_IAS2_INDEX] = head[stamp.PR6_IAS2_INDEX].replace(
            'data-pack="ias2"',
            'data-pack="ias2" data-page="map"',
            1,
        )
        return head

    def test_the_approved_edits_pass(self):
        import tempfile

        base = self.base_files()
        head = self.approved_head(base)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_any_other_teaching_edit_fails(self):
        import tempfile

        base = self.base_files()
        head = self.approved_head(base)
        rel = "ifrs-18/draft-v1-linked/ch03.html"
        head[rel] = head[rel].replace("Teaching.", "Teachinx.", 1)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, head)
            code, output = self.run_gate(root, base)
        self.assertEqual(code, 1, output)
        self.assertIn("ch03.html", output)
        self.assertNotIn("stamp-only: PASS", output)


class StampHashTests(unittest.TestCase):
    """Each checked ?v= must be the target sha256[:12], with one name stamp."""

    REL = "ias-16/draft-v1-linked/ch01.html"

    def run_gate(self, root, base_files):
        return IframeFloorFoldTests.run_gate(self, root, base_files)

    def write_tree(self, root, files):
        return IframeFloorFoldTests.write_tree(self, root, files)

    def _css(self, root, text):
        path = root / "ias-16/draft-v1-linked/assets/extra.css"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_wrong_hash_fails(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._css(root, "body{color:red}")
            good = stamp.file_stamp(root / "ias-16/draft-v1-linked/assets/extra.css")
            base = page(f'<link rel="stylesheet" href="assets/extra.css?v={good}">')
            head = page('<link rel="stylesheet" href="assets/extra.css?v=000000000000">')
            self.write_tree(root, {self.REL: head})
            code, output = self.run_gate(root, {self.REL: base})
        self.assertEqual(code, 1, output)
        self.assertIn("stamp hash mismatch", output)
        self.assertIn("ch01.html", output)

    def test_stale_old_hash_fails(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            css = self._css(root, "v1")
            old = stamp.file_stamp(css)
            css.write_text("v2", encoding="utf-8")
            html = page(f'<link rel="stylesheet" href="assets/extra.css?v={old}">')
            self.write_tree(root, {self.REL: html})
            code, output = self.run_gate(root, {self.REL: html})
        self.assertEqual(code, 1, output)
        self.assertIn("stamp hash mismatch", output)
        self.assertIn(old, output)

    def test_correct_hash_passes(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            css = self._css(root, "body{color:red}")
            good = stamp.file_stamp(css)
            html = page(f'<link rel="stylesheet" href="assets/extra.css?v={good}">')
            self.write_tree(root, {self.REL: html})
            code, output = self.run_gate(root, {self.REL: html})
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_hand_token_fails(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._css(root, "body{color:red}")
            html = page(
                '<link rel="stylesheet" href="assets/extra.css?v=ias16-flow-v3-20261010">'
            )
            self.write_tree(root, {self.REL: html})
            code, output = self.run_gate(root, {self.REL: html})
        self.assertEqual(code, 1, output)
        self.assertIn("stamp hand token", output)

    def test_version_added_off_the_allowlist_fails(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            css = self._css(root, "body{color:red}")
            good = stamp.file_stamp(css)
            base = page('<link rel="stylesheet" href="assets/extra.css">')
            head = page(f'<link rel="stylesheet" href="assets/extra.css?v={good}">')
            self.write_tree(root, {self.REL: head})
            code, output = self.run_gate(root, {self.REL: base})
        self.assertEqual(code, 1, output)
        self.assertIn("added off the allowlist", output)
        self.assertIn("ch01.html", output)

    def test_non_version_byte_change_fails(self):
        import tempfile

        rel = self.REL
        base = page("Teaching.")
        head = page("Teachinx.")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
        self.assertEqual(code, 1, output)
        self.assertIn("HTML changed", output)
        self.assertIn("ch01.html", output)

    def test_footer_nav_name_stamp_passes(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / "_shared" / "footer-nav.js"
            script.parent.mkdir(parents=True, exist_ok=True)
            script.write_text("/* name stamp, not a hash */", encoding="utf-8")
            html = page(
                '<script src="../../_shared/footer-nav.js?v=footer-nav-20261010"></script>'
            )
            self.write_tree(root, {self.REL: html})
            code, output = self.run_gate(root, {self.REL: html})
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_settings_version_must_match_disk(self):
        """N-A8: a wrong settings ?v= or a non-?v= edit fails."""
        import hashlib
        import tempfile

        rel = stamp.SETTINGS_PAGE
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / "_shared" / "chrome-include.js"
            script.parent.mkdir(parents=True, exist_ok=True)
            script.write_text("include", encoding="utf-8")
            good = stamp.file_stamp(script)
            last_hash = hashlib.sha256(LAST_UPDATE.encode("utf-8")).hexdigest()[:12]
            base = (
                f'<script src="../../_shared/chrome-include.js?v={good}"></script>\n'
                f'<script src="../../_shared/last-update.js?v={last_hash}"></script>\n'
                "<p>Kept.</p>\n"
            )
            head = base
            self.write_tree(root, {rel: head})
            code, output = self.run_gate(root, {rel: base})
            self.assertEqual(code, 0, output)
            wrong = base.replace(good, "000000000000")
            self.write_tree(root, {rel: wrong})
            code, output = self.run_gate(root, {rel: base})
            self.assertEqual(code, 1, output)
            self.assertIn("settings stamp hash mismatch", output)
            stale_last = base.replace(last_hash, "111111111111")
            self.write_tree(root, {rel: stale_last})
            code, output = self.run_gate(root, {rel: base})
            self.assertEqual(code, 1, output)
            self.assertIn("settings stamp hash mismatch", output)
            edited = head.replace("Kept.", "Edited.")
            self.write_tree(root, {rel: edited})
            code, output = self.run_gate(root, {rel: base})
            self.assertEqual(code, 1, output)
            self.assertIn("diff outside the allowlist", output)


class ChromeMapTests(unittest.TestCase):
    """Per-asset V map: N-A1 through P-A10."""

    def setUp(self):
        self.host = StampHashTests()

    def _assets(self, root):
        values = {}
        for name in stamp.CHROME_ASSETS:
            path = root / "_shared" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(name + "\n", encoding="utf-8")
            values[name] = stamp.file_stamp(path)
        return values

    def _include(self, values, index="04ac0c0d58be", asset_expr="V[file]", write_extra=""):
        lines = ",\n".join(
            f'    "{name}": "{values[name]}"' for name in stamp.CHROME_ASSETS
        )
        return (
            "/* chrome */\n"
            "   Map values are sha256[:12]. stamp-assets.py rewrites them.\n"
            "(function () {\n"
            "  var V = {\n"
            f"{lines}\n"
            "  };\n"
            f'  var INDEX = "{index}";\n'
            "  function asset(file) {\n"
            f'    return dir + file + "?v=" + {asset_expr};\n'
            "  }\n"
            "  document.write('<link rel=\"stylesheet\" href=\"' + asset(\"chrome.css\") + '\">');\n"
            "  document.write('<script src=\"' + asset(\"theme.js\") + '\"><\\/script>');\n"
            f"{write_extra}"
            "})();\n"
        )

    def _gate(self, root, files, base):
        return self.host.run_gate(root, base)

    def test_n_a1_wrong_theme_hash_fails(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            values = self._assets(root)
            bad = dict(values)
            bad["theme.js"] = "000000000000"
            text = self._include(bad)
            self.host.write_tree(root, {stamp.CHROME_INCLUDE: text})
            code, output = self._gate(root, {}, {stamp.CHROME_INCLUDE: text})
        self.assertEqual(code, 1, output)
        self.assertIn("theme.js", output)

    def test_n_a2_missing_key_fails(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            values = self._assets(root)
            text = self._include(values).replace(
                '    "search.js": "' + values["search.js"] + '"\n', ""
            )
            self.host.write_tree(root, {stamp.CHROME_INCLUDE: text})
            code, output = self._gate(root, {}, {stamp.CHROME_INCLUDE: text})
        self.assertEqual(code, 1, output)
        self.assertIn("missing a key", output)

    def test_n_a3_extra_key_fails(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            values = self._assets(root)
            text = self._include(values).replace(
                "  };",
                '    "extra.js": "0123456789ab"\n  };',
                1,
            )
            self.host.write_tree(root, {stamp.CHROME_INCLUDE: text})
            code, output = self._gate(root, {}, {stamp.CHROME_INCLUDE: text})
        self.assertEqual(code, 1, output)
        self.assertIn("extra key", output)

    def test_n_a4_write_list_edit_fails(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            values = self._assets(root)
            good = self._include(values)
            bad = good.replace('asset("theme.js")', 'asset("other.js")', 1)
            self.host.write_tree(root, {stamp.CHROME_INCLUDE: bad})
            code, output = self._gate(root, {}, {stamp.CHROME_INCLUDE: good})
        self.assertEqual(code, 1, output)
        self.assertIn("outside the V map", output)

    def test_p_a5_correct_map_passes(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            values = self._assets(root)
            text = self._include(values)
            self.host.write_tree(root, {stamp.CHROME_INCLUDE: text})
            code, output = self._gate(root, {}, {stamp.CHROME_INCLUDE: text})
        self.assertEqual(code, 0, output)
        self.assertIn("stamp-only: PASS", output)

    def test_n_a6_and_p_a7_page_stamp(self):
        import tempfile

        rel = "ias-16/draft-v1-linked/ch01.html"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / "_shared" / "chrome-include.js"
            script.parent.mkdir(parents=True, exist_ok=True)
            script.write_text("include-bytes", encoding="utf-8")
            good = stamp.file_stamp(script)
            ok = page(f'<script src="../../_shared/chrome-include.js?v={good}"></script>')
            self.host.write_tree(root, {rel: ok})
            code, output = self._gate(root, {}, {rel: ok})
            self.assertEqual(code, 0, output)
            stale = page(
                '<script src="../../_shared/chrome-include.js?v=c185ed7f207b"></script>'
            )
            self.host.write_tree(root, {rel: stale})
            code, output = self._gate(root, {}, {rel: ok})
            self.assertEqual(code, 1, output)
            self.assertIn("stamp hash mismatch", output)

    def test_p_a10_index_must_match_search_index(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            values = self._assets(root)
            search = root / "homepage" / "search-index.js"
            search.parent.mkdir(parents=True, exist_ok=True)
            search.write_text("search", encoding="utf-8")
            digest = stamp.file_stamp(search)
            good = self._include(values, index=digest)
            self.host.write_tree(root, {stamp.CHROME_INCLUDE: good})
            code, output = self._gate(root, {}, {stamp.CHROME_INCLUDE: good})
            self.assertEqual(code, 0, output)
            bad = self._include(values, index="000000000000")
            self.host.write_tree(root, {stamp.CHROME_INCLUDE: bad})
            code, output = self._gate(root, {}, {stamp.CHROME_INCLUDE: good})
            self.assertEqual(code, 1, output)
            self.assertIn("INDEX=", output)


class Row86FoldTests(unittest.TestCase):
    def test_sibling_heads_and_bprime_fold_back_to_base(self):
        base = (
            '<div class="st-down"><span class="stem-shaft"></span>\n'
            '<span class="stem-head"></span>\n'
            '</div>\n'
            '<fieldset class="visual-fieldset">\n'
            '<legend class="visual-legend">Concept Map</legend>\n'
            '<div class="cfmap m-l0">\n'
            '\n'
            '<section>\n'
        )
        head = (
            '<div class="st-down"><span class="stem-shaft"></span>\n'
            '</div>\n'
            '<fieldset class="visual-fieldset board-l0-onlabel">\n'
            '<legend class="visual-legend board-legend">Concept Map</legend>\n'
            '<div class="cfmap m-l0 board-l0-div">\n'
            '<p class="board-legend-abs">Concept Map</p>\n'
            '\n'
            '<section>\n'
        )
        self.assertEqual(stamp.fold_row86(base), stamp.fold_row86(head))
        self.assertNotIn("stem-head", stamp.fold_row86(head))
        kept = stamp.fold_row86(head + "<span>yes</span>\n")
        self.assertIn(">yes<", kept)

    def test_unrelated_label_is_not_folded_away(self):
        base = "<p>carrying amount derecognised</p>\n"
        head = "<p>carrying amount removed</p>\n"
        self.assertNotEqual(stamp.fold_row86(base), stamp.fold_row86(head))


class HowNotes108FoldTests(unittest.TestCase):
    """#108. SIGNED how-notes teaching folds. Freestyle chrome does not.

    Not a CONTENT_ALLOW. Stamp still owns the Home link, the title, and h1.
    """

    TIP = "1a591c83bc8bab3d0ccd137907b17003d0a2cc91"

    def tip_html(self):
        import subprocess

        return subprocess.check_output(
            ["git", "show", f"{self.TIP}:{stamp.HOW_NOTES}"],
            cwd=stamp.ROOT,
            text=True,
        )

    def live_html(self):
        return (stamp.ROOT / stamp.HOW_NOTES).read_text(encoding="utf-8")

    def test_signed_structure_folds_equal_to_four_box(self):
        base = self.tip_html()
        live = self.live_html()
        folded = stamp.fold_how_notes(live)
        self.assertEqual(stamp.fold_how_notes(base), folded)
        self.assertIn('href="homepage-wireframe-v0.1.html"', folded)
        self.assertIn("<title>How these notes are made</title>", folded)
        self.assertIn("<h1>How these notes are made</h1>", folded)
        self.assertNotIn('class="flow"', folded)
        self.assertNotIn("proof-banner", folded)

    def test_wording_inside_the_shell_still_folds(self):
        live = self.live_html()
        edited = live.replace("personal study pack", "personal study pack edited", 1)
        self.assertNotEqual(live, edited)
        self.assertEqual(stamp.fold_how_notes(live), stamp.fold_how_notes(edited))

    def test_freestyle_outside_the_fold_does_not_fold(self):
        folded_base = stamp.fold_how_notes(self.tip_html())
        live = self.live_html()
        extra = live.replace(
            "</main>",
            '<p class="traffic">Go</p>\n  </main>',
            1,
        )
        self.assertNotEqual(stamp.fold_how_notes(extra), folded_base)
        self.assertIn("traffic", stamp.fold_how_notes(extra))
        bad_h1 = live.replace(
            "<h1>How these notes are made</h1>",
            "<h1>Notes</h1>",
            1,
        )
        self.assertNotEqual(stamp.fold_how_notes(bad_h1), folded_base)
        bad_href = live.replace(
            'href="homepage-wireframe-v0.1.html"',
            'href="elsewhere.html"',
            1,
        )
        self.assertNotEqual(stamp.fold_how_notes(bad_href), folded_base)
        bad_title = live.replace(
            "<title>How these notes are made</title>",
            "<title>Other</title>",
            1,
        )
        self.assertNotEqual(stamp.fold_how_notes(bad_title), folded_base)
        bad_css = live.replace(
            "</style>",
            ".traffic { color: red; }\n  </style>",
            1,
        )
        self.assertNotEqual(stamp.fold_how_notes(bad_css), folded_base)

    def test_how_notes_is_not_a_content_allow(self):
        self.assertNotIn(stamp.HOW_NOTES, stamp.CONTENT_ALLOW)
        self.assertEqual(stamp.CONTENT_ALLOW, ("_shared/settings-rows.html",))

    def test_gate_passes_signed_and_fails_freestyle(self):
        import tempfile

        base = self.tip_html()
        live = self.live_html()

        def git_text(rev, path):
            if path == "_shared/last-update.js":
                return LAST_UPDATE
            if path == stamp.HOW_NOTES:
                return base
            raise KeyError(path)

        def git_paths(rev):
            return [stamp.HOW_NOTES]

        def run(root):
            original_root = stamp.ROOT
            original_text = stamp.git_text
            original_paths = stamp.git_paths
            stamp.ROOT = root
            stamp.git_text = git_text
            stamp.git_paths = git_paths
            buffer = io.StringIO()
            try:
                with redirect_stdout(buffer):
                    code = stamp.main(["--base", "fixture"])
            finally:
                stamp.ROOT = original_root
                stamp.git_text = original_text
                stamp.git_paths = original_paths
            return code, buffer.getvalue()

        def write(root, html):
            page = root / stamp.HOW_NOTES
            page.parent.mkdir(parents=True, exist_ok=True)
            page.write_text(html, encoding="utf-8")
            last = root / "_shared" / "last-update.js"
            last.parent.mkdir(parents=True, exist_ok=True)
            last.write_text(LAST_UPDATE, encoding="utf-8")

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, live)
            code, output = run(root)
            self.assertEqual(code, 0, output)
            self.assertIn("stamp-only: PASS", output)
            write(
                root,
                live.replace(
                    "</main>",
                    '<p class="traffic">Go</p>\n  </main>',
                    1,
                ),
            )
            code, output = run(root)
            self.assertEqual(code, 1, output)
            self.assertIn(
                "HTML changed outside ?v= and the homepage link: " + stamp.HOW_NOTES,
                output,
            )


class MfLegoEntry112FoldTests(unittest.TestCase):
    """#112: one exact Master Map anchor folds. Freestyle chrome still fails."""

    PAGE = stamp.MF_LEGO_ENTRY_PAGE
    NEEDLE = stamp.MF_LEGO_ENTRY

    def base_page(self):
        return (
            '<div class="page">\n'
            '<link rel="stylesheet" href="ias16.css?v=aaaaaaaaaaaa" />\n'
            '<div class="ppe pack">\n'
            "</div>\n"
        )

    def signed_head(self):
        return self.base_page().replace(
            '<div class="page">\n',
            '<div class="page">\n' + self.NEEDLE + "\n",
            1,
        ).replace("aaaaaaaaaaaa", "bbbbbbbbbbbb")

    def test_signed_entry_passes_shared_visual(self):
        base = self.base_page()
        head = self.signed_head()
        folded_base = stamp.fold_mf_lego_entry(base, self.PAGE)
        folded_head = stamp.fold_mf_lego_entry(head, self.PAGE)
        self.assertEqual(folded_base, base)
        self.assertNotIn(self.NEEDLE, folded_head)
        self.assertIsNone(
            stamp.shared_visual_stamp_failure(folded_base, folded_head, self.PAGE)
        )

    def test_live_map_folds_back_to_tip(self):
        import subprocess

        # #111 splices one attribute onto the ch05 Method bar inside the
        # master include. The #112 pin still rejects every other byte.
        b13_old = (
            '<p class="consume-bar">'
            "<span>Reflect the pattern of consumption of future economic benefits</span></p>"
        )
        b13_new = (
            '<p class="consume-bar" data-brick="B13">'
            "<span>Reflect the pattern of consumption of future economic benefits</span></p>"
        )
        base = subprocess.check_output(
            ["git", "show", f"d2cd6c9f:{self.PAGE}"],
            cwd=stamp.ROOT,
            text=True,
        )
        head = (stamp.ROOT / self.PAGE).read_text(encoding="utf-8")
        self.assertEqual(head.count(self.NEEDLE), 1)
        self.assertNotIn(self.NEEDLE, base)
        self.assertEqual(head.count(b13_new), 1)
        self.assertEqual(base.count(b13_old), 1)
        self.assertNotIn(b13_new, base)
        folded_head = stamp.fold_mf_lego_entry(head, self.PAGE)
        self.assertNotIn("mf-lego-entry", folded_head)
        folded_head = folded_head.replace(b13_new, b13_old, 1)
        self.assertIsNone(
            stamp.shared_visual_stamp_failure(
                stamp.fold_mf_lego_entry(base, self.PAGE),
                folded_head,
                self.PAGE,
            )
        )

    def test_freestyle_chrome_still_fails(self):
        base = stamp.fold_mf_lego_entry(self.base_page(), self.PAGE)
        extra = self.signed_head().replace(
            self.NEEDLE + "\n",
            self.NEEDLE + '\n<a class="rail-link" href="elsewhere.html">More</a>\n',
            1,
        )
        folded = stamp.fold_mf_lego_entry(extra, self.PAGE)
        self.assertIsNotNone(
            stamp.shared_visual_stamp_failure(base, folded, self.PAGE)
        )
        wrong = self.signed_head().replace("#lego-sheet", "#other", 1)
        self.assertIn("mf-lego-entry", stamp.fold_mf_lego_entry(wrong, self.PAGE))
        self.assertIsNotNone(
            stamp.shared_visual_stamp_failure(
                base, stamp.fold_mf_lego_entry(wrong, self.PAGE), self.PAGE
            )
        )
        indented = self.base_page().replace(
            '<div class="page">\n',
            '<div class="page">\n  ' + self.NEEDLE + "\n",
            1,
        )
        self.assertIn(self.NEEDLE, stamp.fold_mf_lego_entry(indented, self.PAGE))

    def test_chapter_path_is_not_folded_and_page_stays_gated(self):
        chapter = "ias-16/draft-v1-linked/ch01.html"
        html = "<p>\n" + self.NEEDLE + "\n</p>\n"
        self.assertEqual(stamp.fold_mf_lego_entry(html, chapter), html)
        self.assertIn(self.PAGE, stamp.SHARED_VISUAL_PAGES)
        self.assertNotIn(self.PAGE, stamp.CONTENT_ALLOW)


if __name__ == "__main__":
    unittest.main()
