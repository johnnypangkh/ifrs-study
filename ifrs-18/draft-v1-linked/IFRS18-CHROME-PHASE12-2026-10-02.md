# IFRS 18 — Chrome Phase 1 + Phase 2 — 2026-10-02

## Outcome

Implemented the shared chrome migration and Phase 2 token/citation ownership for **IFRS 18 only**. No IAS 2, CF 2018, Documents sync, Opus launch, teaching densify rewrite, or Phase 3 Illus primitives were performed.

Release value used consistently across the live pack:

- Visible update: `Last update · 2026-10-02 01:29 HKT`
- Stylesheet cache key: `?v=ifrs18-chrome-phase2-20261002`

## Inventory

Live teaching HTML under `draft-v1-linked/`:

- `index.html` — Map
- `ch01.html` through `ch08.html` — 8 chapter pages
- `references.html` — new References shell

Total live chrome pages: **10**.

Embedded visual HTML under `visuals/` (including `ch03-mba-nest.html`) remains visual embeds, not separate chrome pages. They were not migrated.

## Files touched

- `index.html`
- `ch01.html`–`ch08.html`
- `references.html` (created)
- `assets/shared.css`
- `assets/draft.css`
- `IFRS18-CHROME-PHASE12-2026-10-02.md` (this report)

Shared module files used, not rewritten in this wave:

- `../../_shared/tokens.css`
- `../../_shared/chrome.css`
- `../../_shared/cite.css`

## Changes made

### Phase 1 chrome

- Added the shared stylesheet sequence to all 10 live pages:
  `tokens.css` → `chrome.css` → `cite.css` → IFRS 18 pack CSS (`shared.css` → `draft.css` → `map.css` on Map only).
- Added the IFRS 18 cache key `ifrs18-chrome-phase2-20261002` to all live-page stylesheet links.
- Added `data-pack="ifrs18"`, `data-page`, and chapter metadata where applicable.
- Preserved static `chrome:start/end` and `footer-nav:start/end` boundaries.
- Added Home, pack title, shared visible update stamp (`.chrome-title-cluster` / `.chrome-last-update`), active tag state, and **References** to every tag row.
- Added the pack disclaimer immediately before footer navigation on every page (CF-family personal-study wording, IFRS 18 pack name; no new legal claims).
- Added a References page shell with only sources evidenced by METHOD/cite chips: Official IFRS 18, IAS 7 as amended, IAS 33 as amended, KPMG FI 2024, EY Closer look 2026, DTT A4 2022 (IAS 1 bridge). PwC explicitly not listed (not on disk — no invent).
- Ch8 footer now links Next → References; References footer links back to Transition + Map.
- Did **not** add any Map chip-order lecture note.

### Phase 2 modularisation

- Removed duplicated IFRS 18 token declarations and dark-mode token remaps from `assets/shared.css` and `assets/draft.css`; `_shared/tokens.css` is now the shared owner (including category/MPM compatibility tokens already present there).
- Removed duplicated chrome / tag-row / footer-nav rules from `assets/draft.css`; `_shared/chrome.css` is now the owner.
- Removed duplicated citation-chip module from `assets/draft.css` and the trailing cite font-only duplicate from `assets/shared.css`; `_shared/cite.css` is now the owner.
- Kept IFRS 18-specific body, map (`map.css`), visual, teaching, callout, table, contain*/Illus, and layout rules pack-owned.

### Light chrome-lock Gate → Decision/Test sweep

Renamed reader-facing **UI labels** only:

- All `.box-title` **Gate** → **Decision** (Ch2–Ch5) or **Test** (Ch6–Ch8).
- Table `<th>Gate</th>` headers → Decision / Test.
- Section titles: overview gate → overview decision; para 117 gates → tests; Gate-order → Test-order.
- Ch6 **Gate 1–4** list leads → **Test 1–4**.
- A few clear Decision/Test chrome phrases (e.g. “Para 24 test”, “§117 test”, “All tests pass”).

**Not rewritten:** Official `<q>` quote text; teaching density; First/Second/Third gate sequence language (flagged below).

## Gate leftovers

| Category | Count | Notes |
|---|---|---|
| `.box-title` Gate | **0** | Cleared |
| `<th>Gate</th>` | **0** | Cleared |
| Capital `Gate` UI labels | **0** | Cleared |
| `First` / `Second` / `Third` gate teaching-sequence phrases | **9** | Ch2×3, Ch3×3, Ch4×3 — left as narrative sequence language per task; flag for optional later pass |
| Other lowercase `gate` narrative (e.g. “next gate”, “gate labels”, “at that gate”) | **12** | Path/teaching prose leftovers — not UI chrome labels |

