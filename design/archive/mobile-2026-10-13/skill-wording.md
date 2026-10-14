## ifrs-site-rules/SKILL.md
5:  module: top bar, pills, search, Desktop|Mobile switch, map frame/iframe width,
25:1. [ ] **Shared = one module, site-wide by default.** Each of these is exactly one `refs/_shared/` module (CSS + JS) that every pack loads with no per-pack switch: top bar / `header.chrome-bar`, pack title cluster + Last update stamp, tag pills / chapter pills, section `top` pill, search (`refs/_shared/search.js` + generated index), Desktop｜Mobile switch, Concept Map frame + iframe width / fit, left rails and inner rails, boxes and peer grids, formula / ledger rows, timeline, arrows / connectors, cite chips, See also strip, decision forks, design tokens.
32:8. [ ] **Acceptance shots** for a shared change: one chapter page each of IAS 2, CF 2018, IFRS 18, IAS 16 (plus homepage when it carries the component) at 390 / 922 / 1280 — proved in L3.
38:| Measured Map QC (arrow, gap, text-clip, layout) | 390 / 667 / 922 / 1280 |
39:| Human visual scan | 390 / 922 / 1280 |
40:| UX user-task walkthrough | 390 / 922 |
41:| Decision forks + See also strips (minimum) | 390 + 1280 |
46:- No hardcoded formatting value in any CSS or inline `style=` — tokens from MASTER-STYLES.xlsx via `_shared/tokens.css` and `_shared` modules only (lint report-only until each pack's #71 PR; hard fail from PR8). Breakpoints are `--bp-mobile` 560px and `--bp-wide` 800px, written into `@media` by the generator at build time (CSS vars cannot be used in media queries).
69:- Desktop｜Mobile switch sits next to the pack title, smaller than the title; search gets the remaining width so a full query stays visible (UX walkthrough in L3).
87:- **Cite chip commas:** added by CSS, never typed; hidden at `max-width: 560px` so no line starts with a comma.
## ifrs-visual-grammar/SKILL.md
51:- **Desktop process flows left → right.** Mobile vertical is allowed as an exception (timeline ≤800px, fork elbows). DOM order = reading order; never CSS `order:`.
81:| Pervasive constraint | Side rail spanning the stack (narrow: drops below) | A third tier |
118:1. **Hierarchy + side rail** — stack; tier→tier labelled flow (tip up); rail↔tiers link; items collection. Narrow: rail = one bar below.
187:1. **Mobile (`--bp-mobile`, max-width 560px):** a fork always keeps a visible branch and never reads as a linear chain. Question and branch side by side if they fit; otherwise branch hangs under the question, indented on an elbow. No arrow may leave a terminal outcome box. Main path runs straight down. DOM order = reading order, no CSS `order`.
190:4. Breakpoints: target `--bp-mobile` 560px / `--bp-wide` 800px; enforced per pack in PR4-7 (other @media widths in _shared/packs remain until that pack's PR).
231:- **Narrow cell → adjust within architecture (principle, not a hardcoded px recipe).** If a grid cell is too narrow for its text (heavy wrap, many forced rows), rethink column widths/heights *inside* the existing table design so text fits. Prefer: slim internal row-labels, redistribute spare inside a parent column, modest padding/row-height. Do **not** break established alignments (e.g. Cost-model column and Revaluation-model column each fully vertically aligned across lens rows) to buy width — breaking alignment is usually wrong unless the redesign is deliberate and justified. (Johnny 2026-10-10 teaching note.)
268:- Narrow: operators stay readable; default to layout 3.
270:- **Formula row widths:** result box deliberately NOT the term width; terms equal width and evenly distributed; operators in fixed narrow equal columns (no empty column, no floating `+`). A row under a formula is independent of the formula columns; its title tab is the same width as the box beneath it.
282:- At ≤`--bp-wide` (800px) the timeline turns vertical (axis down the left, start flag top, lanes beside, end flag bottom, downward arrowhead).
283:- Every tick / axis / lane label sits wholly inside its frame, ≥ 4px from any border, divider or axis line, at every width incl. vertical mobile (L3 text-clip; control = ch05 Year-end ticks).
344:| IFRS 18 Ch2 | Role peers + shared rules + checklist | Same-format peers, no hub; one shared panel (incl. materiality); matrix as principles, headers not yes/no; narrow restack; student-voice trap | 3 |
346:| IFRS 18 Ch4 | Subtotals + measure regimes | Subtotals = rule line + full name; double rule on final; no `+` on bands; one-subtotal rail (narrow: indented under); section chip once; regimes as same-format cards; trap under its regime; cut layout legends | 6+1 |
## ifrs-teaching-body/SKILL.md
149:- Steps read L→R on desktop, stack T→B narrow; step heads are technical labels, no "1 / 2 / 3".
150:- A question step never shares a box with its outcomes. End-of-flow decisions use the branch kit: question → join → bar → one labelled arm per outcome (label mid-arm) → one outcome step each. Narrow: join and bar run down the left edge, arms point right into stacked outcomes (fork layout per visual-grammar).
## ifrs-teaching-body-qa/SKILL.md
30:**Widths** (sole home of numbers: [site rules](sand-workflow:ifrs-site-rules) §2): measured §3 at 390/667/922/1280; human scan §5 at 390/922/1280; UX §6 at 390/922.
43:2. [ ] FAIL if a shared change was shot on fewer than IAS 2, CF 2018, IFRS 18 and IAS 16 (plus homepage when it carries the component) at 390/922/1280.
50:9. [ ] See also strip: CSS `::before` `·`, no typed `·`/arrow in HTML, no typed comma between cite chips, wrap keeps bit with its `·`. At 390 FAIL if a row starts with a comma or a bit splits from its `·`.
60:## 3. Map / visual measured checks (390 / 667 / 922 / 1280)
77:FAIL if: a fork reads linear at 390px; an arrow appears to leave an outcome box; text overlaps or drops to one word per line; a badge renders as an oval; a concept map at 1280px has more than 3 fork columns; fork layout uses a fixed px width or CSS `order`; a mobile fix changes desktop rendering.
101:1. [ ] Full-map (or full-page chrome) screenshots at **390 / 922 / 1280**.
104:4. [ ] Pass needs the zone list with "seen at 390 / 922 / 1280" for each zone.
107:## 6. UX user-task walkthrough (390 and 922)
110:2. [ ] **Desktop｜Mobile switch:** tap both states; label readable; hit target comfortable on 390; page actually changes; switch does not push or crowd title or search.
112:4. [ ] **Read Concept Map on mobile (390):** scroll whole map; every label readable without zoom; no clipped text; no sideways scroll; reading path obvious.
## ifrs-website-pm/SKILL.md
25:3. **Mock** if new layout/visual (922 + 390), iterate till Johnny OKs. Gate: mock-first. (§1.3)
48:  L -->|yes| D1[Design: mock 922 + 390, self-checked]
88:3. [ ] **Detailed brief:** exact wording, widths, acceptance points. If new layout → static HTML mock on the box (922 + 390), iterated with Johnny until agreed. Brief must contain a **Skill locks touched** table: `Lock | L1 section ref | How met` — fill only section refs (e.g. `site-rules §1`), never copy lock text. No table = do not send.
191:4. [ ] Do not narrow a stated requirement; ask first if a smaller scope seems needed.
## cursor-cloud-opus-fable-launch/SKILL.md
68:6. Rendered checks at 390 / 922 / 1280 with human visual scan crops (L3 §5).
