# Opus handoff — IFRS 18 pack review (post-CF wave)

**Date:** 2026-10-02 (Asia/Shanghai / HKT)  
**From:** Johnny Pang via Grok Bot  
**Pack:** **IFRS 18 only** (CF 2018 is owned by the CF Opus wave — **do not edit any CF HTML**)  
**Pace:** **NO RUSH — quality over speed.** Paste-ready English brief.  
**Required runner:** Claude Opus **5.5 high**.  
**Execution note:** **Johnny runs Opus in Cursor; Grok prepares this brief and later reviews KEY CHANGES; Grok does not launch Opus.**

Companion files in this prep folder:

- `I18-DEBT-INVENTORY-2026-10-02.md` — honest pre-scan vs skills 2026.10.02b  
- `OPUS-KEY-REITERATIONS-IFRS18-2026-10-02.md` — checklist  
- Canonical skills snapshots (must match `/home/box/agent-data/workflows/…` at run time)  
- `CHROME-MODULE-DESIGN-2026-10-02.md`

Also mirrored under:  
`/workspace/ifrs-website/refs/ifrs-18/draft-v1-linked/OPUS-REVIEW-BRIEF-IFRS18-2026-10-02.md`

---

## 1. Locked product goals

1. **Ultimate study notes** — for a covered IFRS 18 topic, Johnny should not need to reopen Official / KPMG FI / EY Closer look PDFs.  
2. **Reader-friendly organising + visualisation** — big structural change OK when skills are followed; **do not invent** substance, examples, citations, source locators, or firm views.  
3. **Technically accurate IFRS 18 wording** — titles, Maps, tables, teaching cues: strict Standard language, not consultancy/marketing.  
4. **Preserve pack identity** — IFRS 18 stays separate from CF 2018 / IAS 2. Shared chrome standardises presentation only.

---

## 2. HARD — work order (mirrors CF gate pattern)

1. **Overall review first** — scan every live page: `index.html` (Map), `ch01.html`–`ch08.html`, navigated Ch3 companions (`visuals/ch03-mba-nest.html`, `visuals/ch03-classification-path.html`), `visuals/map-jumpboard.html`, `references.html`, pack CSS, shared CSS links. Short internal notes only. **No invent.**  
2. **Amend chapters in order** — Ch1 → Ch2 → Ch3 (incl. mba-nest / classification-path) → Ch4 → Ch5 → Ch6 → Ch7 → Ch8.  
3. **Enhance pack Map last among structure work** — `index.html` + jumpboard companion; story + visit path; **no** “Section chips follow…” lecture note.  
4. **Consistency pass** — reading order, cite grammar, Illus/section shape, Map/body consistency, multi-firm write-once, `.callout.differ` where firms truly differ, chrome locks, densify (never cut unique detail).  
5. **KEY CHANGES handoff to Grok** — write `OPUS-IFRS18-KEY-CHANGES-2026-10-02.md` in the pack folder.

### HARD prerequisite — shared CSS already landed

Grok already applied Phase 1+2 to IFRS 18 (`IFRS18-CHROME-PHASE12-2026-10-02.md`). Before starting, **re-verify** every live page links:

- `../../_shared/tokens.css`  
- `../../_shared/chrome.css`  
- `../../_shared/cite.css`  
- then pack `assets/shared.css` → `draft.css` (+ `map.css` on Map)

**If links missing/stale: STOP and report. Do not invent chrome/cite CSS or fork colours.**

---

## 3. HARD per-step stop gates (Johnny approval)

After **each** gate: desktop screenshots of the relevant page/Map/Illustration, update `OPUS-WORKING-MEMORY.md`, status report, ask **continue**, wait.

Gates:

1. Overall review  
2. Each chapter Ch1…Ch8 (Ch3 includes companions)  
3. Pack Map enhance  
4. Consistency pass  
5. KEY CHANGES handoff  

**Viewport HARD:** IFRS 18 is **desktop-only** this stage. No mobile/iPad screenshots or layout passes.

