# CF 2018 — References + tag align — 2026-10-02

## Outcome (Job #5 refresh · 16:05 HKT)

Aligned CF References shell + EY cite short forms to IAS 2 / skill patterns. Fixed Ch11 → References footer. No `_shared` CSS edit (CF already consumes Phase 2 modules). No teaching densify; no invented sources.

Release values after Job #5:

- Visible update: `Last update · 2026-10-02 16:05 HKT`
- Stylesheet cache key (shared): `?v=cf2018-refs-chrome-20261002`
- `draft.css` cache: `?v=cf2018-chrome-job3-20261002` (unchanged)

## Cite-chip inventory (ch01–ch11 HTML only) — short forms after align

### Official

| Short form (chip prefix) | Files |
|---|---|
| `CF 2018` | ch01–ch11 |
| `IAS 8` | ch09, ch11 |
| `IFRS 9` | ch03 |

### Big 4

| Short form (chip prefix) | Files |
|---|---|
| `DTT A2 2022` | ch01–ch11 |
| `PwC MOA 2020` | ch01–ch11 |
| `PwC MOA 2020 · A2` | ch09, ch10 (Appendix 2 work; locators `A2.*` / Exhibit A2.*) |
| `EY iGAAP 2026 Ch2` | ch01–ch11 (**was** `EY IGAAP 2026 · Ch2`) |
| `EY IFRS Developments 169 · May 2020` | ch05 |
| `KPMG Insights 2019/20 · 1.2` | ch01–ch06, ch09–ch11 |
| `KPMG Combined/Carve 2022` | ch03, ch09, ch10 |
| `KPMG New Foundation 2018` | ch04–ch07, ch11 (locators p1/p2) |

No invented sources. ACCA remains visit-path only (not listed).

## Changes this Job #5 pass

### Cite short forms

- All live EY book chips: `IGAAP 2026 · Ch2` → `iGAAP 2026 Ch2` (IAS 2 / skill `EY iGAAP 2026 ChNN` pattern).

### `references.html`

- Purpose → honest-inventory line (IAS 2).
- Official intro → `cite-official` example chip (IAS 2).
- Big 4 / Official tables: EY short form `EY iGAAP 2026 Ch2`.
- How derived → cite-chips-only / METHOD+XREF filenames / **No invent** (IAS 2).
- Disclaimer retained (includes CF “does not override” sentence).

### Footer

- `ch11.html`: `Next: References →` (matched IAS 2 last-chapter pattern).

### Live chrome confirm (13 pages)

- References tag present on Map, ch01–ch11, References (active).
- CSS order unchanged: `tokens.css` → `chrome.css` → `cite.css` → pack CSS.
- Stamp: `2026-10-02 16:05 HKT`.

## Files touched

- `references.html`
- `index.html`, `ch01.html`–`ch11.html` (EY short form and/or stamp/cache; ch11 footer)
- `CF-REFS-TAG-ALIGN-2026-10-02.md` (this report)
- QA: `/workspace/cf-pullback/QA-REPORT-REFS-CHROME-2026-10-02.md`

## Out of scope (honoured)

- Opus launch / teaching densify
- Invented citations
- `_shared` CSS edits (would ripple IAS 2)
- IAS 2 / IFRS 18 tree rewrites
