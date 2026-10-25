# Site infra runbook — workbook #95

**Owner:** IFRS Build · pairs with `SITE-INFRA-DIAGRAM.md` · update in same PR as infra change.  
**Updated:** 2026-10-25 Asia/Hong_Kong · #114 ch05 See-also `p.see` / `p.see.see-wide` `data-brick="B09"` ×4 include pin (`p.junction-tip.see` chapter-only) · #113 ch05 Operator `.cost-op`/`.def-op` `data-brick="B14"` ×5 include pin · #111 ch05 Method `data-brick="B13"` include pin · #112 Master Map mf-lego-entry SHARED_VISUAL fold · #110 homepage `.card-updated` STAMPS consumer · #100 live `site/master-formatting/` · #109 timeline module.

## Who

| Action | Who |
|---|---|
| Squash-merge | **PM only** (Johnny yes) |
| Draft PR | Cursor via Build (reply living agent) |
| Brief / Skill locks | Build |
| Round-2 QC | IFRS QC · PM W3 |
| OD backup `draft-v1-linked` | Executor after Johnny yes |
| Merge | **Never** Build / Cursor / QC / Design |

After **W2b**: Build **FAIL-only** until W4 or new GO.

## Deploy path

1. Draft PR from living agent → CI green  
2. QC PASS → Johnny merge yes → **PM squash-merges** to `main`  
3. Pages tracks `main` (lag OK for a few minutes)  
4. Johnny OD yes → Executor: GitHub raw @ merge SHA → `00. IFRS Web/ifrs-website-refs/<pack>/draft-v1-linked/`

Live base: `https://johnnypangkh.github.io/ifrs-study/`

## Pages vs main (when stuck / after merge)

1. Note merge SHA on `main`  
2. Compare live `_shared` / stamp / map-box to that SHA  
3. Report: `live matches <sha>` or `live stale vs <sha>`  
4. If stale: wait deploy + hard-refresh — do not invent a new look

## Living agent

- Id: `bc-0d5f2356-769c-5035-99f6-b057b5ad7190`  
- Repo: `johnnypangkh/ifrs-study` only  
- Effort: Johnny picks before every reply  
- Reuse: reply; do not launch a second chrome agent

## CI gates with pinned counts

