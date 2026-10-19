# #98 addendum — Master formatting page + chapter structural alignment (DRAFT)

**Status:** page-scope under **#98** · **SIGNED by Johnny 2026-10-19 ~01:42 HKT** (`row98-mocks/audit-98/mf-align/ba-mf-align.png`) · page-scope SIGNED · atlas freeze unchanged · no Build / no chapter rollout / no skill edits until Johnny GO Build.  
**Workbook:** **#98** (Johnny 2026-10-18: page update **folds into #98**, not a new row).  
**Owner:** IFRS Master Design 2 · **Date:** 2026-10-18 Asia/Shanghai  
**Freeze stamp:** Atlas meaning in `CONCEPT-MAP-BUILDING-BLOCKS-98.md` + `row98-mocks/` stays **SIGNED — FROZEN**. This addendum does **not** reopen kit IDs / meanings / gaps. It only scopes **how the live Master formatting page + chapter Concept Maps use that frozen index**.  
**Hard fence:** Cite locked **#94 / #91 / #96 / #97** (+ #86). **#89 / kit 2 STRUCK** pending study sign + G6 Build (see `MAP-GRID-BG-DIAG-98.md`). No rewrite of locked bibles. **No Build until Johnny GO** (PM Pre-brief).  
**Supersedes:** `MASTER-FORMATTING-PAGE-99-PROPOSAL.md` (retired).

---

## 0. Awaiting Johnny sign on MAP-4PACK-STUDY-98

**Do not freeze this page-scope** until Johnny signs:

→ **`deliverables/MAP-4PACK-STUDY-98.md`** (**DRAFT-FOR-SIGN** · IAS 2 · IAS 16 · IFRS 18 · CF · gate card §11)

That study holds: H1–H5 Johnny HARD · logic coverage · dialect drift · G1–G8 (G6 = **retire** kit 2 / graph-paper) · skill P0 propose · grid-removal cite `MAP-GRID-BG-DIAG-98.md` · queue #99 + retro #82/#85/#93.

**This addendum:** **SIGNED** (MF mock). Still blocked on Johnny GO before Build / skill edits / chapter rollout.

**Atlas** `CONCEPT-MAP-BUILDING-BLOCKS-98.md` stays FROZEN. Controlled reopen for kit-2 retire + any signed G-rows only after Johnny signs the study.

**Same job when GO:** Master formatting page update **plus** skill MD P0 patches (study §10) — still no Build / no page mocks until GO.


---

## 1. Johnny expectation (locked intent)

1. **Better update** the site’s Master formatting page — fold signed #97 enhance + #98 atlas into it.  
2. **Live Master formatting page and chapter pages must be mechanically / structurally aligned** — same kit blocks, same hierarchy, **not a parallel dialect**.  
3. Atlas/index on Master formatting **drives (or mirrors)** what chapters use.  
4. Still under **#98**; freeze stamp still applies.

---

## 2. What lands on the Master formatting page (v1 · Concept Map kit)

Night @ 1280 specimen first. Path recommend: `homepage/master-formatting.html` (site-wide; link from homepage + How these notes are made). Alt: `design/master-formatting.html` if Johnny wants noindex first.

