# IAS 2 — Worked-strip colour SAVE (2026-10-01)

**Owner:** Design executor · Johnny LOCK · PM reports  
**Pack:** `refs/ias-2/draft-v1-linked/` (preview symlink → same)  
**Lock:** Johnny LOCK OVERRIDE — **all Illustration peer columns NEUTRAL**. No ok/warn fills at all (not even include/exclude). Supersedes Option A carve-out in the proposal.

## Applied

### CSS (`assets/shared.css`)
- `.worked-strip` shell: `background: var(--surface)` (was `--band`). Border kept.
- Belt-and-suspenders: `.worked-strip .box.ok` / `.box.warn` forced to surface + `--line` border; titles `--muted` (match peers).
- **No** `.include` / `.exclude` colour rules (Johnny: no fills).
- Outside strips: contrast-pair / decision ok/warn unchanged.
- Night tokens still remap via vars — no hard-coded colours.

### HTML class cleanup (ch01–ch06)
- Stripped `.ok` / `.warn` from every peer `.box` inside `.worked-strip`.
- Stripped Illus-standalone peers: Illus 3.6.3 nested contrast-pair (Include / Expense); Illus 3.10.3 LIFO shell (`box.warn` → `box`).
- **Kept** teaching contrast-pair (not Illus peers): ch02 Inventory / Not this chapter’s asset.
- Teaching prose unchanged. No Content densify rewrites.

## Counts

| | |
|--|--:|
| ok/warn **removed** from Illus peers | **55** |
| ok/warn **kept** (teaching contrast-pair) | **2** (ch02 only) |
| `.include` / `.exclude` added | **0** |

By chapter removed: ch01 5 · ch02 4 · ch03 32 · ch04 13 · ch05 1 · ch06 0.

## Files touched
- `draft-v1-linked/assets/shared.css`
- `draft-v1-linked/ch01.html` … `ch05.html` (ch06 no class change)
- This SAVE note; proposal note marked applied/overridden

## Documents sync
Twin found: `C:\Users\johnny\Documents\ifrs-website-refs\refs\ias-2\draft-v1-linked`  
**Synced OK (2026-10-01 ~15:16 CST):** `shared.css`, `ch01`–`ch05.html`, this SAVE, proposal note.

## Leftovers
- ch02 teaching contrast-pair still uses `.ok` / `.warn` (intentional — not Illus).
- CSS neutralize only scopes **inside** `.worked-strip`; standalone Illus peers rely on HTML strip (done). If Content later re-adds `ok`/`warn` inside strips, CSS keeps them visually neutral.
- visuals/*.html: no worked-strip ok/warn paint to change.
- No mid-edit Content densify conflicts observed; colour/classes only.

## Proposal status
`IAS2-WORKED-STRIP-COLOUR-PROPOSAL-2026-10-01.md` — Option A superseded by full-neutral LOCK; see SAVE.
