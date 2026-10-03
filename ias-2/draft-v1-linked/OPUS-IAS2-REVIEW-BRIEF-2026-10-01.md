# Opus handoff — IAS 2 pack review / reorganise / visuals

**Date:** 2026-10-01 (Asia/Shanghai)  
**From:** Johnny Pang (PM via Grok Bot)  
**Pack:** `refs/ias-2/draft-v1-linked/`  
**Pace:** NO RUSH — quality over speed. Paste-ready English brief.
**Required runner:** Claude Opus 5.5, high effort (**Opus 5.5 high**).
**Execution note:** Johnny runs Opus himself in Cursor. Grok only prepares this paste-ready brief and later reviews the KEY CHANGES handoff; Grok does not launch Opus.

---

## 1. Locked product goals

1. **Ultimate study notes** — Johnny studies from the site alone; **no need to reopen** Official + Big4 PDFs for the same IAS 2 topic.
2. **Reader-friendly organising + visualization** — big structural change OK if skills followed; **no invent**.
3. **Technically accurate IFRS wording** on all titles / subtitles / section labels / Map node labels — **not** consultancy / flowery / marketing language.

---

## 2. HARD — Johnny's work order (2026-10-01 evening)

**Required runner:** Claude Opus 5.5, high effort (**Opus 5.5 high**).

Opus MUST follow this order:

1. **Overall review first** — read/scan **all IAS 2 pages in the pack** (index + `ch01`–`ch06` + chapter Maps + pack Map + styles as needed) before amending. Produce short internal notes of issues/opportunities; do not invent content.
2. **Amend chapters in order** — Ch1 → Ch2 → Ch3 → Ch4 → Ch5 → Ch6 (body + chapter-top Concept Maps as you go, still following skills).
3. **Overall Map last among structure work** — enhance the pack Map tab (`visuals/map-formula-board.html` / index Map) so it flows across chapters **after chapter work**.
4. **Consistency pass** — review **all pages again** for cite grammar, titles, Illus shape, Map/body consistency, multi-firm write-once, and densify (no cut unique detail).
5. **Handoff to Grok Bot (IFRS Website PM)** — at the end, write a **KEY CHANGES** report (suggested file: `OPUS-IAS2-KEY-CHANGES-2026-10-01.md` in this pack folder) listing material structural/visual/content moves. Grok will review that report + diffs and flag anything that does not seem right to Johnny; Opus must not skip this report.

This sequence is HARD and does not replace any existing lock below; it is the required order of operations.


### HARD per-step stop gates (Johnny approval required)

After **each** step below, Opus MUST stop and send Johnny a status report. Every status report MUST include screenshots showing the outcome (the relevant key page, Concept/pack Map, and/or Illustration changed or reviewed), plus the durable working-memory update described below. Opus MUST ask whether to continue and MUST NOT begin the next step until Johnny explicitly says **continue**.

1. After the **overall review**.
2. After **Ch1**.
3. After **Ch2**.
4. After **Ch3**.
5. After **Ch4**.
6. After **Ch5**.
7. After **Ch6**.
8. After the **overall Map enhance**.
9. After the **consistency pass**.
10. With the **KEY CHANGES handoff to Grok** (send the report/status, screenshots, and ask Johnny whether to continue; do not proceed beyond the handoff without approval).

These are hard stop gates in addition to the work order above. A screenshot is required at every gate, including the review and handoff gates; use the most relevant key page, Map, or Illustration outcome when a gate itself makes no HTML change.

---

## 3. HARD — detail / densify / duplication (Johnny 2026-10-01)

| Do | Do not |
|----|--------|
| Keep Official + pack Big4 **substance** | Cut detail or **densify down** to make pages look cleaner |
| Big reorganise + visuals OK | Invent facts, gates, or firm views |
| On multi-firm **overlap**: eliminate **duplicate prose**; keep **one dense teaching unit** | Thin **unique** detail (numbers, gates, exceptions, firm-specific views) |
| **Ensure** cite chips for **every firm/Official that supports that point** | Inventlessly pile cite chips for firms that do **not** support the material |
| **Example:** PwC and EY say the same thing → **write once** + cite chips for **both** (`PwC MOA 2020 Ch25 · …` + `EY iGAAP 2026 Ch23 · …`). Same for any multi-firm (or Official+firm) overlap | Write the same FAQ/example once per firm with identical prose |

