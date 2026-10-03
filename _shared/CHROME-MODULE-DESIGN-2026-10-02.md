# IFRS teaching packs: shared chrome module design

**Status:** design only. This document plans the next implementation wave; it does not rewrite pack HTML or CSS.

**Owner / audience:** Johnny Pang, PM, Grok/Opus agents.

**Scope:** shared page chrome for `ias-2`, `cf-2018`, and `ifrs-18`, stored in:

```text
/workspace/ifrs-website/refs/_shared/
```

The current golden reference is:

```text
/workspace/ifrs-website/refs/ias-2/draft-v1-linked/
```

Its chrome is bounded by `<!-- chrome:start -->` and `<!-- chrome:end -->`. Existing `pack-disclaimer` and `footer-nav:start/end` markers are the reference pattern.

---

## 1. Goal

Make the navigation and pack-level notices consistent across all IFRS teaching packs without merging their teaching content.

Phase 1 is **Chrome only**:

- header bar: Home, pack title, and last-update stamp;
- tag row: Map, chapters, References;
- pack disclaimer at the bottom of page content, before footer navigation;
- footer navigation: previous / Map / next as applicable;
- References page shell, with reference content remaining pack-owned;
- shared CSS for the chrome classes;
- a pack-level cache-key convention.

The static HTML file remains the source of truth. A page must render correctly when opened from the filesystem or served as ordinary static files. No build step is required.

### Required visible update format

Every page in a pack uses the same pack-wide value and format:

```text
Last update · YYYY-MM-DD HH:MM HKT
```

The value is a visible page label, not just a file or query-string version. Keep it identical across all pages in one implementation wave.

---

## 2. Shared folder layout

Planned shared assets (Phase 1 implementation comes later):

```text
/workspace/ifrs-website/refs/_shared/
├── README.md
├── CHROME-MODULE-DESIGN-2026-10-02.md
├── chrome.css                 # Phase 1 shared chrome rules
└── chrome.js                  # optional helper only; not required for static rendering
```

`chrome.css` is the intended shared stylesheet for the classes in this document. It should own layout and responsive behavior for the chrome, not pack content styles.

`chrome.js` is optional. Static pages must not depend on JavaScript to show Home, title, tags, disclaimer, References, or footer navigation. If a later implementation uses a helper for injection or validation, it must be progressive enhancement and loaded with `defer`. Do not introduce a build dependency just to assemble chrome.

Pack-owned assets remain inside each pack, for example:

```text
refs/ias-2/draft-v1-linked/assets/
refs/cf-2018/draft-v1-linked/assets/
refs/ifrs-18/draft-v1-linked/assets/
```

A pack may continue to have its own `shared.css` and `draft.css` while migration is in progress. Phase 2 decides whether duplicated colour variables and common tokens move to a single owner.

---

## 3. What is shared and what stays pack-owned

### Shared

The following are the module contract and should look and behave consistently:

- `.chrome-bar`, `.chrome-bar-title`, `.chrome-home`, `.chrome-title-cluster`, `.chrome-last-update`;
- `.tag-row-wrap`, `.tag-row`, `.tag`, `.tag.active`;
- `.pack-disclaimer` and its placement rule;
- `.footer-nav` and its previous / Map / next layout;
- the `chrome:start/end` and `footer-nav:start/end` copy boundaries;
- responsive wrapping, focus states, link treatment, spacing, and basic accessibility rules;
- the cache-key naming convention;
- the References page shell structure (not its references).

### Pack-owned

The following must remain in each pack:

- pack title, chapter titles, chapter order, labels, and hrefs;
- all teaching prose, examples, figures, tables, maps, and diagrams;
- the actual disclaimer wording, if pack/legal review requires wording differences;
- the actual References entries, source notes, citations, and ordering;
- pack-specific `shared.css`, `draft.css`, theme rules, visual assets, and scripts;
- page-specific previous / next destinations;
- page-specific update timestamp value, provided it is the same pack-wide value for that wave.

