# Restore mobile layout from design/archive/mobile-2026-10-13/

Archived at cfc59d2b before PR4c removed it. Nothing here is linked or imported.

1. Run `python3 tools/xlsx_to_tokens.py --mobile`. Rename the xlsx headers back from `Mobile (ARCHIVED 2026-10-13)` (Text keeps `Mobile rem` and `Mobile px`, Box keeps `Padding mobile`) and set the 11 breakpoint/preview rows plus the GENERATED-MQ row Status back to live (`TARGET` / `GENERATED-MQ`). `--design-w` stays documented and is not emitted.
2. Restore the served style files from base. This replaces inserting archived blocks by line number, which does not rebuild cascade order. From the repo root:

```
git checkout cfc59d2b -- \
  _shared/cite.css \
  _shared/modules/chrome/chrome-1.css \
  _shared/modules/teaching/box-1.css \
  _shared/modules/teaching/chrome-1.css \
  _shared/modules/teaching/components-1.css \
  _shared/modules/teaching/components-2.css \
  _shared/modules/teaching/components-3.css \
  _shared/modules/teaching/grid-1.css \
  _shared/modules/type-scale/text-1.css \
  _shared/modules/visuals/box-1.css \
  _shared/modules/visuals/components-1.css \
  _shared/modules/visuals/components-2.css \
  _shared/modules/visuals/components-3.css \
  _shared/modules/visuals/components-4.css \
  _shared/modules/visuals/components-6.css \
  _shared/modules/visuals/grid-1.css \
  _shared/modules/visuals/grid-3.css \
  _shared/settings-gen.css \
  _shared/tokens-core.css \
  _shared/tokens.css \
  cf-2018/chapter-visuals/ch02-qualitative-characteristics.css \
  cf-2018/chapter-visuals/ch04-elements.css \
  cf-2018/draft-v1-linked/assets/map.css \
  cf-2018/draft-v1-linked/assets/shared.css \
  cf-2018/draft-v1-linked/ch05.html \
  cf-2018/draft-v1-linked/visuals/ch01-objective-users.css \
  cf-2018/draft-v1-linked/visuals/ch02-qualitative-characteristics.css \
  cf-2018/draft-v1-linked/visuals/ch03-reporting-entity.css \
  cf-2018/draft-v1-linked/visuals/ch04-elements.css \
  cf-2018/draft-v1-linked/visuals/ch05-recognition-derecognition.css \
  cf-2018/draft-v1-linked/visuals/ch06-measurement.css \
  cf-2018/draft-v1-linked/visuals/ch07-presentation-disclosure.css \
  cf-2018/draft-v1-linked/visuals/ch08-capital.css \
  cf-2018/draft-v1-linked/visuals/ch09-combined.css \
  cf-2018/draft-v1-linked/visuals/ch10-carve.css \
  cf-2018/draft-v1-linked/visuals/ch11-status.css \
  homepage/homepage-wireframe-v0.1.html \
  homepage/how-these-notes-are-made.html \
  ias-16/draft-v1-linked/assets/draft.css \
  ias-16/draft-v1-linked/visuals/ias16-cx.js \
  ias-16/draft-v1-linked/visuals/ias16.css \
  ias-16/draft-v1-linked/visuals/master-concept-map.html \
  ias-2/draft-v1-linked/assets/draft.css \
  ias-2/draft-v1-linked/ch01.html \
  ias-2/draft-v1-linked/ch02.html \
  ias-2/draft-v1-linked/ch03.html \
  ias-2/draft-v1-linked/ch04.html \
  ias-2/draft-v1-linked/ch05.html \
  ias-2/draft-v1-linked/visuals/ias2.css \
  ifrs-18/draft-v1-linked/assets/map.css \
  ifrs-18/draft-v1-linked/visuals/ch01-whats-new.css \
  ifrs-18/draft-v1-linked/visuals/ch02-pfs-aggregation.css \
  ifrs-18/draft-v1-linked/visuals/ch03-classification-path.css \
  ifrs-18/draft-v1-linked/visuals/ch03-mba-nest.css \
  ifrs-18/draft-v1-linked/visuals/ch03-pnl-categories.css \
  ifrs-18/draft-v1-linked/visuals/ch04-totals-subtotals.css \
  ifrs-18/draft-v1-linked/visuals/ch05-operating-expenses.css \
  ifrs-18/draft-v1-linked/visuals/ch06-mpms.css \
  ifrs-18/draft-v1-linked/visuals/ch07-other-fs.css \
  ifrs-18/draft-v1-linked/visuals/ch08-transition.css \
  ifrs-18/draft-v1-linked/visuals/map-jumpboard.css
```

That command restores each listed file to `cfc59d2b`, including width `@media` wrappers, the two Map `.page.map-page` overrides, and the five `matchMedia` branches in `master-concept-map.html`. Run it after step 1 so the checkout is the byte copy of those files. The archive under `design/archive/mobile-2026-10-13/` stays as reference and is not checked out. The three homepage drafts (`homepage/homepage-wireframe-v0.html`, `homepage/homepage-wireframe-v0.1.before-7c.html`, `homepage/_shot-search-demo.html`) are not in this restore.
3. Restore `chrome-bar.js` (this folder's copy) including the view switch and the `.map-viewport` wrapper. That file is the switching behaviour. The live bar keeps only an inert Desktop|Mobile placeholder (rev 2b, Johnny via PM 4, 2026-10-13 14:04): same markup and token styling, Desktop `aria-pressed="true"`, Mobile `aria-disabled="true"`, no class toggle, no storage, no viewport change. Restore the `chrome-1-view-switch.css` rules (including `.map-viewport` and `.view-switch-hint`) and `chrome-1-line438.css` (`var(--page-max, 61.25rem)`). Restore `settings-gen.css` and the /settings toggle, M cells, and ruler from `settings/`. The /settings toggle stays removed while the placeholder is in place.
4. Revert the viewport meta to `width=device-width, initial-scale=1` (sed over the 101 files).
5. Restore skill wording from `skill-wording.md` (PM 4 applies).
6. Full QC at 390/667/922/1280, day and dark. `check-settings-rows.py` goes back to 287/287.

The three homepage drafts were left in place and are not in this restore. The eight `@media` strings in the settings type-scale role text are workbook prose, not style blocks, and were not removed.
