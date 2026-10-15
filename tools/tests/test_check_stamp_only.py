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


if __name__ == "__main__":
    unittest.main()
