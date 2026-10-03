# IAS 2 — cite reattach + Illustration grid lock (2026-10-01)

**Johnny angry-bug fix + quality bar.** Apologies: the cite-placement realign left many Big4 chips as **house-only** (`<span class="cite-house">PwC</span>` with locator orphaned after bold leads + stray `</span>`). That should never have shipped.

## 1) Bare-chip reattach (ch01–ch06) — DONE

| Chapter | Units fixed |
|---------|-------------|
| ch01 | 5 |
| ch02 | 5 |
| ch03 | 13 (incl. 2 Illustration-body IFRS 9 locators hoisted to title) |
| ch04 | 7 |
| ch05 | 5 |
| ch06 | 7 |
| **Total** | **42** |

**What fixed:**
1. Find bare firm-only chips (visible text only PwC/DTT/EY/KPMG).
2. Reattach matching orphan locator (`MOA 2020 · …`, `A11 2022 · …`, `IGAAP…`, FAQ ids, `· IFRS 9 paras…`) **into** the cite span.
3. Remove orphan text + stray `</span>` after bold leads.
4. Placement kept: Illustration chips on title (FULL detail); teaching unit chips at **end** with FULL detail.
5. Audit: **zero** house-only Big4 chips remaining on ch01–ch06.

**Sorry counts:** 42 broken teaching units left house-only chips after the prior placement split — all reattached this pass.

## 2) Skill lock — `ifrs-teaching-body` (Opus-ready)

**Canonical:** `/home/box/sand-data/workflows/ifrs-teaching-body/SKILL.md`  
**Bundle twin:** `/workspace/ias2-opus-bundle/ifrs-teaching-body-SKILL.md` (identical)

Locked now:
- Cite chip **MUST** = firm + work + locator (e.g. `PwC MOA 2020 · FAQ 25.10.1` / `DTT A11 2022 · 2.1-2` / `EY IGAAP 2026 · Ch23 · …`). **NEVER** house-only.
- Placement split still applies (Illustration title; teaching unit end).
- **Illustration quality bar:** structured visualization first — worked-strip peer grids (Ch4 **4.5.1–4.5.3** FACTS / CONCLUSION / EXCEPTION with `.ok` green / `.warn` yellow), tables, contrast-pair, chapter visuals when needed. Text dump = **fail**.
- Simpler plates may use Facts + Assessment **bullets** (no content cut).
- Full **formatting inventory** from `assets/draft.css` + `assets/shared.css` + live HTML (fonts, sizes, weights, colours, container chooser, headings, tables, ok/warn).

## 3) Illustration grid pass (IAS 2 weak plates) — DONE

Converted **20** prose-dump Illustrations to 4.5.x-style worked-strip / contrast-pair / table+lead structures (no content cut):

| Chapter | IDs rewritten |
|---------|----------------|
| ch01 | `s-1-ex-pipeline`, `s-1-ex-crypto`, `s-1-ex-spare`, `s-1-ex-nrv-fv` |
| ch02 | `s-2-ex-spare`, `s-2-ex-consign` |
| ch03 | `s-3-ex-vol-rebate`, `s-3-ex-pwc-rebate`, `s-3-ex-pwc-oh`, `s-3-ex-rou`, `s-3-ex-storage`, `s-3-ex-pwc-252`, `s-3-ex-pwc-251` |
| ch04 | `s-4-ex-costs-sell`, `s-4-ex-formula`, `s-4-ex-dev`, `s-4-ex-pwc-post`, `s-4-ex-long`, `s-4-ex-pwc-mat` |
| ch05 | `s-5-ex-rev` |

Post-pass audit: **0** remaining prose dumps by wall-of-words heuristic; **27** worked-strip-ish plates; bare-chip audit still **0**.

**CF / IFRS 18:** WAIT (Johnny confirm) — not touched.

## Backups

`/workspace/ias2-content-extract/*-before-cite-reattach-20261001-144223+0800*`  
`/workspace/ias2-content-extract/*-before-illus-grid-20261001-144724+0800*`  
`/workspace/ias2-content-extract/SKILL-before-format-doc-*` / `SKILL-before-cite-reattach-*`

## Documents sync

- Machine: LAPTOP-MODGPP0C (`2a06a250-7384-4878-8b5c-ffbf4a1f68e5`)
- Target pack: `C:\Users\johnny\Documents\ifrs-website-refs\refs\ias-2\draft-v1-linked\`
- Also: `refs\ias-2\IAS2-CITE-REATTACH-ILLUS-GRID-2026-10-01.md`
