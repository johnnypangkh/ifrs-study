# Site infra — workbook #95

**Owner:** IFRS Build · **Updated:** 2026-10-21 Asia/Shanghai · #100 live `site/master-formatting/` · #109 timeline module  
**Update:** same PR as any infra change.

## Source of truth

| Layer | Role | Where |
|---|---|---|
| **GitHub `main`** | **SoT** for site code | `https://github.com/johnnypangkh/ifrs-study` |
| **GitHub Pages** | Mirror of `main` (can lag) | `https://johnnypangkh.github.io/ifrs-study/` |
| **OneDrive** | Backup after Johnny yes — never edit & copy back | `00. IFRS Web/ifrs-website-refs/` (Johnny confirmed) · workbook `00. IFRS Web/IFRS-STATUS.xlsx` |
| Box `/workspace/style-base/` | Scratch only | Not live |
| Draft PR | WIP | Not live until PM squash-merge |

## Pipeline

```mermaid
flowchart LR
  J[Johnny] --> PM[PM gates]
  PM --> BD[Build brief]
  BD -->|effort pick| CA[Living chrome agent<br/>bc-0d5f2356…]
  CA -->|draft PR| QC[QC + PM scan]
  QC -->|PASS + Johnny yes| PM
  PM -->|squash-merge only| MAIN[(GitHub main SoT)]
  MAIN --> PAGES[Pages mirror]
  J -->|OD yes| OD[OneDrive backup]
```

**Build never merges.** After W2b → FAIL-only until W4 / new GO.

## When stuck — look here

| Stuck on | Look |
|---|---|
| What is live vs draft? | SoT table above · runbook § Pages check |
| Who merges? | PM only after Johnny yes |
| Which Cursor agent? | `bc-0d5f2356-769c-5035-99f6-b057b5ad7190` · [agent](https://cursor.com/agents/bc-0d5f2356-769c-5035-99f6-b057b5ad7190) |
| OD path? | `00. IFRS Web/ifrs-website-refs/` |
| Repo docs path? | `docs/site-infra/` |
| Full ops steps | `SITE-INFRA-RUNBOOK.md` |
| Map cite count lint fails? | runbook § CI gates with pinned counts |
| Map lint says shared class collision? | runbook § CI gates with pinned counts (rename the plate class; never edit the shared rule) |
| Where is the live Master formatting page? | `site/master-formatting/` (Johnny V6 path A, #100). Settings (`site/settings/`) is the token table, not MF. LEGO sheet is section `#lego-sheet` on the MF page. |
| Where is shared timeline chrome? | `_shared/modules/visuals/timeline-1.css`, imported by `_shared/visuals.css` (#109). Not `map-box.css`. Packs load the kit; IAS 16 keeps plate placement in `ias16.css`. |

## Live pages under `site/`

| Path | What it is | Stamp |
|---|---|---|
| `site/settings/` | Settings — Master styles token table. Not Master formatting. | Pack key `site` |
| `site/master-formatting/` | Live Master formatting page (#100). LEGO kit sheet is `#lego-sheet` on this same page. | Pack key `site`. `stamp-assets.py` `settings_pages()`, `build-last-update.py` path list + site fingerprint, `chrome-packs.js` `CHROME_PACK_PATHS`, `check-stamp-only.py` `?v=`-only (same shape as Settings). Page CSS stays on the page. `kit.css` is not in `_shared`. |