Do not copy IAS 2 content into CF 2018 or IFRS 18. Shared chrome supplies structure and styling only.

---

## 4. Page contract for Phase 1

Each page should have this high-level order inside `<body>`:

```text
chrome:start
  header bar
  tag row
chrome:end
main page content (pack-owned)
pack disclaimer (pack-owned wording, shared class)
footer-nav:start
  previous / Map / next links
footer-nav:end
```

The disclaimer must be after the page-specific content and immediately before the footer navigation. The footer navigation must remain inside the page’s main content wrapper, as in the IAS 2 golden reference.

### 4.1 Suggested attributes and classes

Use attributes to make checks and later tooling straightforward. They are metadata, not a replacement for visible text.

```html
<body data-pack="ias2" data-page="map">
```

Recommended values:

- `data-pack`: stable lowercase pack key: `ias2`, `cf2018`, or `ifrs18`;
- `data-page`: `map`, `chapter`, or `references`;
- optional `data-chapter`: the pack-owned chapter key, such as `ch01`;
- optional `data-chrome-version`: a human-readable implementation marker if useful.

The active tag remains an ordinary link with class `tag active`; do not make active state JavaScript-only.

The update stamp may carry a machine-readable attribute while retaining the required visible label:

```html
<span class="chrome-last-update" data-last-update="2026-10-02T00:25+08:00">
  Last update · 2026-10-02 00:25 HKT
</span>
```

Use the actual agreed pack-wide timestamp when implementing. Do not infer or generate a new timestamp separately on each page.

### 4.2 Copy-include markers for agents (preferred now)

For static HTML, agents should copy the same chrome block into each page and change only pack-owned values: title, active tag, hrefs, and update value.

Keep these boundaries intact:

```html
<!-- chrome:start -->
<header class="chrome-bar">
  <!-- Home + pack title + Last update · YYYY-MM-DD HH:MM HKT -->
  <nav class="tag-row-wrap" aria-label="Chapters">
    <!-- Map + pack-owned chapter links + References -->
  </nav>
</header>
<!-- chrome:end -->
```

Keep the bottom boundaries intact:

```html
<aside class="callout pack-disclaimer" id="pack-disclaimer">
  <!-- Pack-owned disclaimer wording; do not invent or transplant content. -->
</aside>

<!-- footer-nav:start -->
<nav class="footer-nav">
  <!-- Pack-owned previous / Map / next links; omit unavailable ends. -->
</nav>
<!-- footer-nav:end -->
```

The comments are operational markers for agents and QA. They are not a request to add a runtime include system.

### 4.3 Optional later SSI/build include

If a server-side include or build process is introduced later, it may assemble the same blocks from shared templates. It must produce the same final static HTML contract and preserve the markers so a reviewer can inspect the result.

Possible future includes are illustrative only:

```text
_shared/chrome/header.html
_shared/chrome/tag-row.html
_shared/chrome/footer-nav.html
```

Do not implement SSI/build in this wave. Do not make local preview depend on it.

---

## 5. Shared CSS inclusion and path rules

From any page in `draft-v1-linked/`, the shared folder is two levels up and then `_shared`:

```text
../../_shared/chrome.css
```

For example, a future page head will include the shared CSS before pack-specific overrides:

```html
<link rel="stylesheet" href="../../_shared/chrome.css?v=ias2-refs-lastupdate-20261002">
<link rel="stylesheet" href="assets/shared.css?v=ias2-refs-lastupdate-20261002">
<link rel="stylesheet" href="assets/draft.css?v=ias2-refs-lastupdate-20261002">
```

The exact order should be confirmed during implementation, but the rule is: shared chrome first, pack styles after it, and no inline chrome styles when the shared rule exists. Pack CSS may override a shared rule only when a deliberate pack-specific difference is documented.

If a future helper is actually needed:

```html
<script src="../../_shared/chrome.js?v=ias2-refs-lastupdate-20261002" defer></script>
```

Do not add this script merely because the file exists. A page that has copied static chrome should work with JavaScript disabled.

