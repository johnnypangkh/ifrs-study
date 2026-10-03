# CF 2018 — chapter visuals

**Folder:** `/workspace/ifrs-website/refs/cf-2018/chapter-visuals/`  
**Style:** solid chrome (`shared.css` / `.visual-shell`) · dense teaching graphics · Conceptual Framework / IFRS labels only  
**Grammar:** solid = peer / containment; dashed = see-also (rare); composition → `.contain*` (never `.box.nest` / dashed hang)  
**Status:** Visual-grammar roll 2026-09-27 · twin of `draft-v1-linked/visuals/`  
**Out of scope:** inventing CF process spines · Build theme.js (night-only owned by Build)

Open any `chNN-*.html` via `file://` (relative `shared.css`).

## Chapters → visual types

| File | Chapter | Visual types present |
|------|---------|----------------------|
| [ch01-overview.html](_archive/ch01-overview.html) | Overview *(retired 2026.09.27-4)* | Archived start-here graphic — not live nav/embed |
| [ch01-objective-users.html](ch01-objective-users.html) | Objective & users | Dense concept map (purpose / users / decisions / info needs / GPFS + stewardship on one plate); party cast; accrual vs cash **contrast-pair** (no duplicate 3-box) |
| [ch02-qualitative-characteristics.html](ch02-qualitative-characteristics.html) | Qualitative characteristics | One denser hierarchy+contain plate: Relevance nests predictive/confirmatory + materiality; Faithful representation inner cells; four enhancers as inner grid; cost constraint |
| [ch03-reporting-entity.html](ch03-reporting-entity.html) | Reporting entity | Ch3 L1 horizontal (Entity \| Going concern \| Boundary); group/org chart (parent–sub) + party icons; Boundary containment (Consolidated / Unconsolidated inner cells); compare table; mini boundary tree; thin IFRS 10 / IAS 27 see-also |
| [ch04-elements.html](ch04-elements.html) | Elements | **Formula board**: Asset − Liability = Equity; Income/Expenses inside Equity via `.contain` / `.contain-grid` / `.contain-cell`; UoA tip 4.6; N.x jump chips; side legend. Checklists live in chapter body only. |
| [ch05-recognition-derecognition.html](ch05-recognition-derecognition.html) | Recognition & derecognition | Recognition filters tree (untouched spine); pre-2018 vs 2018 **contrast-pair**; derecognition twin-aim + full/partial **contrast-pair** |
| [ch06-measurement.html](ch06-measurement.html) | Measurement | 3-col HC / current value / selection; **card-grid measurement-basis matrix** (primary); selection-factors concept map; selection considerations as unordered **peer-row** (not numbered pipeline); thin IFRS 13 see-also |
| [ch07-presentation-disclosure.html](ch07-presentation-disclosure.html) | Presentation & disclosure | Communication-principles concept map; statement-layout schematic with **inner classification cues**; IFRS 18 dashed see-also; separate CF classification grid folded into stmt chips |
| [ch08-capital.html](ch08-capital.html) | Capital | Financial vs physical 2-col contrast + formula/identity cues under each; profit-determination table; small IFRS-practice≈financial-capital callout |
| [ch09-status.html](ch09-status.html) | Status & use with Standards | Hierarchy stack (Standards over CF); purpose triad; **full IAS 8 gap-fill flowchart** |

## Shared
- [shared.css](shared.css) — low-fi chrome shared by all 9 HTML files (+ concept-map, party-cast, org-chart, formula-cue, **formula-board**, start-here, stmt-layout, **matrix card-grid**, contrast-pair, peer-row, catalog-grid helpers)
- Legend + semantic colour tokens in `shared.css` (`.legend` helpers; role/elem/outcome/see-also/stmt/formula/org tokens wired to utility classes) — cheap pass on ch01/02/03/04/06/07/08/09
