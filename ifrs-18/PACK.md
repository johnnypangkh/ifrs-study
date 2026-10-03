# IFRS 18 pack inventory

Status: **UNLOCKED for draft** (Johnny go-ahead **2026-09-27**).
Official + KPMG + **EY MOA 2026** are sufficient to draft. **PwC IFRS 18 N/A** (Johnny: MOA only has IAS 1) — not a blocker. Optional: newer Deloitte IFRS 18 chapter.

Teaching structure brief: [`wip/IFRS18-TEACHING-STRUCTURE-2026-09-27.md`](wip/IFRS18-TEACHING-STRUCTURE-2026-09-27.md)

Teaching target: **IFRS 18** (site labels IFRS only; HKFRS = same). Effective periods beginning on/after **1 Jan 2027**. Replaces IAS 1 for presentation teaching.

## Items

### 0. Official — HKFRS 18 Presentation and Disclosure in Financial Statements
- File: `inputs/ifrs-18/official-hkfrs18-2026-06.pdf` (193 pages)
- Publisher: **HKICPA** (incorporates IFRS Foundation material)
- Edition marks: Revised **May 2025 / June 2026**; labelled HKFRS 18 (2027)
- Includes: Standard text + **Basis for Conclusions** + **Illustrative Examples**
- Authority: **PRIMARY** — all Big 4 checked against this
- Site labels: show **IFRS 18** only (no HKFRS dual code)
- Copyright: Foundation/HKICPA — teach/summarise; never paste verbatim

### 1. EY — **MOA 2026** / Applying IFRS: A closer look at IFRS 18 (Updated April 2026)
- File: `inputs/ifrs-18/ey-2026-04-applying-ifrs-closer-look-ifrs18.pdf` (185 pages)
- Role: **EY Manual of Accounting 2026** depth source for IFRS 18 (Johnny 2026-09-27) — FAQ/illustration indexes; check teaching against official

### 2. Deloitte (DTT) — A4 Presentation of financial statements (DART Volume A)
- File: `inputs/ifrs-18/dtt-2022-a4-presentation-fs-ias1.pdf` (77 pages) — **IAS 1 / pre-IFRS 18 bridge only** (do not structure the pack as IAS 1)

### 3. KPMG — First Impressions (June 2024)
- File: `inputs/ifrs-18/kpmg-first-impressions-ifrs18.pdf` (90 pages) — **primary visuals/structure flow**

### Closed / not blocking
- [x] **PwC IFRS 18** — N/A (Johnny 2026-09-27): PwC MOA only covers IAS 1 (bridge only, with DTT A4). Do not HOLD for PwC.
- [ ] Optional: newer Deloitte IFRS 18 chapter (not required for v1)


## Sticky chrome (single-source)

Config: [`chrome.json`](chrome.json) (pack title, Home, chapter tags).

After chapter add/renumber, edit `chrome.json` then regenerate:

```bash
node tools/generate-chrome.mjs ifrs-18
```

See [`tools/README.md`](../../tools/README.md). Targets: `draft-v1-linked/` Map + chapters only (not `visuals/`, `_archive*`).

## Site chrome (2026.09.28-1)

Homepage Open dual-path locked: READY Open → `../<pack>/preview/index.html` + `refs/<pack>/preview` → `draft-v1-linked`. See root `FOLDER-RULES.md` / `PRODUCT-SPEC.md`.
