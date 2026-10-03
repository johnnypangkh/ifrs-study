# IFRS 18 — Content TYPE picks + Design brief

**Owner:** Content (draft) → Design (draw)  
**Date:** 2026-09-27 (Asia/Shanghai)  
**Canon:** **2026.09.27-7** — chapter numbers remapped to contiguous **Map · 1…8** (PRODUCT-SPEC §7b). Old Map·2…9 superseded.  
**Pack:** IFRS 18 Presentation and Disclosure  
**Locks:** CF template · VISUAL-TYPES / PRODUCT-SPEC **2026.09.27-7** · night-only · colour only with teaching meaning · dashed rare  
**HTML shell:** `refs/ifrs-18/draft-v1-linked/` (Build remapped HTML filenames/ids; Content synced MD twins + this brief)  
**Authority spine:** official IFRS 18 (§ chips) · KPMG FI (visual flow) · EY MOA 2026 (depth)

---

## 1. TYPE map (chapter → TYPE → stub → Design priority)

| Ch | Working title | VISUAL TYPE(s) | Stub path (`draft-v1-linked/visuals/`) | Priority |
|----|---------------|----------------|----------------------------------------|----------|
| **Map** | Map jump board | **Concept map** (jump board — **no** Concept Map fieldset on Map page) | `map-jumpboard.html` (optional; pillars live on `index.html`) | **P0** (Map openable) |
| **1** | What’s new vs IAS 1 | **Two-column contrast cards** + small **timeline** | `ch01-whats-new.html` | P1 |
| **2** | PFS roles & aggregation | **Concept map** (PFS ∥ Notes) + **checklist table** | `ch02-pfs-aggregation.html` | **P0** (aggregation roles plate) |
| **3** | P&L categories | **Statement layout** (category colour bands) + nested **decision tree** (main path) | `ch03-pnl-categories.html` | **P0** |
| **4** | Totals & subtotals | **Statement layout** (brackets on bands) + **matrix** (required vs §118 vs MPM) | `ch04-totals-subtotals.html` | **P0** |
| **5** | Operating expenses | **Matrix** (nature ∥ function ∥ mixed) + small **statement-layout** operating slice | `ch05-operating-expenses.html` | P1 |
| **6** | MPMs | **Decision tree** (is MPM?) + **waterfall / build-up** reconciliation | `ch06-mpms.html` | **P0** |
| **7** | Other FS impacts | **By-phase / see-also strip** + tiny **statement layout** (SCF) | `ch07-other-fs.html` | P2 |
| **8** | Transition | **Timeline** + **checklist table** (annual vs interim) | `ch08-transition.html` | P1 |

**Stub law:** each stub is labelled with chosen TYPE(s) + “Design draws next.” Do **not** treat stubs as finished drawings.

---

## 2. Priority P0 unlock pack (Design first)

| Visual | Why P0 | Content anchors | Design notes |
|--------|--------|-----------------|--------------|
| **Ch3 categories schematic** | Core new P&L structure | `#s-3-1`–`#s-3-2` · five bands | Full-height statement layout; five category tokens; placeholders for Ch4 brackets; legend one-liners or on-band labels |
| **Ch4 / Ch6 MPM contrast** | Measure-regime teaching | Ch4 `#s-4-4` · Ch6 `#s-6-3`–`#s-6-4` | Two tokens only: `--ifrs-subtotal` vs `--mpm`; Ch4 matrix columns; Ch6 waterfall MPM→anchor |
| **Ch2 aggregation roles plate** | Foundations before category mechanics | `#s-2-1` · `#s-2-3` | Dual-role plate PFS ∥ Notes (§16 / §17 chips); checklist not a fake flowchart |
| **Map jump board** | Entry / openable pack | Pillar cards → Ch3–4 / Ch2 / Ch6 | Three pillar cards; thin “1 Jan 2027” chip → Ch8; dashed see-also Banks/insurers; **no** Concept Map fieldset |

---

## 3. Colour grammar proposal (copy structure §4)

Same logic as Johnny Ch3 consol decode: colour only when legend (or on-node label) can state teaching meaning in one plain line; same meaning → same token across the pack; peers that are not categorical stay neutral.

### Category bands (Ch3 / Ch4 / Ch5 operating slice)

| Token | Meaning (legend one-liner) | Where |
|-------|----------------------------|--------|
| `--cat-operating` | Operating category (default) | Band + chips |
| `--cat-investing` | Investing category | Band + chips |
| `--cat-financing` | Financing category | Band + chips |
| `--cat-tax` | Income taxes category | Band + chips |
| `--cat-discontinued` | Discontinued operations category | Band + chips |

