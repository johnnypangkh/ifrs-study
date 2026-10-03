# Homepage wireframe brief v0

Owner: IFRS Website PM  
Reviewer: Johnny  
Date: 2026-09-27  
Cadence: **low-fi first** (structure over polish)

## Goal

Rebuild the Claude Artifacts **All standards** hub as the site homepage — same navigation idea, updated product rules.

## Locked product rules

1. **Dark UI** card wall titled **All standards**.
2. Top workflow strip: **1 Sources → 2 Skill → 3 Study notes** (Study notes = what green READY cards open).
3. Cards grouped by **category**.
4. Statuses:
   - **READY** — solid green border; **Open >** clickable
   - **PLANNED** — dashed grey border; not openable
   - **NEXT UP** — orange/amber border; queued / needs sources
5. Labels: **IFRS / IAS / CF only** — **no HKFRS / HKAS dual codes** (Claude screenshot still showed dual codes; drop them).
6. Progress line e.g. “N of M ready. Select a standard to open its notes.”
7. Green study-note bodies rebuild from zero; homepage only shows status + link shell for now.
8. Wireframe is low-fi: boxes, labels, status chrome — not final art.

## Reference (Claude original)

`/workspace/ifrs-website/refs/homepage/claude-all-standards-ref.jpg`

Categories / cards in that shot (for layout reference only; dual HK codes **must not** appear in new wireframe):

| Category | Cards (Claude) |
|----------|----------------|
| Framework and basis of preparation | CF 2018 READY · IAS 8 READY · IAS 10 READY |
| Presentation | IFRS 18 READY · IAS 1 PLANNED |
| Assets | IAS 16, 2, 36, 40, 38, IFRS 5 READY · IAS 23 PLANNED |
| Measurement | IFRS 13 READY |
| Leases | IFRS 16 NEXT UP |

## Suggested v0 card set for wireframe (illustrative statuses)

Align with current build order without pretending more pages exist:

| Category | Card | Status (illustrative) | Note |
|----------|------|----------------------|------|
| Framework | Conceptual Framework 2018 | NEXT UP or READY shell | First deep-dive; map v2.1 approved |
| Presentation | IFRS 18 | PLANNED | Second; replaces IAS 1 for presentation teaching |
| Presentation | IAS 1 | PLANNED | Legacy / bridge only if shown |
| Revenue | IFRS 15 | PLANNED | Multi-page later |
| Financial instruments | IFRS 9 | PLANNED | Multi-page (General / ECL / Hedge) — one hub card OK for now |
| Leases | IFRS 16 | PLANNED | |
| Business combinations | IFRS 3 | PLANNED | Multi-page later |
| Share-based payment | IFRS 2 | PLANNED | Multi-page later |
| Consolidation | IFRS 10 | PLANNED | |
| Income taxes | IAS 12 | PLANNED | |
| Impairment | IAS 36 | PLANNED | |
| Provisions | IAS 37 | PLANNED | |

Design may keep Claude’s fuller card wall if it better shows density — but **must** strip HK dual codes and mark real readiness honestly (most PLANNED; CF highlighted).

## Deliverables

1. `homepage-wireframe-v0.html` under `/workspace/ifrs-website/refs/homepage/`
2. Short `homepage-nodes-v0.md` (regions → purpose)
3. Reply PM with paths + one-line confirmation

## Out of scope for v0

- Final visual polish / brand system
- Working links into real pages
- CF / IFRS 18 sub-page content
