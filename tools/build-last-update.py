#!/usr/bin/env python3
"""Rebuild _shared/last-update.js from each pack's content fingerprint.

A pack's visible stamp moves only when a fingerprint of that pack's
draft-v1-linked tree, plus _shared, differs from the fingerprint stored
beside the stamp. last-update.js itself is not part of the fingerprint.
Every ?v= query is stripped before hashing, so a cache-bust on
search-index.js or last-update.js cannot move a stamp or change the
fingerprint. Unchanged fingerprints keep the stored time, so a second
run does not depend on the clock.

The script also writes last-update.js?v=<hash> on every page that loads
the file. The value is the first 12 hex digits of the SHA-256 of the
generated file. Other script src values are left as they are.
"""

import hashlib
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover - Python 3.9+ has zoneinfo
    ZoneInfo = None

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_shared" / "last-update.js"

# Cache-bust queries only. The value charset is the tokens this site uses
# (hex, dates, hyphens). Stripping them keeps the fingerprint stable when
# a ?v= stamp is rewritten and nothing else is.
V_QUERY = re.compile(r"\?v=[A-Za-z0-9._~%-]*")

SCRIPT_SRC = re.compile(
    r'(<script\b[^>]*?\bsrc=")([^"]*?last-update\.js)(?:\?[^"]*)?(")'
    r"|(<script\b[^>]*?\bsrc=')([^']*?last-update\.js)(?:\?[^']*)?(')"
)
DATA_PACK = re.compile(r'<body\b[^>]*\bdata-pack="([^"]+)"')
OTHER_SRC = re.compile(r'<script\b[^>]*?\bsrc=(["\'])(.*?)\1')


def now_hkt():
    if ZoneInfo is not None:
        try:
            zone = ZoneInfo("Asia/Hong_Kong")
        except Exception:
            zone = timezone(timedelta(hours=8))
    else:
        zone = timezone(timedelta(hours=8))
    return datetime.now(zone).replace(second=0, microsecond=0)


def stamp_text(moment):
    return "Last update \u00b7 " + moment.strftime("%Y-%m-%d %H:%M") + " HKT"


def stamp_iso(moment):
    return moment.isoformat(timespec="seconds")


def iter_files(directory):
    files = []
    for path in directory.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        if path.resolve() == OUT.resolve():
            continue
        files.append(path)
    return files


def content_for_hash(path):
    data = path.read_bytes()
    if b"?v=" not in data:
        return data
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return data
    return V_QUERY.sub("", text).encode("utf-8")


def feed(hasher, blob):
    hasher.update(len(blob).to_bytes(8, "big"))
    hasher.update(blob)


def fingerprint(paths):
    hasher = hashlib.sha256()
    ordered = sorted(paths, key=lambda item: item.relative_to(ROOT).as_posix())
    for path in ordered:
        feed(hasher, path.relative_to(ROOT).as_posix().encode("utf-8"))
        feed(hasher, content_for_hash(path))
    return hasher.hexdigest()


def loads_stamp(draft):
    for path in iter_files(draft):
        if path.suffix.lower() != ".html":
            continue
        if b"last-update.js" in path.read_bytes():
            return True
    return False


def pack_key(draft, directory_name):
    keys = []
    seen = set()
    for path in iter_files(draft):
        if path.suffix.lower() != ".html":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for match in DATA_PACK.finditer(text):
            key = match.group(1)
            if key not in seen:
                seen.add(key)
                keys.append(key)
    if len(keys) > 1:
        joined = ", ".join(keys)
        raise SystemExit(f"{draft.relative_to(ROOT)} declares multiple data-pack values: {joined}")
    if len(keys) == 1:
        return keys[0]
    return directory_name.replace("-", "")


def discover_packs():
    packs = []
    for entry in sorted(ROOT.iterdir(), key=lambda item: item.name):
        draft = entry / "draft-v1-linked"
        if not draft.is_dir() or draft.is_symlink():
            continue
        if not loads_stamp(draft):
            continue
        packs.append({
            "key": pack_key(draft, entry.name),
            "directory": entry.name,
            "draft": draft,
        })
    keys = [pack["key"] for pack in packs]
    if len(keys) != len(set(keys)):
        raise SystemExit("two packs resolved to the same data-pack key: " + ", ".join(keys))
    return packs


