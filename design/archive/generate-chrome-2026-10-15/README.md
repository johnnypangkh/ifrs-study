`generate-chrome.mjs` used to rewrite a static top bar and footer from `refs/<pack>/chrome.json`. The bar included an inline `font-weight:500`, which the type rules ban, and the `chrome.json` files it read are not in the tree. No live HTML page, script, or workflow loads it. The top bar now comes from `_shared/chrome-packs.js` at runtime.

This copy is the file that was at `tools/generate-chrome.mjs` on aa1d379b, moved here on 2026-10-15. It is not linked or imported. To restore it, move it back to `tools/generate-chrome.mjs`.

`cf-2018/LOCK-STAMP.md` and `ifrs-18/LOCK-STAMP.md` still name the old path. Those lines are the 2026-09-28 QC record, left as written.
