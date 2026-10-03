# Opus 5.5 — CF 2018 / IFRS 18 non-negotiables

Paste beside `OPUS-REVIEW-BRIEF-CF-IFRS18-2026-10-02.md`. **NO RUSH — quality over speed.** Johnny runs Opus in Cursor; Grok prepares the brief and reviews KEY CHANGES; Grok does not launch Opus.

## Locked work order

- [ ] Use **Opus 5.5 high**.
- [ ] Run one pack at a time; do not interleave CF 2018 and IFRS 18 chapters.
- [ ] Overall review of every page, Map/visual, References/end matter and relevant styles → amend chapters in order → pack Map last → consistency pass → KEY CHANGES handoff to Grok.
- [ ] Use the actual `{PACK}`, `{PATH}`, `{CHAPTERS}`, `{INPUTS}` and `{PACK MAP}` slots; do not assume IAS 2 filenames or chapter count.

## HARD prerequisite — STOP if shared links are missing

- [ ] Before Opus starts, verify Grok has applied Phase 1 + Phase 2 shared CSS wiring at the agreed C4/C6 checkpoint.
- [ ] Verify the selected pack uses `../../_shared/chrome.css`, `tokens.css` and `cite.css` as landed, rather than merely having shared files present.
- [ ] Use `refs/_shared/CHROME-MODULE-DESIGN-2026-10-02.md` as the module contract.
- [ ] If links/wiring are missing or stale: **STOP and report; do not invent chrome CSS, token ownership or cite colours.**
- [ ] Do not fork pack-local chrome/cite colours or edit shared CSS during the Opus run.

## HARD stop gates — no automatic continuation

After **each** item, update `OPUS-WORKING-MEMORY.md`, include desktop screenshots of the relevant page/Map/Illustration, send Johnny a status report, ask whether to continue, and wait for explicit **continue**:

- [ ] Overall review.
- [ ] CF 2018 Ch1, Ch2, Ch3, Ch4, Ch5, Ch6, Ch7, Ch8, Ch9, Ch10, Ch11 — if running CF 2018.
- [ ] IFRS 18 Ch1, Ch2, Ch3, Ch4, Ch5, Ch6, Ch7, Ch8 — if running IFRS 18.
- [ ] Overall pack Map enhance.
- [ ] Consistency pass.
- [ ] KEY CHANGES handoff to Grok.

Screenshots are mandatory even where a gate makes no HTML change. Do not begin the next pack after the first pack's handoff without Johnny's explicit continue.

**Viewport lock:** CF 2018 and IFRS 18 are desktop-only now. No mobile/iPad screenshots or layout passes.

## Detail / densify / duplication

- [ ] Keep Official + all supported pack Big4 substance; never densify-down.
- [ ] Thin only overlapping duplicate prose; keep one dense teaching unit.
- [ ] Preserve unique numbers, definitions, exceptions, tests, examples and firm-specific views.
- [ ] Same point across firms = write once + cite every supporting firm/source.
- [ ] Different firm views = preserve, label and show with `.callout.differ` or separate rows; never reconcile silently.
- [ ] No invent: no facts, examples, numbers, citations, source locators, links, gates or firm views.

## Shape, route and language

- [ ] FAQ ≠ Illustration; classify content shape, not source label.
- [ ] Case study / worked entity / numeric / multi-Decision-Test-Assessment logic = Illustration + `.worked-strip`; peer examples neutral.
- [ ] Reference matrices = sections/tables/lists, not Illustrations.
- [ ] Every screen reads **left → right, then top → bottom**, with clear **start → next → end**.
- [ ] Story order wins over section numbers; chip jumps may support navigation but must not make readers hunt.
- [ ] Reader-facing logic says **Decision / Test / Assessment**, never “Gate”.
- [ ] Technical-strict CF 2018 / IFRS 18 titles and Map labels only.
- [ ] Add diagrams/mini-flows/tables to complex teaching units when source-supported; do not flatten useful content.

## Map locks

- [ ] Check chapter-top/companion Maps and enhance the pack Map only after chapters.
- [ ] Pack Map must flow across chapters and provide a learner visit path.
- [ ] Do not add the Map lecture note “Section chips follow…”
- [ ] Do not use Map leaf green/red treatment for neutral Illustration peers.

## Shared modulisation locks

Grok landed shared modulisation since IAS 2:

- [ ] Use `refs/_shared/chrome.css`, `tokens.css`, `cite.css`.
- [ ] Preserve visible `Last update · YYYY-MM-DD HH:MM HKT`.
- [ ] Disclaimer remains at the bottom of page content immediately before footer navigation.
- [ ] References remains after the last chapter.
- [ ] Shared chrome/cite colours are not forked pack-locally.
- [ ] Do not reinvent shared CSS or typography-modularise in this run.
- [ ] Follow `CHROME-MODULE-DESIGN-2026-10-02.md`; report deliberate exceptions instead of silently changing the contract.

Short-form alignment example when the relevant works exist: `PwC MOA 2020 Ch25 · …`; `DTT iGAAP 2022 A11 · …`; `EY iGAAP 2026 Ch23 · …`; `KPMG Insights 2019/20 · Part 1 · 3.8`. This is only a grammar example. Use actual pack-supported works/locators; never invent them and never put `§` in `.cite`.

## Skills and QA

- [ ] Read current `/home/box/agent-data/workflows/ifrs-teaching-body/SKILL.md` (v2026.10.02 or newer).
- [ ] Read current `/home/box/agent-data/workflows/ifrs-teaching-body-qa/SKILL.md` (v2026.10.02 or newer).
- [ ] Read current `/home/box/agent-data/workflows/ifrs-visual-grammar/SKILL.md` (v2026.10.02-22 or newer).
- [ ] Read `refs/_shared/CHROME-MODULE-DESIGN-2026-10-02.md` and use the landed shared assets.
- [ ] QA is green for structure, route, body density, citations, hyperlinks, Maps, visual grammar and chrome; structure PASS alone is not enough.

## Product / source locks

- [ ] Ultimate study notes: the site should replace reopening source PDFs for covered topics.
- [ ] Big reorganise + visuals are allowed; no invent.
- [ ] CF 2018 sources come only from the pack's documented Official/DTT/PwC/EY/KPMG/other files; ACCA storyline is visit-path-only when so marked.
- [ ] IFRS 18 uses the documented Official/KPMG/EY sources and DTT only as the IAS 1 bridge; **no PwC invent** where it is not on disk.
- [ ] Missing source/chapter/visual = record and report, not fabricate.
- [ ] No mobile/iPad work, typography modulisation, Phase 3 primitives, whole-site rewrite or Documents sync.

## Durable memory and handoff

- [ ] Create/update pack-local `OPUS-WORKING-MEMORY.md` continuously and at every gate.
- [ ] Record decisions, traps, Map/Illustration conventions, write-once merges + cite chips, shared-asset verification, screenshots, blocked dependencies and Johnny approvals.
- [ ] Produce a per-pack KEY CHANGES report with material structural/visual/content moves, files changed, unresolved risks and screenshots.
- [ ] Final handoff explicitly confirms References remains after the final chapter and reports any exception.
