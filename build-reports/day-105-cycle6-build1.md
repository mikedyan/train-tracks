# Day 105 — Cycle 6 Build Day 1: 🗺️ Adventure Journey Map

**Date:** Fri Jul 3, 2026
**Builder:** Mochi
**Cycle:** 6 (Build Week Day 1) — the **reshape cycle** the Cycle 5 review called for.

## What shipped

The flat 🧩 puzzle-card list is now a winding, star-gated **Adventure Journey** — a town-to-town map where beating one stop opens the next. First structural reshape in six cycles; deliberately rides on top of the existing puzzle engine (`PUZZLES` + `loadPuzzle` + `getPuzzleStars`), which is untouched.

- **`ADVENTURE_STOPS`** — ordered `{puzzleId, x%, y px, region}` array, serpentine layout down the map. Maps journey order to existing puzzle ids (order tuned for a gentle difficulty ramp: First Loop → Around the Lake → Cow Pasture → Figure Eight → Switchyard → Tunnel Run → Speed Run → Grand Station → Night Express → Twin Loops). `region` reserved for Day-2 theming.
- **`isAdventureStopUnlocked(i)`** — stop 0 always open; stop *i* opens once the previous stop has ≥1 star. The campaign spine.
- **`renderAdventureMap()`** — builds an SVG dashed rail `polyline` (non-scaling stroke) behind absolutely-positioned node markers; each node is `done` (gold 🚉 + earned stars via the reused `renderStarDisplay`), `available` (green 🚩 + pulsing ring), or `locked` (grey 🔒, no onclick). Header shows a live "N/10 stops" counter.
- **`startAdventureStop(id)`** → `closePuzzleModal(); loadPuzzle(id)`.
- **`openPuzzleModal()`** now renders the map instead of the flat list; modal heading `🧩 Challenge Puzzles` → `🗺️ Adventure Journey`.
- CSS: `.adventure-map / .adv-track / .adv-path / .adv-node{,-dot,-name}` + `done/available/locked` states, `adv-pulse` keyframe, reduced-motion + high-contrast + night-mode variants.

## Chrome discipline

- Toolbar: **15 + HONK** (unchanged — no new button).
- Settings: **8 tiles** (unchanged).
- Modals: **13 overlays** (unchanged — reshape reuses `#puzzle-overlay`).
- Palette: **26** (unchanged).

The 6-cycle "0 new chrome" streak is deliberately spent this cycle (a reshape needs it), but minimally: the **only** visible chrome change is the modal heading. `renderStarDisplay` was kept live (reused for node stars), so no dead function created.

## Size

- LOC: **12,718 → 12,777 (+59)** — within the 50–90 Day-1 estimate; per LESSON-DAY89-C, Day 1 is the small tested foundation, not the cycle's heaviest.
- Bytes: **455,567 → 459,702 (+4,135)**.
- Functions: +3 (`isAdventureStopUnlocked`, `startAdventureStop`, `renderAdventureMap`); `openPuzzleModal` rewritten; old flat-list body removed.

## Verification (live `?v=105&fresh=1&cb=adv1`, served 459,702 B)

- ✅ Fresh boot: heading `🗺️ Adventure Journey`, 10 nodes, stop 1 `available`, stops 2–10 `locked`, "0/10 stops", rail path present, **0 console errors**.
- ✅ Award 2★ at stop 1 → stop 1 `done` (2 filled stars), stop 2 `available`, rest locked, "1/10".
- ✅ Real node click ("First Loop") → modal closes, `loadPuzzle` fires: `puzzleState.active=true`, `puzzleId=1`, 4 locked cells (the 4 curves).
- ✅ Screenshot confirms winding dashed rail, gold done-stations with stars, green pulsing available flags, grey locked 🔒.
- ✅ JS parse clean (`new Function` on inline script), div 191/191, button 55/55, script 1/1, style 1/1.

## Bugs

Found: 0. Introduced: 0. Open: 0.

## Next

Day 106 = Cycle 6 Build Day 2: 🚂 Journey Train marker at the furthest-reached stop + region color-coding (meadow/hills/desert/night) using the `region` field already seeded in `ADVENTURE_STOPS`.