Neutral ink/surface for non-category chrome (titles, operators, § chip source class unchanged).

### MPM vs IFRS subtotals contrast (Ch4 matrix · Ch6 waterfall)

| Token | Meaning | Parallel |
|-------|---------|----------|
| `--ifrs-subtotal` | IFRS-required or §118-listed subtotal (audited IFRS measure space) | “In the Standard’s measure set” |
| `--mpm` | Management-defined performance measure (single-note reconciliation world) | Different regime — **not** “more important colour” |

**Do not** paint every §118 row a different hue. Required §69 brackets share `--ifrs-subtotal` with weight/bracket treatment difference (line weight / label), not a third rainbow.

### Dashed (rare — unchanged site law)

- See-also bridges/chips (Banks/insurers later; IAS 7 bridge)
- Matrix N/A cells if any
- Consol group plate **only** if consol relationship taught (unlikely in v1 IFRS 18 core)
- **Not** for nesting MPM under P&L — use containment or the MPM token

### Legend

Right-rail only when bands or MPM contrast appear; skip if every band is already labelled on the schematic.

**Propose tokens in pack `shared.css` / `visuals/shared.css` on Design pass** — Content does not invent finished token hex here; night-only palette must meet PRODUCT-SPEC contrast.

---

## 4. Assumptions on open questions (structure §7)

| # | Question | Content assumption for v1 draft |
|---|----------|----------------------------------|
| **Q1** | Ch2 early vs KPMG-late aggregation? | **YES — Ch2 early** (official + EY). Roles/aggregation before category mechanics. |
| **Q2** | Banks/insurers see-also: Map-only or also Ch3? | **Map-only** dashed chip in v1 (prefer Map-only per open Q2 default). Ch3 keeps a thin “later” callout text without a second dashed Map-style chip competing on the sticky row. |
| **Q3** | Five category tokens + two-measure contrast, or collapse tax+discontinued? | **Five category tokens + `--ifrs-subtotal` / `--mpm`** (do not collapse). |

---

## 5. Per-chapter Design cues (short)

| Ch | Key visual ideas (from structure) | Traps for Design |
|----|-----------------------------------|------------------|
| Map | Three pillars · 1 Jan 2027 timeline chip · dashed banks see-also | No Overview; no grammar-decoding `.map-legend`; no HKFRS dual code |
| 1 | IAS 1 diversity → IFRS 18 structure contrast; “net profit familiar / shape changes” | Don’t rebuild IAS 1 pack visuals |
| 2 | PFS ∥ Notes dual plate; shared-characteristics cluster | No fake aggregation flowchart; dashed only see-also |
| 3 | Five colour bands + compact main-path decision | No full bank AG dump; no “operating = recurring”; no rainbow without meaning |
| 4 | Brackets on Ch3 skeleton; 3-column matrix | Don’t equate gross profit with MPM; show §73 path as trap callout |
| 5 | Three-option matrix; §83 note as **solid containment** | Mixed allowed; don’t dash the §83 plate |
| 6 | Gate tree → waterfall with MPM vs IFRS-subtotal colours | §118 ≠ MPM; no non-GAAP invention beyond Standard definition |
| 7 | Three thin bridge cards; operating profit → SCF start | Don’t grow into IAS 7/33 course art |
| 8 | Timeline to 1 Jan 2027; annual ∥ interim checklist | Don’t bury effective date |

---

## 6. Chrome checklist (Design inherits)

- Chapter pages: `.visual-section` > `fieldset.visual-fieldset` > `legend.visual-legend` = “Concept Map” + iframe to stub
- Map page: **NO** Concept Map fieldset
- Citation chips: `<span class="cite cite-official">§…</span>`
- Footer Prev / Map / Next; sticky tag row identical on every page (**Map · 1…8**)
- Title only in page-header (no purpose blurb)
- Effective-date cue: periods beginning on/after **1 Jan 2027**

---

## 7. Handoff

- **Content status:** Map + Ch1–Ch8 HTML remapped by Build; MD twins + this brief + STATUS synced 2026-09-27 (Asia/Shanghai) under canon **2026.09.27-7**
- **Design unlock:** Map + Ch3 + Ch4 + Ch6 bodies substantive; Ch2 P0 plate ready for roles schematic
- **Homepage READY flip:** PM owns — do not mark homepage READY from Content
- **STATUS:** `wip/IFRS18-CONTENT-STATUS-2026-09-27.md`
