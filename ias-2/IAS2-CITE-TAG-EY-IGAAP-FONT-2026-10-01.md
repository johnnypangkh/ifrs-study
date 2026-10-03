# IAS 2 — Cite-tag locks: EY IGAAP + Calibri Light (2026-10-01 Asia/Shanghai)

**Owner:** Content implement (Grok)  
**Reviewer:** Johnny Pang  
**Pack:** `refs/ias-2/draft-v1-linked/`

## Johnny locks

| # | Lock | Rule |
|---|------|------|
| 1 | Official chips | `[Standard] · para [ref]` e.g. `IAS 2 · para 3` / `BC1` / `IN7` (prior lock; kept) |
| 2 | EY chip label | **`EY IGAAP 2026`** — not `EY International GAAP 2026`; keep path e.g. `EY IGAAP 2026 · Ch23 · §2.3` |
| 3 | Cite typography | **All** `.cite` / `.cite-house`: font **Calibri Light**, **not bold** (`font-weight: 300`; stack `"Calibri Light", Calibri, "Segoe UI", sans-serif`) |

Other Big4 chip patterns unchanged (`DTT A11 2022 · …`, `PwC MOA 2020 · …`).

## What changed

1. **HTML EY chips** — `International GAAP 2026` → `IGAAP 2026` in `ch01.html` (7) + `ch03.html` (1).
2. **CSS** — `assets/draft.css`, `assets/shared.css` (appended base rule), `visuals/shared.css`: Calibri Light + weight 300 on `.cite` / `.cite-house`.
3. **Skill** `ifrs-teaching-body` — rules 6–9 (Official / EY IGAAP / typography / other Big4 keep).
4. **METHOD** — header locks + format rule 8 + checklist.

## Counts

| Metric | Count |
|--------|------:|
| EY chips relabelled | 8 |
| Total `.cite` chips ch01–ch06 | 342 |
| EY chips with IGAAP label | 8 |
| CSS files patched | 3 |

### Per-chapter cite chips

| File | All `.cite` | EY |
|------|------------:|---:|
| ch01.html | 64 | 7 |
| ch02.html | 24 | 0 |
| ch03.html | 146 | 1 |
| ch04.html | 50 | 0 |
| ch05.html | 26 | 0 |
| ch06.html | 32 | 0 | |

## Skill path (confirmed)

- Canonical workflow: `/home/box/sand-data/workflows/ifrs-teaching-body/SKILL.md`
- Bundle twin: `/workspace/ias2-opus-bundle/ifrs-teaching-body-SKILL.md` (identical)

## Backups

`/workspace/ias2-content-extract/*-before-ey-igaap-cite-20261001-142457+0800*`  
`draft-css-before-cite-font-20261001-142457+0800.css`  
`visuals-shared-css-before-cite-font-20261001-142457+0800.css`

## Documents sync

- Machine: LAPTOP-MODGPP0C (`2a06a250-7384-4878-8b5c-ffbf4a1f68e5`)
- Target: `C:\Users\johnny\Documents\ifrs-website-refs\refs\ias-2\draft-v1-linked\`
- Changelog also at: `refs\ias-2\IAS2-CITE-TAG-EY-IGAAP-FONT-2026-10-01.md`