Do **not** start IFRS 18 until Johnny says the CF wave is finished / continue into I18. Do **not** edit CF files.

---

## 4. HARD — invent / wrong-shape (teaching-body 2026.10.02b)

| Class | Meaning | Fix |
|---|---|---|
| **Wrong-shape** | Illus (or Facts/Assessment strip) that is a plain firm paragraph, FAQ-without-case-facts, or Official restatement / reference matrix | Convert to teaching + Decision/Test/Assessment **or** section `h3`/`h4` + table/list. **Do not call invent.** Keep old ids. |
| **True invent** | Fake company, CU amounts, or case facts **not** in Official or pack Big4 | Remove; replace **only** with sourced content. |

**HARD:** Call invent **only** when facts/numbers/companies are absent from Official + pack Big4. Pure Official restatement = wrong-shape, never invent.

**Pre-scan highlight:** 9 matrices still titled `Illustration: … (section matrix — not an Illustration)` — finish demotion (see inventory).

FAQ ≠ Illustration. Reference matrices ≠ Illustration. Every true Illus = `.worked-strip` with **neutral** peers.

---

## 5. HARD — densify / duplication / differ

| Do | Do not |
|---|---|
| Keep Official + KPMG FI + EY Closer look substance | Densify-down / cut unique detail |
| Same point across firms → write once + chips for every supporting source | Invent chips for firms that do not support the point |
| Real firm/Official differences → table or side-by-side `.callout.differ`, closing “not reconciled” | Reconcile, silently choose, or invent a consensus |
| Cite every Official/firm source that supports the point | Put `§` in `.cite` chips |

**PwC:** not on disk for IFRS 18 — **no PwC invent**. DTT A4 = IAS 1 bridge only.

---

## 6. HARD — language / chrome / Map / cites

- Reader-facing logic: **Decision / Test / Assessment** — never “Gate” (including narrative “next gate” / “overview gate” where reader-facing).  
- Visible `Last update · YYYY-MM-DD HH:MM HKT`; disclaimer at **bottom** before footer-nav; **References after last chapter**.  
- No Map chip-order lecture note “Section chips follow…”.  
- Reading order: left→right, then top→bottom; story over section numbers; clear start→next→end.  
- Cite chips: Official `IFRS 18 · para …` / `Figure …`; EY `Closer look 2026 · section …` / `Ill …`; KPMG `FI 2024 · section …` / `Example …`. **No `§` in chips.**  
- **Ask Johnny before any cite rename** (short-form realignment, locator rewrite, chip house/work string changes). Repair of obvious broken/placeholder chips (e.g. `para B…`) still **ask first** with the proposed replacement locator from source — do not invent the locator.

---

## 7. Skills to follow (canonical — refresh at run)

| Skill / design | Path | Version at prep |
|---|---|---|
| IFRS teaching body | `/home/box/agent-data/workflows/ifrs-teaching-body/SKILL.md` | **2026.10.02b** |
| IFRS teaching body QA | `/home/box/agent-data/workflows/ifrs-teaching-body-qa/SKILL.md` | **2026.10.02b** |
| IFRS visual grammar | `/home/box/agent-data/workflows/ifrs-visual-grammar/SKILL.md` | **2026.10.02-23** |
| Chrome module design | `refs/_shared/CHROME-MODULE-DESIGN-2026-10-02.md` | 2026-10-02 |
| Shared assets | `refs/_shared/{tokens,chrome,cite}.css` | landed |

**Do not use stale copies from `/workspace/cf-opus-bundle/`** (those snapshots miss the 2026.10.02b invent/wrong-shape changelog). Prefer canonical workflows paths; prep-folder copies are convenience snapshots only.

Pack METHOD/NOTES/XREF are evidence; **canonical skills + this brief win** on drift.

---

## 8. Durable `OPUS-WORKING-MEMORY.md`

Create/update continuously in `refs/ifrs-18/draft-v1-linked/` at every gate:

- decisions, traps, blocked dependencies  
- demotions (wrong-shape vs invent)  
- Map visit paths + Illustration conventions  
- multi-firm write-once merges + any `.callout.differ`  
- shared-asset verification  
- desktop screenshot filenames  
- exact Johnny approvals  

