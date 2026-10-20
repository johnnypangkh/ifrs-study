# Site infra runbook — workbook #95

**Owner:** IFRS Build · pairs with `SITE-INFRA-DIAGRAM.md` · update in same PR as infra change.

## Who

| Action | Who |
|---|---|
| Squash-merge | **PM only** (Johnny yes) |
| Draft PR | Cursor via Build (reply living agent) |
| Brief / Skill locks | Build |
| Round-2 QC | IFRS QC · PM W3 |
| OD backup `draft-v1-linked` | Executor after Johnny yes |
| Merge | **Never** Build / Cursor / QC / Design |

After **W2b**: Build **FAIL-only** until W4 or new GO.

## Deploy path

1. Draft PR from living agent → CI green  
2. QC PASS → Johnny merge yes → **PM squash-merges** to `main`  
3. Pages tracks `main` (lag OK for a few minutes)  
4. Johnny OD yes → Executor: GitHub raw @ merge SHA → `00. IFRS Web/ifrs-website-refs/<pack>/draft-v1-linked/`

Live base: `https://johnnypangkh.github.io/ifrs-study/`

## Pages vs main (when stuck / after merge)

1. Note merge SHA on `main`  
2. Compare live `_shared` / stamp / map-box to that SHA  
3. Report: `live matches <sha>` or `live stale vs <sha>`  
4. If stale: wait deploy + hard-refresh — do not invent a new look

## Living agent

- Id: `bc-0d5f2356-769c-5035-99f6-b057b5ad7190`  
- Repo: `johnnypangkh/ifrs-study` only  
- Effort: Johnny picks before every reply  
- Reuse: reply; do not launch a second chrome agent

## CI gates with pinned counts

| Gate | Pin | Source |
|---|---|---|
| `tools/map-lint.py` `CITE_ALLOW` for `ias-16/draft-v1-linked/visuals/master-concept-map.html` | **4** | Johnny lock FINAL-B2 2026-10-20 19:31 / PR #98. The three #98 plates cite 0. The remaining 4 are ch07 Disclosure. Do not trim ch07. |
| `tools/check-stamp-only.py` | #98 scoped allow | visuals `ch04-models.html`, `ch05-depreciation.html`, `master-concept-map.html` (plate regions), `ch06-derecognition.html` (compensation wrapper), and `ch04.html` + `ch05.html` + `references.html` (#98 change spots only). PM 5 approved 2026-10-20 15:23 + 18:02 + FINAL-B2 19:39 / PR #98. `check-incremental` owns the teaching rows. |

## Docs home

- Repo: `docs/site-infra/`  
- Box scratch: `/workspace/style-base/site-infra/`
