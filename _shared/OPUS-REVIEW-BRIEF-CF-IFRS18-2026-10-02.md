# Opus handoff — CF 2018 / IFRS 18 pack review, reorganise and visuals

**Date:** 2026-10-02 (Asia/Shanghai / HKT)  
**From:** Johnny Pang via Grok Bot  
**Pack slots:** CF 2018 and IFRS 18 (filled examples in Appendix A)  
**Pace:** **NO RUSH — quality over speed.** Paste-ready English brief.  
**Required runner:** Claude Opus 5.5, high effort (**Opus 5.5 high**).  
**Execution note:** Grok Bot launches Opus via Cursor CloudAgent when Johnny asks; Johnny may also run Opus in Cursor. Grok reviews KEY CHANGES after pull-back.

---

## 2. Locked product goals

1. **Ultimate study notes** — Johnny studies from the site alone; for a covered CF 2018 or IFRS 18 topic, he should not need to reopen the Official or Big4 PDFs.
2. **Reader-friendly organising + visualisation** — a major structural change is allowed when the canonical skills are followed; **do not invent** substance, examples, citations, source locators, or firm views.
3. **Technically accurate IFRS wording** — titles, subtitles, section labels, chapter-top Maps, pack Map labels, tables and teaching cues must use technically strict CF 2018 / IFRS 18 language, not consultancy, flowery or marketing language.
4. **Preserve pack identity** — CF 2018 and IFRS 18 remain separate packs. Shared chrome/assets standardise presentation only; they do not authorise copying one pack's content into the other.

---

## 3. HARD — Johnny's work order

Run **one pack at a time** using the same sequence below. Do not interleave chapters across packs. Use the actual chapter inventory in the selected `{PACK}` slot; the filled inventories are in Appendix A.

1. **Overall review first** — read/scan every page in the selected pack (index/Map, all chapter pages, any chapter-top or companion Maps/visuals, References/end matter, and relevant styles) before amending. Make short internal notes of issues and opportunities. Do not invent content.
2. **Amend chapters in order** — `{CHAPTERS}` in numeric order. Review/amend body, chapter-top Concept Map or companion visual, examples, citations and exit/next route as each chapter is reached. For IFRS 18, treat the `ch03-mba-nest` companion page as part of Ch3's gate unless the pack's current navigation makes it a separate chapter.
3. **Enhance the pack Map last among structure work** — improve `{PACK MAP}` only after chapter work, so it tells the cross-chapter story and sends the learner to the right next chapter.
4. **Consistency pass** — review every page again for reading order, cite grammar, technical titles, Illustration/working-strip shape, Map/body consistency, multi-firm write-once merges, shared chrome locks, References placement and densify (never cut unique detail).
5. **KEY CHANGES handoff to Grok** — write a report for each pack (suggested location: the selected pack folder, e.g. `OPUS-{PACK}-KEY-CHANGES-2026-10-02.md`) listing material structural, visual and content moves, unresolved risks, screenshots/checkpoints and files changed. Grok reviews the report and diffs for Johnny. Do not skip this report.

This sequence is HARD and does not replace any lock below.

### HARD prerequisite — shared CSS must already be landed

Before Opus starts a pack, Grok must already have applied **Phase 1 + Phase 2 shared CSS wiring** to that pack at the agreed C4/C6 checkpoint. That means the pack pages must actually link/use the shared assets, not merely have the files present in `refs/_shared/`.

Shared assets landed since the IAS 2 review are:

- `refs/_shared/chrome.css`
- `refs/_shared/tokens.css`
- `refs/_shared/cite.css`
- `refs/_shared/CHROME-MODULE-DESIGN-2026-10-02.md`
- this brief and its companion checklist

**If the required shared links are missing, stale, or not applied to the pack: STOP and report the dependency to Johnny. Do not invent chrome CSS, local token ownership, cite colours, or a workaround.** Opus must use the shared assets and must not fork pack-local chrome/cite colours.

## 4. HARD per-step stop gates (Johnny approval required)

After **each** step below, Opus MUST stop and send Johnny a status report. Every status report MUST include desktop screenshots showing the outcome (the relevant key page, chapter visual/Map, or Illustration changed or reviewed), plus the durable working-memory update described in §8. Opus MUST ask whether to continue and MUST NOT begin the next step until Johnny explicitly says **continue**.

For a selected pack, the gates are:

1. After the **overall review**.
2. After **each chapter in `{CHAPTERS}`**, in order.
3. After the **overall pack Map enhance**.
4. After the **consistency pass**.
5. With the **KEY CHANGES handoff to Grok** — send the report/status, screenshots and ask Johnny whether to continue.

