# Restore mobile layout from design/archive/mobile-2026-10-13/

Archived at cfc59d2b before PR4c removed it. Nothing here is linked or imported.

1. Run `python3 tools/xlsx_to_tokens.py --mobile`. Rename the xlsx headers back from `Mobile (ARCHIVED 2026-10-13)` (Text keeps `Mobile rem` and `Mobile px`, Box keeps `Padding mobile`) and set the 11 breakpoint/preview rows plus the GENERATED-MQ row Status back to live (`TARGET` / `GENERATED-MQ`). `--design-w` stays documented and is not emitted.
2. Re-insert each `css/` block at its `SOURCE file:line`. Blocks are self-contained. Insert bottom-up per file so line numbers hold. The two Map `.page.map-page` overrides are in those same css files and are not @media blocks.
3. Restore `chrome-bar.js` (this folder's copy) including the view switch and the `.map-viewport` wrapper. Restore the `chrome-1-view-switch.css` rules and `chrome-1-line438.css` (`var(--page-max, 61.25rem)`). Restore `settings-gen.css` and the /settings toggle, M cells, and ruler from `settings/`.
4. Revert the viewport meta to `width=device-width, initial-scale=1` (sed over the 101 files).
5. Restore skill wording from `skill-wording.md` (PM 4 applies).
6. Full QC at 390/667/922/1280, day and dark. `check-settings-rows.py` goes back to 287/287.

The three homepage drafts were left in place and are not in this restore. The eight `@media` strings in the settings type-scale role text are workbook prose, not style blocks, and were not removed.