**Thinning allowed only to eliminate obvious overlapping duplicate prose — never to shorten unique teaching content.**

---

## 4. In scope (Opus may)

- Tidy typesetting / sectioning (add or collapse sections when it makes sense).
- Check **chapter-top Concept Maps** (`visuals/ch01-scope.html` … `ch06-disclosure.html`) against [IFRS visual grammar](sand-workflow:ifrs-visual-grammar) (story + learner visit path + logic→type).
- Add visuals in **main teaching content**; for **Illustrations**, add diagrams / mini-flows / tables when complex (many Illus currently have **zero** diagram — open debt when complexity warrants).
- Enhance **overall Map tab** (`index.html` → `visuals/map-formula-board.html`) so it **flows across chapters** (jump board), not only a single formula iframe.
- Reorganise body HTML for scanability while preserving density (skills below).
- Use Johnny rough visuals as **layout hints only** (fix wording to IAS 2 technical language).

### Map unlock note

Concept Map / pack Map were **previously parked** during body densify. **Johnny now unlocks Map enhance for Opus on IAS 2** — chapter-top Maps + pack Map tab. Follow visual-grammar. Other packs stay parked.

---

## 5. Out of scope

- Inventing entity fact patterns, Official links, or firm views not in pack sources.
- Mass-applying IAS 2 cite/Illus grammar to CF 2018 (WAIT). IFRS 18 skill-MD rollout is unlocked for Grok as a parallel job when Opus starts IAS 2; Opus stays on IAS 2 and must not do the IFRS 18 rollout.
- Trading densify for chrome; deleting supporting cite chips when collapsing overlap.
- Applying Map leaf green/red to Illustration worked-strip peers (Illus peers stay **all neutral**).
- Large verbatim reprint of copyrighted Big4/EY prose (paraphrase + cite; personal-study unlock already covers EY FS Practical examples).
- LOCK-STAMP / whole-site rewrite / inventing iframe-fit behaviour.

---

## 6. Skills to follow (canonical)

| Skill | Path | Owns |
|-------|------|------|
| **IFRS teaching body** | `/home/box/agent-data/workflows/ifrs-teaching-body/SKILL.md` | Body rewrite, cites, Illus=worked-strip, densify, titles, duplication, technical-strict labels |
| **IFRS teaching body QA** | `/home/box/agent-data/workflows/ifrs-teaching-body-qa/SKILL.md` | Mandatory gate before “done” / sync |
| **IFRS visual grammar** | `/home/box/agent-data/workflows/ifrs-visual-grammar/SKILL.md` v2026.10.01-18 | Concept Map / pack Map method (story → visit path → draw) |

Pack METHOD / NOTES / XREF are pack-local evidence; **skills win** on HARD locks if METHOD drifts.


### HARD — durable working memory (not HTML-only)

While helping, Opus MUST maintain durable pack notes, not only edit HTML. Create/update `OPUS-WORKING-MEMORY.md` in this pack folder continuously and **at every stop gate** (and update METHOD/NOTES as needed). Record decisions, recurring patterns, traps, Map/Illustration conventions, multi-firm write-once merges and their supporting cite chips, and exactly what Johnny approved. The next Opus/Grok run must be able to reuse this record without rediscovery. The gate status report must identify the working-memory update.

---

## 7. Johnny locks Opus must honour

| Lock | Rule |
|------|------|
| **FAQ ≠ Illus** | Classify **content shape**, not the source label. FAQ → Illus **only** if case study / Facts→Assessment. |
| **Illus = case study** | Named case / worked entity / numeric / multi-gate scenario → `Illustration: N.M.k` + `.worked-strip` (neutral peers). |
| **Reference matrices = section** | Include/exclude / cost-component / classification tables → section `h3`/`h4` + lead + `<table>`/`<ul>` + cites — **not** Illus. |
| **Multi-firm = cite tags** | Same point → write once + chips for every supporting firm (PwC+EY example). |
| **Technical-strict titles** | IFRS/IAS wording only — no consultancy/flowery/marketing. |
| **Illus may include diagrams** | When complex; peers stay neutral. |
| **Chapter-top Map + pack Map** | Unlocked for this handoff; visual-grammar. |
| **No invent** | Structure/visuals may change; substance must come from Official + pack Big4. |
| **No densify-down** | See §2. |

