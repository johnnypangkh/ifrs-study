# CF 2018 — IAS 2 trial skill grammar rollout (2026-10-01 Asia/Shanghai)

**Owner:** Content implement (Grok executor)  
**Reviewer:** Johnny Pang  
**Pack:** `refs/cf-2018/draft-v1-linked/`  
**Skills applied:** ifrs-teaching-body · ifrs-teaching-body-qa · ifrs-visual-grammar (cite/body only; **Map not rewritten**)  
**IFRS 18 / IAS 2:** NOT touched

## Pack path

`/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/` — ch01–ch09.html + assets + METHOD/NOTES  
Pack root: `/workspace/ifrs-website/refs/cf-2018/`

## What changed (this wave)

1. **Official cite chips** (~804) → `CF 2018 · para [ref]` (SP / BC / para ranges / fn as applicable). Cross-standard → `IAS 8 · para 11`. Cover meta → `CF 2018 · 2026 cover`. **Zero** bare `§N` / `Official · …` in chips.
2. **Firm cite chips** — DTT `§` dropped; order normalised to `DTT A2 2022 · …`. PwC `§` dropped; weak chips normalised (`1.29–1.51-ish` → `1.29–1.51`, `1.51 area` → `1.51`; topic locators `cost constraint` / `elements` / `presentation` retained as firm+work+locator). **No EY/KPMG** chips in pack (none invent).
3. **Cite CSS** — `assets/draft.css` + `visuals/shared.css` + `chapter-visuals/shared.css`: Calibri Light / 11px / weight 300; house inherits (matches IAS 2 / I18 trial).
4. **Illustration titles** → `Illustration: N.M.k — Teaching Title` for worked cue/pair/strip + going-concern plate:
   - 3.5.1 Going concern assumption
   - 4.4.1 Claim that fails liability → equity
   - 4.5.1 Owner cash contribution vs inventory sale
   - 5.5.1 Not recognising an acquired resource distorts performance
   - 6.6.1 Day-2 P&L from basis flip / deemed cost
   - 8.4.1 Three-way landing of the same CU15
5. **FAQ ≠ Illus** — Decision strips stay Decision strips (not titled `Illustration:`). Official quote plates `§1.23` / `§1.14` retitled to teaching names (not Illus this wave — quote plates, not Facts→Assessment).
6. **Cite placement C1** — Illus body cite chips **hoisted to title**; Illus peer/table bodies prose-only.
7. **Illus peer colour** — `.ok`/`.warn` on Illus peers neutralized (Decision-strip ok/warn left for non-Illus teaching).
8. **h3 labels** — `§N` → `para N` in section titles (e.g. Ch5 recognition gates).
9. **METHOD + CITATION-CHIPS** — cite + Illus title rules updated to IAS 2 trial grammar; Map still parked for CF.
10. **Map / IFRS 18 / IAS 2** — untouched.

## QA summary (ifrs-teaching-body-qa)

| Gate | Result |
|------|--------|
| A Cite — zero house-only / zero `§` in chips / Official=`CF 2018 · para…` | **PASS** |
| A Placement — Illus title chips (C1) | **PASS** (body cites hoisted on Illus) |
| A Multi-firm write-once | **Partial** — prior pack already merged many DTT+PwC rows; no new invent-piled chips; further overlap collapse = later densify pass |
| B Illus = worked-strip | **PASS** (all 6 Illus are worked-strip) |
| B Illus peers neutral | **PASS** |
| B ALL Illus = worked-strip-**grid** peer shape | **OPEN GAP** — 8.4.1 is table shell inside worked-strip (not Facts\|Assessment peers); other Illus use Start/Gate/Conclusion peers already |
| C `p.box-body>ul` | **PASS** (none) |
| D Densify quantitative | **OPEN GAP** — not densified this wave (no invent; no densify-down). All 6 Illus currently thin vs IAS 2 densify bar (mostly short teaching cues). Full densify from Official+Big4 PDFs = next wave |
| E Title essence | **OPEN GAP** — automated still finds `<strong>DTT.</strong>` / `<strong>PwC.</strong>` / `<strong>Official.</strong>` bare firm leads (~25). Cite/Illus grammar wave did not mass-rewrite bullet leads (risk invent). Follow-on title-essence pass |
| E2 Technical-strict titles | **PASS** automated flowery scan; Illus titles now technical teaching names |
| E3 Visual-when-complex | **OPEN** — deferred (Map/diagram pass not unlocked for CF this wave) |
| F Hyperlink | **Not re-run deep** — no id renumbers this wave; anchors preserved |
| I Big4 pre-flight / two-way crosswalk | **Prior METHOD/PACK** lists Official + DTT A2 + PwC MOA intro; **EY/KPMG = no invent / not packed**. Full Crosswalk A/B locator tables still debt if Johnny requires pack-complete claim |
| Map | **Parked** (Johnny: cite/body first; CF Map not unlocked for big-rewrite this wave) |

## Files touched

- `draft-v1-linked/ch01.html` … `ch09.html`
- `draft-v1-linked/assets/draft.css`
- `draft-v1-linked/visuals/shared.css`
- `chapter-visuals/shared.css`
- `draft-v1-linked/CF-CONTENT-REWRITE-METHOD.md`
- `CITATION-CHIPS.md`
- `refs/cf-2018/CF-SKILL-ROLLOUT-2026-10-01.md` (this note)

## Backups

`/workspace/cf2018-skill-rollout-20261001/` (pre-edit ch01–ch09 + METHOD + draft.css + shared.css + CITATION-CHIPS + visuals-shared.css)

## Open gaps for Johnny

1. **Densify** thin Illus from Official + DTT/PwC (all 6 currently under quantitative densify bar) — no invent; pull source body.
2. **Title essence** — rewrite bare `<strong>DTT.</strong>` / `<strong>PwC.</strong>` / `<strong>Official.</strong>` leads to teaching substance (chips already carry firm).
3. **Illus → richer peers / bullets** where plates are still Start|Gate|Conclusion short cues or table-only (8.4.1).
4. **Decision strips** still use `.ok`/`.warn` peers inside worked-strip (non-Illus teaching) — confirm allowed as contrast, or convert to `.contrast-pair`.
5. **Body prose** still uses `§` / “Teaching §§” in running text (chips clean). Optional later pass → `para` in prose for consistency.
6. **CF Concept Maps** — not enhanced this wave (parked).
7. **Crosswalk A/B** locator-level completeness — still required before any pack-complete claim.
8. **EY/KPMG CF** — still not on disk; remain Blocking for pack-complete until scanned or Johnny confirms unavailable.
9. **IFRS 18** — already rolled earlier; not re-touched.

## Sync target

Documents laptop `2a06a250-7384-4878-8b5c-ffbf4a1f68e5` → `C:\Users\johnny\Documents\ifrs-website-refs\…` matching pack path under `refs/cf-2018/…`

**Sync status (2026-10-01 ~18:04 Asia/Shanghai):** **FAIL** — laptop `LAPTOP-MODGPP0C` (`2a06a250-…`) listed **connected: false**. Box edits complete; retry CopyFromBox when Johnny reconnects the Documents machine.
