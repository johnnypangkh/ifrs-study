# IAS 2 — Official cite chip lock (2026-10-01 Asia/Shanghai)

**Owner:** Content implement (Grok)  
**Reviewer:** Johnny Pang  
**Pack:** `refs/ias-2/draft-v1-linked/`

## Johnny lock

Pattern: `[Standard] · para [ref]` with middle-dot, class `cite-official` kept for colour.

| Locked | Forbidden |
|--------|-----------|
| `IAS 2 · para 3` | `Official · §3` |
| `IAS 2 · para 3(a)` | `Official · §3(a)` |
| `IAS 2 · para B1` / `BC1` / `IN7` | `Official · BC1` / `Official · IN7` |

General form Johnny also stated: `[IFRS X] Para [X such as 3, B1, BC1, …]` — **this pack** spells it `IAS 2 · para …` (middle-dot consistent with existing chips).

Cross-standard in this pack: `IAS 16 · para 8`, `IAS 23 · para 4(b)`; bare `IFRS 13` when no para cited.

## What changed

1. **All Official cite chips** in `ch01`–`ch06.html` (~150) rewritten `Official · §…` / `Official · IN…` / `Official · BC…` → `IAS 2 · para …`. Visuals had no Official chips — untouched.
2. **List bold titles** — sibling pass already finished (`IAS2-LIST-TITLE-DEDUPE-2026-10-01.md`); Ch1 §1.3 screenshot block landmarks verified; no §-as-title remaining. This pass did not re-touch titles.
3. **Skill** `ifrs-teaching-body` — new rule **Official cite chip format (Johnny lock 2026-10-01)**.
4. **METHOD** `IAS2-CONTENT-REWRITE-METHOD.md` — header lock + format rule 8 rewrite + checklist.

## Samples before → after

| Where | Before | After |
|-------|--------|-------|
| Ch1 · 1.3 carve-out | `Official · §3(a)` | `IAS 2 · para 3(a)` |
| Ch1 · 1.3 IN | `Official · IN7` | `IAS 2 · para IN7` |
| Ch1 · BC plate | `Official · BC7` | `IAS 2 · para BC7` |
| Ch1 · spare parts | `Official · IAS 16 §8` | `IAS 16 · para 8` |
| Ch1 · NRV≠FV | `Official · IFRS 13` | `IFRS 13` |
| Ch3 · cost | `Official · §10` | `IAS 2 · para 10` |
| Ch3 · LIFO BC | `Official · BC9–BC20` | `IAS 2 · para BC9–BC20` |
| Ch3 · IAS 23 | `IAS 23 · §4(b)` | `IAS 23 · para 4(b)` |
| Ch4 · lower-of | `Official · §9` | `IAS 2 · para 9` |
| Ch6 · disclosure | `Official · §36(a)` | `IAS 2 · para 36(a)` |
| Ch6 · IN | `Official · IN16` | `IAS 2 · para IN16` |

## Counts (cite-official chips with `IAS 2 · para`)

| File | Count |
|------|------:|
| ch01 | 28 |
| ch02 | 10 |
| ch03 | 65 |
| ch04 | 23 |
| ch05 | 10 |
| ch06 | 14 |

(+ cross-standard: `IAS 16 · para 8` ×1, `IAS 23 · para 4(b)` ×2, `IFRS 13` ×1)

## Backups

`/workspace/ias2-content-extract/ch0N-before-cite-lock-20261001-142051+0800.html`  
`METHOD-before-cite-lock-20261001-142051+0800.md`  
`SKILL-before-cite-lock-20261001-142051+0800.md`

## Documents sync

- Machine: LAPTOP-MODGPP0C (`2a06a250-7384-4878-8b5c-ffbf4a1f68e5`)
- Target: `C:\Users\johnny\Documents\ifrs-website-refs\refs\ias-2\draft-v1-linked\`
- Synced: ch01–ch06.html, IAS2-CONTENT-REWRITE-METHOD.md
- Also: `refs\ias-2\IAS2-OFFICIAL-CITE-LOCK-2026-10-01.md`, `ias2-official-cite-lock-20261001.tgz`
