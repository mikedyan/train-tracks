# Day 111 — Cycle 6 Harden Week Day 2: Puzzle & Mode Testing

**Date:** Thu Jul 9, 2026
**Tester:** Mochi 🐯 (QA Agent)
**Environment:** Desktop Chromium (headless), https://mikedyan.github.io/train-tracks/?v=111*&fresh=1
**Anchor:** 12,892 LOC / 467,828 bytes (Cycle 6 Build close, Day 109 — unchanged; Harden zero-growth mandate)
**Goal:** Deep-dive on the puzzle system + supporting modes after the Cycle 6 🗺️ Adventure Journey reshape (Days 105–109). Verify every stop is solvable, stars award/persist correctly, and passenger delivery + progression/unlocks + share links + screenshot all work end-to-end. **ZERO new features.**

---

## Test 1 — All 12 Adventure-Journey Puzzles Solvable E2E (3 stars, within piece budget)

Each puzzle was loaded, filled with a within-budget solution (piece counts ≤ `available`), auto-oriented with the game's own `findBestRotation`, then validated with the real `checkPuzzleSolution()`. Stars read back from `getPuzzleStars()` and persisted progress inspected in `localStorage['trainTracks_puzzles']`.

Journey order: `[11, 12, 1, 2, 8, 3, 6, 4, 7, 5, 9, 10]`

| Order | ID | Name | Placed | par / optimal | Stars |
|------:|---:|------|-------:|:-------------:|:-----:|
| 1 | 11 | First Track (🌱 warm-up, straights) | 2 | 2 / 2 | ⭐⭐⭐ |
| 2 | 12 | Round the Bend (🌱 warm-up, curves) | 2 | 2 / 2 | ⭐⭐⭐ |
| 3 | 1 | First Loop | 4 | 4 / 4 | ⭐⭐⭐ |
| 4 | 2 | Around the Lake | 10 | 10 / 10 | ⭐⭐⭐ |
| 5 | 8 | Cow Pasture | 12 | 14 / 12 | ⭐⭐⭐ |
| 6 | 3 | Figure Eight (crossover) | 6 | 6 / 6 | ⭐⭐⭐ |
| 7 | 6 | Switchyard (2× T-junction) | 9 | 9 / 9 | ⭐⭐⭐ |
| 8 | 4 | Tunnel Run (2× tunnel) | 8 | 8 / 8 | ⭐⭐⭐ |
| 9 | 7 | Speed Run | 18 | 20 / 18 | ⭐⭐⭐ |
| 10 | 5 | Grand Station (3 stations) | 17 | 17 / 17 | ⭐⭐⭐ |
| 11 | 9 | Night Express (forceNight + tunnel) | 9 | 9 / 9 | ⭐⭐⭐ |
| 12 | 10 | Twin Loops (2 trains, 2 components) | 8 | 8 / 8 | ⭐⭐⭐ |

