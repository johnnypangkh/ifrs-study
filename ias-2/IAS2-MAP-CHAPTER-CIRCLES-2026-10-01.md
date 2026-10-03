# IAS 2 — Map / chapter circle badges → chapter section numbers (2026-10-01)

**Agent:** Grok Bot (local)  
**Pack:** `/workspace/ifrs-website/refs/ias-2/draft-v1-linked/`  
**Time:** 2026-10-01 ~14:12 Asia/Shanghai (UTC+8)  
**Trigger:** Johnny locked — circles must show **章節序號** (site chapter / body section numbers), not Official §§. Confusion case: Map Scope Inventories card showed **6**, Measurement board **9**.  
**Backups:** `/workspace/ias2-content-extract/*-before-chcircles-20261001-141055+0800.*`  
**Cache:** `?v=ias2-chcircles-20261001`

---

## Rule applied

| Layer | Circle digit | Official § |
|-------|--------------|------------|
| Map + chapter visual `a.fb-num` | Site **N** / **N.M** matching deep-link `#s-N-M` | Unchanged in body/chips |
| Range of Official §§ → **one** body section | Collapse to **one** circle with that **N.M** | — |
| Range of Official §§ → **two** body sections | Keep `.fb-num-range` with **N.M – N.M** (one digit per circle) | — |
| Mute chip `IN13` | Unchanged (not a section circle) | — |

Prefer **N.M** when the card deep-links a specific body section (IFRS 18 chapter-visual precedent). Map is a jump board (not a numbered content chapter). No Map redraw / Cost Build wireframe.

---

## Before → after (every circle)

### Map (`visuals/map-formula-board.html`)

| Topic | Before (§) | After | href (unchanged) |
|-------|------------|-------|------------------|
| Inventory asset (GO) | 6 | **1.1** | `ch01#s-1-1` |
| Full exclusion | 2 | **1.2** | `ch01#s-1-2` |
| Measurement only | 3–5 | **1.3** (collapsed) | `ch01#s-1-3` |
| Lower of cost / NRV (board) | 9 | **4.0** | `ch04#s-4-0` |
| Cost arm | 10 | **3.1** | `ch03#s-3-1` |
| Purchase | 11 | **3.2** | `ch03#s-3-2` |
| Conversion | 12–13 | **3.3** (collapsed) | `ch03#s-3-3` |
| Other | 15 | **3.5** | `ch03#s-3-5` |
| Not in cost | 16 | **3.6** | `ch03#s-3-6` |
| Specific identification | 23 | **3.10** | `ch03#s-3-10` |
| FIFO ∥ weighted average | 25–27 | **3.10** (collapsed) | `ch03#s-3-10` |
| NRV arm | 6–7 | **4.2** (collapsed) | `ch04#s-4-2` |
| Write-down | 28–29 | **4.3–4.4** | `s-4-3` / `s-4-4` |
| Reversal, capped | 33 | **4.7** | `ch04#s-4-7` |
| Expense exit | 34–35 | **5.1–5.4** | `s-5-1` / `s-5-4` |
| Disclosure | 36–39 | **6.1–6.5** | `s-6-1` / `s-6-5` |

### Ch1 Scope

| Before | After | href |
|--------|-------|------|
| 6 | **1.1** | `#s-1-1` |
| 2 | **1.2** | `#s-1-2` |
| 3–5 | **1.3** | `#s-1-3` |

### Ch2 Recognition

| Before | After | href |
|--------|-------|------|
| 6 | **2.1** | `#s-2-1` |

### Ch3 Initial measurement

| Before | After | href |
|--------|-------|------|
| 10 | **3.1** | `#s-3-1` |
| 11 | **3.2** | `#s-3-2` |
| 12–13 | **3.3** | `#s-3-3` |
| 15 | **3.5** | `#s-3-5` |
| 16 | **3.6** | `#s-3-6` |
| 23 | **3.10** | `#s-3-10` |
| 25–27 | **3.10** | `#s-3-10` |

### Ch4 Subsequent measurement

| Before | After | href |
|--------|-------|------|
| 9 | **4.0** | `#s-4-0` |
| 10 | **3.1** | `ch03#s-3-1` |
| 16 | **3.6** | `ch03#s-3-6` |
| 23–27 | **3.10** | `ch03#s-3-10` |
| 6–7 | **4.2** | `#s-4-2` |
| 29 | **4.4** | `#s-4-4` |
| 33 | **4.7** | `#s-4-7` |
| 32 | **4.6** | `#s-4-6` |
| 30–31 | **4.5** | `#s-4-5` |

### Ch5 Derecognition

| Before | After | href |
|--------|-------|------|
| 9 | **4.0** | `ch04#s-4-0` |
| 34 | **5.1** | `#s-5-1` |
| 35 | **5.4** | `#s-5-4` |

### Ch6 Disclosure

| Before | After | href |
|--------|-------|------|
| 36–39 | **6.1–6.5** | `s-6-1` / `s-6-5` |

---

## Files touched

- `visuals/map-formula-board.html` + `ch01`–`ch06` chapter visuals — circle digits only; hrefs unchanged  
- `visuals/shared.css` — comment text only (§ → section)  
- `index.html`, `ch01`–`ch06.html` — iframe `?v=ias2-chcircles-20261001`  
- Visual CSS links `ias2.css?v=ias2-chcircles-20261001`

**Not changed:** Map layout / arm structure / Cost Build wireframe; body Official · § cite chips; `IN13` mute chip; deep-link targets.

---

## Documents sync

See end of agent report / sync block below (LAPTOP-MODGPP0C).

---

## Documents sync (done)

**2026-10-01 ~14:12 Asia/Shanghai** → laptop `LAPTOP-MODGPP0C`:

- Target pack: `C:\Users\johnny\Documents\ifrs-website-refs\refs\ias-2\draft-v1-linked\`
- Synced: `index.html`, `ch01`–`ch06.html`, all chapter visuals + Map HTML, `visuals/shared.css`
- Report: `refs\ias-2\IAS2-MAP-CHAPTER-CIRCLES-2026-10-01.md`
- Bundle: `refs\ias-2\ias2-chcircles-sync-20261001.tgz`
- Verified on disk: Map GO **1.1**, board **4.0**, Cost **3.1**, NRV **4.2**, write-down **4.3–4.4**; iframe `?v=ias2-chcircles-20261001`