def extract_json_object(text, marker):
    start = text.find(marker)
    if start < 0:
        return None
    opening = text.find("{", start)
    if opening < 0:
        return None
    depth = 0
    in_string = False
    escape = False
    for index in range(opening, len(text)):
        char = text[index]
        if in_string:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[opening:index + 1]
    return None


def load_stored(text):
    raw = extract_json_object(text, "var STAMPS = ")
    if not raw:
        return {}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    stored = {}
    for key, value in data.items():
        if not isinstance(value, dict):
            continue
        fp = value.get("fingerprint")
        iso = value.get("iso")
        label = value.get("text")
        if isinstance(fp, str) and isinstance(iso, str) and isinstance(label, str):
            stored[key] = {
                "text": label,
                "iso": iso,
                "fingerprint": fp,
            }
    return stored


def embed_json(value):
    """Pretty-print JSON so continuation lines sit two spaces further in."""
    raw = json.dumps(value, indent=2, ensure_ascii=False)
    lines = raw.split("\n")
    body = "\n".join("  " + line for line in lines[1:])
    return lines[0] + "\n" + body


def render(stamps, packs):
    paths = [[f"/{pack['directory']}/", pack["key"]] for pack in packs]
    paths.sort()
    ordered = {key: stamps[key] for key in sorted(stamps)}
    stamps_js = embed_json(ordered)
    path_lines = ",\n".join(
        "    " + json.dumps(pair, ensure_ascii=False) for pair in paths
    )
    paths_js = "[\n" + path_lines + "\n  ]"
    return (
        "/* Generated by tools/build-last-update.py. Do not hand-edit.\n"
        "   Each stamp moves only when that pack's content fingerprint changes.\n"
        "   The fingerprint covers the pack's draft-v1-linked tree plus _shared,\n"
        "   excluding this file, with every ?v= query stripped first.\n"
        "   Re-run the script and commit this file plus the last-update.js?v=\n"
        "   stamps it writes. */\n"
        "(function () {\n"
        "  var STAMPS = " + stamps_js + ";\n"
        "\n"
        "  var PACK_PATHS = " + paths_js + ";\n"
        "\n"
        "  function packId() {\n"
        "    var body = document.body;\n"
        "    var fromBody = body && body.getAttribute(\"data-pack\");\n"
        "    if (fromBody && STAMPS[fromBody]) return fromBody;\n"
        "    var path = location.pathname || \"\";\n"
        "    var i;\n"
        "    for (i = 0; i < PACK_PATHS.length; i++) {\n"
        "      if (path.indexOf(PACK_PATHS[i][0]) !== -1) return PACK_PATHS[i][1];\n"
        "    }\n"
        "    return \"\";\n"
        "  }\n"
        "\n"
        "  function formatStamp(stamp) {\n"
        "    var match = /^(\\d{4}-\\d{2}-\\d{2})T(\\d{2}:\\d{2})/.exec(stamp.iso || \"\");\n"
        "    if (match) return \"Last update \\u00b7 \" + match[1] + \" \" + match[2] + \" HKT\";\n"
        "    return stamp.text || \"\";\n"
        "  }\n"
        "\n"
        "  function mount() {\n"
        "    var stamp = STAMPS[packId()];\n"
        "    if (!stamp) return false;\n"
        "    var el = document.querySelector(\"span.chrome-last-update\");\n"
        "    if (!el) {\n"
        "      var host = document.querySelector(\".chrome-title-cluster\") || document.querySelector(\".chrome-bar-title\");\n"
        "      if (!host) return false;\n"
        "      el = document.createElement(\"span\");\n"
        "      el.className = \"chrome-last-update\";\n"
        "      host.appendChild(el);\n"
        "    }\n"
        "    if (el.getAttribute(\"data-last-update-ready\") === \"true\") return true;\n"
        "    el.textContent = formatStamp(stamp);\n"
        "    el.setAttribute(\"data-last-update\", stamp.iso);\n"
        "    el.removeAttribute(\"title\");\n"
        "    el.setAttribute(\"data-last-update-ready\", \"true\");\n"
        "    return true;\n"
        "  }\n"
        "\n"
        "  if (document.readyState === \"loading\") {\n"
        "    document.addEventListener(\"DOMContentLoaded\", mount);\n"
        "  } else {\n"
        "    mount();\n"
        "  }\n"
        "})();\n"
    )