Live root teaching-page reader-facing **box-title / class-label Gate** leftover count: **0**.

## QA checklist

- [x] 10 live pages inventoried: Map, 8 chapters, References.
- [x] Every live page has exactly one `chrome:start` / `chrome:end` pair.
- [x] Every live page has exactly one `footer-nav:start` / `footer-nav:end` pair.
- [x] Every live page has one pack disclaimer aside before footer navigation.
- [x] Every live page has Home, pack title, visible update stamp, and tag-row References link.
- [x] The References page has the active References tag and back-to-Transition / Map footer links.
- [x] All live pages use the required stylesheet order and the same Phase 2 cache key.
- [x] Update label is identical on all pages: `2026-10-02 01:29 HKT`.
- [x] Local `href` smoke check for pack HTML + shared/pack CSS: 0 missing targets among checked assets.
- [x] Pack CSS scan shows no duplicated `:root`, `.chrome-bar`, `.footer-nav`, or base `.cite` module selectors.
- [x] No Map chip-order lecture note added.
- [x] No IAS 2 / CF 2018 / Documents sync / Opus / teaching densify / Phase 3 Illus work.

## Report summary

- Pages touched: **10** live HTML pages (+ 2 pack CSS files + this report).
- References added: **Yes** — `references.html`.
- Cache version string: `ifrs18-chrome-phase2-20261002`.
- Leftover reader-facing box-title/th **Gate** count: **0**.
- Leftover First/Second/Third gate narrative phrases: **9** (flagged).
- Other lowercase gate narrative leftovers: **12** (flagged).
- Blockers: **None**.

---

## Addendum — References + tag align — 2026-10-02 01:37 HKT

Aligned `references.html` to the IAS 2 refs body shape (preferred) while keeping IFRS 18 chrome/tag-row structure already present on all live pages.

### Misaligned (before)

- Refs **h1** was `References — IFRS 18 Presentation and Disclosure` (CF-style); IAS 2 prefers bare `References`.
- Purpose text followed CF METHOD wording, not IAS 2’s cite-chip inventory line (`ch01–ch0N` + full/short form).
- Official table listed only `IAS 7 as amended` / `IAS 33 as amended` — omitted bare **`IAS 7`** (ch02) and **`IAS 33`** (ch07) chip prefixes actually used.
- Big 4 heading/intro lacked IAS 2-style nested `cite-house` example chips; heading said “Big4 … / technical references”.
- Disclaimer omitted the IAS 2 **legal counsel** line and issuer-FS closing phrasing.

### Changed

- Rewrote `references.html` Official + Big 4 tables from honest ch01–ch08 cite inventory: `IFRS 18`, `IAS 7`, `IAS 7 as amended`, `IAS 33`, `IAS 33 as amended`, `KPMG FI 2024`, `EY Closer look 2026`, `DTT A4 2022` (PwC still not listed — not on disk).
- Purpose / How derived / disclaimer match IAS 2 pattern (legal counsel line included).
- Tag labels **kept** as existing short forms (`1 What’s new` … `8 Transition` + References) — already scanable; Map visit-path uses overlapping short names.
- Bumped visible stamp to `Last update · 2026-10-02 01:37 HKT` and stylesheet cache to `?v=ifrs18-chrome-phase2-20261002b` on all **10** live HTML pages.

### Pages touched

`index.html`, `ch01.html`–`ch08.html`, `references.html` (+ this addendum). No cf-2018 / ias-2 trees.


---

## Addendum — First/Second/Third gate → decision — 2026-10-02 01:40 HKT

Refs body already IAS 2-aligned from prior 01:37 addendum (bare References, Official+Big4 nested cite-house chips, counsel + issuer FS). No further refs body edits.

### Optional sequence pass

Replaced reader-facing teaching-sequence leads only (not Official `<q>` quotes):

- Ch2–Ch4: `First/Second/Third gate —` → `First/Second/Third decision —` (**9** replacements).

### Remaining lowercase / path `gate` narrative (not UI labels)

**15** leftovers, all in `ch03.html` (e.g. “next gate”, “overview gate”, “gate labels”, “Investing / Financing gates”, worked-strip “ordered category gates”). Left as path/teaching prose per scope — not First/Second/Third sequence chrome.

### Stamp / cache

Edited HTML → bumped all **10** live pages to:

- `Last update · 2026-10-02 01:40 HKT`
- `?v=ifrs18-chrome-phase2-20261002c`

No Opus; no densify; no CF/IAS2 tree edits in this IFRS 18 addendum.
