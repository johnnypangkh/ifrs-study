# Skill chrome locks — 2026-10-02 (HKT)

**Owner:** Grok Bot (executor)  
**Pack:** `refs/ias-2/draft-v1-linked/`  
**Skills touched:** `ifrs-teaching-body` · `ifrs-teaching-body-qa` · `ifrs-visual-grammar`

## Locks encoded (Johnny HARD)

| # | Lock | Where encoded |
|---|------|----------------|
| 1 | **Last update** — pack-level stamp `Last update · YYYY-MM-DD HH:MM HKT` (date **and** time), boxed beside pack title on **every** page; same stamp pack-wide | teaching-body § *Pack chrome locks* · QA § **J** |
| 2 | **Disclaimer — personal study pack** at the **BOTTOM** of every page (before `footer-nav`), never under title / top of Map | teaching-body § *Pack chrome locks* + Research essence personal-study line · QA § **J** |
| 3 | **References** page after last teaching chapter (IAS 2: after Ch6); nav `Map \| 1…n \| References`; table Full name \| Short form; **evidenced sources only** (cite chips / METHOD / XREF / pre-flight) — no invent | teaching-body § *Pack chrome locks* · QA § **J** |
| 4 | **NO Map lecture note** — do not put “Section chips follow the order of the decisions…” (or similar). Chip jumps OK (story order). Drift log = agents only. **FAIL if lecture note present** | visual-grammar Pack Map / jump board + §3 IAS 2 pack Map row + Before shipping 1g · QA **F3** flipped · teaching-body chrome §4 |
| 5 | Story order over section numbers stays HARD; viewport: IAS 2 desktop+mobile; CF / IFRS 18 desktop-only for now | visual-grammar §0 story-order + Viewport (restated) · teaching-body chrome §5 |

## Skill version / changelog bumps

| Skill | Version | Changelog line |
|-------|---------|----------------|
| IFRS teaching body | `2026.10.02` (kept) | Pack chrome locks (Last update date+time HKT; Disclaimer bottom; References after last chapter; no Map lecture note) |
| IFRS teaching body QA | `2026.10.02` (kept) | Pack chrome locks QA + **FAIL if Map chip-order lecture note**; flip old F3 “reader note required” |
| IFRS visual grammar | `2026.10.02-22` (was `-21`) | No Map chip-order lecture note (FAIL if present); chrome owned by teaching-body; viewport restated |

## Exact sections changed

### `ifrs-teaching-body/SKILL.md`
- Frontmatter changelog (2026.10.02 chrome locks lead).
- *Research essence* — personal-study unlock: disclaimer → **bottom of every page**.
- **New** `## Pack chrome locks (Johnny HARD 2026-10-02)` — Last update / Disclaimer / References / No Map lecture note / Viewport.
- *Done when* — pack chrome checklist bullet.

### `ifrs-teaching-body-qa/SKILL.md`
- Frontmatter changelog.
- **F3** item 3 flipped: chip jumps OK; **FAIL if Map lecture note present** (was “reader note present if chips jump”).
- **New** `## J. Pack chrome locks` + shell checks.
- *Done when* — F3 + **J** bullets updated.

### `ifrs-visual-grammar/SKILL.md`
- Version → `2026.10.02-22` + changelog.
- §0 Reading-order self-test — chrome list no longer treats lecture note as expected chrome.
- §2 *Pack Map / jump board* — remove “add muted reader line…”; **FAIL if present**.
- §3 IAS 2 pack Map row — drop “reader note on chip order”.
- §4 *Viewport* unchanged in substance; **new** *Pack page chrome* pointer to teaching-body.
- Before shipping **1g** — zero Map lecture note.

## HTML status (`draft-v1-linked`) — check-only this pass

| Check | Status |
|-------|--------|
| Last update `Last update · 2026-10-02 00:25 HKT` on index + ch01–06 + references | **Present** (pack-wide same stamp; date+time HKT) |
| Disclaimer `.pack-disclaimer` before `footer-nav` on every page | **Present / bottom** — no top-of-Map / under-title placement |
| Map chip-order lecture note (“Section chips follow…”) | **Absent** from `visuals/*.html` + `index.html` (was in an earlier pack-Map wave; not on live board now) |
| `references.html` after Ch6; tag-row includes References | **Present** (see `IAS2-REFERENCES-PAGE-2026-10-02.md`) |

No HTML rewrite required this pass. Sync not run.

## Not in scope
- Section restructure (still deferred).
- Documents sync.
- Re-stamp Last update time unless Johnny opens a new content wave.
