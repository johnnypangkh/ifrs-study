# IAS 2 Phase 2 — shared tokens and citation chips — 2026-10-02

## Scope

Phase 2 is implemented for IAS 2 only. No CF 2018 or IFRS 18 files were changed. No HTML teaching content or citation-chip text was changed, and Phase 3 illustration/worked-strip primitives were not introduced.

## Files changed

- `refs/_shared/tokens.css` — new shared owner for the colour custom properties previously repeated in IAS 2 `assets/shared.css` and `assets/draft.css`, including the existing light/dark remaps and firm citation colour variables.
- `refs/_shared/cite.css` — new shared owner for `.cite`, nested `.cite-house`, `.cite-official`, `.cite-pwc`, `.cite-dtt`, `.cite-ey`, `.cite-kpmg`, `.cite-extract`, and `.cite-row`.
- `refs/ias-2/draft-v1-linked/assets/shared.css` — removed its root token declarations and duplicate citation font rule; body, layout, teaching, illustration, worked-strip, and other pack-owned rules remain.
- `refs/ias-2/draft-v1-linked/assets/draft.css` — removed its root token declarations and citation-chip module; pack-specific body/teaching/visual rules remain.
- `index.html`, `ch01.html`–`ch06.html`, `references.html` — all eight pages now load, in order: `tokens.css` → `chrome.css` → `cite.css` → `assets/shared.css` → `assets/draft.css`, with `?v=ias2-chrome-phase2-20261002`.
- `refs/_shared/README.md` — brief Phase 2 update note.

## Ownership notes

- The shared token file preserves the source values and existing light/dark behaviour. It supports both `prefers-color-scheme: dark` and `data-theme="dark"` exactly as before.
- `assets/theme.js` remains pack-owned. It is still responsible for the IAS 2 pack's runtime theme override (`data-theme="dark"`) and was not changed.
- Pack-owned body typography, teaching selectors, map/layout rules, illustration rules, worked strips, and page-specific visual treatment remain in the pack CSS.
- The citation strings and nested firm labels remain HTML-owned. The shared stylesheet only supplies the existing chip geometry, typography, and colours; it does not add or rename a source label.
- Source-defined category/MPM compatibility tokens remain in `tokens.css` so the extracted source stylesheet does not lose declarations; no IAS 2 HTML or teaching styling uses them.

## QA

- [x] Eight IAS 2 HTML pages contain the five Phase 2 stylesheet links in the required order.
- [x] All Phase 2 stylesheet links use `ias2-chrome-phase2-20261002`.
- [x] No `:root` token block remains in either IAS 2 pack stylesheet.
- [x] No duplicate base citation-chip module remains in the pack CSS; pack-specific `.cite-row` placement selectors remain intentionally pack-owned.
- [x] All five cite classes occur in the unchanged IAS 2 HTML and are covered by `cite.css`.
- [x] Existing firm foreground/background/border values were retained, so Official, PwC, DTT, EY, and KPMG chips remain distinct and coloured.
- [x] Headless Chrome file rendering of `ch01.html` and `references.html` completed; the References screenshot shows coloured Official chips and direct file paths resolve.
- [x] No HTML teaching content, cite chip string, CF 2018/IFRS 18 file, Phase 3 illustration primitive, or Documents sync was touched.

Visual spot-check target: `file:///workspace/ifrs-website/refs/ias-2/draft-v1-linked/index.html` and a chapter page such as `ch01.html`; both resolve the new shared assets directly from the page directory.
