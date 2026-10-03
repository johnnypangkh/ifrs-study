# KEY CHANGES — IFRS 18 E2 technical-strict titles

**Stamp:** 2026-10-03 00:39 Asia/Shanghai (HKT)

**Checklist:** pack HTML attached; skills QA attached; no Big4 PDFs needed for title-only fix.

Documents were not synced. The teaching-body QA skill file was not amended.

## Old title → new title

Section ids are unchanged. Each replacement is the Standard’s own heading for that block. Neither new title contains “at a glance”.

| File | Id | Old title | New title |
|---|---|---|---|
| `refs/ifrs-18/draft-v1-linked/ch05.html` | `s-5-0-1` | 5.0.1 — IAS 1 versus IFRS 18 at a glance | 5.0.1 — Presentation and disclosure of expenses classified in the operating category — IAS 1 compared with IFRS 18 |
| `refs/ifrs-18/draft-v1-linked/ch08.html` | `s-8-0-1` | 8.0.1 — Appendix C at a glance | 8.0.1 — Appendix C — Effective date and transition |

Wording basis, already in the sections and in IFRS 18:

- Ch5. The heading above IFRS 18 paragraph 78 is “Presentation and disclosure of expenses classified in the operating category”. The table under 5.0.1 compares that presentation and disclosure with IAS 1 (location of the analysis, mixed nature and function, the basis for the method, and the note package). “Compared with” names that two-column comparison.
- Ch8. The heading of IFRS 18 Appendix C is “Effective date and transition”. The table under 8.0.1 is paragraphs C1–C8 of that appendix.

Diff against the unpacked pack is those two `<h4>` lines only. Table cells, cite chips, links, and ids were not edited. The pack Last update on both pages remains `2026-10-02 20:16 HKT`, so the two chapters still carry the same stamp.

## QA (title / markup / link)

Ran on `ch05.html` and `ch08.html` after the edit. Skill file not modified.

| Check | Result |
|---|---|
| E2 — `journey`, `unlock value`, `key takeaway`, `at a glance`, `insights for`, `best practice tip`, `game changer` | Pass. No hits in either chapter, and none in the two visual HTML files. |
| E2 — the two new `h4` titles | Pass. Standard headings; no consultancy phrase. |
| Ids `s-5-0-1` and `s-8-0-1` | Pass. One each, unchanged. |
| C — `<p class="box-body">` wrapping a list | Pass. No hits. |
| A — `§` inside a `.cite`; house-only `PwC` / `DTT` / `EY` chip | Pass. No hits. |
| F — same-file `href="#…"` | Pass. Every fragment matches an `id` in that file. |
| F — plain `see N.M` outside an `<a>` | Pass. No hits. |
| J — Last update | Pass for this slice. Both pages still read `Last update · 2026-10-02 20:16 HKT`. |
| J — disclaimer | Pass. `Disclaimer — personal study pack` sits immediately before `footer-nav` on both pages. |
| Reader-visible `gate` / `gates` in the two chapters | Pass. No hits. |

## Screenshots

This pack slice does not name a review-viewport list. Shots use the widths the stylesheets actually switch on:

- **1280×900** — wider than the 980px page column, so the section is at full measure.
- **390×844** — below the 480px chrome breakpoint (and below the 640px and 720px body breakpoints).

The sticky chapter bar was set to static only inside the screenshot session, so it does not cover the heading. The HTML files were not changed for the shots.

| Section | 1280 | 390 |
|---|---|---|
| Ch5 5.0.1 | `handoff/screenshots/ch05-5-0-1-1280.png` | `handoff/screenshots/ch05-5-0-1-390.png` |
| Ch8 8.0.1 | `handoff/screenshots/ch08-8-0-1-1280.png` | `handoff/screenshots/ch08-8-0-1-390.png` |

At 1280 both titles and the full tables, including cite chips and in-table links, are visible. At 390 both new titles wrap and remain fully readable. The Ch5 Cite column is clipped by the existing `.table-wrap` overflow; the same chips are complete at 1280.

Open the sections:

- [Ch5 5.0.1](http://127.0.0.1:43123/refs/ifrs-18/draft-v1-linked/ch05.html#s-5-0-1)
- [Ch8 8.0.1](http://127.0.0.1:43123/refs/ifrs-18/draft-v1-linked/ch08.html#s-8-0-1)

## Unresolved

- **Cross-chapter links were not re-resolved.** Fifteen `href`s in Ch5 and five in Ch8 point at `ch01.html`–`ch04.html`, `ch06.html`, and `ch07.html`, which are not in this pack. Those `href`s were not edited. Same-file targets do resolve.
- **Pre-existing title-essence shell hit, not in 5.0.1 or 8.0.1.** Ch5’s paragraph 84 source table has `<strong>EY</strong>` in the Source column, with the cite chip in the Cite column. Left as-is so the table content stays. It is not one of the two failing section titles.
- **Pre-existing visual class `oe-gate`.** `visuals/ch05-operating-expenses.html` uses that class name. It is not reader-visible text. The visual was not edited.
- **Not run as content gates.** Densify, illustration diagrams, map reading-order, map-mirror, and the Big4 crosswalk were not run. No illustration, map, or source text was edited, and no Big4 PDF was attached. The Ch5 390 Cite-column clip is existing table overflow, not a title defect.
