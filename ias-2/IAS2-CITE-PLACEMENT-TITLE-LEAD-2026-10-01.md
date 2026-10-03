# IAS 2 — Cite chip placement: title / lead only (2026-10-01 Asia/Shanghai)

**Owner:** Content implement (Grok)  
**Reviewer:** Johnny Pang  
**Pack:** `refs/ias-2/draft-v1-linked/`

## Johnny lock

**All cite chips on title / bold-lead only. Strip body / paragraph-end chips.**

| Pattern | Chips live on | Body |
|---------|---------------|------|
| Illustration `.box` / `.worked-strip` | `box-title` / `worked-strip-title` after `Illustration: N.M.k — Title` | Prose only — no mid-paragraph or after-last-sentence chips |
| Teaching list / bullet with bold lead | End of lead line (right after `</strong>`), or immediately under lead | Long body paragraph has no trailing chips |
| Deduplicate | Same cite on title **and** body → keep title | Body-only → **move up** (do not delete sources) |

Also confirmed still locked from prior pass:

| # | Lock | Status |
|---|------|--------|
| 1 | Official = `IAS 2 · para …` | OK (no `Official ·` left) |
| 2 | EY = `EY IGAAP 2026` | OK (8 chips; no `International GAAP` in HTML chips) |
| 3 | Cite CSS = Calibri Light / `font-weight: 300` | OK (`draft.css`, `shared.css`, `visuals/shared.css`) |

## What changed

1. **ch01–ch06.html** — body / paragraph-end chips moved to title or bold lead; title↔body dedupe.
2. **Skill** `ifrs-teaching-body` — new full **Cite-tag formatting** section (labels + typography + placement + crypto worked example).
3. **METHOD** — header placement lock + format rule 8 + checklist.

## Counts

| Metric | Count |
|--------|------:|
| Cite spans touched (moved / repositioned) | **201** |
| Illustration boxes: body→title | 7 boxes / 9 spans |
| Worked-strip nested body→strip title | 3 strips / 3 spans |
| Non-illustration box title hoist | 2 boxes / 4 spans |
| List items: chips → after bold lead | 110 lis / 166 spans |
| Section lead `<p>`: chips → after bold lead | 13 / 19 spans |
| Title↔body dedupe dropped | 4 |
| Net `.cite` chips ch01–ch06 after | 338 (was 342; −4 dedupe) |

### Per-chapter `.cite` chips (after)

| File | Count |
|------|------:|
| ch01.html | 63 |
| ch02.html | 24 |
| ch03.html | 143 |
| ch04.html | 50 |
| ch05.html | 26 |
| ch06.html | 32 |

## Sample — Illustration 1.1.2 crypto

**Before:** DTT + `IAS 2 · para 3` on title; `IAS 2 · para 36–39` + two EY chips on `box-body`.

**After:** all five chips on `box-title`; `box-body` prose only:

```html
<p class="box-title"><strong>Illustration: 1.1.2 — Cryptocurrencies held for ordinary-course sale</strong>
  … DTT A11 2022 · 2.1-3 …
  IAS 2 · para 3 …
  IAS 2 · para 36–39 …
  EY IGAAP 2026 · Ch23 · §2.3.1.F …
  EY IGAAP 2026 · Ch23 · §3.4.2 …
</p>
<p class="box-body">…prose only…</p>
```

## Skill path (updated)

- Canonical: `/home/box/sand-data/workflows/ifrs-teaching-body/SKILL.md`
- Bundle twin: `/workspace/ias2-opus-bundle/ifrs-teaching-body-SKILL.md` (identical)

## Backups

`/workspace/ias2-content-extract/*-before-cite-placement-20261001-142720+0800*`

## Documents sync (done)

- Machine: LAPTOP-MODGPP0C (`2a06a250-7384-4878-8b5c-ffbf4a1f68e5`)
- Target: `C:\Users\johnny\Documents\ifrs-website-refs\refs\ias-2\draft-v1-linked\`
- Also: `refs\ias-2\IAS2-CITE-PLACEMENT-TITLE-LEAD-2026-10-01.md`

- Synced: ch01–ch06.html, IAS2-CONTENT-REWRITE-METHOD.md, ifrs-teaching-body-SKILL.md, changelog, tgz
