# CF 2018 — Chrome Phase 1 + Phase 2 — 2026-10-02

## Outcome

Implemented the shared chrome migration and Phase 2 token/citation ownership for **CF 2018 only**. No IAS 2, IFRS 18, Documents sync, Opus launch, or teaching-content rewrite was performed.

Release value used consistently across the live pack:

- Visible update: `Last update · 2026-10-02 01:21 HKT`
- Stylesheet cache key: `?v=cf2018-chrome-phase2-20261002`

## Inventory

Live teaching HTML under `draft-v1-linked/`:

- `index.html` — Map
- `ch01.html` through `ch11.html` — 11 chapter pages
- `references.html` — new References shell

Total live chrome pages: **13**.

Embedded visual HTML: 11 files under `visuals/`. These remain visual embeds, not separate chrome pages. One reader-facing accessible label in `visuals/ch05-recognition-derecognition.html` was changed from “Usefulness gates” to “Usefulness tests” during the light terminology sweep. Archived HTML under `_archive/` and `_archive-index-stub.html` was not migrated.

## Files touched

- `index.html`
- `ch01.html`–`ch11.html`
- `references.html` (created)
- `assets/shared.css`
- `assets/draft.css`
- `visuals/ch05-recognition-derecognition.html` (accessible wording only)
- `CF-CHROME-PHASE12-2026-10-02.md` (this report)

Shared module files used, not rewritten in this wave:

- `../../_shared/tokens.css`
- `../../_shared/chrome.css`
- `../../_shared/cite.css`

## Changes made

### Phase 1 chrome

- Added the shared stylesheet sequence to all 13 live pages:
  `tokens.css` → `chrome.css` → `cite.css` → CF pack CSS.
- Added the CF cache key to all live-page stylesheet links.
- Added `data-pack="cf2018"`, `data-page`, and chapter metadata where applicable.
- Preserved static `chrome:start/end` and `footer-nav:start/end` boundaries.
- Added Home, pack title, shared visible update stamp, active tag state, and References to every tag row.
- Added the pack disclaimer immediately before footer navigation on every page.
- Added a References page shell with only CF sources evidenced by the CF METHOD/XREF notes and used works: Official CF 2018, IAS 8, IFRS 9, DTT A2 2022, PwC MOA 2020 (including Appendix 2), EY IGAAP 2026 Ch2, KPMG Insights 2019/20 · 1.2, and KPMG Combined/Carve 2022.

### Phase 2 modularisation

- Removed duplicated CF token declarations and dark-mode token remaps from `assets/shared.css` and `assets/draft.css`; `_shared/tokens.css` is now the shared owner.
- Removed duplicated chrome rules from `assets/draft.css`; `_shared/chrome.css` is now the owner.
- Removed duplicated citation-chip rules from `assets/draft.css`; `_shared/cite.css` is now the owner.
- Kept CF-specific body, map, visual, teaching, callout, table, and layout rules pack-owned.

### Light chrome-lock sweep

- Replaced remaining reader-facing `gate` wording in live chapter teaching HTML with `test` wording where it described a decision/test concept.
- Internal visual class hooks such as `rc-gate`/`st-gate` and archived content were left untouched; they are not reader-facing live-page chrome.

## QA checklist

- [x] 13 live pages inventoried: Map, 11 chapters, References.
- [x] Every live page has exactly one `chrome:start` / `chrome:end` pair.
- [x] Every live page has exactly one `footer-nav:start` / `footer-nav:end` pair.
- [x] Every live page has one pack disclaimer aside before footer navigation.
- [x] Every live page has Home, pack title, visible update stamp, and tag-row References link.
- [x] The References page has the active References tag and back-to-Status / Map footer links.
- [x] All live pages use the required stylesheet order and the same Phase 2 cache key.
- [x] Update label is identical on all pages: `2026-10-02 01:21 HKT`.
- [x] Local `href` / `src` smoke check: 0 missing targets.
- [x] Pack CSS scan shows no duplicated token, chrome, footer, or citation module selectors.
- [x] Direct file-render smoke checks completed for `index.html`, `ch05.html`, and `references.html`.
- [x] Live root teaching-page reader-facing `gate` leftover count: **0**.
- [x] No teaching content, source claim, IFRS 18 file, Documents sync, or Opus launch was touched.

## Report

- Pages touched: 13 live HTML pages, plus one embedded visual for accessible wording.
- References added: **Yes** — `references.html`.
- Leftover reader-facing `gate` count: **0** in live root teaching pages.
- Blockers: **None**.