A screenshot is mandatory at every gate, including review and handoff gates where no HTML changed. Use the most relevant desktop page/Map/Illustration outcome when a gate itself makes no HTML change. Do not proceed automatically from the last gate of CF 2018 into IFRS 18: start the next pack only after Johnny says continue.

**Viewport HARD:** CF 2018 and IFRS 18 are **desktop-only at this stage**. Do not take mobile/iPad screenshots and do not perform mobile/iPad layout passes. This differs from the IAS 2 brief.

---

## 5. HARD — detail / densify / duplication

| Do | Do not |
|---|---|
| Keep Official + pack Big4 **substance**, including unique examples, exceptions, numbers, definitions, application guidance and firm-specific views. | Cut detail or **densify down** merely to make pages look cleaner. |
| Big reorganise + visuals are OK when source-supported. | Invent facts, examples, decisions, source locators, gates, firm views or legal conclusions. |
| On multi-firm **overlap**: eliminate duplicate prose and keep **one dense teaching unit**. | Thin **unique** detail (numbers, tests, exceptions, differing firm views or pack-specific context). |
| Ensure cite chips for **every Official/firm source that supports that point**. | Inventlessly pile cite chips for firms or sources that do not support the material. |
| Where firms differ, preserve the difference in a labelled `.callout.differ` or separate row/bullet. | Reconcile, silently choose, or present distinct firm views as one invented consensus. |
| Use a table when the source-supported content is naturally comparative or has more than two meaningful columns. | Turn a reference matrix into an Illustration merely because it is visually useful. |

**Example:** if two firms say the same thing, write it once and cite both. If they differ, retain both views and label them. Thinning is allowed only to remove obvious overlapping duplicate prose; it must never shorten unique teaching content.

---

## 6. In scope / out of scope

- Tidy typesetting, hierarchy and sectioning; reorganise body HTML for scanability while preserving density.
- Review/enhance chapter-top Concept Maps, companion visuals and the pack Map using the IFRS visual grammar: story → learner visit path → logic-to-visual type.
- Add or repair visuals in main teaching content; use worked-strips for numeric or multi-Decision/Test/Assessment logic, with neutral peer examples.
- Check every teaching path **left to right, then top to bottom**. Every screen needs a clear **start → next → end**; story order wins over section-number order. Section-chip jumps are acceptable, but readers must not hunt, infer the route or reverse direction.
- Apply the shared chrome/tokens/cite assets already wired by Grok. Preserve pack-owned content, links, references and disclaimer wording.
- Merge genuinely duplicated multi-firm prose into one dense unit with all supporting cite chips; retain distinct views.
- Perform the consistency and QA review described below, and record decisions in durable working memory.

### Shared modulisation / chrome locks (NEW)

Since the IAS 2 review, Grok landed shared modulisation: `chrome.css`, `tokens.css`, `cite.css`, the design document `CHROME-MODULE-DESIGN-2026-10-02.md`, and this brief/checklist. Skills now lock:

- **Pack chrome:** visible `Last update · YYYY-MM-DD HH:MM HKT`; disclaimer at the bottom of page content immediately before footer navigation; **References after the last chapter**.
- **Map:** do **not** add the Map chip-order lecture note “Section chips follow…”.
- **Reading route:** left-to-right, then top-to-bottom; story over section numbers.
- **Teaching language:** reader-facing logic uses **Decision / Test / Assessment**, not “Gate”.
- **Assets:** use the shared module. Do not fork pack-local chrome or cite colours, and do not reinvent shared CSS.

If a shared asset needs a deliberate exception, report it and stop at the relevant gate rather than silently forking it.

---

### 6.1 Out of scope

- Starting before the Phase 1 + Phase 2 shared CSS links are applied to the selected pack; inventing or forking shared chrome, token or citation CSS.
- Typography modularisation, Phase 3 illustration primitives, or a whole-site rewrite.
- Mobile/iPad screenshots, responsive passes, or layout optimisation: desktop-only for both packs in this stage.
- Inventing Official links, source locators, examples, numbers, firm views, citations, disclaimer wording or cross-pack content.
- Cutting unique teaching detail to trade for chrome density; deleting supporting cite chips when collapsing overlap.
- Treating every FAQ, decision strip, teaching cue or reference matrix as an Illustration.
- Calling a reader-facing step a “Gate”; use Decision, Test or Assessment.
- Adding the Map lecture note “Section chips follow…”.
- Editing files outside the selected pack and its durable notes, except to consume already-landed shared assets. Do not edit shared CSS during the Opus run.
- Documents sync. This task does not require sync.

