# IFRS 18 — shell scaffold notes (2026-09-27 Asia/Shanghai)

## Copied from CF pack (`refs/cf-2018/draft-v1-linked/`)

Into `refs/ifrs-18/draft-v1-linked/`:

- `assets/theme.js` (night-only force-dark)
- `assets/draft.css` (body/chrome kit)
- `assets/map.css`
- `assets/iframe-fit.js`
- `assets/shared.css` (pack-local body kit — CF had no separate “root” shared outside draft assets)
- `visuals/shared.css` (Concept Map / visual kit)

Titles adapted for **IFRS 18 Presentation and Disclosure**. Map-only shell; no CF ch01–ch10 HTML content copied. No chapter stub (Map has no live chapter link yet). Teaching-structure brief `IFRS18-TEACHING-STRUCTURE-2026-09-27.md` was **missing** at scaffold time → “chapters landing soon” band used.

## Known debt (ARCHITECTURE)

Assets remain **pack-local** copies (same as CF today). `ARCHITECTURE.md` already flags: extract `theme.js` / body-kit CSS to a shared library before more packs proliferate. Do not invent a new visual language — keep copying CF kit until Build consolidates.