| Page section ID | Title (reader) | Kit IDs (#98 index #) | Cites | Specimen source |
|---|---|---|---|---|
| `mf-intro` | One rule | — | #94 header | prose |
| `mf-kit-index` | Concept Map kit index | **1–23** (full table) | #98 | row98 after-full-kit + legend |
| `mf-embed` | Embed / clip / slots | **1, 8** | #97 + enhance | row97 enhance strip + narrow after |
| `mf-plates` | Plates L0–L4 | **3–7** | #94 §1 | row94 / row98 |
| `mf-type` | Type T0–T3 (map) | **9, 20, 21** | #94 §2 / #96 | row98 type strip |
| `mf-arrows` | Arrows four roles | **10–13** | #94 §3 / #91 | row91 / row98 |
| `mf-colour-grid` | Colour + spacing | **14, 15** | #94 §4–§5 · kit 2/#89 **STRUCK** (solid bg) | row98 |
| `mf-mods` | Specials see/stop/mute/warn… | **16–19, 23** | #94 mods | row98 |
| `mf-formula` | Formula / ledger note | **22** | #94 mention + grammar | row98 mini strip |
| `mf-gaps` | Not kit (yet) | — | #98 §4 | callouts only |

**Defer (not v1 unless Johnny expands):** body teaching ladder (#82 / Copilot Georgia T0–T2 body), Illus densifiers, right-grid peer-kit.

---

## 3. Chapter alignment — same machine, not a dialect

### 3.1 Rule
Every chapter Concept Map (embed board + parent chrome) may only use classes/tokens that appear in **#98 kit IDs 1–23** (or a documented §4 gap that Johnny later signs). Master formatting page sections **are keyed by the same kit IDs**. If a chapter invents a look with no kit ID → **FAIL** (parallel dialect).

### 3.2 Enforcement map (page section ↔ kit ID ↔ chapter surface)

| Kit ID | Class / contract | Master formatting section | Chapter must use |
|---:|---|---|---|
| 1 | embed reflow / iframe | `mf-embed` | every map iframe + board root |
| 2 | field pitch **STRUCK** | `mf-gaps` / L0 note | **solid `var(--bg)`** — no graph-paper; retire after study sign (G6) |
| 3 | L0 + B′ | `mf-plates` | one Concept Map chrome |
| 4–7 | `.m-l1`…`.m-l4` | `mf-plates` | plates only these ranks |
| 8 | title|text slots | `mf-embed` | no empty content slot |
| 9 | T1/T2/T3 | `mf-type` | map type land only |
| 10–13 | `.m-shaft.*` | `mf-arrows` | four roles only |
| 14–15 | colour / spacing | `mf-colour-grid` | tokens only |
| 16–19, 23 | modifiers | `mf-mods` | see/stop/mute/warn… |
| 20–22 | chip / op / formula | `mf-type` / `mf-formula` | as indexed |

### 3.3 How alignment is enforced (propose — Build implements later)

| Layer | Mechanism |
|---|---|
| **A. Spec** | This addendum + frozen #98 index = SoT. Chapter maps reference kit IDs in QC notes. |
| **B. Markup** | Shared map-box module only exposes kit classes; no pack-local twin classes for the same meaning (site-rules §1). |
| **C. Lint** | Extend map-lint (report→hard): unknown map chrome class / inverted type / empty slot / fixed-1280 embed = FAIL. |
| **D. QC checklist** | teaching-body-qa / map QC: “kit ID present on Master formatting `mf-*` section” + “chapter uses same class”. |
| **E. Specimen** | Master formatting page embeds **the same** full-kit figure family as chapters (row98 after), not a restyled twin. |

**Mechanical test (acceptance):** Pick any labeled block on Master formatting → grep class in one IAS 2 / IAS 16 / IFRS 18 chapter map → same class + token. Diff look = FAIL.

---

## 4. Mock delta (under #98 · after Johnny GO)

Keep frozen `row98-mocks/` baseline. Add sibling folder or files (do not overwrite signed baseline without stamp note):

| File (proposed) | What |
|---|---|
| `map-master/row98-mocks/specimen-master-formatting-page.html` | Page wire: `mf-*` sections + kit ID badges + cite chips to #94/#91/#96/#97 |
| `…/mf-page-1280.png` | Full page night |
| `…/mf-align-chapter-strip-1280.png` | Side-by-side: Master formatting L1 plate specimen ‖ live chapter L1 (same class) |
| `MOCK-NOTES.md` | Add “page-scope DRAFT / SIGNED” subsection; **atlas freeze unchanged** |

Optional: one “before = Copilot dialect / no live page” callout.

---

## 5. Freeze / reopen policy

| Artifact | Policy |
|---|---|
| `CONCEPT-MAP-BUILDING-BLOCKS-98.md` index §1–§5 | **Stay FROZEN** — no kit ID / meaning / gap edits |
| This addendum | Editable until Johnny signs page-scope; then freeze with #98 |
| `row98-mocks/` baseline full-kit | **Stay FROZEN** |
| New `mf-*` mocks | New files; stamp when Johnny signs page |

Reopen frozen atlas **only** if Johnny changes kit inventory (new block / drop gap into kit).

---

## 6. Johnny check ask

**See also** `MAP-4PACK-STUDY-98.md` §11 gate card Q1–Q9 (embed / G1–G8 / grid removal / chip / CF chapter parity / skills / path / queue) — those decisions gate this freeze.

1. Confirm page-scope stays under **#98** (no #99) — already ruled; MD2 follows.  
2. Path: **P1** `homepage/master-formatting.html` vs P2 `design/` vs P3 style-base-only first?  
3. v1 = Concept Map kit only (`mf-*` table) — body ladder later OK?  
4. Alignment enforcement A–E OK (lint+QC+same specimen family)?  
5. GO MD2 to draft `specimen-master-formatting-page.html` + align strip mock?

---

## 7. Non-scope

- No Build / no product repo edit until Johnny GO + PM Pre-brief  
- No reopen #94/#91/#96/#97 meaning  
- No invent collection / densifiers / right-grid as kit  
- Product CSS for #91/#96/#97 stays their own Build briefs (page cites them; does not implement them)

---

## 8. Skill MD updates (same job as Master formatting page — propose; edit only after Johnny GO)

Johnny 2026-10-18 via PM 5: page update **plus** relevant skill MD(s) in the **same #98 job**. No Build until GO. Do not edit skills until signed.

| Priority | Skill file | Why / what to add (cite only) |
|---|---|---|
| **P0** | `ifrs-visual-grammar` (`/home/box/agent-data/workflows/ifrs-visual-grammar/SKILL.md`) | Owns Concept Map / chapter visual. Add: north star (steps·flow·components); pointer to frozen #98 kit index; same/similar for same logic flow; MF page ↔ chapter kit-ID alignment; no invent vs #94. |
| **P0** | `ifrs-site-rules` (`…/ifrs-site-rules/SKILL.md`) | Map frame / iframe / B′ chrome / shared module locks. Add: embed reflow contract (#97) as architecture lock; Master formatting page path when live; kit classes only via shared map-box. |
| **P0** | `ifrs-teaching-body-qa` (`…/ifrs-teaching-body-qa/SKILL.md`) | Acceptance. Add FAIL checks: dialect drift (same role ≠ same/similar look across packs); unknown non-kit map class; empty content slot; MF specimen family mismatch. |
| **P1** | `ifrs-website-pm` (`…/ifrs-website-pm/SKILL.md`) | Pipeline. Note #98 page+skills same job; atlas freeze ≠ page done; 4-map study gate before page-scope freeze. |
| **P2** | `ifrs-team-protocol` (`…/ifrs-team-protocol/SKILL.md`) | One line: Master Design 2 owns kit index + MF page spec; skills patched in same job after Johnny GO. |
| **Out** | `ifrs-teaching-body` | Body prose / Illus — only if Johnny expands v1 beyond map kit. |
| **Out** | `VISUAL-TYPES.md` (repo) | Taxonomy twin — sync later via PM if grammar changes; not first skill edit. |

**Edit order after GO:** visual-grammar → site-rules → teaching-body-qa → PM/protocol one-liners. Point skills at `CONCEPT-MAP-BUILDING-BLOCKS-98.md` + this addendum; do not duplicate full kit tables into skills.


---

## 9. STEP 8 addendum — align MF page to signed Recognition + Timeline (2026-10-19 ~01:25 HKT)

**Mocks only.** No chapter rollout. No Build. No hardcoded sizes/colours. Atlas `CONCEPT-MAP-BUILDING-BLOCKS-98.md` stays **FROZEN** (cite only) — kit IDs 25/26/27 + junction noted as **controlled reopen** candidates after Johnny signs study/MF.

### 9.1 MF section → signed kit IDs

| MF section | Specimen | Kit IDs / pattern | Status |
|---|---|---|---|
| `mf-bg` | Solid `--bg` callout | **kit 2 STRUCK** (G6); colour/spacing **#14 #15** | existing |
| `mf-type` | T0–T3 + `--mchip` + gap strip | **#9** type · **#20** chip · **#15** spacing | existing tokens |
| `mf-rec` | Recognition pattern (min): criteria AND + fork LEFT; one rail row RIGHT | **#26** AND · **#27** rail-group · **junction** geometry (signed with Rec) · Flow/Mute **#10 #12** | controlled reopen vs atlas 1–23 |
| `mf-tl` | Timeline (min): During use = L1 `.inner-rail` over one kit 25 pane. Begins, Ceases, and markers on that axis. Span `span (Start→End)`. | **kit 25** shared timeline | **Q2=A punch:** no head sticker, no under-axis Begins/Ceases row. Second band under the axis = FAIL. |
| **`mf-master-revise`** (§10) | Left rail **building blocks** Dep-aligned: `.inner-rail` · kit 25 · nested `.inner-rail` layers | live `.inner-rail` · **kit 25** · visual-grammar Layers · atlas cite · `#27` When-not only | **SIGNED 2026-10-19 ~11:07 HKT** `deliverables/mf-master-revise/ba-mf-master-revise.png` · prior `mf-rail`/`mf-rail-v2` archive |
| `mf-kit-map` | Index note | cites frozen 1–23 + proposed 25/26/27 | — |

Recognition full signed layout (Rev d four sibling rail rows) lives at `step2-mocks/rec-layout/` (SIGNED). Timeline full package at `step2-mocks/timeline-final/` (SIGNED). MF page shows **min** specimens of those patterns for alignment, not a second dialect.

### 9.2 Tokens used (all existing — none new)

`--bg` `--surface` `--band` `--ink` `--muted` `--line` `--dash` `--accent` `--accent-soft` `--link-semantic` `--see-also` / `--see` `--warn` · `--stroke-1` `--stroke-2` · `--card-radius` `--radius-s` `--radius-pill` · `--space-1`…`--space-6` `--space-cell` `--space-hairline` · `--rail-bar-m` · `--t0-*` `--t1-*` `--t2-*` `--t2-band-*` `--t3-*` `--t3-strong-*` `--t3-arm-*` · `--mchip-*` · `--arrowhead` (via #91 shaft)

**New tokens proposed:** **none.** Junction / AND / rail-group / timeline leaders compose existing colour + stroke + space tokens.

### 9.3 Mock paths

| File | What |
|---|---|
| `row98-mocks/audit-98/mf-align/mf-align.html` | AFTER page wire |
| `…/before-mf.png` | BEFORE = frozen row98 `after-full-kit-1280.png` (field pitch era; no signed Rec/Timeline) |
| `…/after-mf.png` | AFTER night 1280 |
| `…/ba-mf-align.png` | Side-by-side |

**BA path:** `/workspace/style-base/row98-mocks/audit-98/mf-align/ba-mf-align.png`

### 9.4 Status

**§9 MF align SIGNED by Johnny 2026-10-19 ~01:42 HKT** (`ba-mf-align.png`). Do not Build. Do not edit chapter maps. Do not edit FROZEN atlas until controlled reopen is signed.

**§10 Left rail** = **SIGNED 2026-10-19 ~11:07 HKT** (`deliverables/mf-master-revise/ba-mf-master-revise.png`) — Dep-aligned `.inner-rail` family · kit 25 · nested layers. Prior `mf-rail/ba-mf-rail.png` (~07:02) **UNDER CHALLENGE / superseded**; `mf-rail-v2/` **superseded**. Prior A/B/C specimen approach stays **REJECTED**. §9 stamp unchanged. dep-v2 stays SIGNED freeze. Step 6 GB-MF10 **HOLD** until PM re-pack job card (do not replace golden PNG yet).

---

## 10. Left rail — building blocks / components (**SIGNED 2026-10-19 ~11:07 HKT**)

> **SIGNED by Johnny 2026-10-19 ~11:07 HKT (Asia/Shanghai) via PM 5.** Lock BA: `deliverables/mf-master-revise/ba-mf-master-revise.png` (+ twins `row98-mocks/audit-98/mf-master-revise/` · `map-master/row98-mocks/audit-98/mf-master-revise/`). Dep-aligned §10: `.inner-rail` family · kit 25 · nested `.inner-rail` layers. Freeze · **No Build**. Prior `mf-rail/ba-mf-rail.png` (~07:02) = **UNDER CHALLENGE / superseded**. `mf-rail-v2/` = **superseded**. Step 6 re-pack DONE ~11:12 HKT: GB-MF10 = `04-mf-master-revise.png` (= SIGNED `ba-mf-master-revise.png`). Old essence name retired. Pack **DRAFT-FOR-SIGN HOLD**. No Build.

**Status:** **SIGNED 2026-10-19 ~11:07 HKT** · BA `mf-master-revise/ba-mf-master-revise.png` · Dep-aligned component inventory locked. Prior A/B/C specimen approach stays **REJECTED**. MF align **§9 SIGNED** stamp stays. Atlas `CONCEPT-MAP-BUILDING-BLOCKS-98.md` stays **FROZEN** — cite Layers · **kit 25** · live `.inner-rail` (no atlas body edit). **`#27` thick-left** = When-not for Dep (IFRS 18 FS `.m-strip` / Rec mock-only). **dep-v2 SIGNED freeze** (do not reopen). Step 6 GB-MF10 HOLD (wait PM re-pack).

### 10.0 Signed components (Dep-verified · SoT)

| # | Building block | Chrome | When |
|---|---|---|---|
| 1 | Primary left label | live `.inner-rail` + `.rail-name` | Section / phase / group name beside detail |
| 2 | Phase + timeline | left = `.inner-rail`; right = **kit 25** | Phase name beside shared timeline |
| 3 | Nested layers | nested `.inner-rail` / wrap-row | Outer → board → inner → peers · **add layers, never fold** |

**Not Dep default:** `#27` `.rcell` + `--rail-bar-m` thick left accent (unify-A removed it from Dep).

**Archive history** (challenged / superseded — cite only):

**Johnny HARD REJECT (2026-10-19):** all prior MF §10 work that piled A/B/C **chapter specimens** (Rec prose rows · During-use teaching timeline · Useful-life Content paragraphs). Verdicts: 「唔覺得係 template」「根本冇抽過精髓」→ discard specimen approach. Restart = **essence master templates only**.

**Scope:** IAS 16 only. **Not** default for IAS 2 / IFRS 18 / CF. See `MF-LEFT-RAIL-GENERALIZE-98.md` (A).

**Why:** Master formatting must teach **reusable left-rail grammar** (Pattern · When · Chrome · Reusable min schematic), not dump chapter Content. Johnny: **add layers, never fold** (`ifrs-visual-grammar` § Layers & hierarchy + Rail-cell).

### 10.1 What “essence” means

Each template card on the MF §10 page has **exactly** four blocks (labels visible):

1. **Pattern name**
2. **When to use**
3. **Chrome recipe** — cite existing tokens only (#27 / kit 25 / Layers stack)
4. **Reusable min** — **abstract schematic only** (boxes labeled `Outer` / `Inner` / `Peer` / `Group` / `Phase` / `Start` / `End`). **No** IAS 16 teaching paragraphs.

**Forbidden on MF §10 page:** chapter Content dump · A/B/C specimen pile · folding nested rails into one column.

### 10.2 Logic (locked intent — plain)

1. Left rail lists **named groups / phase / outer section** under one parent beat.
2. **Select-one → show-that-group-only** (Group rail). Phase name **is** the left-rail label beside kit 25 (Phase + timeline). Nested depth = **add layers** Outer → board → inner → peers (Progressive nest).
3. Labels on live chapters stay Content-confirmed; MF templates use **abstract** labels so the page is a kit, not a second chapter.
4. Do **not** substitute a chapter spine list (Rec / Dep / Reval / Impair) for content-group rails **inside** a section.

### 10.3 Presentation — chrome cites (existing only)

**#27 mechanical chrome** (cite signed `step2-mocks/rec-layout/`):

| Token / structure | Value |
|---|---|
| Grid columns | `calc(4*var(--space-6))` \| `minmax(0,1fr)` · `gap: var(--space-cell)` · `align-items: stretch` |
| `.rcell` | `--band` · stroke-1 `--line` · `--card-radius` · pad `--space-2` · `border-left: var(--rail-bar-m) solid var(--accent)` · height 100% · label **T2 band** |
| Selected / mute | `.on` → `--accent-soft` · mute peers ~0.55 |
| Rail-cell | Separate bordered left-rail cell \| bordered content; gap ~7px; **never** wrap rail+content in one box |

**Layers stack** (cite `ifrs-visual-grammar` § Layers & hierarchy): Outer rail → board → inner rail|detail → peers/formula · parent covers children · max 2 bordered levels · named peers = stacked rail|detail · **add layers, never fold**.

**kit 25** (cite signed `timeline-final/`): rings ON axis · markers of this phase on that axis, inside the one L1 drawer (not a rail per marker) · one continuous span Start→End on the MF schematic (abstract span label). A second band under the axis fails (§10.10.3).

Full-height chapter `.rail-link` = separate chrome TBD Build — **not** #27.

### 10.4 When to use (pack)

**Pack scope:** **IAS 16 only** today. Other packs: fit-test later.

| Use… | Do **not** use when… |
|---|---|
| **Group rail (#27)** — named peer groups, select-one | Sequence/time → Flow (#10) / kit 25 |
| **Phase + timeline** — phase name as left rail; right = kit 25 | Map-wide constraint → Kit 1 side rail |
| **Progressive nest** — Outer→board→inner→peers | IAS 2 spines · IFRS 18 pillars · CF forks/formula |

### 10.5 MF page templates (`mf-rail`) — REJECTED vs NOW

| Prior (REJECTED) | Now (essence) |
|---|---|
| A Rec per-group with IAS 16 teaching prose | **Group rail (#27)** kit card — abstract Peer / content |
| B During use + Begins/Ceases teaching cards | **Phase + timeline** kit card — abstract Phase / Start / End / span |
| C Useful life Definition/Factors/Land paragraphs | **Progressive nest** kit card — abstract Outer / Inner / Group / Peer |

Page is **§10-focused kit** (no full MF encyclopedia dump on this BA). Night 1280. Solid `--bg`. **No new tokens.** Status **SIGNED by Johnny 2026-10-19 ~07:02 HKT**.

### 10.6 Mock paths

| File | What |
|---|---|
| `row98-mocks/audit-98/mf-rail/mf-rail.html` | §10 essence master-template kit page |
| `…/before-mf-rail.png` | BEFORE = signed MF align (no left-rail template kit) |
| `…/after-mf-rail.png` | AFTER night 1280 essence templates |
| `…/ba-mf-rail.png` | Before/after composite |
| `…/verify-mf-essence.png` | Full §10 templates crop |
| `…/TEMPLATE-ESSENCE-98.md` | 粵：Johnny reject + essence definition |
| `…/CHANGES-RAIL.txt` | Change log |

**BA path:** `/workspace/style-base/row98-mocks/audit-98/mf-rail/ba-mf-rail.png`

### 10.8a Archive — REOPEN v2 paths (superseded)

| File | What |
|---|---|
| `row98-mocks/audit-98/mf-rail-v2/mf-rail-v2.html` | §10 v2 component inventory (Decision strip + 3 cards) |
| `…/ba-mf-rail-v2.png` | Full-page AFTER DRAFT |
| `…/ba-mf-rail-v2-contrast.png` | Prior challenged vs v2 side-by-side |
| `…/verify-decision-strip.png` | Decision strip crop |
| `…/verify-three-templates.png` | Three component cards crop |
| `…/DUMP-VS-LOGIC-98.md` | Dump vs distilled |
| `…/MF10-REOPEN-98.md` | Job card (§0d first) |

**BA path (v2 DRAFT):** `/workspace/style-base/row98-mocks/audit-98/mf-rail-v2/ba-mf-rail-v2.png`



### 10.7 Tokens

Reuse §9.2 list only. **New tokens: none.** #27 / kit 25 / Layers remain cites vs frozen atlas 1–23.

### 10.8 Status (history → current)

| Stamp | BA | Verdict |
|---|---|---|
| ~07:02 HKT | `mf-rail/ba-mf-rail.png` | **UNDER CHALLENGE / superseded** (visual dump) |
| reopen DRAFT | `mf-rail-v2/ba-mf-rail-v2.png` | **superseded** (#27 encyclopedia ≠ Dep) |
| **~11:07 HKT** | **`mf-master-revise/ba-mf-master-revise.png`** | **SIGNED** · Dep-aligned `.inner-rail` · kit 25 · nest · freeze · No Build |

Scope **IAS 16** left-rail grammar on MF. Johnny: **add layers, never fold**. §9 untouched. dep-v2 **SIGNED freeze**. Step 6 GB-MF10 HOLD until PM re-pack.

### 10.9 Signed revise paths (`mf-master-revise`)

| File | What |
|---|---|
| `deliverables/mf-master-revise/mf-master-revise.html` | Full MF §9+§10 SIGNED page |
| `…/ba-mf-master-revise.png` | SIGNED BA (night 1280) |
| `…/SIGNED.txt` | Stamp ~11:07 HKT |
| `…/CHANGES.txt` · `WHAT-CHANGED-98.md` | Lock notes |
| twins | `row98-mocks/audit-98/mf-master-revise/` · `map-master/row98-mocks/audit-98/mf-master-revise/` |

**BA path (SIGNED SoT):** `/workspace/style-base/deliverables/mf-master-revise/ba-mf-master-revise.png`

**Apply 2026-10-19:** Johnny signed P0–P3. The PNG above stays the chrome lock and is not overwritten. Applied twins in this folder: `mf-master-revise.html` · `mf-sec10-gate.html`. Status of the applied page: **DRAFT-FOR-SIGN** (text is signed; the render is the check).

### 10.9a Principle — why left rail / nest（百子櫃）

**SIGNED** Johnny 2026-10-19 ~18:16 · applied on the MF page **above** §10.10.

讀 Concept Map 嘅 left rail，唔係貼紙名——係 **標準邏輯**：大格包細格。

想像 **百子櫃**。大 **櫃桶** 蓋住一排細櫃桶；每個細櫃桶再開一層更細嘅。讀者由 **top→bottom** 或者 **left→right** 讀：先見大櫃桶個名（left rail），再入去佢蓋住嘅內容。

- **L1** = 外層 left rail（一個 beat／phase／section 嘅外層名）。
- **L1 = some of L2**：L1 包住（加總）佢下面嘅 L2——L1 係 Σ 對應嘅 L2。
- **each L2 = sum of corresponding L3**：每個 L2 再拆開，等於佢下面嗰排 L3；**all those L3 = that L2**。
- 再入一層就係再加一個櫃桶，**唔摺**兩名落同一格。

| 視覺 | 對應等式 |
|---|---|
| Outer left rail 伸到蓋住成個 beat | L1 真係包住佢啲 L2 |
| 每個 named peer／nest row 有自己嘅 `.inner-rail` | 每個 L2／L3 有自己個櫃桶名 |
| Phase 名喺 left；右邊 kit 25 一條軸 Begins→Ceases | 一個 L1 phase 包住呢個 timeline pane |
| Outer → board → inner rail\|detail → peers | 大櫃桶 → 板 → 細櫃桶｜內容 → 同行 peer |

會破壞等式嘅做法（點解 §10.10 要量）：

1. **短 L1 stub** — 外層 rail 只得一行高，蓋唔到下面嘅 L2／beat → L1 ≠ Σ L2。
2. **缺 rail cell** — 右邊有 named beat，左邊空／冇格／摺兩名一格 → 少咗櫃桶，或者兩個櫃桶共用一個拉手。
3. **摺 nest** — 本應分層嘅 L2／L3 摺成一欄 → 讀者睇唔到「大包細」。

Phase + timeline 就係一個大櫃桶（phase 名 = L1 left rail）蓋住一個 kit 25 pane；pane 入面嘅事件屬呢個 phase，打喺同一條軸上——唔係第二個櫃桶橫插喺下面。

Principle 講「**點解**」。§10.10 講「**點量**」。

> Left rail is containment, not a sticker: a larger drawer (L1) covers the drawers it sums (L2); each of those sums its own L3. Short stubs, missing cells, and folded names break that sum. Phase + kit 25 is one L1 drawer over one timeline pane.

**Signed Q locks**

| Q | Lock |
|---|---|
| Q1 | 短 L1 stub = **FAIL** |
| Q2 = A | kit 25 markers sit **on** the axis **inside** the During-use L1 drawer. No per-marker L2 rail. A second band under the axis still **FAIL** |
| Q3 | Same-depth L2, same style. Exception = Johnny writes one sentence |

### 10.10 Gate — FAIL rules

**SIGNED** with P1. Full measure text: `MF-SEC10-FAIL-ADDENDUM-98.md`. On the page, under the decision strip and **after** §10.9a.

1. **Missing grid = FAIL** unless Johnny names the special logic in one sentence on that mock.
2. **Rail | detail ≤2px**, and the parent covers the children. Do not subtract padding.
3. **Markers on the kit 25 axis.** A second band under the axis = FAIL. Dep year-end review is rail 5.8 (chapter lock, not a ban on markers).
4. **Short L1 stub = FAIL.** L1 here is the outer left rail, not atlas `.m-l1`.

**P2 applied** on the Phase card: the lines “optional markers” and “no YE markers on signed lock” are replaced by the §10.10.3 sentences.

**P3 applied** on the §9 min: 「Year-end」→ `marker`; span → `span (Start→End)`; caption that a second band under the axis fails. Kit 25 geometry stays.

No new kit ID. No new token. `#27` When-not unchanged. PR #163 is not this job.
