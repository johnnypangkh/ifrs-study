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

## Docs home

- Repo: `docs/site-infra/`  
- Box scratch: `/workspace/style-base/site-infra/`