---

## 8. Source paths (box)

**Draft pack:** `/workspace/ifrs-website/refs/ias-2/draft-v1-linked/`

| Layer | Work | Path |
|-------|------|------|
| Official | HKAS 2 / IAS 2 | `inputs/hkas/hkas-2-inventories.pdf` |
| PwC | MOA 2020 Ch25 | `inputs/pwc-2020-moa/chapters/25-ias2-inventories.pdf` |
| DTT | A11 2022 | `inputs/dtt-moa-2022-june21/dtt-2022-a11.pdf` |
| EY | IGAAP 2026 Ch23 | `inputs/ey-international-gaap-2026/` (part1/part2) |
| KPMG | Insights 2019/20 · 3.8 | `inputs/kpmg-2019-2020/part1-non-fi.pdf` |

**Chapters:** `ch01.html` … `ch06.html`, `index.html` (Map tab).  
**Chapter Maps:** `visuals/ch01-scope.html` … `ch06-disclosure.html`, `visuals/map-formula-board.html`.  
**METHOD / XREF / NOTES:** `IAS2-CONTENT-REWRITE-METHOD.md`, `IAS2-XREF-*.md`, `IAS2-CH0N-CONTENT-NOTES.md`, preflight + completeness docs in same folder.

Cite chip grammar: Official `IAS 2 · para …`; Big4 = firm + work + locator; **no `§`** in `.cite`; EY chip = `EY iGAAP 2026 Ch23 · …`.

---

## 9. Johnny rough visuals (layout hints — wording inaccurate)

Archived at:

`refs/ias-2/draft-v1-linked/visuals/johnny-rough/`

| File | Intent (layout only) | Opus must |
|------|----------------------|-----------|
| `scope-definition-flow-rough.png` | Scope / definition → exclusions → IAS 2 inventory → measurement branches | Replace “Bla” / incomplete “Lower of cost…” / “blablbal” with **IAS 2 technical wording** (definition para 6; scope exclusions; lower of cost and NRV; measurement carve-outs only if in Standard/pack) |
| `cost-components-matrix-rough.png` | Cost components vs not in cost | Replace A/B/C / “…” placeholders with Official cost-of-purchase / conversion / other costs and para 16 exclusions — **technical-strict**; this shape is a **section matrix**, not an Illus |

Rough PNGs are **not** final art and **not** authority for wording.

---

## 10. Acceptance criteria

- [ ] Official + all pack Big4 substance retained (no densify-down); unique detail intact.
- [ ] Multi-firm overlap: one dense unit + cite chips for every supporting firm (PwC+EY pattern); no invent-piled chips; no dropped supporting source.
- [ ] FAQ ≠ Illus; Illus = case study worked-strips (neutral peers); reference matrices = sections.
- [ ] Titles / Map labels = technical-strict IFRS wording.
- [ ] Complex Illus: diagram / mini-flow / table added where warranted (not left prose-only without NOTES reason).
- [ ] Chapter-top Maps checked/enhanced vs visual-grammar (story + visit path).
- [ ] Pack Map tab enhanced to flow across chapters.
- [ ] Johnny rough wording fixed to IAS 2 technical language wherever used.
- [ ] Cite grammar + densify quant + title essence + hyperlink QA green ([IFRS teaching body QA](sand-workflow:ifrs-teaching-body-qa)).
- [ ] No invent; NOTES/METHOD updated for material moves.

---

## 11. Reiterate (read twice)

1. **Ultimate notes** — replace PDF reopen.  
2. **Do NOT cut detail / densify down** — only eliminate overlapping duplicate prose; ensure supporting cite tags present (PwC+EY write-once example).  
3. **Big reorganise + visuals OK; no invent.**  
4. **Map unlocked** for IAS 2 Opus (was parked).  
5. **Technical-strict titles** — IFRS wording only.  
6. Follow teaching-body + QA + visual-grammar without contradiction.

Also see: `OPUS-KEY-REITERATIONS.md` (checklist) and `OPUS-SKILLS-PATCH-NOTE-2026-10-01.md` (skill contradictions fixed this handoff).