### Cache-key convention

Use one query-string key per pack implementation wave:

```text
?v=<pack-key>-refs-lastupdate-YYYYMMDD
```

Examples:

```text
?v=ias2-refs-lastupdate-20261002
?v=cf2018-refs-lastupdate-20261002
?v=ifrs18-refs-lastupdate-20261002
```

Rules:

1. Use the same key on every page and every shared asset used by that pack wave.
2. Change the date/key when shared chrome CSS/JS or pack-wide chrome changes.
3. Keep the visible HKT timestamp and the cache date aligned to the same release wave unless a deliberate hotfix is recorded.
4. Do not use a per-chapter cache key for shared chrome.
5. Existing keys such as IAS 2’s `ias2-refs-lastupdate-20261002` are the starting convention; do not rename them casually during migration.

---

## 6. References page shell

The References page is a page type, not a shared content database. Every pack supplies its own entries.

Required shell order:

1. normal Phase 1 header and tag row, with `References` active;
2. the page’s main wrapper;
3. a pack-owned page heading identifying the pack’s references;
4. pack-owned reference sections and entries;
5. the pack disclaimer;
6. footer navigation, normally back to the final chapter and to Map as appropriate.

Recommended structural markers, with no invented reference content:

```html
<main class="page references-page" data-page="references">
  <div class="page-header">
    <h1><!-- pack-owned References title --></h1>
  </div>

  <!-- pack-owned references content starts -->
  <!-- Official / firm / issuer sections only when this pack has them. -->
  <!-- pack-owned references content ends -->

  <aside class="callout pack-disclaimer" id="pack-disclaimer">
    <!-- pack-owned disclaimer -->
  </aside>

  <!-- footer-nav:start -->
  <nav class="footer-nav"><!-- pack-owned links --></nav>
  <!-- footer-nav:end -->
</main>
```

Use actual sections only when supported by that pack’s content. This design does not authorize adding sources, citations, firms, or reference prose.

---

## 7. Phase boundaries

### Phase 1: implement next wave

Implement only the chrome contract in this document: shared chrome CSS, static copied blocks, References shell, and cache-key updates. Keep teaching content HTML per pack.

### Phase 2: design now, do not implement now

Plan, but do not add in the Phase 1 wave:

- `.cite` and `.cite-house`;
- firm colours for Official, PwC, DTT, EY, and KPMG;
- shared CSS variables such as `--ink`, `--line`, `--band`, and related tokens currently duplicated in pack `shared.css` / `draft.css`;
- possible `.callout.differ` and basic `.box` chrome.

Phase 2 needs its own review of token ownership, contrast, and source-label semantics. Do not smuggle these changes into the chrome migration.

### Phase 3: optional later

Defer illustration and worked-strip primitives. They are likely pack-specific and should not become shared chrome without repeated use across packs.

---

## 8. Migration plan: IAS 2 → CF 2018 → IFRS 18

### Step 0 — design gate (this document)

- Confirm the shared folder and class/marker contract.
- Confirm that no pack HTML is changed as part of this design task.
- Keep IAS 2 as the visual and structural golden reference.

### Step 1 — IAS 2 pilot

- Inventory every page under `refs/ias-2/draft-v1-linked/`.
- Preserve its existing `chrome:start/end`, `pack-disclaimer`, and `footer-nav:start/end` boundaries.
- Replace repeated chrome styling with the future shared stylesheet, without changing teaching content.
- Verify all chapter labels, hrefs, active states, disclaimer wording, References entries, and visual assets remain IAS 2-owned.
- Verify the existing IAS 2 cache key and visible timestamp as one pack-wide release value.

### Step 2 — CF 2018

- Inventory the actual page filenames and navigation order first; do not assume IAS 2 chapter names or count.
- Add the same structural markers and shared class names.
- Populate only CF 2018’s own title, chapters, links, disclaimer wording, and References entries.
- Use `cf2018` for the cache key and one CF 2018 release timestamp.

