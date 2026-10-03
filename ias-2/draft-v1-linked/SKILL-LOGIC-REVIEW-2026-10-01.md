# IFRS teaching skills — logic review (code-review style)

**Date:** 2026-10-01 (Asia/Shanghai)  
**Reviewer:** Grok Bot (executor) for Johnny Pang  
**Scope:** `ifrs-teaching-body`, `ifrs-teaching-body-qa`, `ifrs-visual-grammar` (+ IAS 2 METHOD skim)  
**Bar:** comprehensive; fix real contradictions / gaps / duplicate conflicting rules; preserve Johnny locks  

---

### 1. Inventory — what each skill owns (single responsibility)

| Skill | Owns | Must not own |
|-------|------|--------------|
| **IFRS teaching body** | Authoring rules for teaching `<article>` HTML: research essence, cite grammar, Illus format (ALL worked-strip + neutral peers), densify / title essence / hyperlink procedures, global formatting grammar, pack sources, repeat-mistake lock, post-edit QA pointer | Concept Map draw method; Map § circle chrome; inventing Map layouts |
| **IFRS teaching body QA** | Mandatory gate after any body edit: automated fail patterns mirroring HARD locks (cite, all-strip, neutral peers, markup, densify quant, title essence, hyperlink); process gate A–F before sync | Authoring how-to essays; Map redesign |
| **IFRS visual grammar** | Concept Map / chapter visual **method spine**: story → visit path → logic→type → draw; Map product locks; green/red on decision-tree outcome leaves | Teaching-body Illus peer colour; cite chip `§` rules (Map `a.fb-num` ≠ `.cite`) |
| **IAS2-CONTENT-REWRITE-METHOD.md** | Pack-local standing notes (chapter map, sources, phase). **Skills win** on HARD Illus locks if METHOD drifts | Parallel conflicting Illus format law |

**Control principle:** teaching-body = write; teaching-body-qa = gate; visual-grammar = Map/visual spine. One lock → one canonical statement; superseded text marked or deleted.

---

### 2. Control flow — when to run teaching-body → QA → sync; where visual-grammar sits

```
Johnny unlocks body pass (Map parked)
        │
        ▼
[IFRS teaching body]  author / rewrite chapter HTML
        │
        ▼
[IFRS teaching body QA]  A cite → B all-strip+neutral → C markup
                         → D densify quant → E title essence → F hyperlink
        │
        ├─ any FAIL → fix → re-run QA
        │
        ▼
Documents sync + report green checklist
```

| Pass type | Run | Skip |
|-----------|-----|------|
| Cite / Illus / densify / title / link body edit | teaching-body rules + **full QA A–F** | visual-grammar draw; Map iframe/cache-bust |
| Structure / id / renumber | teaching-body hyperlink procedure + **QA F** (plus A–E if Illus touched) | Map edits |
| Concept Map / chapter visual (only when Johnny unlocks) | **visual-grammar** §§0–2 | teaching-body content dump into Map |
| CF / I18 cite+title+Illus rollout | **WAIT** Johnny IAS 2 trial OK | Mass-apply now |

**visual-grammar sits beside body, not in the body sync chain.** Content passes leave Map alone. Ownership table in visual-grammar (2026.10.01-17) forbids applying Map leaf green/red to Illus worked-strip peers.

---

### 3. Contradictions / dead rules — found and disposition

| # | Conflict | Where (pre-fix) | Disposition |
|---|----------|------------------|-------------|
| **C1** | “Simple Facts/Assessment `.box` OK for short conceptual” **vs** “ALL Illus worked-strip” (Done when / QA / Johnny lock) | teaching-body chooser + “Simpler plates” + mandatory #6 + workflow #3 **vs** Done when / QA C | **FIXED** — single HARD: ALL Illus = worked-strip; simple `.box` Illus marked **SUPERSEDED**; short conceptual = Facts|Assessment peers inside strip |
| **C2** | Reference shapes / example HTML with `.box.ok` / `.box.warn` on Illus **vs** “all peers neutral” | teaching-body 4.5.x refs + worked-strip HTML sample; QA B.3 “neutral / ok / warn per teaching meaning” | **FIXED** — refs + samples all neutral; QA B/C say meaning is in label text, not fills; ok/warn only non-Illus contrast / Map leaves |
| **C3** | Product intent “ok/warn contrast” readable as Illus-allowed | teaching-body dual mandate line | **FIXED** — clarified ok/warn **outside Illus**; Illus peers all-neutral |
| **C4** | Crypto cite worked-example still a lone `.box` Illustration | teaching-body §D | **FIXED** — rewritten as worked-strip + neutral Facts|Assessment |
| **C5** | Official · § vs para | teaching-body / QA already locked `para` / no `§` in chips | **No conflict** (canonical). METHOD prose may still say “§16” in chapter maps — OK as Official para shorthand in notes, not chip text |
| **C6** | Structure PASS vs densify PASS | Partially mirrored; post-edit QA list incomplete | **FIXED** — teaching-body post-edit gate lists densify quant + title + link; QA process **A–F** (was A–C only); Done when separates D/E/F |
| **C7** | visual-grammar Map green/red **vs** Illus neutral | No explicit ownership; § chips could confuse with cite `§` ban | **FIXED** — ownership table + Colour line Illus exclusion + Map § circle chips ≠ cite chips |
| **C8** | QA section lettering scrambled (A, B0, B, C, E, F, D) | teaching-body-qa | **FIXED** — renumbered A–H cleanly |

---

### 4. Gaps — Johnny-demanded automated checks