**All 12 → 3 stars, all within the authored piece budget.** Notable:
- **P5 Grand Station** solved with an honest **9-straight + 8-curve, 8-corner loop** connecting all three E-W stations into one closed component (matches the hand-constructed solution from Days 65/80/95 — the generic backtracker's node-cap is a documented solver limitation, NOT a game bug). Full traced solution: curves at (2,2)(2,9)(4,9)(4,6)(5,6)(5,4)(4,4)(4,2); straights at (2,4-7)(3,2)(3,9)(4,3)(4,7)(4,8).
- **P3 Figure Eight** solves as two 2×2 loops sharing the locked crossover (`_matched≥2` multi-connection path exercised).
- **P6 Switchyard** solves as a theta (outer rectangle + center station bridged by 2 T-junctions) — 1 connected component, passes the single-train component gate.
- **P10 Twin Loops** validated the multi-train `allowedComponents = trains.length` path (2 separate loops accepted).

**Star pipeline:** `checkPuzzleSolution` correctly computed 1/2/3 stars from `playerPieces` vs par/optimal, wrote `{stars:3}` for all 12 to `localStorage['trainTracks_puzzles']`, and only upgrades on improvement (`stars > prev`).

## Test 2 — Journey Map Progression (driven by the real solves above)

After the 12 sequential E2E solves, `openPuzzleModal()` rendered the Adventure Journey:
- `.adv-node.done` = **12**, `.adv-node.locked` = **0**, `.adv-beckon` = **0**
- Certificate present: **"🏅 Journey Complete! You rode the whole line — ⭐ 36/36"**
- `.adv-path-done` gold progress rail = **1** (spans the full route)
- Intro counter: **"(12/12 stops)"**

Frontier-gate math confirmed live: solving each stop opened the next (`isAdventureStopUnlocked` reads previous stop's stars), beckon advanced then vanished at completion. Screenshot captured (certificate + WARM-UP/MEADOW region bands + gold drawn-in rail + 🚉/⭐⭐⭐ stations).

## Test 3 — Passenger Delivery End-to-End

Built a 2-station rectangle loop (stations at (2,4) & (4,5), E-W) + 1 green train, `togglePassengers()` ON, `startPlay()` at speed 4.0:
- 2 stations registered in `passengerState.stations`; HUD `.active`.
- Live animation advanced (rAF running in this headless session: progress moved 0.878 → 0.693 across the loop).
- Train picked up + delivered across visits: **`passengerState.delivered = 4`**, `gameStats.passengersDelivered = 4`, `onboard.green` drained to 0 after delivery, one station emptied + re-spawned (respawn timer working).
- **Teardown on stop:** `stopPlay()` → 0 anim states, 0 `.animated-train`, 0 `.station-passenger`, HUD deactivated, `delivered` reset to 0, `highScore` persisted (4) to `trainTracks_passengerHighScore`.

## Test 4 — Progression / Unlocks (10 milestones)

From a clean 6-piece default set, pumped each stat to threshold and ran `checkAndUnlockMilestones()`:
- **All 10 milestones fire** (Builder→tjunction, Architect→crossover, Engineer→bridge, Miner→tunnel, Conductor→station/crossing/freight/passenger/caboose, Loop Master→train-blue/green, Naturalist→water/flower/sheep, Explorer→horse/duck-land/people, Rainbow Fleet→train-yellow/purple, Magician→rainbow). `everyMilestoneFired = true`.
- **Gating correct:** with the default set, `isPieceUnlocked('tunnel'/'station'/'bridge') = false`, `isPieceUnlocked('straight') = true`.
- **Persistence:** controlled single-step check — `tjunction` locked→unlocked at Builder (tracksPlaced=10), full unlocked set written to `localStorage['trainTracks_unlocks']`.

## Test 5 — Share Link Round-Trip (fresh session)

Built a 12-piece mixed loop (curves + straights + tunnel + station) + 1 green train:
- `encodeGridState()` → **140-char v2 hash** (prefix `AggMAAAA`).
- Wiped `state.grid`/`trains`/`switchStates`, `decodeGridState(hash)` → **true**.
- **Grid byte-identical** after decode; **green train preserved** at correct cell (`trainsIdentical = true`, count 1).

## Test 6 — Screenshot / Download

- `openScreenshotModal()` → `#screenshot-preview` canvas **2924×1948**, overlay `.open`.
- `toDataURL('image/png')` → valid PNG (236,698-char dataURL); center pixel non-transparent (grass `104,159,56,255`).
- `downloadScreenshot` + `copyScreenshot` handlers present (functions); `closeScreenshotModal()` removes `.open` cleanly.

---

## Console & Code Health
- **Console errors across the entire session:** **0** (error-level poll returned empty).
- **No code edits today** (Harden mandate). File size FLAT at anchor **12,892 LOC / 467,828 bytes**.

## Bugs Found Today: 0
## Bugs Fixed Today: 0
## Open Bugs: 0

## Verdict: CLEAN SHEET ✅
Every one of the 12 Adventure-Journey stops is solvable to 3 stars within its piece budget; the star award + persistence + journey progression + completion certificate all work end-to-end. Passenger delivery, all 10 unlock milestones, 140-char v2 share round-trip, and the 4× screenshot canvas are all green with zero console errors. The Cycle 6 reshape left the underlying puzzle engine fully intact.

**NEXT: Day 112 = Cycle 6 Harden Week Day 3 — Platform & Edge Cases** (mobile 375px viewport, pinch-zoom, bottom drawer, keyboard-only nav, high-contrast/reduced-motion, all biomes × night, fresh-localStorage cold start, stress: rapid placement / many trains / big grid). ZERO new features.
