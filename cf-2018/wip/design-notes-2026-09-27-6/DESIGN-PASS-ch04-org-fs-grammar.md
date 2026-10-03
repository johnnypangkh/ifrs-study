# Design pass — Ch4 Concept Map org / FS grammar redraw

*(Note 2026.09.27-7: live site Reporting entity is now **Ch3** / `ch03.html` — this Design-pass note keeps pre-remap Ch4 ids as historical.)*
**Canon:** 2026.09.27-6 · PM unlock · Johnny plate exemplar  
**When:** 2026-09-27 (Asia/Shanghai) · Design executor  
**File:** `ch04-reporting-entity.html` (+ twin)  
**Exemplars:** Johnny `6bb3ba39…png` (canonical); night FAIL `dd916a06…png` (single ↓ into gap); party-cast FAIL `d7ea9b07…png`

## Problem (before)
1. **Party cast** — `.icon-label-grid` Parent | Subsidiary | Reporting entity triple-taught roles as peer icons (KILL).
2. **Broken org stem** — `.rel-connect.rel-connect--down` single arrow into the empty gap between Subsid A/B (not a T-junction).
3. **Consol|Unconsol peer hang** — L2 kids under Boundary *and* a peer `.grid-2` under kids triple-taught the same Consol|Unconsol lesson; Johnny plate is the clear figure.
4. **No group-boundary grammar** — dashed plate / dashed Conso FS / solid Parent↔Unconso FS mapping missing.

## Fix (HTML + structural CSS)

### HTML structure
1. **L1 row** — Entity perspective (4.3) / Going concern (4.4) / Boundary (4.5). Boundary **slimmed to containment-only** hub box — dropped Consol|Unconsol L2 kids (no more `.boundary-shell` / `.boundary-kids`).
2. **See-strips** — IFRS 10 / IAS 27 stay thin `.see-strip` (dashed chip ≠ group plate).
3. **Johnny plate (main figure)** — `.org-fs-row`:
   - **Left** `.consol-boundary` (dashed group plate) → `.org-chart` → Parent `.box.entity-parent.org-parent` → `.org-branch` with **T-junction** `.org-fork` (stem + rail + leg×2 meeting each sub top-center) → `.org-kids` Subsid A/B `.box.entity-sub`.
   - **Right** `.fs-stack` → `.box.fs-consol` (Conso FS, §4.6) + `.box.fs-unconsol` (Unconso FS, §4.6).
4. **Table** + **YES/NO hard-boundary** flow kept (no IFRS 10 mechanics invent).

### CSS classes used (Build GREEN colour tokens — no parallel invent)
| Class | Role |
|-------|------|
| `.consol-boundary` | Dashed group plate |
| `.entity-parent` / `.org-parent` | Solid-fill Parent |
| `.entity-sub` | Outline Subsid A/B |
| `.fs-consol` | Dashed Conso FS card |
| `.fs-unconsol` | Solid Unconso FS card (matches Parent) |

### CSS classes added (Design structural — colour from `--entity-parent-line` only)
| Class | Role |
|-------|------|
| `.org-fs-row` | Plate ‖ FS side-by-side grid; gap 14px |
| `.fs-stack` | Vertical Conso / Unconso stack; gap 14px |
| `.org-branch` | Shared width wrapper so fork legs align with kid centers |
| `.org-fork` / `.org-fork-stem` / `.org-fork-rail` / `.org-fork-leg` | T-junction branched stems |
| `.see-row` / `.see-strip-note` | See-strip row helper (replaces inline style) |

Also: `.l1-row` columns `1fr 1fr 1fr` (was `1fr 1fr 1.4fr` for Boundary kids — Ch4-only consumer).

### Grammar lock
- **Dashed** = Consol chrome only (`.consol-boundary` / `.fs-consol`) + existing see-strips.
- **Solid fill** = Parent / Unconso FS.
- **Outline** = Subsid A/B.
- **Org lines** = solid 2px via `--entity-parent-line`; T-junction to each sub — never one arrow to empty gap.
- Spacing stays Canon 2026.09.27-5 (~14px major gaps; fork uses gap-cancel like `.rel-connect`).

## Boundary slim choice
**Slim further to hub box (containment-only).** Dropped Consol|Unconsol L2 kids from Boundary so Johnny plate is the sole Consol|Unconsol teaching figure. Kept chip 4.5 + short body. Table + YES/NO still carry 4.5/4.6 detail.

## Files touched
- `refs/cf-2018/draft-v1-linked/visuals/ch04-reporting-entity.html`
- `refs/cf-2018/draft-v1-linked/visuals/shared.css` (structural helpers + l1-row equalize)
- `refs/cf-2018/chapter-visuals/ch04-reporting-entity.html` (twin; `theme.js` local path)
- `refs/cf-2018/chapter-visuals/shared.css` (twin sync — picks up Build GREEN consol tokens + Design helpers)
- `refs/cf-2018/wip/design-notes-2026-09-27-6/DESIGN-PASS-ch04-org-fs-grammar.md` (this note)

**Not edited:** other chapters, Overview/chrome, colour-decode legend rails, parent chapter pages, parent `assets/shared.css`.

## Self-scan (pre-SAVE)
- [x] No `.icon-label-grid` party cast
- [x] No single ↓ into gap between kids (T-junction present)
- [x] No Consol|Unconsol L2 hang under Boundary; no peer FS grid under kids
- [x] Dashed only for consol plate + Conso FS (+ see-strips)
- [x] § chips 4.3 / 4.4 / 4.5 / 4.6 stay (`target="_parent"`)
- [x] No gap:0 major stacks (org-fs-row / fs-stack / org-chart / sections stay ~14px; fork internal gap:0 is connector chrome only)
- [x] Fieldset Concept Map remains sole outer on parent page (`body.embed` untouched)
- [x] Twin parity shared.css; ch04 html twin (theme.js path differs by tree)

## Build notes
- **Colour tokens already GREEN** in draft `visuals/shared.css` (`.consol-boundary`, `.entity-parent`, `.entity-sub`, `.fs-consol`, `.fs-unconsol`). Design did not invent parallel colour tokens.
- **T-rail helper:** Design shipped `.org-fork*` structural CSS in iframe `shared.css` using `--entity-parent-line`. If Build wants a canonical shared T-rail kit name later, remount is fine — no parent `assets/` token needed for this pass.
- **Prefer iframe `shared.css` only** — parent assets not required for this redraw.
- Possible Build polish (not blocking): Johnny sketch shows stronger solid Parent/Unconso fill + light text; current `--entity-parent-fill: var(--accent-soft)` is soft wash. Subs “outline only” vs `--entity-sub-fill: var(--surface)` (surface chip inside transparent plate). Colour-only if Johnny wants tighter match.

## Ambiguities
- Boundary body copy (“containment only”) is Design paraphrase — swap if Johnny wants CF wording closer to 4.5.
- Subsid labels shortened to Johnny sketch “Subsid A/B” (was “Subsidiary A/B”).
- chapter-visuals `theme.js` uses local path (file exists beside html); siblings still point at missing `../assets/theme.js` — out of scope beyond Ch4 twin.
- Fork leg centers assume 2 equal grid kids; >2 subs would need a generalized T-rail (note for Build if ever needed).