| Gate | Pin | Source |
|---|---|---|
| `tools/map-lint.py` `CITE_ALLOW` for `ias-16/draft-v1-linked/visuals/master-concept-map.html` | **4** | Johnny lock FINAL-B2 2026-10-20 19:31 / PR #98. The three #98 plates cite 0. The remaining 4 are ch07 Disclosure. Do not trim ch07. |
| `tools/check-stamp-only.py` | #98 scoped allow | visuals `ch04-models.html`, `ch05-depreciation.html`, `master-concept-map.html` (plate regions), `ch06-derecognition.html` (compensation wrapper), and `ch04.html` + `ch05.html` + `references.html` (#98 change spots only). PM 5 approved 2026-10-20 15:23 + 18:02 + FINAL-B2 19:39 / PR #98. `check-incremental` owns the teaching rows. |
| `tools/map-lint.py` `PLATE98_SHARED_OK` | `{cap, inner-board, see-bit, see-label, m-tl}` | #98 plate classes allowed to match bare `_shared` selectors; any other collision FAILs (root cause: PR #165 `tl-row` vs components-6.css L402). Source = QC round 2 + PM 5 FAIL-only order 2026-10-21. #109 adds bare `.m-tl` only: that is the shared timeline root. Child `.m-tl-*` rules are descendants, not bare. |
| Shared timeline module | `_shared/modules/visuals/timeline-1.css` | #109. Imported by `_shared/visuals.css` after `map-box.css`. Stamp `?v=` via `tools/stamp-assets.py` / `bash tools/build-all.sh` (do not hand-edit hashes). `tools/check-stamp-only.py` allows that one trailing `timeline-1.css` import when its hash matches disk (same shape as the map-box trailing import). Packs that load the kit inherit it (IAS 16 via the existing visuals import). IAS 16 `ias16.css` keeps plate placement only (shaft height, `--mo-n`, flex, flag extras, ch05 span show, ribbon hide, Reval evt/nil, Impair rd/foot/cease). Not part of `map-box.css`. `tools/map-lint.py` fails a new pack paint class that does not alias into L* / `m-flow\|link\|visit` / `m-tl*`. |
| `site/master-formatting/index.html` | #100 live MF | Johnny V6 path A, 2026-10-21. `tools/stamp-assets.py` `settings_pages()` hashes `_shared` `?v=` on this page. `tools/build-last-update.py` maps `/site/master-formatting/` to pack `site` and includes that folder in the site fingerprint. `_shared/chrome-packs.js` `CHROME_PACK_PATHS` has the same path (generated `_shared/last-update.js` `PACK_PATHS` follows). `tools/check-stamp-only.py` allows `?v=`-only edits once the page is on main (same shape as Settings; not a blank cheque). Page CSS stays on the page. Do not copy `kit.css` into `_shared`. |
| Homepage READY card dates | #110 | Homepage READY pack + Settings cards use empty `.card-updated` under `[data-pack]` filled from `_shared/last-update.js` `STAMPS` as `Updated · YYYY-MM-DD`. How-notes and PLANNED omit. `tools/build-last-update.py` template must keep the `#110-card-mount` card filler so `build-all.sh` does not wipe it. STAMPS keys / fingerprints / iso unchanged. Chrome-bar `mount()` unchanged. |
| Master Map LEGO entry | #112 | Live `ias-16/draft-v1-linked/visuals/master-concept-map.html` may add one chrome line `a.mf-lego-entry` (label `LEGO kit · Master formatting`, href `../../../site/master-formatting/index.html#lego-sheet`, `target="_top"`) above `.ppe.pack`. Page stays in `SHARED_VISUAL_PAGES`. `tools/check-stamp-only.py` folds that exact anchor out of the shared-visual / stamp compare (same dedicated-fold shape as #98 plates / #108 how-notes / #110 homepage card chrome). Stamp still owns freestyle outside that needle. Pack token CSS lives in `ias16.css` (not `_shared`). `check-incremental` owns teaching rows — chrome label ADD alone does not require `changes/<pr>.yml`. #111 may splice `data-brick="B13"` onto the one ch05 Method `.consume-bar` inside the master include (`build-map-includes.py`). `test_live_map_folds_back_to_tip` accepts that exact substring, plus the #113 B14 Operator substrings and the #114 B09 See-also substrings below, and nothing else; the CLI plate fold (#98) already ignores the same region. |
| ch05 Operator B14 include pin | #113 | `build-map-includes.py` splices `data-brick="B14"` onto the five ch05 Operator nodes inside the master `#ch05-dep` include: `.cost-op` ×4 (`=` `−` `=` `−`) and `.def-op` ×1 (`OR`). Teaching glyphs stay byte-identical. Master-owned cost-ops outside that include (`op-eq` / `op-p1` / `op-p2` / `fx-o1` / `fx-o2`) stay untouched. `test_live_map_folds_back_to_tip` folds those five exact substrings back to the pre-#113 text and re-checks every other byte. The CLI plate fold (#98) already ignores the ch05-dep region. |
| ch05 See-also B09 include pin | #114 | `build-map-includes.py` splices `data-brick="B09"` onto the four ch05 See-also nodes inside the master `#ch05-dep` include: timeline `p.see` Ceases IFRS 5, `p.see.see-wide` Replacement, `p.see` Lessee, and hidden-axis `p.see` lc-cease IFRS 5. Teaching strings stay byte-identical. `p.junction-tip.see` (Impairment, IAS 36) is chapter-only — it sits after `map-section:ch05-dep:end` on `ch05-depreciation.html` and the master has no `junction-tip` twin, so do not invent one. Master-owned `p.see` outside that include stay untouched (the ch04 Revaluation / Impairment IFRS 5 copies keep the pre-#114 tag). `test_live_map_folds_back_to_tip` folds those four exact substrings back to the pre-#114 text, keeps the B13 and B14 pins, and re-checks every other byte. The chapter file carries the same four plus the junction-tip attribute (B09×5). The CLI plate fold (#98) already ignores the ch05-dep region, which covers the four in-include sees. `p.junction-tip.see` sits after that region, so `fold_b09_junction` folds one exact open tag (`<p class="junction-tip see" data-brick="B09">` back to `<p class="junction-tip see">`) on `ch05-depreciation.html` only, and only when it appears once. A second copy, a different brick, an extra class, or any other byte still fails. Master is not folded by that function. |

## Live Master formatting path

`site/master-formatting/` is the live Master formatting page. `site/settings/` stays the Settings token table and is not MF. The LEGO kit sheet is section `#lego-sheet` on the MF page (signed `lego-sheet.png`), not a separate `design/` page. IAS 16 Concept Map plates are not edited for this path.

`check-incremental` unpairs a tool-paired `changed` row when explicit `removed` + `added` yml entries match both sides.

## Docs home

- Repo: `docs/site-infra/`  
- Box scratch: `/workspace/style-base/site-infra/`