---

## 7. Skills to follow (canonical)

| Skill / design | Path | Owns |
|---|---|---|
| **IFRS teaching body** | `/home/box/agent-data/workflows/ifrs-teaching-body/SKILL.md` — v2026.10.02 | Body rewrite, cites, worked-strips, densify, titles, duplication and technical-strict labels. |
| **IFRS teaching body QA** | `/home/box/agent-data/workflows/ifrs-teaching-body-qa/SKILL.md` — v2026.10.02 | Mandatory structural, content, citation, hyperlink and visual QA before “done”. |
| **IFRS visual grammar** | `/home/box/agent-data/workflows/ifrs-visual-grammar/SKILL.md` — v2026.10.02-22 | Concept/pack Map method: story → visit path → draw; reading-order and visual selection. |
| **Shared chrome module design** | `/workspace/ifrs-website/refs/_shared/CHROME-MODULE-DESIGN-2026-10-02.md` | Shared chrome contract, update stamp, disclaimer/footer placement, References shell, asset/path/cache rules. |
| **Shared assets** | `/workspace/ifrs-website/refs/_shared/{chrome.css,tokens.css,cite.css}` | Use as landed; do not fork or replace with pack-local chrome/cite colours. |

Versions may be newer by the time of a run (for example, 2026.10.02+). Read the current canonical files before working. Pack-local METHOD / NOTES / XREF documents are evidence; canonical skills and this brief win if they drift.

---

## 8. Durable `OPUS-WORKING-MEMORY.md`

While helping, Opus MUST maintain durable pack notes, not only edit HTML. Create/update `OPUS-WORKING-MEMORY.md` in the selected pack folder continuously and **at every stop gate**. Update pack METHOD/NOTES/XREF documents only when appropriate and source-supported.

Record:

- decisions, recurring patterns, traps and blocked dependencies;
- chapter and Map visit paths, visual choices and Illustration/worked-strip conventions;
- multi-firm write-once merges, their supporting cite chips and any preserved differences;
- shared-asset verification (links, cache key, update stamp, disclaimer, footer and References order);
- desktop screenshots/checkpoint filenames and what each proves;
- exactly what Johnny approved at each gate.

Every gate status must identify the working-memory update. The next Opus/Grok run must be able to reuse this record without rediscovery.

---

## 9. Johnny locks Opus must honour

| Lock | Rule |
|---|---|
| **FAQ ≠ Illustration** | Classify content shape, not the source label. FAQ → Illustration only when it is a case study / Facts→Assessment worked unit. |
| **Illustration = case study** | Named case / worked entity / numeric / multi-Decision-Test-Assessment scenario → `Illustration: N.M.k` + `.worked-strip`; peer examples remain neutral. |
| **Reference matrices = section** | Include/exclude, component, classification or comparison matrices are `h3`/`h4` sections with lead + table/list + cites, not Illustrations. |
| **Multi-firm = cite tags** | Same point: write once + chips for every supporting source. Different views: preserve and label; do not reconcile. |
| **Technical-strict titles** | CF 2018 / IFRS 18 wording only; no consultancy/flowery/marketing labels. |
| **Illustrations may include diagrams** | Add a diagram/mini-flow/table when complexity warrants it; keep worked-strip peers neutral. |
| **Maps** | Check/enhance chapter-top/companion Maps and the pack Map against visual grammar; Map must flow across chapters. |
| **Reading order** | Left→right, top→bottom; start→next→end; story before section numbers. |
| **Chrome** | Shared assets only; visible HKT update, bottom disclaimer, footer navigation and References after the final chapter. |
| **No Map lecture note** | Do not add “Section chips follow…” or similar chip-order instruction. |
| **No invent** | Structure/visuals may change; substance must come from the Official and the pack's supported sources. |
| **No densify-down** | Remove only overlapping duplicate prose; preserve unique detail. |

### 9.1 NEW — modulisation / shared assets

Since the IAS 2 review, Grok landed shared modulisation: `refs/_shared/chrome.css`, `tokens.css`, `cite.css`, the design MD `CHROME-MODULE-DESIGN-2026-10-02.md`, this brief and the companion checklist. Opus must use the assets already wired by Grok, not fork pack-local chrome/cite colours or reinvent shared CSS.

The shared locks are: visible `Last update · YYYY-MM-DD HH:MM HKT`; disclaimer at the bottom of page content immediately before footer navigation; **References after the last chapter**; left-to-right/top-to-bottom reading order; story over section numbers; no Map chip-order lecture note “Section chips follow…”; and reader-facing **Decision / Test / Assessment** language instead of “Gate”. If wiring is missing or a deliberate exception is needed, stop and report it rather than silently changing the module contract.

