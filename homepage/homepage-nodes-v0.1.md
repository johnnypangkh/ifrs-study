# Homepage wireframe nodes v0.1

Source: `homepage-wireframe-v0.1.html`  
Brief: `HOMEPAGE-BRIEF-v0.md`  
Revision: 2026-09-27 — CF READY + IFRS 18 READY (P0 Map Open); progress 2 of 21; dark card-wall unchanged.

## Regions → purpose

| Region | Purpose |
|--------|---------|
| **Preview badge** (fixed top-right, subtle) | Quiet review mark — not loud Wireframe chrome |
| **Title “All standards”** | Hub identity — dark card wall of IFRS learning topics |
| **Progress line** | Honest readiness: “2 of 21 ready. Select a standard to open its notes.” |
| **Standard picker** (native `<select>`) | Filter to a category or one IFRS / IAS / CF card and jump it into view |
| **Search bar + results panel** | Small file://-safe JS demo; typing filters cards and shows matching hits, including “IFRS 15” and “impairment” |
| **Workflow strip: 1 Sources → 2 Skill → 3 Study notes** | Explains build pipeline; green-bordered Study notes = what READY **Open >** opens |
| **Category sections** | Group cards by topic; blue uppercase labels; horizontal rule between groups |
| **Card: code + English title + status** | IFRS / IAS / CF only — no HKFRS/HKAS |
| **READY chrome** | Solid green border + working **Open >** → draft Map |
| **PLANNED chrome** | Dashed grey border; dimmed; not openable |
| **NEXT UP chrome** | Amber/orange border; queued / notes WIP (none on board now) |
| **Footnote** | Preview caveats and honest status note |

## Card set (illustrative, honest)

| Category | Cards | Status |
|----------|-------|--------|
| Framework and basis of preparation | CF 2018 · IAS 8 · IAS 10 | **CF READY** (Open → `../cf-2018/draft-v1-linked/index.html`); IAS 8/10 PLANNED |
| Presentation | IFRS 18 · IAS 1 | **IFRS 18 READY** (Open → `../ifrs-18/draft-v1-linked/index.html`); IAS 1 PLANNED |
| Revenue | IFRS 15 | PLANNED |
| Financial instruments | IFRS 9 (one hub) | PLANNED |
| Assets | IAS 16, 2, 36, 40, 38 · IFRS 5 · IAS 23 | all PLANNED |
| Measurement | IFRS 13 | PLANNED |
| Leases | IFRS 16 | PLANNED |
| Business combinations | IFRS 3 | PLANNED |
| Share-based payment | IFRS 2 | PLANNED |
| Consolidation | IFRS 10 | PLANNED |
| Income taxes | IAS 12 | PLANNED |
| Provisions | IAS 37 | PLANNED |

**READY count: 2** — CF 2018 and IFRS 18 open their draft Maps. IFRS 18 P0 (Map + Ch3/4/5/7) QC PASS under 2026.09.27-6; Ch2/6/8/9 stubs remain WIP.

## v0.1 interaction notes

- The native picker has **All standards**, category options, and each card code. Selecting a category filters the wall; selecting a standard filters to that card and scrolls to it.
- The search is client-side only and works offline from `file://`. It filters the cards and renders a results panel; sample queries are **IFRS 15** and **impairment**.
- CF **Open >** → `../cf-2018/draft-v1-linked/index.html`; IFRS 18 **Open >** → `../ifrs-18/draft-v1-linked/index.html`; other cards stay non-openable.

## Out of scope

Final polish, brand art, IFRS 18 P1/P2 chapter visuals, and production search.