| Demand | Pre-review | Post-review |
|--------|------------|-------------|
| Densify quantitative (≤5 bullets OR ≲350 chars = FAIL densify) | Present in both skills | **Kept**; post-edit QA + process gate now force D |
| Title essence (no bare Official:/DTT:/PwC:/IFRS 15: leads) | Present + rg patterns | **Kept**; process gate E explicit |
| Hyperlink review after structure change | Present + rg/python hint | **Kept**; process gate F explicit |
| Repeat-mistake → lock skill+QA with automated check | Present both | **Kept**; QA G mirrors teaching-body |
| ALL Illus worked-strip fail pattern | Weak / conflicting | **Added** QA B + shell spot-checks |
| Neutral peers fail pattern | B0 present; B.3 contradicted | **Aligned**; shell check for `box ok|warn|danger` inside worked-strip-grid |
| CF/I18 wait flag on QA | Implicit | **Added** trial scope line on QA |

**Still deferred (not a skill contradiction):** shipping a single pack-wide python densify/href walker as a checked-in script — skills specify the gate; implement when next densify pass runs.

---

### 5. Fixes applied — exact skill edits

#### `ifrs-teaching-body/SKILL.md`
1. Dual mandate: ok/warn contrast scoped **outside Illus**; Illus peers all-neutral pointer.
2. Replaced Illustration chooser + “Simpler plates” with **HARD — ALL Illustrations = worked-strip**; SUPERSEDED row for simple `.box`.
3. Reference shapes 4.5.1–4.5.3 → **neutral** (removed `.ok`/`.warn`).
4. Worked-strip sample HTML: Conclusion peer no longer `class="box ok"`.
5. Crypto cite example → worked-strip + neutral Facts|Assessment.
6. Container chooser: Illustration (ALL); Illustration (simple) marked SUPERSEDED.
7. §5 ok/warn: **Illus exclusion (HARD)** paragraph.
8. Mandatory format #6 + per-chapter workflow #3 → ALL worked-strip + densify/title/link.
9. Post-edit QA gate expanded to cite / neutral+all-strip / markup / densify quant / title / hyperlink.
10. Done when Illus line: explicit **neutral** peers.

#### `ifrs-teaching-body-qa/SKILL.md`
1. Full gate rewrite with stable **A–H** letters.
2. Ambition: ALL worked-strip (not “preferred”).
3. **B** = format + peer colour (all-strip fail + neutral fail + shell checks).
4. **C** peer labels: meaning in text, not ok/warn fills (removed conflicting B.3).
5. **D/E/F** densify / title / hyperlink unchanged in substance; process **H** runs **A–F**.
6. Trial scope WAIT CF/I18; Structure PASS ≠ densify PASS called out up front.
7. Done when lists A–C / D / E / F separately.

#### `ifrs-visual-grammar/SKILL.md`
1. Version → **2026.10.01-17**.
2. **Ownership vs teaching body** table (Map leaves vs Illus neutral vs cite chips vs Map § circles).
3. Colour rule: does not apply to teaching-body Illus grids.
4. Product lock: § circle chips = Map chrome only; not teaching cite chips.

#### `IAS2-CONTENT-REWRITE-METHOD.md` (pointer only)
1. Skills list + QA skill link.
2. One-line HARD Illus locks pointer (skills win on drift) + link to this review.
3. Soft SUPERSEDED on “or a single `.box` when one plate is enough”.

**Not weakened:** Johnny product / cite / Illus densify / title / link / repeat-mistake / IAS 2 trial / firm-colour-on-chips-only locks.

---

### 6. Residual risks / deferred

| Item | Status | Reason |
|------|--------|--------|
| **CF / I18 cite + title + Illus rollout** | **WAIT** | Johnny IAS 2 trial OK required — flagged in all three skills + QA |
| **Map / Concept Map body pass** | **Parked** | visual-grammar ownership; content passes do not touch iframe/cache-bust |
| **METHOD still has older checklist wording** in places (e.g. “Prefer box/strip” remnants beyond the one line fixed) | Acceptable drift | Skills are canonical; full METHOD rewrite out of scope; pointer added |
| **Pack HTML may still contain old simple-list Illus or ok/warn peers** | Content debt | Skills now FAIL those; next body/QA pass must remediate live HTML |
| **Checked-in densify/href python harness** | Deferred | Gate specified; script can land on next densify run |
| **QA shell `rg -nU worked-strip-grid…ok`** can false-negative on large grids | Known | Prefer python walk; rg is spot-fail aid |

---

### Re-read confirmation (§3)

After edits, re-read all three skills:

| §3 item | Resolved? |
|---------|-----------|
| C1 simple vs ALL strip | **Yes** — one HARD + SUPERSEDED |
| C2 ok/warn on Illus | **Yes** — samples/QA/ownership aligned |
| C3 product ok/warn wording | **Yes** |
| C4 crypto example | **Yes** |
| C5 Official § vs para | **Already OK** / deferred METHOD prose shorthand |
| C6 structure vs densify | **Yes** — dual gate in author + QA process |
| C7 visual-grammar vs Illus colour | **Yes** — ownership table |
| C8 QA lettering | **Yes** |

**Verdict:** Skills are **coherent enough to stop re-arguing densify / title / link / all-strip / Illus-neutral**. Further argument should be HTML remediation against these gates, not skill re-litigation — unless Johnny raises a new defect class twice (repeat-mistake lock).

---

### Sync

- Audit path (box): `/workspace/ifrs-website/refs/ias-2/draft-v1-linked/SKILL-LOGIC-REVIEW-2026-10-01.md`
- CopyFromBox to Documents `ias-2` draft folder: **pending** if laptop offline at review time (see agent report).
