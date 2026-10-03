# IAS 2 — References page + Last update chrome (2026-10-02)

**Owner:** Grok Bot (executor)  
**Pack:** `refs/ias-2/draft-v1-linked/`  
**Scope:** Task A (References) + Task B (Last update pill). **Not** modularisation (Task C deferred).

## What landed

| Item | Detail |
|------|--------|
| New page | `references.html` — nav label **References**, after Ch6 in tag-row |
| Nav | Tag-row on `index.html`, `ch01.html`–`ch06.html`, `references.html`: Map \| 1…6 \| References |
| Footer | `ch06` → Next: References; `references` → Prev: Disclosure / Map / no next |
| Last update | Boxed pill `Last update · 2026-10-02` beside pack title in chrome (all HTML pages above) |
| CSS | `assets/draft.css` — `.chrome-title-cluster`, `.chrome-last-update` (`--line` / `--band`) |
| Cache key | `?v=ias2-refs-lastupdate-20261002` on shared/draft CSS links |
| Shots | `/workspace/ifrs-website/wip/ias2-refs-lastupdate/` |

## Last-update date

**2026-10-02** — Opus pack Map final wave (`ias2-packmap-final-20261002` / `OPUS-WORKING-MEMORY.md` checkpoint step 3). Aligns with `index.html` / `visuals/map-formula-board.html` mtimes on 2026-10-02 Asia/Shanghai.

## Source rows (honest — cite chips + METHOD/XREF/pre-flight)

### Official (primary + cross-standards that appear as `cite-official`)

| Full name | Short form |
|-----------|------------|
| IAS 2 Inventories (HKAS 2 on box inputs) | IAS 2 |
| Conceptual Framework for Financial Reporting | Conceptual Framework |
| IAS 1 Presentation of Financial Statements | IAS 1 |
| IAS 8 Accounting Policies, Changes in Accounting Estimates and Errors | IAS 8 |
| IAS 10 Events after the Reporting Period | IAS 10 |
| IAS 16 Property, Plant and Equipment | IAS 16 |
| IAS 23 Borrowing Costs | IAS 23 |
| IAS 34 Interim Financial Reporting | IAS 34 |
| IAS 36 Impairment of Assets | IAS 36 |
| IAS 38 Intangible Assets | IAS 38 |
| IAS 40 Investment Property | IAS 40 |
| IAS 41 Agriculture | IAS 41 |
| IFRS 3 Business Combinations | IFRS 3 |
| IFRS 5 Non-current Assets Held for Sale and Discontinued Operations | IFRS 5 |
| IFRS 9 Financial Instruments | IFRS 9 |
| IFRS 13 Fair Value Measurement | IFRS 13 |
| IFRS 15 Revenue from Contracts with Customers | IFRS 15 |
| IFRS 16 Leases | IFRS 16 |
| IFRIC 1 Changes in Existing Decommissioning, Restoration and Similar Liabilities | IFRIC 1 |
| IFRIC 20 Stripping Costs in the Production Phase of a Surface Mine | IFRIC 20 |

### Big 4

| Full name | Short form (cite chip) |
|-----------|------------------------|
| PwC Manual of Accounting 2020 — Chapter 25 Inventories | PwC MOA 2020 Ch25 |
| Deloitte (DTT) iGAAP / Manual of Accounting — A11 Inventories (2022) | DTT iGAAP 2022 A11 |
| EY International GAAP 2026 — Chapter 23 Inventories | EY iGAAP 2026 Ch23 |
| KPMG Insights into IFRS 2019/20 — Part 1 · 3.8 Inventories | KPMG Insights 2019/20 · Part 1 · 3.8 |

**Derivation:** unique work-title prefixes from nested `.cite` chips in ch01–ch06; full names from `IAS2-BIG4-COMPLETE-PREFLIGHT-2026-10-01.md` / METHOD / XREF. No invented houses.

## QA

- [x] References after Ch6 in every tag-row
- [x] All tag `href`s resolve to existing files
- [x] Last-update pill on index + ch01–06 + references
- [x] Modularisation **not** started

## Not done (Task C)

Shared header partial / further modularisation — leave for Grok advice to Johnny.
