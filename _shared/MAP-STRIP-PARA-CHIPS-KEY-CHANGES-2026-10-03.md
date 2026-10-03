# Concept Map — strip Standard paragraph chips (2026-10-03)

Chrome-only pass. Concept Map HTML only. No densify, no new cites, no skill-MD edits.

Target look: IAS 2 maps, which have no `cite` / `para-hint` / `§` chips. Pack section jumps (`a.fb-num`) stay. Teaching words such as “paragraph 83 note” and “Listed in para 118” stay. Chip markup only is removed.

Counts are element counts (`<span class="cite cite-*">` or `<span class="para-hint">`), not line counts.

## Totals

| Pack | Before | After |
|---|---:|---:|
| IFRS 18 `cite cite-official` | 93 | 0 |
| CF `para-hint` | 7 | 0 |
| IAS 2 `cite` / `para-hint` / `§` | 0 | 0 |
| Bare `§NN` chips (all three packs) | 0 | 0 |

`a.fb-num` markup was compared to the source tarball after the edit. No section-jump chip was added, removed, or retargeted.

## IFRS 18 — `visuals/*.html`

Every `cite cite-*` span removed. No other cite class was present (`cite-pwc`, `cite-ey`, `cite-kpmg`, `cite-dtt`: 0).

| File | Before | After | What was tidied |
|---|---:|---:|---|
| `ch01-whats-new.html` | 10 | 0 | Trailing ` · ` before IN / para / C chips. Chapter links (`Ch2` / `Ch3` / `Ch4` / `Ch6`) kept. Narrative “subject to paragraph 73” and “annual para C3 · first-year interim para C4–C5” kept. |
| `ch02-pfs-aggregation.html` | 17 | 0 | Cite-only peer footers removed. Cite-only matrix column and its “Cite” header removed (`data-cols` 4 → 3). Trailing ` · ` on the shared-rule lines removed. “paragraph 41” and “Para 41 test” kept. |
| `ch03-classification-path.html` | 6 | 0 | Cite-only `p.pc-gate-cite` removed. Sentences that already ended before the chip kept their period. Kicker “para 47–68” kept (prose, not a chip). |
| `ch03-mba-nest.html` | 13 | 0 | Chips dropped from heads and bodies. No empty plates left. |
| `ch03-pnl-categories.html` | 3 | 0 | Cite-only `p.pc-mba-cites` removed. |
| `ch04-totals-subtotals.html` | 10 | 0 | `span.ts-cites` wrappers removed from the three subtotal rules. Regime-head chips removed. “Listed in para 118”, “paragraph 73”, “paragraph 65(a)(ii)”, “paragraph 117”, “paragraph 118(a)” kept. |
| `ch05-operating-expenses.html` | 8 | 0 | `para 83` beside the yes-leaf title, `para 82` on Cost of sales, and `para 78` / `80` / `81` / `79` / `B81` on Nature · Function · Mixed removed. “Para 83 note”, “One para 83 note”, “Paragraph 84”, “paragraph 41”, “paragraph 83 note” kept. |
| `ch06-mpms.html` | 9 | 0 | Cite-only `span.gt-cites` removed from the four tests. Trailing chips on the MPM leaf, the “why reconcile” line, and the tax/NCI line removed. “the para 117 tests”, “Listed in para 118”, “paragraph 118-listed” kept. Section chips `6.1`–`6.4` unchanged. |
| `ch07-other-fs.html` | 8 | 0 | Cite-only `p.ofs-cites` removed (peer pointers and the indirect-method start line). |
| `ch08-transition.html` | 9 | 0 | Chips removed from the effective-date line, the retrospective bracket, and the annual/interim heads. Two cite-only `p.tr-cite` lines removed. “paragraph 69–74” and “IAS 34 paragraph 10” kept. |
| `map-jumpboard.html` | 0 | 0 | Already clean. Not edited. |

Other IFRS 18 visual HTML files had no cite chips and were not edited.

### CSS (only where the grid would break)

`ch02-pfs-aggregation.css`

- Peer subgrid was four rows because the last row was the cite footer. It is now three rows (`head / role line / detail list`).
- Matrix column tracks were four, with the last track sized for the cite column. Both the default and the `max-width: 900px` tracks are now three columns, matching `data-cols="3"`.

Unused `.cite` / `.pa-peer-cite` / `.pa-mx-cite` rules were left in the stylesheets. They no longer match any element, so they do not paint an empty chip row.

## CF 2018 — `span.para-hint` only

| File | Before | After |
|---|---:|---:|
| `ch09-combined.html` | 2 | 0 — `(CF 3.12)`, `(CF 3.14)` |
| `ch10-carve.html` | 2 | 0 — `(CF 3.10, 3.13)`, `(CF 3.14, BC3.17)` |
| `ch11-status.html` | 3 | 0 — `(CF SP1.1, BC0.18–BC0.20)`, `(CF SP1.2, BC0.22)`, `(IAS 8.11)` |

Ch1–Ch8 maps had no `para-hint` and were not edited. `.para-hint` rules remain in `ch09-combined.css`, `ch10-carve.css`, and `ch11-status.css` with nothing left to style.

Narrative that was never a chip stays, including “(OCI, CF 7.17)” on the Ch11 Board card and the stem “IAS 8.11 order”. HTML comments were not rewritten.

## IAS 2

All eight map HTML files (`ch01`–`ch06`, `map-formula-board.html`) scanned: zero `cite`, zero `para-hint`, zero `§`. Not edited.

Parenthetical teaching words such as “(para 6)” and “(para 9)” are the IAS 2 pattern and were left in place.

## Kept on purpose (not chip markup)

- `a.fb-num` section jumps, including ranges (`fb-num-range` / `fb-num-sep`).
- IFRS 18 Ch7 pointer text `IFRS 18 App D` (`span.ofs-cite-text`, not `cite cite-*`).
- IFRS 18 Ch2 labelling tip still ends `· B16–B26`. That reference was plain text beside the `para 43` chip, not inside a cite span. The chip and the extra separator were removed; the bare appendix range was not rewritten into a chip and was not deleted.
- Source labels on CF maps (`Official`, `DTT`, `EY`, `KPMG`, `PwC`) are not paragraph-number chips.

## Out of scope

- No `chNN.html` teaching bodies are in this tree, so iframe `?v=` was not bumped. Bump the parent iframe query when these visuals sync.
- Skill markdown was not edited.
- No PwC / Big4 cites were added.

## Grok Bot pull-back note (2026-10-03)

- Merged agent visuals into box `/workspace/ifrs-website/refs/{ifrs-18,cf-2018}/draft-v1-linked/visuals/`.
- Bumped parent iframe `?v=map-strip-para-20261003` on CF Ch1–11 and IFRS 18 Ch1–8.
- Documents sync: both nested `refs/…` and top-level pack trees.
