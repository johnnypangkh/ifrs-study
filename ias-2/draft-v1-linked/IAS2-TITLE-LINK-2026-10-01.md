# IAS 2 — Title essence + internal hyperlink fix (2026-10-01)

**Pack:** `refs/ias-2/draft-v1-linked/`  
**Backup:** `/workspace/ias2-content-extract/ch0N-before-title-link-20261001-154320+0800.html`  
**QC stamp:** none (Johnny trial)

## A. Title essence fixes (teaching leads — cite chips untouched)

| File | Location | Before (lead) | After (lead) |
|------|----------|---------------|--------------|
| `ch02.html` | Illus 2.1.2 Usual gate | `IFRS 15: a product delivered…` | `<strong>No revenue while dealer lacks control (IFRS 15 consignment):</strong> a product delivered…` |
| `ch02.html` | Illus 2.1.2 Usual gate | `DTT: until the transfer…` | `<strong>Until transfer is substantive — manufacturer still holds inventory (DTT):</strong> until the transfer…` |
| `ch03.html` | Illus formula-change Assessment | `IAS 2:36(a) requires disclosure…` | `<strong>Cost-formula disclosure confirms policy status:</strong> IAS 2 para 36(a) requires disclosure…` |

Pack-wide `rg` after fix: zero bare `(IFRS 15|DTT|PwC|EY|Official|IAS 2):` teaching prefixes; zero bare `<strong>(IFRS 15|DTT|PwC|EY|Official).?</strong>` leads.

Left intact (substance already in lead): e.g. `DTT pipeline fill (recognition angle).`, `IFRS 15 hand-off for fulfilment costs…`, mid-sentence `PwC: an entity should…` after a teaching bold lead.

## B. Illustration 3.2.2 hyperlink

| File | Change |
|------|--------|
| `ch03.html` Illus 3.2.1 Principal | plain `see 3.2.2` → `see <a href="#s-3-ex-vol-rebate">Illustration 3.2.2</a>` |

Target confirmed: `<div class="worked-strip" id="s-3-ex-vol-rebate">` (Illustration: 3.2.2 — Volume rebate not yet fully earned).

## C. Pack-wide internal cross-ref audit

| Check | Result |
|-------|--------|
| Existing `href="…#…"` targets resolve | **41 OK / 0 broken** |
| Plain `see N.M(.k)` without `<a>` when target exists | **1 fixed** (3.2.2 above); **0 remain** |
| Invented ids | none |
| Orphan / missing targets | none found |
| Non-nav editorial text left unlinked | `Keep this plate on Chapter 1…` (placement note, not a jump target) |

## D. Skill lock

Patched (direct file edit, not UpdateSkill truncate):

1. `/home/box/agent-data/workflows/ifrs-teaching-body/SKILL.md`
   - **Title essence rule (HARD)** — extended empty-source-title table + `IFRS 15:` / `IAS 2:` / `DTT:` colon prefixes; Johnny rewrite examples; cite chips excluded.
   - **Hyperlink procedure (HARD)** — after structure/id change: (a) every Illus/section cross-ref is `<a href>`; (b) every href target exists; (c) numbers match; fail on plain `see N.M.k` when id exists; no fake ids.
2. `/home/box/agent-data/workflows/ifrs-teaching-body-qa/SKILL.md`
   - **E** retitled Title essence — expanded rg patterns.
   - **F Hyperlink review (HARD)** — automated fail criteria + Done checkbox.

## E. Self-QA (touched pack)

- Cite house-only / `§` in chips: green  
- `<p class="box-body"><ul`: green  
- Title essence rg: green  
- Hyperlink python audit: green  
- No invent; no QC stamp

## Deferred packs (not rewritten this pass)

Per Johnny: CF 2018 / IFRS 18 bare `DTT.` / `Official.` leads wait until IAS 2 trial OK.

| Pack | Pattern | Count |
|------|---------|-------|
| `cf-2018/draft-v1-linked` | `<strong>Official.</strong>` / `<strong>Official PRIMARY.</strong>` / `<strong>DTT.</strong>` / `<strong>PwC.</strong>` / `<strong>EY.</strong>` teaching leads | **30** lines (Official-family ~11; DTT. 6; PwC. 13; EY. 0) |
| `cf-2018` | bare `Official:` / `DTT:` colon-prefix style | **0** |
| `ifrs-18/draft-v1-linked` | same bare firm/Official leads + colon prefixes | **0** |

## Files changed this pass

- `ch02.html`, `ch03.html`
- `IAS2-TITLE-LINK-2026-10-01.md` (this file)
- Skills: `ifrs-teaching-body/SKILL.md`, `ifrs-teaching-body-qa/SKILL.md`