def other_script_srcs(html):
    found = []
    for match in OTHER_SRC.finditer(html):
        src = match.group(2)
        if "last-update.js" in src:
            continue
        found.append(src)
    return found


def pages_loading_stamp():
    """HTML files that load last-update.js, one path per real file.

    Resolve and skip duplicates so the stamp is written once.
    """
    seen = set()
    pages = []
    for path in sorted(ROOT.rglob("*.html")):
        if not path.is_file() or path.is_symlink():
            continue
        real = path.resolve()
        if real in seen:
            continue
        seen.add(real)
        if b"last-update.js" not in real.read_bytes():
            continue
        pages.append(real)
    return pages


def stamp_references(stamp):
    changed = []
    missed = []
    for path in pages_loading_stamp():
        # Keep the original bytes aside from the last-update.js query.
        # read_text() would rewrite line endings and move the fingerprint.
        html = path.read_bytes().decode("utf-8")

        def repl(match, stamp=stamp):
            if match.group(1) is not None:
                return f"{match.group(1)}{match.group(2)}?v={stamp}{match.group(3)}"
            return f"{match.group(4)}{match.group(5)}?v={stamp}{match.group(6)}"

        updated, count = SCRIPT_SRC.subn(repl, html)
        rel = str(path.relative_to(ROOT))
        if count == 0:
            missed.append(rel)
            continue
        if other_script_srcs(updated) != other_script_srcs(html):
            raise SystemExit(f"refusing to rewrite non-last-update script src in {rel}")
        encoded = updated.encode("utf-8")
        if encoded != path.read_bytes():
            path.write_bytes(encoded)
            changed.append(rel)
    return changed, missed


def file_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def main():
    packs = discover_packs()
    if not packs:
        raise SystemExit("no pack with draft-v1-linked loads last-update.js")
    shared = iter_files(ROOT / "_shared")
    fingerprints = {}
    for pack in packs:
        fingerprints[pack["key"]] = fingerprint(iter_files(pack["draft"]) + shared)

    stored = load_stored(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    moment = None
    stamps = {}
    for pack in packs:
        key = pack["key"]
        previous = stored.get(key)
        if previous and previous["fingerprint"] == fingerprints[key]:
            stamps[key] = {
                "text": previous["text"],
                "iso": previous["iso"],
                "fingerprint": previous["fingerprint"],
            }
            state = "unchanged"
        else:
            if moment is None:
                moment = now_hkt()
            stamps[key] = {
                "text": stamp_text(moment),
                "iso": stamp_iso(moment),
                "fingerprint": fingerprints[key],
            }
            state = "updated"
        print(f"{key} {state} {stamps[key]['text']} {fingerprints[key][:12]}")

    generated = render(stamps, packs)
    parsed = load_stored(generated)
    for pack in packs:
        key = pack["key"]
        if parsed.get(key) != stamps[key]:
            raise SystemExit(f"generated last-update.js does not round-trip {key}")
    if render(stamps, packs) != generated:
        raise SystemExit("last-update.js render is not stable")

    encoded = generated.encode("utf-8")
    if not OUT.exists() or OUT.read_bytes() != encoded:
        OUT.write_bytes(encoded)
    cache = file_hash(generated)
    changed, missed = stamp_references(cache)
    print(f"pages {len(pages_loading_stamp())} cache {cache} -> {OUT.relative_to(ROOT)}")
    for name in changed:
        print("stamp", name)
    for name in missed:
        print("unstamped", name)
    if missed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
