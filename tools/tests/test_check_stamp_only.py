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
            if has_note == note_box:
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


if __name__ == "__main__":
    unittest.main()
