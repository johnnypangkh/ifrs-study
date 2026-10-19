# DIFF — MF §10 revisit (clarity)

**From:** signed §10 in `MAP-MASTER-FORMATTING-PAGE-98.md` (~11:07 HKT) and `ba-mf-master-revise.png`
**To:** `MF-SEC10-FAIL-ADDENDUM-98.md` §10.10 + `mf-sec10-gate.html` · render `mf-sec10-gate-1280.png`
**Chrome lock:** the signed BA is not edited. Label and card-text swaps are PROPOSE only.

Johnny: PM 跟住 Dep 嘅短 label 去估，因為 MF 冇寫明缺格、矮 rail、同軸下面再加一條 band 算唔算 FAIL。而家四條測試寫死。第二條 band（Reval ◆）= FAIL。事件打喺 kit 25 軸上先算過。左 rail 縮成一行、蓋唔到個 beat = FAIL。

---

## What was unclear → what this writes

| # | Unclear on signed §10 | What §10.10 writes |
|---|---|---|
| 1 | §10.2 says the left rail lists groups / phase / outer. It never says a missing or empty rail cell fails. PM could treat a gap as optional. | **Missing grid = FAIL** for every beat that needs a name (peer, section, phase, each nest row). Empty cell, no cell, collapsed column, and one rail shared by two names are the same fail. Exception only when Johnny writes one sentence on that mock. |
| 2 | Equal height ≤2px and “parent covers children” live in visual-grammar, not on the MF page. The §10 schematics stretch, and the page never says a mismatch fails. | **FAIL** when rail vs detail `\|Δtop\|`, `\|Δbottom\|`, or `\|Δheight\|` **> 2px**. The parent rail vs its child board is that same pair. Do not subtract padding. Centered words inside a stretched rail stay legal (signed Dep). |
| 3 | Phase card says both “rings ON axis · optional markers” and “no YE markers on signed lock”. §9 min still draws **Year-end** on the axis. Dep dropped the Year-end **band**. Reval kept a ◆ **band** under kit 25. Three readings were possible: markers banned, markers required, or a second band required. | **One axis.** Events of this phase sit **on** the kit 25 axis (one mark, one label). Begins/Ceases belong to that axis. A **second band** under the ends (`.reval-date-row`, Dep’s old `.lc-band`, live Impairment `.lc-band`) = **FAIL**. Dep’s dropped YE band stays dropped on Dep. Year-end review on Dep is the 5.8 rail, not a band. Reval may drop the dates or move them onto the axis (audit P1/P2, still Johnny). The band fails either way. |
| 4 | “L1 short stub vs beat” was not a stated test. Live `.lc-head-k` is a short label (`align-self: end`). Signed Dep stretches the rail. PM followed the stub. | **Yes, FAIL.** L1 here means the outer left rail of the beat, not atlas `.m-l1`. A text-height phase or outer rail that misses the beat by more than 2px fails. Reval punch3 L1 stretch stays. A nested peer that matches its own short detail passes. A dropped plate title is not a stub. |

## What did not change

- Three building blocks: `.inner-rail` label, Phase + kit 25, nested `.inner-rail`. No fourth component.
- Essence labels (`Phase`, `Peer`, `Outer`, `Start`, `End`, `marker`). No chapter paragraphs added to the templates.
- `#27` thick-left stays When-not for Dep.
- Tokens, atlas 1–23, dep-v2 freeze, kit 25 geometry.
- No Build. PR #163 not touched.

## Sentences the gate overrides until the card edit is signed

| Signed sentence | Gate reading |
|---|---|
| “no YE markers on signed lock” | Dep chapter lock only. Not a ban on on-axis markers. Not a pass for a second band. |
| “optional markers” | Markers of this phase go on the axis. The second band is not the optional form. |
| §9 min “Year-end” ×2 and “Depreciate over useful life” | Specimen labels on the frozen BA. Not an order to restore Dep’s band. Relabel is PROPOSE P3. |
