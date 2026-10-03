# IFRS 18 — IAS 2 trial skill grammar rollout (2026-10-01 Asia/Shanghai)

**Owner:** Content implement (Grok executor)  
**Reviewer:** Johnny Pang  
**Pack:** `refs/ifrs-18/draft-v1-linked/`  
**Skills applied:** ifrs-teaching-body · ifrs-teaching-body-qa · ifrs-visual-grammar (cite/body only; **Map not rewritten**)  
**CF 2018:** WAIT — not touched

## Pack path

`/workspace/ifrs-website/refs/ifrs-18/draft-v1-linked/` — ch01–ch08.html + assets + METHOD/NOTES

## What changed (this wave)

1. **Official cite chips** (~750) → `IFRS 18 · para [ref]` (IN/BC/B/IE/C/Figure/App D cross as applicable). **Zero** bare `§N` / `Official · …` in chips.
2. **Firm cite chips** (~250) — EY/KPMG `§` → **`section`**; weak house chips normalised (`KPMG FI 2024 · Appendix`, `EY Closer look 2026 · Overview`, `DTT A4 2022 · …`).
3. **Cite CSS** — `assets/draft.css` + `assets/shared.css`: Calibri Light / 11px / weight 300; house inherits (matches IAS 2 trial).
4. **Illustration titles** → `Illustration: N.M.k — Teaching Title` for case/IE/figure/firm worked plates; firm/IE ids live in chips only.
5. **FAQ ≠ Illus demotions** — EY Ill 3-1–3-12 index, App C C3 duty (no numeric IE), KPMG transition pointers (no numeric Ill) **not** titled `Illustration:`.
6. **Cite placement C1** — Illus body cite chips **hoisted to title**; peer bodies prose-only for Illus.
7. **Illus peer colour** — ch01 IE pack map ok/warn peers neutralized; Illus peers stay neutral.
8. **h3 / Decision-strip labels** — `§N` → `para N` in section/strip titles (ch04–ch06).
9. **METHOD** — cite + Illus title rules updated to IAS 2 trial grammar; Map still parked for I18.
10. **Map / CF** — untouched.

## QA summary (ifrs-teaching-body-qa)

| Gate | Result |
|------|--------|
| A Cite — zero house-only / zero `§` in chips / Official=`IFRS 18 · para…` | **PASS** |
| A Placement — Illus title chips (C1) | **PASS** (body cites hoisted) |
| A Multi-firm write-once | **Partial** — prior pack already merged many KPMG+EY rows; no new invent-piled chips; further overlap collapse = later densify pass |
| B Illus = worked-strip | **PASS** (all Illus are worked-strip) |
| B Illus peers neutral | **PASS** for Illus titled strips |
| B ALL Illus = worked-strip-**grid** peer shape | **OPEN GAP** — most Illus are single-`.box` / table shells inside worked-strip (not yet peer-grid Facts\|Assessment); converting without cutting table fidelity needs a follow-on shape pass |
| C `p.box-body>ul` | **PASS** (none) |
| D Densify quantitative | **OPEN GAP** — not densified this wave (no invent; no densify-down). Spot: ch05 Illus 5.2.1 thin (~324 chars). Full densify from Official+Big4 PDFs = next wave |
| E Title essence | **PASS** automated (no bare Official:/firm: leads in fail patterns) |
| E2 Technical-strict titles | **PASS** automated flowery scan; Illus titles now technical teaching names |
| E3 Visual-when-complex | **OPEN** — deferred (Map/diagram pass not unlocked for I18 this wave) |
| F Hyperlink | **Not re-run deep** — no id renumbers this wave; anchors preserved |
| I Big4 pre-flight / two-way crosswalk | **Prior METHOD** lists KPMG FI + EY Closer look + DTT A4 bridge + Official; **PwC = no invent / not on disk for I18**. Full Crosswalk A/B locator tables still debt if Johnny requires pack-complete claim |
| Map | **Parked** (Johnny: cite/body first; I18 Map not unlocked for big-rewrite) |

## Files touched

- `draft-v1-linked/ch01.html` … `ch08.html`
- `draft-v1-linked/assets/draft.css`
- `draft-v1-linked/assets/shared.css`
- `draft-v1-linked/IFRS18-CONTENT-REWRITE-METHOD.md`
- `refs/ifrs-18/I18-SKILL-ROLLOUT-2026-10-01.md` (this note)

## Backups

`/workspace/ifrs18-skill-rollout-20261001/` (pre-edit ch01–ch08 + METHOD)

## Open gaps for Johnny

1. **Illus → worked-strip-grid peers** for table/single-box Illus (keep tables; add Facts\|Assessment peers where content already supports it — no invent).
2. **Densify** thin Illus from Official IE + KPMG/EY plates (esp. 5.2.1); quantitative densify gate.
3. **Decision strips** still use `.ok`/`.warn` peers inside worked-strip (non-Illus teaching) — confirm allowed as contrast, or convert to `.contrast-pair`.
4. **Body prose** still uses `§` in running text (chips clean). Optional later pass → `para` in prose for consistency.
5. **I18 Concept Maps** — not enhanced this wave.
6. **CF 2018** — still WAIT.
7. **Crosswalk A/B** locator-level completeness — still required before any pack-complete claim.
8. **Multi-firm write-once polish** — spot-collapse remaining near-duplicate firm paragraphs with dual chips.

## Sync target

Documents laptop `2a06a250-7384-4878-8b5c-ffbf4a1f68e5` → `C:\Users\johnny\Documents\ifrs-website-refs\refs\ifrs-18\…`