### 9.2 Short-form cite alignment example

When a pack contains the relevant works, prefer the established short-form pattern from IAS 2: `PwC MOA 2020 Ch25 · …`, `DTT iGAAP 2022 A11 · …`, `EY iGAAP 2026 Ch23 · …`, `KPMG Insights 2019/20 · Part 1 · 3.8`. This is an **alignment example**, not permission to invent a CF 2018 or IFRS 18 locator. Use the actual pack-local work and locator only when supported by the source and METHOD/NOTES. No `§` in cite chips.

---

## 10. Source paths (box) — placeholders for a reusable run

Fill these slots before pasting/running the brief:

- **Pack:** `{PACK}`
- **Draft path:** `{PATH}`
- **Chapters in actual order:** `{CHAPTERS}`
- **Pack Map / index:** `{PACK MAP}`
- **Inputs / source inventory:** `{INPUTS}`

Use the selected pack's actual filenames, not assumed IAS 2 names. Preserve the distinction between root navigation aliases (`ch01.html`) and any pack-owned visual/companion files.

| Layer | Work | Path |
|---|---|---|
| Official | Pack's controlling Official / adopted text | `{INPUTS}` |
| Big4 / other | Pack-supported firm and teaching sources | `{INPUTS}` |
| Pack evidence | METHOD / NOTES / XREF / local skills | `{PATH}` |

Cite chips must use the pack's actual source grammar, with no invented locator and no `§` in `.cite`.

---

## 11. Acceptance criteria

- [ ] Shared Phase 1 + Phase 2 links are verified before work; missing links caused a STOP, not an invented CSS fix.
- [ ] Official + all supported pack Big4 substance retained; unique detail intact; no densify-down.
- [ ] Multi-firm overlap: one dense unit + cite chips for every supporting source; distinct views remain distinct and labelled.
- [ ] FAQ ≠ Illustration; case-study/numeric/multi-Decision-Test-Assessment units use worked-strips; peers neutral; reference matrices remain sections.
- [ ] Titles, subtitles, section labels and Map labels are technically strict.
- [ ] Complex teaching units have an appropriate diagram/mini-flow/table where warranted and source-supported.
- [ ] Every page reads left→right and top→bottom with a clear start → next → end; story order works even where section chips jump.
- [ ] Chapter-top/companion Maps and pack Map checked/enhanced against visual grammar; pack Map flows across chapters.
- [ ] No reader-facing “Gate” language and no “Section chips follow…” Map lecture note.
- [ ] Shared chrome is used: visible HKT update, bottom disclaimer, footer navigation, and References after the last chapter.
- [ ] Desktop-only checkpoints are attached to working memory; no mobile/iPad pass was performed.
- [ ] Cite grammar, hyperlink QA, title essence, visual grammar and densify QA are green under the current canonical skills.
- [ ] `OPUS-WORKING-MEMORY.md`, METHOD/NOTES/XREF as needed, and the per-pack KEY CHANGES report are complete.
- [ ] No invent; unresolved risks and blocked dependencies are explicit.

---

## 12. Reiterate (read twice)

1. **Ultimate notes** — the site should replace reopening source PDFs for covered CF 2018 / IFRS 18 topics.
2. **Do NOT cut detail / densify down** — only eliminate overlapping duplicate prose; retain unique detail and supporting cite chips.
3. **Big reorganise + visuals OK; no invent.**
4. **Shared CSS prerequisite is hard** — if Phase 1 + 2 links are not already applied, STOP; do not invent chrome CSS or cite colours.
5. **Desktop-only** — no mobile/iPad screenshots or layout pass for CF 2018 or IFRS 18 at this stage.
6. **Use shared assets** — preserve HKT update, bottom disclaimer, References after the last chapter, story-over-section-numbers, and Decision/Test/Assessment language; never add the Map chip-order lecture note.
7. Follow teaching-body + QA + visual-grammar + chrome-module design without contradiction.
8. Stop after every gate, show screenshots, update working memory, and ask Johnny to continue.

Also see: `OPUS-KEY-REITERATIONS-CF-IFRS18-2026-10-02.md` and `CHROME-MODULE-DESIGN-2026-10-02.md`.

---

# Appendix A — filled pack examples

These examples were filled from the current box inventory on 2026-10-02 (HKT). Re-list before a future run; do not assume filenames or chapter counts remain unchanged.

## A1. CF 2018

