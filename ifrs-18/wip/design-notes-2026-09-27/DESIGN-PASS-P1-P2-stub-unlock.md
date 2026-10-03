# Design pass — IFRS 18 P1/P2 stub visuals unlock
**Canon:** VISUAL-TYPES / PRODUCT-SPEC **2026.09.27-7** · night-only · spacing ~14px · § chips `a.fb-num` → `#s-x-y` `target="_parent"` · single-frame fieldset on chapters (no `.visual-shell` in iframe) · dashed rare · colour only with teaching meaning · FIRST DRAFT dense kit  
**When:** 2026-09-27 ~23:26 Asia/Shanghai · Design executor · Johnny go-ahead ~23:24  
**Pack:** `refs/ifrs-18/draft-v1-linked/`  
**Tokens:** Build-owned in `visuals/shared.css` — Design mounts only (no provisional hex)

## Brief cue
`wip/IFRS18-CONTENT-DESIGN-BRIEF-2026-09-27.md` §1 TYPE map + §5 traps.

## Files touched
| Path | Action |
|------|--------|
| `visuals/ch01-whats-new.html` | Replace stub → P1 contrast + three sets + small timeline |
| `visuals/ch05-operating-expenses.html` | Replace stub → P1 nature∥function∥mixed matrix + operating slice + §83 solid contain |
| `visuals/ch08-transition.html` | Replace stub → P1 timeline (1 Jan 2027 hub) + annual∥interim checklist |
| `visuals/ch07-other-fs.html` | Replace stub → P2 three thin bridges + tiny SCF stmt |
| `wip/design-notes-2026-09-27/DESIGN-PASS-P1-P2-stub-unlock.md` | This note |

**Not edited:** parent chapter teaching bodies · Concept Map fieldsets (already wired) · homepage READY · LOCK-STAMP · `shared.css` colour tokens · P0 plates · Map jump board

**Twin sync:** **Skipped** — no `refs/ifrs-18/chapter-visuals/` tree.

## Per-plate summary

### Ch1 — What’s new (P1)
- `.contrast-pair.dense`: IAS 1-era gaps (`.box.warn`) ∥ IFRS 18 answer (`.box.ok`).
- Familiar net profit ≠ unchanged shape callout.
- Three hub cards (Set 1 structured P&L → Ch3–4 · Set 2 grouping → Ch2 · Set 3 MPM → Ch6) + `.rel-connect--down` “operating = default”.
- Small page-local timeline: Prepare → **1 Jan 2027** hub → Ch8 detail.
- Chips: 1.1 / 1.2 / 1.4 (+ pointer 8.1). Banks = `.callout.see` only.
- Traps respected: no IAS 1 pack rebuild · no HKFRS dual code · no Overview.

### Ch5 — Operating expenses (P1)
- 4-col `.matrix`: Nature ∥ Function ∥ Mixed (§78–79) with mixed-allowed trap callout.
- Operating slice mounts `.cat-band--operating` / `.cat-operating` only (no other category rainbow).
- Function example lines (COGS / distribution / admin) → `.rel-connect--down` → **solid** `.contain` §83 nature-totals plate (depreciation · amortisation · employee benefits · IAS 36 impairment · inventory write-downs) — **not dashed**.
- Thin §84 see-callout → 5.4.
- Chips: 5.1 / 5.3 / 5.4.

### Ch8 — Transition (P1)
- Timeline with **prominent** 1 Jan 2027 hub (accent border/soft) — Prepare → hub → first-year interims → first annual.
- Retrospective cue callout → 8.2.
- 3-col checklist matrix: Duty × Annual §C3 × Interim §C4–C5 (headings/subtotals · reconciliations · extra periods).
- Trap callout: do not bury effective date.
- Chips: 8.1 / 8.2 / 8.3 / 8.4 / 8.5.
- Page-local `.matrix[data-cols="3"]` (kit has 4/5/6 only) — Build ask below.

### Ch7 — Other FS impacts (P2)
- Three thin bridge cards: 7.1 SCF operating-profit start · 7.2 SFP structured-summary lens · 7.3 EPS + 7.4 interim pointer.
- Tiny `.stmt-block`: Operating profit (`.ifrs-subtotal`) → adjustments → operating CF hub.
- Banks SCF = `.see-strip` dashed only (Map later).
- Trap: do not grow into IAS 7 / IAS 33 course art.
- Chips: 7.1 / 7.2 / 7.3 / 7.4.

## Parent fieldset / iframe / anchor verification
| Page | Fieldset “Concept Map” | iframe src | Anchors used (all present) |
|------|------------------------|------------|----------------------------|
| `ch01.html` | Wired (untouched) | `visuals/ch01-whats-new.html` | `#s-1-1` `#s-1-2` `#s-1-4` (+ `#s-8-1` pointer) |
| `ch05.html` | Wired | `visuals/ch05-operating-expenses.html` | `#s-5-1` `#s-5-3` `#s-5-4` |
| `ch07.html` | Wired | `visuals/ch07-other-fs.html` | `#s-7-1` `#s-7-2` `#s-7-3` `#s-7-4` |
| `ch08.html` | Wired | `visuals/ch08-transition.html` | `#s-8-1` `#s-8-2` `#s-8-3` `#s-8-4` `#s-8-5` |

No Concept Map fieldset added inside embeds. Content teaching bodies untouched.

## Standing bar self-scan
- [x] Night-only (theme.js; no day invent)
- [x] Post-renumber Ch kickers 1 / 5 / 7 / 8 correct
- [x] § chips `a.fb-num` → parent `#s-x-y` + `target="_parent"`
- [x] No `.visual-shell` / no double full-bleed plate in iframe
- [x] Spacing: kit gaps + page-local ~8–14px; no `gap:0` major stacks
- [x] Real connectors (`.rel-connect` / labelled arrows) — no floating ⟷
- [x] Dashed rare: banks see-also · §84 thin see · §C7 thin see only
- [x] §83 = solid `.contain` (explicitly not dashed)
- [x] Operating colour only on Ch5 operating slice (`--cat-operating` family)
- [x] Stub “Design draws next” chrome stripped
- [x] Homepage READY **not** flipped · no LOCK-STAMP
- [x] Twin `chapter-visuals/` skipped (folder absent)

## Build follow-ups (non-blocking)
1. Promote `.matrix[data-cols="3"] { --matrix-cols: 3; }` into kit `shared.css` (Ch8 uses page-local until then).
2. Optional: promote page-local `.tl-row` / `.tl-step` / `.tl-hub` timeline pattern (Ch1 + Ch8 + Map chip family) into shared kit if reused again.
3. Optional: promote `.bridge-row` / tiny SCF stack helpers if other packs need by-phase strips.
4. Twin `chapter-visuals/` tree only if pack wants CF-parity offline twins (still absent for IFRS 18).

## Ambiguities
- Ch1 three-set cards point to Ch2/3/4/6 by text only (no cross-chapter `fb-num` into those sections) — keeps Ch1 frame self-contained; timeline alone jumps to 8.1.
- Ch5 function slice is a teaching sketch (COGS / distribution / admin) — not a prescribed IE layout.
- Ch7 EPS + interim share one bridge card (both thin pointers) to avoid growing the strip into a four-card course map.
- Ch8 matrix “Headings / subtotals” annual cell is “Full IFRS 18 presentation” paraphrase — §C3 text focuses on reconciliations; headings implied by first annual under the Standard.
