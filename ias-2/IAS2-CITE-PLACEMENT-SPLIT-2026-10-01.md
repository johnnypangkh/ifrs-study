# IAS 2 — Cite chip placement: REFINED split rule (2026-10-01 Asia/Shanghai)

**Owner:** Content implement (Grok)  
**Reviewer:** Johnny Pang  
**Pack:** `refs/ias-2/draft-v1-linked/`  
**Supersedes:** `IAS2-CITE-PLACEMENT-TITLE-LEAD-2026-10-01.md` (title/lead-only for everything)

## Johnny REFINED lock

| # | Pattern | Chips live |
|---|---------|------------|
| 1 | **Illustration** `.box` / `.worked-strip` with `Illustration: N.M.k — …` | ONLY at **end of title** line; body prose only — no chips in/after body |
| 2 | **Main teaching paras / list items** (non-Illustration) | At the **back** of that para or bullet (**end of the unit**) — NOT on a fake bold lead-only line if that emptied the body |
| — | Non-Illustration callout `.box` | End of `box-body` (not hoisted onto title) |

Also still locked:

| # | Lock | Status |
|---|------|--------|
| 1 | Official = `IAS 2 · para …` | OK (no `Official ·` left) |
| 2 | EY = `EY IGAAP 2026` | OK (8 chips; no `International GAAP` in HTML chips) |
| 3 | Cite CSS = Calibri Light / `font-weight: 300` | OK (`draft.css`, `shared.css`, `visuals/shared.css`) |

## What changed

1. **Skill** `ifrs-teaching-body` — Cite-tag §C rewritten as **split rule** (C1 Illustration title; C2 teaching unit end). Bundle twin synced.
2. **METHOD** — header placement lock + format rules 5/8 + checklist updated to split rule.
3. **ch01–ch06.html** — undo bold-lead over-hoist on non-Illustration list/section leads; chips moved to **end of unit**. Illustration title chips **kept** (e.g. 1.1.2 crypto all five on title). Ch2 definitional callouts: chips returned to end of `box-body`.

## Counts

| Metric | Count |
|--------|------:|
| List `<li>` units realigned (chips → end) | **111** |
| List spans moved | **131** |
| Teaching `<p>` units realigned | **13** |
| Teaching `<p>` spans moved | **19** |
| Non-Illustration box title → body end | **2** boxes / **4** spans |
| Illustration title blocks kept (chips on title) | **56** blocks / **134** spans |
| Net `.cite` chips ch01–ch06 (unchanged) | **338** |
| Remaining non-Illustration over-hoists | **0** |
| Illustration `box-body` with cites | **0** |

### Per-chapter

| File | `.cite` | li units/spans | p units/spans | box→body | Ill title kept |
|------|--------:|---------------:|--------------:|---------:|---------------:|
| ch01.html | 63 | 19/23 | 2/6 | 0/0 | 8/26 |
| ch02.html | 24 | 9/12 | 2/2 | 2/4 | 3/5 |
| ch03.html | 143 | 39/44 | 4/5 | 0/0 | 34/80 |
| ch04.html | 50 | 18/19 | 2/2 | 0/0 | 10/21 |
| ch05.html | 26 | 12/15 | 2/3 | 0/0 | 1/2 |
| ch06.html | 32 | 14/18 | 1/1 | 0/0 | 0/0 |

## Sample — Illustration 1.1.2 crypto (unchanged — C1)

All five chips remain on `box-title`; `box-body` prose only:

- DTT A11 2022 · 2.1-3
- IAS 2 · para 3
- IAS 2 · para 36–39
- EY IGAAP 2026 · Ch23 · §2.3.1.F
- EY IGAAP 2026 · Ch23 · §3.4.2

## Sample — teaching list (C2 undo)

**Before (over-hoist):** `<strong>Lead.</strong> <cite…> body prose…`

**After:** `<strong>Lead.</strong> body prose… <cite…>`

## Skill paths

- Canonical: `/home/box/sand-data/workflows/ifrs-teaching-body/SKILL.md`
- Bundle twin: `/workspace/ias2-opus-bundle/ifrs-teaching-body-SKILL.md` (identical)

## Backups

`/workspace/ias2-content-extract/*-before-cite-split-20261001-143530+0800*`

## Documents sync

- Machine: LAPTOP-MODGPP0C (`2a06a250-7384-4878-8b5c-ffbf4a1f68e5`)
- Target: `C:\Users\johnny\Documents\ifrs-website-refs\refs\ias-2\draft-v1-linked\`
- Also: `refs\ias-2\IAS2-CITE-PLACEMENT-SPLIT-2026-10-01.md`
