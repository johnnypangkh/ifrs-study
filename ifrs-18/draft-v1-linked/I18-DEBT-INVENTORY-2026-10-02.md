# IFRS 18 — honest debt inventory vs skills 2026.10.02b

**Date:** 2026-10-02 ~09:39 HKT  
**Scanner:** Grok (prep only; no Opus launch; no CF HTML edits)  
**Live pack:** `/workspace/ifrs-website/refs/ifrs-18/draft-v1-linked/`  
**Skills baseline:** teaching-body / teaching-body-qa **2026.10.02b**; visual-grammar **2026.10.02-23**  
**Chrome:** Phase 1+2 already landed (`IFRS18-CHROME-PHASE12-2026-10-02.md`); shared links present; Last update `2026-10-02 01:48 HKT`; cache `ifrs18-chrome-phase2-20261002f`

Documents mirror note: laptop `2a06a250-7384-4878-8b5c-ffbf4a1f68e5` → `C:\Users\johnny\Documents\ifrs-website-refs\refs\ifrs-18\` (sync deferred in Big Pass / chrome notes). Box live pack is the source of truth for this prep.

---

## Scorecard (honest — no invent)

| Debt class | Finding | Severity |
|---|---|---|
| **True invent Illus** | No clear fake company/CU/case facts found. Named entities (XYZ, AA–FF Groups, Entity R/U/X/A/E/Q/C/G/I) carry Official IE or EY Ill cites where checked. | **Low** — keep scanning; do not label Official restatement as invent |
| **Wrong-shape Illus** | **9 incomplete demotions** still titled `Illustration: …` with italic `(section matrix — not an Illustration)` — title shape contradicts demotion. | **High** |
| **Gate leftover wording** | UI `.box-title` / `<th>` Gate = **0**. Narrative `gate` leftovers concentrated in **Ch3 (12 hits)**: “next gate”, “overview gate”, “at that gate”, “gate labels”. Chrome Phase12’s older First/Second/Third counts appear cleared outside Ch3. | **Med** (Ch3) |
| **`.callout.differ` / never-reconcile** | **Zero** `.callout.differ` in live chapters. Multi-firm write-once chips exist; no labelled sources-differ plates found. | **Med** — verify real firm diffs before inventing callouts |
| **Cite `§`** | **Zero `§` inside `.cite` chips** (PASS). Body prose still heavy on `§` (Ch3≈160, Ch6≈91, Ch4≈70, Ch5≈48) — optional later `para` pass per Big Pass. | Chip: **PASS** / Body: optional |
| **Broken / placeholder cite** | Ch3 Entity C box: `IFRS 18 · para B… returns test` — truncated locator. | **High** (cite integrity) |
| **Map reading-order** | Visit spine Ch1→Ch8 present on `index.html` + `visuals/map-jumpboard.html`. **No** “Section chips follow…” lecture note. Pillar row LTR = Structured P&L (3/4) → Grouping (2) → MPM (6) while visit path is numeric 1→8 — dual route; Opus must confirm story-first LTR/TTB without forcing section-number order. Chapter-top iframes present (Ch3 also mba-nest + classification-path). | **Med** (review, don’t invent rewrite) |
| **Missing densify** | Crosswalk A/B locator tables still **open** (blocking pack-complete only). Explicit thin bridges remain (Ch1 carry/IAS1; Ch2 offsetting; Ch3 FX overview; Ch4/6 OPDAI; Ch7 banks/insurers SCF + capital sticky; Ch8 optional election). CONTENT-NOTES dated 2026-09-30 — may lag Big Pass/chrome. | **Med–High** for completeness claim; many “thin” labels are intentional bridges |
| **Illus peers `.ok`/`.warn`** | No Illus peer colour hits in automated strip scan. | **PASS** (spot) |
| **Shared CSS prerequisite** | Wired on Map + chapters + References. | **PASS** — Opus must re-verify before start |

### Incomplete demotions (wrong-shape title residue) — exact list

1. Illus 1.5.1 — IE pack map (Ch1)  
2. Illus 2.4.1 — Informative labels / Fig 7 (Ch2)  
3. Illus 3.1.1 — Categories without specified MBA / Fig 2 (Ch3)  
4. Illus 3.4.1 — Hybrid host liabilities / Fig 4 (Ch3)  
5. Illus 3.5.1 — Investing MBA / Fig 3.1 (Ch3)  
6. Illus 3.5.2 — Financing-to-customers MBA / Fig 3.2 (Ch3)  
7. Illus 3.5.3 — Cash & CE with specified MBA / Fig 3.3 (Ch3)  
8. Illus 3.4.2 — Derivatives gains/losses / Fig 5 (Ch3)  
9. Illus 6.1.1 — Identifying MPMs / Fig 6 (Ch6)  

**Fix shape (skill):** convert to `h3`/`h4` section + lead + table/list + cites; **keep old ids**; do **not** call this invent. Drop `Illustration:` from the title.

### Case-study Illus kept (24) — Big Pass list, still live

2.1.1, 2.1.2, 2.3.1 · 3.5.4, 3.5.5, 3.8.1–3.8.4 · 4.1.1, 4.2.1, 4.5.1 · 5.1.1, 5.1.2, 5.2.1, 5.3.1 · 6.4.1, 6.4.2 · 7.1.1, 7.2.1, 7.3.1, 7.5.1, 7.5.2 · 8.4.1  

Opus must re-classify any that are plain firm para / Official restatement without case facts as **wrong-shape**, not invent.

---

## Top gaps for Opus wave (priority)

1. Finish demotion of **9** matrix titles still branded `Illustration:`.  
2. Repair Ch3 placeholder cite `para B… returns test` (ask Johnny before cite rename / locator invent).  
3. Ch3 Gate narrative → Decision/Test/Assessment language (reader-facing).  
4. Audit multi-firm points for true differences → `.callout.differ` (never reconcile); do not invent diffs.  
5. Map dual-route QA: pillar story LTR vs Ch1–Ch8 visit spine; desktop screenshots.  
6. Crosswalk A/B + intentional-thin vs missing-densify decisions (document in working memory).  
7. Refresh CONTENT-NOTES after chapter gates (NOTES currently pre-date chrome + skill 02b).

## Intentionally out of this inventory

- CF 2018 HTML (owned by CF Opus wave — do not edit).  
- Mobile/iPad layout.  
- Documents sync.  
- Launching Opus.
