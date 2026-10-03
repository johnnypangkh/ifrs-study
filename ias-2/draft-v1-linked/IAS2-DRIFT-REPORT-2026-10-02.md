# IAS 2 Documents drift / chrome / QC — 2026-10-02

Job #6. Scope: `refs/ias-2/draft-v1-linked/` only. No nested mirror of this pack in the repo. No teaching edits, no CF edits, no IFRS 18 edits.

Pack-level stamp on every reader page: **Last update: 2 Oct 2026, 16:03 HKT** (same block, sha256 `2f98aa6ba615`).

## Criteria

| # | Check | Result |
|---|--------|--------|
| 1 | `_shared` / cite / tokens links resolve | **PASS (nothing to retarget).** No page links `_shared`, `cite.css`, or `tokens.css`. Pack-local links resolve: `assets/shared.css`, `assets/draft.css`, `assets/theme.js`, `assets/iframe-fit.js`, `visuals/shared.css`, `visuals/ias2.css`, chapter and Map iframes. |
| 2 | References + Last update coherent | **FIXED.** Neither existed. All 7 reader pages now carry the same References line and the same HKT stamp. |
| 3 | No Gate leftover | **PASS on reader HTML.** `ch01`–`ch03` and all `ch*.html`, `index.html`, and `visuals/*.html`: zero whole-word Gate. Left in place (not reader-visible): `assets/iframe-fit.js` comment, `assets/shared.css` “meaning gate”, `visuals/shared.css` `.sh-gate` (Build-owned; no IAS 2 page uses `.start-here`). Notes and METHOD still say “gate” as process language — not the site. |
| 4 | Cite short forms still IAS 2 locked | **PASS on chips. Footer now states the short forms.** 1,117 chips, 0 off-lock: `PwC MOA 2020`, `DTT A11 2022`, `EY IGAAP 2026`, `KPMG Insights 2019/20`, plus Official `IAS`/`IFRS`/`IFRIC`. Chips were not rewritten. |
| 5 | Disclaimer at bottom; Decision not Gate | **FIXED.** Disclaimer moved off the Map title (index only) to the bottom of index and ch01–ch06. Wording unchanged. Maps already say Decision (aria-label), not Gate. |
| 6 | Lag vs CF chrome | **Flagged, not copied.** See below. |

## DIFF (reader HTML only)

Same insertion on each file, after `footer-nav`. `index.html` also loses the disclaimer that sat under the h1.

- `index.html` — disclaimer removed from under the title; pack stamp added at the bottom.
- `ch01.html` — pack stamp added.
- `ch02.html` — pack stamp added.
- `ch03.html` — pack stamp added.
- `ch04.html` — pack stamp added.
- `ch05.html` — pack stamp added.
- `ch06.html` — pack stamp added.

Stamp text (identical):

- References: IAS 2 Inventories. PwC MOA 2020 Ch25; DTT iGAAP 2022 A11; EY iGAAP 2026 Ch23; KPMG Insights 2019/20 · Part 1 · 3.8.
- Disclaimer: the existing personal-study paragraph (`#pack-disclaimer`).
- Last update: 2 Oct 2026, 16:03 HKT.

`pack_audit.py` after the edit: broken anchors empty on all six chapters.

## Not changed (intentional lag vs CF chrome)

- **No `_shared` split.** Cite colour and type stay in `assets/shared.css` / `visuals/shared.css` (header still says the file is the IFRS 18 draft kit, `file://` via relative link). Pointing IAS 2 at a Documents `_shared` folder would break offline open; that folder is not in this repo.
- **Home link** `../../homepage/homepage-wireframe-v0.1.html` does not resolve inside this git tree (`refs/` has no `homepage/`). It is the Documents-relative Home path (pack two levels under the folder that contains `homepage/`). Not rewritten.
- **Chip grammar vs footer short form.** Chips stay `DTT A11 2022` and `EY IGAAP 2026` (teaching-body lock). The footer uses the pack short forms `DTT iGAAP 2022 A11` and `EY iGAAP 2026 Ch23`. Both are IAS 2, not CF labels (no “EY Closer look”, no “KPMG FI”).
- **Build “gate” names** in `shared.css` / `iframe-fit.js` (including the `cf-visual-height` message). Renaming them is a shared-kit change, not an IAS 2 reader fix.
- **IFRS 18 category / MPM tokens** inside `assets/shared.css` and `visuals/shared.css`. Left as-is. Not used as IAS 2 teaching.

## Pull-back

HTML only: `/opt/cursor/artifacts/ias2-chrome-pullback-2026-10-02.tar.gz`  
Members: `index.html`, `ch01.html`–`ch06.html`.