---

## 9. Pack slots (filled 2026-10-02 HKT)

- **PACK:** IFRS 18  
- **PATH:** `/workspace/ifrs-website/refs/ifrs-18/draft-v1-linked/`  
- **CHAPTERS:** `ch01.html` What’s new vs IAS 1 → `ch02.html` PFS roles & aggregation → `ch03.html` P&L categories (+ `visuals/ch03-mba-nest.html`, `visuals/ch03-classification-path.html`) → `ch04.html` Totals & subtotals → `ch05.html` Operating expenses → `ch06.html` MPMs → `ch07.html` Other FS impacts → `ch08.html` Transition  
- **PACK MAP:** `index.html` + `visuals/map-jumpboard.html`  
- **INPUTS:**  
  - Official: `inputs/ifrs-18/official-hkfrs18-2026-06.pdf`  
  - KPMG: `inputs/ifrs-18/kpmg-first-impressions-ifrs18.pdf`  
  - EY: `inputs/ifrs-18/ey-2026-04-applying-ifrs-closer-look-ifrs18.pdf`  
  - DTT: `inputs/ifrs-18/dtt-2022-a4-presentation-fs-ias1.pdf` (IAS 1 bridge only)  
  - PwC: **absent** — no invent  
- **PACK EVIDENCE:** `IFRS18-CONTENT-REWRITE-METHOD.md`, `IFRS18-CH01…CH08-CONTENT-NOTES.md`, `I18-BIG-PASS-2026-10-01.md`, `IFRS18-CHROME-PHASE12-2026-10-02.md`, `I18-DEBT-INVENTORY-2026-10-02.md`

**Stop-gate sequence:** overall review → Ch1 → Ch2 → Ch3 (+companions) → Ch4 → Ch5 → Ch6 → Ch7 → Ch8 → pack Map → consistency → KEY CHANGES.

**Recommended start after overall review:** **Ch1** (gate order HARD). Highest residual debt density is **Ch3** (Gate narrative + most incomplete demotions + placeholder cite) — do not jump the queue unless Johnny explicitly reorders.

---

## 10. In scope / out of scope

### In scope

- Reorganise + visuals per skills; finish wrong-shape demotions; Gate→Decision/Test narrative cleanup; densify from on-disk Official/Big4; Map QA; desktop screenshots; working memory + KEY CHANGES.

### Out of scope

- Any CF 2018 HTML / CF visuals / CF NOTES edits  
- Launching additional agents / auto-continuing past gates  
- Mobile/iPad; typography Phase 3 Illus primitives; Documents sync  
- Inventing PwC, locators, examples, or firm consensus  
- Editing shared CSS during the Opus run  
- Cite rename without asking Johnny  

---

## 11. Acceptance criteria

- [ ] Shared Phase 1+2 links re-verified; STOP if broken  
- [ ] Wrong-shape vs invent classified separately; 9 matrix titles demoted or justified  
- [ ] No reader-facing Gate leftovers that should be Decision/Test/Assessment  
- [ ] True firm differences labelled `.callout.differ` (never reconciled); no invented diffs  
- [ ] Cite chips: no `§`; no placeholder locators; ask-before-rename honoured  
- [ ] Official + KPMG + EY substance retained; no densify-down  
- [ ] Maps: story LTR/TTB + visit path; no chip-order lecture note; desktop screenshots  
- [ ] `OPUS-WORKING-MEMORY.md` + KEY CHANGES complete  
- [ ] Zero CF files touched  

---

## 12. Reiterate (read twice)

1. Ultimate notes — site replaces PDF reopen for covered I18 topics.  
2. **No invent**; wrong-shape ≠ invent.  
3. **Do not cut detail.**  
4. Opus **5.5 high**; chapter gates + desktop screenshots; ask continue.  
5. **Desktop-only.**  
6. **Ask before cite rename.**  
7. **Do not edit CF.**  
8. Grok does not launch Opus.
