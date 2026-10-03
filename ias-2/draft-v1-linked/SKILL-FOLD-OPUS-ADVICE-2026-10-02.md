# Skill fold report — Opus 5.5 advice → live Grok Bot skills (2026-10-02)

**Advice:** `cloud-agent-artifacts/bc-db87b330-ac0f-5492-8cdd-19e13018c540/OPUS-SKILL-MD-ADVICE-2026-10-02.md`  
**Executor:** Grok Bot (step 5)  
**Date:** 2026-10-02 (Asia/Shanghai)

## Skills updated

| Skill | Path | Version |
|-------|------|---------|
| IFRS visual grammar | `/home/box/agent-data/workflows/ifrs-visual-grammar/SKILL.md` | `2026.10.02-21` |
| IFRS teaching body | `/home/box/agent-data/workflows/ifrs-teaching-body/SKILL.md` | `2026.10.02` (frontmatter added) |
| IFRS teaching body QA | `/home/box/agent-data/workflows/ifrs-teaching-body-qa/SKILL.md` | `2026.10.02` (frontmatter added) |

Each skill has a short **Changelog 2026.10.02** line at top. No IAS 2 HTML edited.

---

## Priority 1 — contradictions fixed

| Fix | Where |
|-----|--------|
| Reader-facing **Gate / Usual gate** → **Decision / Test / Assessment / Requirement** | TB preferred-layout row; QA C3 peer labels + `rg -w` ban note |
| Stale Ch4 **4.5.1–4.5.3** live-id reference shapes deleted; replaced with shape descriptions (no live ids) | TB Illustration preferred layout |
| Leaf colour: **red** = true hard stop ≤1/board; **muted** = not-X; **no green** by default on decision leaves | VG ownership table; §1 step 6 pointer; new **Colour on decision leaves**; Colour section |
| Method word **gate → decision** throughout VG (so forbidden label cannot leak) | VG description, §0–§3, IFRS 18 method rows (“Decision spine”, etc.) |

---

## Pasted (highest-value §3 patches)

### `ifrs-visual-grammar` (VG-1…VG-14 + IFRS 18 readiness bullets)

- **VG-1** Reading-order self-test — procedure (chrome / narrate / FAIL words / DOM)
- **VG-2** DOM order is reading order
- **VG-3** Column convention (continuing left / terminal right)
- **VG-4** Fork grammar (question + mid-arm labels)
- **VG-5** Colour on decision leaves
- **VG-6** Mistake classes: orphan / decision-as-statement / outcomes-in-one-box / continuing-on-right
- **VG-7** Equations and sums (L→R + operators; stack only with operators)
- **VG-8** Pack Map / jump board (mirror chapter Maps; disclosure by statement; chip-order reader note)
- **VG-9** Section-order drift log
- **VG-10** Map chips = target section numbers
- **VG-11** Words on the page vs words in this skill
- **VG-12** Viewport scope (IAS 2 desktop+mobile; CF/I18 desktop-only)
- **VG-13** IAS 2 Ch1/Ch3–Ch6 + pack Map method rows in §3
- **VG-14** Before shipping 1e / 1f / 1g
- **IFRS 18 readiness** (from advice §4): statement schematic vs decision board; nest disaggregation; group disclosure by destination — short subsection under §4

### `ifrs-teaching-body` (TB-1…TB-9)

- **TB-1** Gate→Requirement labels + shape descriptions (above)
- **TB-2** Sources differ — `aside.callout.differ` (flag, do not reconcile)
- **TB-3** Home chapter and pointers (pack-level write-once)
- **TB-4** Body mini-flow grammar (question never shares box with outcomes)
- **TB-5** Point-chips / editorial / author meta ban
- **TB-6** Source on disk but not attached to this run
- **TB-7** FAQ demotion keeps old id
- **TB-8** Container chooser row for sources-differ callout
- **TB-9** Cache keys move together (visual CSS + iframe + draft.css)

### `ifrs-teaching-body-qa` (QA-1…QA-7)

- **QA-1** C3 peer labels (Requirement / Assessment)
- **QA-2** F2 Visual reading-order gate (BLOCKING)
- **QA-3** F3 Pack Map mirror + drift log
- **QA-4** F4 Automated checks (`rg -w` gate; CSS `order:`; red-leaf count; fork arms; cache keys; differ callout; point-chips)
- **QA-5** H.9–10 one-writer-per-file; exclude `uploads/`
- **QA-6** Done-when rows for F2/F3/gate/differ/regression
- **QA-7** H6 → run F2 (+ F3 for Maps)

---

## Deferred (advice present; not folded into skill prose this pass)

| Item | Why deferred |
|------|----------------|
| Advice **§1 “what worked”** keep-as-is list | Already encoded; no edit needed |
| Advice **§5 anti-patterns** as a dedicated numbered FAIL list | Covered by pasted FAIL classes / F2 / colour / Gate ban; full 20-line ban list not duplicated to avoid bloat |
| **VG-13 IFRS 18 Ch* existing rows** rewrite of “gate spine / fail-outs” wording inside old §3 I18 rows | Decision-spine wording updated where touched (Ch6); older CF/I18 rows left mostly as signed history — new IAS 2 rows + IFRS 18 subsection carry forward rules |
| Full **`tools/pack_audit.py` implementation** of F4 Python checks | Skill documents the checks; code change is a later tooling pass |
| **Build chrome** debt (iframe ratchet, `.worked-strip-grid` fixed 3-col) as QA regressions beyond iframe-fit ≤3px | F4 notes iframe-fit check; deeper Build ownership stays outside content skills |
| **§2.19 / §2.20** residual Build/cache detail beyond TB-9 + F4 | Partial (cache keys + iframe fit); Build CSS grid quirk not skill-owned |
| Live IAS 2 HTML / Maps | Explicitly out of scope for this fold |

---

## Parallel executor check — references.html / last-update

**Status: complete** (do not restart).

Evidence under `draft-v1-linked/`:

- `references.html` present (2026-10-02)
- `IAS2-REFERENCES-PAGE-2026-10-02.md` marks Tasks A+B done: References nav after Ch6, Last update pill `2026-10-02` on index + ch01–06 + references, CSS `.chrome-last-update`, cache `?v=ias2-refs-lastupdate-20261002`
- Task C (modularisation) deferred by that note — not this fold’s work

---

## Success checklist

- [x] Three skills updated + version/changelog bumped
- [x] Contradictions fixed (Gate labels, stale 4.5.x shapes, leaf colour)
- [x] Highest-value §3 patches pasted
- [x] No invent beyond advice; no IAS 2 HTML edits
- [x] This fold report written
