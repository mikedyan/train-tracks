# Day 108 — Cycle 6 Build Week Day 4

**Date:** 2026-07-06 (Monday)
**Feature:** 🌱 Warm-up stops — two brand-new ultra-easy opening stops on the Adventure Journey
**Decision:** SHIPPED (live green on `?v=108&fresh=1&cb=warmup1`)
**Commit:** `b7d108e`

## What shipped

A gentle on-ramp **before** First Loop. The Adventure Journey (Day 105–107) now opens with two brand-new, ultra-easy stops in their own 🌱 **Warm-Up** region — each teaching exactly one piece type — so a 5-year-old gets two guaranteed wins before the real puzzles begin.

### New puzzles (ids 11, 12)
- **Puzzle 11 — First Track** (`Easy`, par 2, straights only): a tiny 3-wide × 2-tall loop with 4 locked corner curves and two open gaps. Player drops 2 straights; smart auto-connect orients both horizontal (rot 90). Solve = 3⭐.
- **Puzzle 12 — Round the Bend** (`Easy`, par 2, curves only): same little loop, but the two straight edges + two diagonal corners are locked and the *other two corners are missing*. Player drops 2 curves; auto-connect orients them (TR→rot 180, BL→rot 0). Solve = 3⭐.

Both are 6-cell loops — smaller and gentler than First Loop (par 4) — and each isolates a single mechanic (straight, then curve).

### Journey integration
- `ADVENTURE_STOPS` prepended with stops 11 & 12 and re-laid as a clean 12-stop serpentine (regions preserved: **start**{11,12} → meadow{1,2,8} → hills{3,6,4} → desert{7,5} → night{9,10}).
- New `ADVENTURE_REGIONS.start` — 🌱 Warm-Up, light-green (`#9CCC65`, band `rgba(197,225,165,0.30)`).
- New CSS `.adv-node.region-start .adv-node-dot { border-color:#9CCC65 }` (dot-border tint only; state fill stays the load-bearing signal, per Day 106).
- The 🏁 Trailblazer `journey` sticker (`ADVENTURE_STOPS.every(getPuzzleStars>0)`) auto-scaled to 12 stops for free.
- Stat-gated `puzzle-star` sticker bumped `>=10 → >=12` and desc "(10)→(12)" — it is decoupled from `PUZZLES.length`, so it needed a manual honesty fix (see LESSON-DAY108-B).

## Chrome discipline
0 new toolbar buttons, 0 settings tiles, 0 modals, 0 palette pieces. Everything lives inside the existing `#puzzle-overlay` map + the `PUZZLES` data array + sticker table. **9-cycle 0-chrome streak intact.**

## Metrics
- LOC: 12,834 → **12,866** (+32; well under the 80–130 Day-4 estimate — honest lean, LESSON-DAY71)
- Bytes: 464,581 → **466,097** (+1,516)
- Functions added: 0
- Data added: `ADVENTURE_REGIONS.start`, `PUZZLES[11]`, `PUZZLES[12]`
- JS parse: clean (`node --check` on 345,447-byte inline script)
- HTML balance: div 194/194, button 55/55, script 1/1, style 1/1
- Console errors: 0
- Open bugs: 0

## Live verification (`?v=108&fresh=1&cb=warmup1`, served 466,097 B, `localStorage.clear()` + reload)
- **Fresh boot:** 12 nodes, order `[11,12,1,2,8,3,6,4,7,5,9,10]`; First Track `available`+beckon+clickable, all 11 others `locked`+not-clickable; intro "0/12 stops"; beckon pill "🎫 All aboard!" on First Track; 5 region bands (🌱 Warm-Up / 🌳 Meadow / ⛰️ Hills / 🏜️ Desert / 🌙 Night); 🚂 train marker present; 0 console errors.
- **Solve First Track (place 2 straights):** auto-connect → both rot 90; `checkPuzzleSolution` → 3⭐; `isAdventureStopUnlocked(1)` → true (Round the Bend opens).
- **Solve Round the Bend (place 2 curves):** auto-connect → rot 180 + rot 0; → 3⭐; `isAdventureStopUnlocked(2)` → true (First Loop opens).
- **Map after 2 solves:** First Track `done`(🚉+⭐⭐⭐), Round the Bend `done`(⭐⭐⭐), First Loop `available`+beckon "🎫 All aboard!", rest locked; intro "2/12 stops"; train advanced.
- **Real DOM click** on the First Loop node → `startAdventureStop(1)` → modal closes + `loadPuzzle` fires (`puzzleState.active=true, puzzleId=1`).
- Screenshot confirms 🌱 Warm-Up band with two gold 3⭐ done-stations + Meadow band with green pulsing First Loop carrying the beckon pill + grey locked stops + dashed rail.

## Next
Day 109 = Cycle 6 Build Day 5 — 🎉 Journey completion celebration + map polish (train chugs stop-to-stop / path draws in / finish-the-line certificate; tutorial pointer to Adventure). Then Cycle 6 closes into Harden Week (Days 110+).
