# IAS 2 Chrome Phase 1 — 2026-10-02

## Files touched

- `refs/_shared/chrome.css` — new shared Phase 1 chrome stylesheet.
- `refs/ias-2/draft-v1-linked/assets/draft.css` — removed the migrated chrome and footer rules; teaching/body/cite/token styles remain pack-owned.
- `index.html`, `ch01.html`–`ch06.html`, `references.html` — added the shared stylesheet link, wave cache key, body metadata, and retained the existing static chrome blocks.
- `IAS2-CHROME-PHASE1-2026-10-02.md` — this report.

No `chrome.js` was added.

## Moved to `chrome.css`

- Header layout: `.chrome-bar`, `.chrome-bar-title`, `.chrome-home`, `.chrome-title-cluster`, `.chrome-last-update`, and `.chrome-bar-actions`.
- Tag navigation: `.tag-row-wrap`, `.tag-row`, `.tag`, `.tag.active`, including narrow-screen scrolling and focus treatment.
- Disclaimer chrome layout: `.callout.pack-disclaimer`; wording remains unchanged in each page.
- Footer navigation: `.footer-nav`, its links, hover/focus treatment, and `.mid` positioning.

The shared stylesheet uses the existing pack custom properties; token consolidation was not introduced.

## Page metadata and cache key

- Map: `<body data-pack="ias2" data-page="map">`.
- Chapters: `<body data-pack="ias2" data-page="chapter" data-chapter="ch01">` through `ch06`.
- References: `<body data-pack="ias2" data-page="references">`.
- All 8 pages load `../../_shared/chrome.css?v=ias2-chrome-phase1-20261002` before pack CSS.
- Existing `assets/shared.css` and `assets/draft.css` links use the same wave key.
- Visible update remains `Last update · 2026-10-02 00:25 HKT` on all pages.

## QA checklist

- [x] 8 pages have exactly one `chrome:start` / `chrome:end` pair.
- [x] 8 pages have exactly one `footer-nav:start` / `footer-nav:end` pair.
- [x] Header, tags, active states, disclaimer placement, and footer links remain static HTML.
- [x] Shared CSS is present on all 8 chrome pages and precedes pack CSS.
- [x] `rg` counts: 8 chrome starts, 8 chrome ends, 8 footer starts, 8 footer ends, 8 update stamps; 24 IAS 2 wave-key stylesheet occurrences.
- [x] All local `href`/`src` targets resolve from the HTML file paths.
- [x] File-path smoke opened `file:///workspace/ifrs-website/refs/ias-2/draft-v1-linked/index.html` and resolved its linked targets.
- [x] No duplicated migrated chrome selectors remain in `assets/draft.css`; `.callout .tag-mini` is unrelated pack content styling.
- [x] No teaching prose, cites, Maps, visuals, disclaimer wording, tag labels/hrefs, or update stamp was changed.
- [x] No Phase 2 cite/token work, other packs, or Documents sync was touched.

No blockers found.