### Step 3 — IFRS 18

- Repeat the CF 2018 process using IFRS 18’s actual page inventory.
- Use `ifrs18` for the cache key and one IFRS 18 release timestamp.
- Keep IFRS 18-specific navigation and references pack-owned.

### Step 4 — cross-pack sweep

- Compare rendered chrome at narrow and wide widths.
- Check keyboard focus and active-tag state.
- Check that opening a page directly from its directory still resolves CSS, links, images, and scripts.
- Record only genuine exceptions; do not fork shared CSS for cosmetic one-offs without a reason.

---

## 9. QA checklist for agents

Run these checks after implementation, not during this design-only task.

### Structure

- [ ] Every page has exactly one `chrome:start` and one `chrome:end`.
- [ ] Header contains Home, pack title, and visible `Last update · YYYY-MM-DD HH:MM HKT`.
- [ ] Tag row has Map, all pack-owned chapter links, and References.
- [ ] The active page has `tag active`; the active state does not rely on JavaScript.
- [ ] `pack-disclaimer` appears after page content and before `footer-nav:start`.
- [ ] Footer markers are present and previous / Map / next links are correct for that page.
- [ ] References pages use the shell but contain only that pack’s references.

### Links and paths

- [ ] From `draft-v1-linked/`, shared assets use `../../_shared/...`.
- [ ] No page points at another pack’s content by accident.
- [ ] Home link is tested from every pack directory.
- [ ] Previous and next links work at the first page, middle pages, final chapter, and References page.
- [ ] Asset paths still work when a page is opened directly, not only through a site root.

### CSS and accessibility

- [ ] Shared chrome CSS loads before pack overrides.
- [ ] No new inline chrome styling duplicates the shared module.
- [ ] Links have visible keyboard focus.
- [ ] Tag row wraps or scrolls without hiding required navigation on narrow screens.
- [ ] Header and footer remain usable at the tested zoom levels.
- [ ] Navigation has an appropriate accessible label.
- [ ] Colour and contrast remain readable in supported light/dark modes.

### Release hygiene

- [ ] One cache key is used consistently across a pack wave.
- [ ] Visible update stamp is identical across that pack’s pages.
- [ ] Phase 2 citation/token work is not mixed into the Phase 1 diff.
- [ ] No pack HTML teaching content was rewritten as part of chrome work.

Useful checks include `rg` for marker counts, update strings, and `../../_shared/` paths, plus a link check or direct browser review of every page.

---

## 10. Non-goals

This design does not:

- rewrite any pack HTML, teaching prose, or references;
- create or populate citations;
- decide legal wording or replace pack disclaimers;
- consolidate all CSS variables or theme tokens;
- introduce a build system, SSI, framework, or runtime dependency;
- standardize illustrations, worked examples, tables, or chapter layouts;
- create a shared content model or reference database;
- implement Phase 2 or Phase 3 primitives;
- sync anything to Documents.

---

## 11. Open questions and default decisions

No question needs Johnny’s decision before the next implementation wave if the defaults below are followed.

| Topic | Default for implementation |
|---|---|
| Static versus build | Static copied HTML is canonical; no build step. |
| Shared JavaScript | Not required; optional later, progressive enhancement only. |
| Chrome boundaries | Preserve the named HTML comments exactly. |
| Disclaimer wording | Pack-owned; shared class and placement only. |
| References content | Pack-owned; shared shell only. |
| Token consolidation | Phase 2, not part of chrome migration. |
| Illustrations / worked strips | Defer; assess as pack-specific in Phase 3. |
| Cache key | `<pack-key>-refs-lastupdate-YYYYMMDD`, pack-wide per wave. |
| Time label | Visible HKT format exactly as specified. |
| Home destination | Preserve and test each pack’s existing site Home destination; do not invent a new route in the design phase. |

**Next action when approved:** implement Phase 1 for IAS 2 only, then QA it before copying the pattern to CF 2018 and IFRS 18. This document itself makes no such implementation.