- **PACK:** `CF 2018`
- **PATH:** `refs/cf-2018/draft-v1-linked/`
- **CHAPTERS:** `ch01.html` → Objective & users; `ch02.html` → Qualitative characteristics; `ch03.html` → Reporting entity; `ch04.html` → Elements; `ch05.html` → Recognition & derecognition; `ch06.html` → Measurement; `ch07.html` → Presentation & disclosure; `ch08.html` → Concepts of capital; `ch09.html` → Combined financial statements; `ch10.html` → Carve-out financial statements; `ch11.html` → Status & use with Standards.
- **PACK MAP:** `index.html` (Map; current concept map/story board). Also inspect `visuals/` and any chapter-linked visual pages actually used by the pack.
- **INPUTS:**
  - Official CF 2018: `inputs/cf-2018/official-conceptual-framework-2026.pdf` (plus the pack's documented HTML/HK archive where cited).
  - DTT: `inputs/cf-2018/dtt-2022-conceptual-framework-moa.pdf` (A2).
  - PwC: `inputs/pwc-2020-moa/01-conceptual-framework-intro.pdf`; `inputs/pwc-2020-moa/appendix-2-combined-carve-out.pdf`.
  - EY: `inputs/ey-international-gaap-2026/International-GAAP-2026-part1.pdf` (pack notes identify the relevant book pages/chapter; do not invent a locator).
  - KPMG: `inputs/kpmg-2019-2020/part1-non-fi.pdf` (1.2); supporting public material only where listed in METHOD, including `inputs/cf-2018/kpmg-public/`.
  - Visit-path-only note: `inputs/cf-2018/acca/ACCA-SBR-CF-storyline-NOTE.md` — not cite authority.
- **PACK EVIDENCE:** `CF-CONTENT-REWRITE-METHOD.md`, `CF-XREF-OFFICIAL-TO-BIG4-2026-10-01.md`, `CF-XREF-BIG4-TO-OFFICIAL-2026-10-01.md`, chapter `CF-CHxx-CONTENT-NOTES.md` and any applicable local skill/amend notes.

**CF stop-gate sequence:** overall review → Ch1 → Ch2 → Ch3 → Ch4 → Ch5 → Ch6 → Ch7 → Ch8 → Ch9 → Ch10 → Ch11 → pack Map → consistency → KEY CHANGES; stop after every item and ask Johnny to continue.

## A2. IFRS 18

- **PACK:** `IFRS 18`
- **PATH:** `refs/ifrs-18/draft-v1-linked/`
- **CHAPTERS:** `ch01.html` → What's new vs IAS 1; `ch02.html` → PFS roles & aggregation; `ch03.html` → P&L categories (with companion `visuals/ch03-mba-nest.html` and `visuals/ch03-classification-path.html` where navigated); `ch04.html` → Totals & subtotals; `ch05.html` → Operating expenses; `ch06.html` → MPMs; `ch07.html` → Other FS impacts; `ch08.html` → Transition.
- **PACK MAP:** `index.html` (Map) and the pack-owned `visuals/map-jumpboard.html` companion where used. Review both, but do not duplicate their story or add the forbidden chip-order lecture note.
- **INPUTS:**
  - Official HKFRS 18 (= IFRS 18 on site): `inputs/ifrs-18/official-hkfrs18-2026-06.pdf`.
  - KPMG: `inputs/ifrs-18/kpmg-first-impressions-ifrs18.pdf`.
  - EY: `inputs/ifrs-18/ey-2026-04-applying-ifrs-closer-look-ifrs18.pdf`.
  - DTT: `inputs/ifrs-18/dtt-2022-a4-presentation-fs-ias1.pdf` — IAS 1 bridge only.
  - PwC: not on disk for IFRS 18; **do not invent PwC content or cites**.
- **PACK EVIDENCE:** `IFRS18-CONTENT-REWRITE-METHOD.md`, `IFRS18-CH01-CONTENT-NOTES.md` through `IFRS18-CH08-CONTENT-NOTES.md`, `I18-BIG-PASS-2026-10-01.md` and any applicable local notes.

**IFRS 18 stop-gate sequence:** overall review → Ch1 → Ch2 → Ch3 (including any navigated MBA-nest/classification companion) → Ch4 → Ch5 → Ch6 → Ch7 → Ch8 → pack Map → consistency → KEY CHANGES; stop after every item and ask Johnny to continue.

## Appendix source rule

The examples above identify files currently documented on disk; they do not authorise new citations. If a source, link, chapter or visual is absent at run time, record the gap in working memory and stop/report rather than inventing it.
