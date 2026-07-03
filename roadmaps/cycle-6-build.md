# Cycle 6 Build Roadmap — July 3 → July 7, 2026

**Cycle:** 6 (Build Week = Days 105–109)
**Theme:** _"The Great Train Journey."_ Six straight cycles of polish took the score to a flat **8.7/10** — the asymptote Cycle 4 predicted and Cycle 5 confirmed. Juice is maxed; Uniqueness / Replayability / Addictiveness can't move without a **structural reshape** (the Cycle 5 review's explicit call). Cycle 6 is that reshape: it turns the flat 🧩 puzzle *list* into a star-gated **Adventure Journey** — a winding town-to-town map where beating one stop opens the next, a train chugs the completed route, and finishing the line is a real destination. This is the first cycle in six that deliberately reshapes an existing surface rather than layering more play-time juice.

---

## Inputs reviewed

- `reviews/prune-cycle-5-review.md` — 8.7/10 close, the factory's **first flat cycle-over-cycle** result; "next gain needs a STRUCTURAL reshape (puzzle campaign / level editor / co-op)."
- `PRUNE_REPORT.md` (Cycle 5) — carried debt: reshape-tier feature (priority), 🧑 Passengers-button discoverability (4×-flagged), tutorial expansion for the 13-feature surface.
- `LESSONS_LEARNED.md` — LESSON-DAY89-C (Day 1 ≠ biggest feature of the cycle; ship small + tested), LESSON-DAY93-D (reuse proven patterns for lowest-cost/highest-safety), LESSON-DAY88-B (structural reshape > polish for score movement).
- `BUGS.md` — 0 open bugs entering Cycle 6.
- The existing `PUZZLES` array + `loadPuzzle()` — 10 authored puzzles + a proven load path. **The reshape rides on top of this, not around it.**

## Design pillar: reshape, don't re-plumb

The Adventure Journey is a **new spine over old bones.** `ADVENTURE_STOPS` is an ordered list that references existing puzzle ids with map coordinates; node clicks call the unchanged `loadPuzzle()`; progress reads the unchanged `getPuzzleStars()` / `trainTracks_puzzles` store. This keeps risk low (the puzzle engine is untouched) while changing the *kind* of thing the mode is: a journey with a beginning, a middle, and an end — not a flat menu.

**Chrome note:** the 6-cycle "0 new toolbar/settings/modal" streak is deliberately spent here — but minimally. The reshape lives *inside the existing 🧩 Puzzles modal* (repurposed, not added): no new toolbar button, no new settings tile, no new overlay. The only chrome change is the modal's heading (🧩 Challenge Puzzles → 🗺️ Adventure Journey). A reshape that costs one heading is the right price.

---

## 5-Day Build Plan

| Day | Date | Feature | LOC est. |
|---|---|---|---|
| **105 Fri** | 2026-07-03 | 🗺️ **Adventure Journey Map** — puzzle list reshaped into a winding, star-gated town-to-town map | 50–90 |
| **106 Sat** | 2026-07-04 | 🚂 **Journey Train + region theming** — a train marker rides at the furthest-reached stop; nodes color-code by region (meadow/hills/desert/night) | 60–110 |
| **107 Sun** | 2026-07-05 | 🎫 **Next-Stop beckon + journey rewards** — auto-highlight the next stop with a gentle "All aboard!" nudge; a Journey sticker when the whole line is cleared | 60–100 |
| **108 Mon** | 2026-07-06 | 🌱 **Warm-up stops** — 2 brand-new ultra-easy opening stops (one mechanic each) so a 5-year-old gets a gentle on-ramp before First Loop | 80–130 |
| **109 Tue** | 2026-07-07 | 🎉 **Journey completion celebration + map polish** — train chugs stop-to-stop, path draws in, finish-the-line certificate; tutorial pointer to Adventure | 60–110 |

**Total estimate: +310 to +540 LOC.** In line with historical reshape cycles (C3 was reshape-tier). Per LESSON-DAY89-C, Day 1 is intentionally the smallest, fully-tested foundation, not the heaviest feature.

---

## Day 105 — 🗺️ Adventure Journey Map (shipped)

Transform the flat puzzle-card list into a winding journey map inside the existing puzzle modal.

- `ADVENTURE_STOPS`: ordered array of `{puzzleId, x%, y px, region}`, hand-laid in a serpentine down the map. Region is reserved for Day-2 theming.
- **Star-gated progression:** `isAdventureStopUnlocked(i)` → stop 0 always open; stop *i* opens once the previous stop has ≥1 star (`getPuzzleStars`). This creates the campaign spine — a real "next stop" instead of an all-you-can-pick menu.
- **Node states:** `done` (gold 🚉 + earned stars), `available` (green 🚩, pulsing ring), `locked` (grey 🔒, not clickable).
- **Rail path:** an SVG `polyline` (dashed, `vector-effect="non-scaling-stroke"`) threads the node centers behind the markers.
- Node click on an unlocked stop → `startAdventureStop(id)` → `closePuzzleModal(); loadPuzzle(id)` (unchanged engine).
- Reduced-motion kills the pulse; high-contrast forces black node borders; night-mode text/colors inherited.

### Acceptance (all verified live on `?v=105&fresh=1`)

- Fresh boot: 10 nodes, stop 1 `available`, stops 2–10 `locked`, "0/10 stops", rail path present, 0 console errors. ✅
- Award a star at stop 1 → stop 1 flips `done` (correct filled-star count), stop 2 unlocks, "1/10". ✅
- Real click on the available node → modal closes, `loadPuzzle` fires (`puzzleState.active`, correct `puzzleId`, 4 locked cells for First Loop). ✅
- Locked nodes carry no onclick (not clickable). ✅
- JS parse clean, div 191/191, button 55/55. ✅

### Out of scope (today)

- The riding train marker + region colors (Day 106).
- Next-stop auto-beckon + journey completion sticker (Day 107).
- New warm-up stops (Day 108).
- Chug animation / certificate (Day 109).

---

## Cycle 6 chrome budget

- **Toolbar:** 15 visible + HONK (unchanged — no new button).
- **Settings tiles:** 8 (unchanged).
- **Modals:** 13 overlays (unchanged — the reshape reuses `#puzzle-overlay`).
- **Palette:** 26 pieces (unchanged).

The reshape is a *content* change to an existing modal, not new chrome. The one visible cost is the modal heading. Everything past that is behavior.
