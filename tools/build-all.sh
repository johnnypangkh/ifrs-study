#!/usr/bin/env bash
# Rebuild IAS 16 map includes, then cache stamps, then the shared indexes.
# Run from anywhere. A second run on a clean tree exits 0 and rewrites nothing.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/build-map-includes.py
python3 tools/stamp-assets.py
python3 homepage/build-search-index.py
python3 tools/build-last-update.py
