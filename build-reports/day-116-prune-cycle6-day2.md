# Day 116 — Cycle 6 Prune Week Day 2: Simplify (Target A)

**Date:** 2026-07-14 (Tue) · **Week:** Prune (Cycle 6) · **Commit:** dcda129
**Site:** https://mikedyan.github.io/train-tracks/?v=116&fresh=1&cb=prune6d2final

## Goal
Target A from PRUNE_REPORT: trim the Days 105–109 Adventure-Journey reshape's redundant **restate-the-WHAT** comments, keeping every **WHY**. Estimate −10..−16 LOC.

## Changes (comment-only, zero functional change)
Full-line removals / merges (−4 LOC):
1. **ADVENTURE_STOPS header** — collapsed the 2-line comment to 1, dropping the now-false `region is reserved for Day 2 theming` (region has been used since Day 106). Kept the `{puzzleId, x%, y px, region}` structure doc.
2. `// Group consecutive stops into region segments...` — removed over the self-evident `segs` grouping loop.
3. `// Furthest-reached stop: the last stop with a star...` — removed; `reachedIdx` / `trainStop` names are self-documenting.
4. `// Journey train rides at the furthest-reached stop...` — removed; the `.adv-train` element already carries `title="Your train is here"`.

Byte-only trims (kept as 1 line, WHY preserved):
- `// Day 106 ...: region palette for the journey.` — dropped the `meadow → hills → desert → night` key restatement.
- Puzzle 11 preamble — kept `the gentlest first stop`, dropped `a tiny 3-wide loop`.
- Puzzle 12 preamble — kept `auto-connect orients them`, dropped the loop restatement.

Kept (all WHY/provenance): Day markers, z-order (`behind the rail`), region-boundary midpoints, star-gate `stops[i-1]`, Day 107 beckon-frontier rationale, `pathLength=100` gold-rail draw-in.

## Metrics
| | Entry (D115) | Exit (D116) | Δ |
|---|---|---|---|
| LOC | 12,892 | **12,888** | **−4** |
| Bytes | 467,828 | **467,382** | **−446** |

- Hard rule ≤12,892 — **cleared by 4** (both axes net-negative).
- Stretch ≤12,862 — not reached today (Target B+C on Day 117).
- JS parse: **CLEAN** (345,985-byte inline script).
- HTML balance: div 197/197, button 55/55, script 1/1, style 1/1, svg 2/2.
- Open bugs: 0.

## Live verification (deployed)
`?v=116&fresh=1&cb=prune6d2final`, served 467,382 B (trimmed marker present, old `meadow → hills → desert → night` gone): Adventure Journey renders **12 nodes / 1 beckon / 5 region bands / 1 base rail / 1 train / "0/12 stops"**, **0 console errors**.

## Honest note
Landed −4 vs the −10..−16 Target-A estimate: the reshape's comments are mostly WHY/provenance, and only 4 lines were true restate-the-WHAT. Per LESSON-DAY71 (don't force cuts) and PRUNE_REPORT Risk #1/#3 (don't scratch a freshly-shipped reshape in its first prune), the honest smaller win is correct — headroom banked for Day 117 Target B+C.

## Next
Day 117 = Cycle 6 Prune Week Day 3 — Code Cleanup (Target B: redundant Cycle-6 closing fences; Target C: intra-`renderAdventureMap` + warm-up-data blank trims), target −10..−18.
