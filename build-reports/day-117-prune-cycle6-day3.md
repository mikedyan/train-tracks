# Day 117 — Cycle 6 Prune Week Day 3: Code Cleanup

**Date:** 2026-07-15 (Wed)
**Phase:** Cycle 6 · Prune Week · Day 3 (Code Cleanup — Targets B + C, per PRUNE_REPORT.md)
**Commit:** `2c4f611`
**Live:** https://mikedyan.github.io/train-tracks/?v=117&fresh=1&cb=prune6d3

## Mandate
PRUNE_REPORT Day-117 plan: **Target B** (collapse redundant Cycle-6 closing fences) + **Target C** (intra-`renderAdventureMap` / warm-up-data blank trims). Target −10..−18 LOC.

## Honest vein assessment (both scoped veins mined out)
- **Target B — Cycle-6 closing-fence twins: 0 material.** The Days 105–109 reshape uses single `// Day NNN (Cycle 6 …)` comment headers, **not** `=====` section fences with closing twins. Grep of all 55 `====` fences confirms none wrap the ADVENTURE / REGION additions. Nothing to collapse.
- **Target C — blank-run trims: 0 material.** Whole-file scan (incl. whitespace-only lines) = **0 blank runs ≥2**. `renderAdventureMap` has **0 internal blank lines** (fully dense). The single blanks near `PUZZLES[11/12]` / `ADVENTURE_STOPS` are all **phase-separating structure** between top-level declarations → keep per LESSON-DAY71 (cut noise, not structure).

This matches the Day-116 pattern: the reshape scribe wrote lean, why-heavy code, so the classic prune veins came in near-zero. Per the report's own guidance ("A clean honest cut beats a forced −45; the hard rule is net-negative"), I did **not** invent fence/blank cuts that don't exist.

## What actually shipped (genuine, lossless material)
1. **Single-pass DRY in `renderAdventureMap` (−2 LOC).** The `reachedIdx` loop (furthest starred stop → train marker) and the `beckonIdx` loop (first unlocked, unstarred stop → next-stop nudge) both iterated the same `stops` array with **mutually-exclusive per-stop conditions** (a stop either has ≥1 star or has 0). Folded into one `forEach` with an `if/else if`:
   - `if (getPuzzleStars>0) reachedIdx=i;` (unchanged — last starred wins)
   - `else if (beckonIdx===-1 && isAdventureStopUnlocked(i)) beckonIdx=i;` (the `else` implies stars===0, so the original `&& getPuzzleStars===0` is preserved implicitly)
   Provably equivalent; also removes redundant `getPuzzleStars` calls. Original 6 lines (2 `let` + 2 `forEach` + `trainStop` + comment) → 4 lines.
2. **Report-flagged comment trim (byte-negative).** `// Region bands (behind the rail): each spans from the midpoint above to the midpoint below its stops.` → `// Region bands render behind the rail (z-index:0).` — kept the z-order WHY, dropped the self-evident midpoint WHAT (the code at the next two lines literally computes the midpoints). Explicitly listed as Target-A residual in PRUNE_REPORT §3.

## Numbers
| Metric | Entry (D116) | Exit (D117) | Δ |
|---|---|---|---|
| Lines | 12,888 | **12,886** | **−2** |
| Bytes | 467,382 | **467,296** | **−86** |
| Hard rule | ≤12,892 | 12,886 | cleared by 6 |
| Cumulative C6 prune LOC | −4 | **−6** | |
| Cumulative C6 prune bytes | −446 | **−532** | |

Both axes net-negative. JS parse **clean** (346,954-byte inline script, `node --check`). HTML balanced: div 197/197, button 55/55, span 104/104, script 1/1, style 1/1, svg 2/2.

## Live verification (?v=117&fresh=1&cb=prune6d3, deployed served 467,296 B)
Because this fold touched the reshape's live beckon/train logic, ran the full Target-D smoke-test protocol (`localStorage.clear` + reload):
- **Fresh:** 12 nodes · 1 beckon on frontier idx 0 (First Track) · train at 20% (stop 0) · 5 region bands · 1 base rail · 0 done rail · 0 certificate · "0/12 stops" · **0 console errors**
- **Partial (first 3 stops starred):** 3 done · **beckon advanced to idx 3 "Around the Lake"** (first unlocked unstarred) · **train at 80%** (furthest-reached = stop idx 2) · 1 progress rail drawn · "3/12 stops" · 0 errors
- **Complete (all 12 starred):** 12 done · **0 beckon** (no frontier) · certificate present "You rode the whole line — ⭐ 36/36" · train at 20% (last stop idx 11) · "12/12 stops" · 0 errors

Behavior **identical** to the pre-fold two-loop version across all three journey states. Reshape stable.

## Discipline notes
- Respected Risk #1 (don't destabilize the reshape in its first prune): the only reshape edit was a **provably-lossless** micro-fold, browser-smoke-tested per the Target-D protocol before ship. The heavier/riskier band+node render-loop DRY stays **deferred** (Day 118 optional, only if lossless).
- LESSON-DAY71 honored: reported the honest under-estimate (−2 vs −10..−18) instead of forcing nonexistent fence/blank cuts.
- 6-cycle chrome-stability streak intact (0 toolbar/settings/modal/palette change).

## Next
Day 118 = Cycle 6 Prune Week Day 4 — Delight Polish (tiny kid-magic inside existing play-time behavior, no new chrome) + optional Target D (remaining `renderAdventureMap` band/node render-loop DRY, ship only if clearly lossless + smoke-tests green).
