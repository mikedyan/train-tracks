# Day 12 Build Report — Animated Scenery

## Tasks Implemented

### T1: Tree Sway Animation
- Added `@keyframes tree-sway` CSS animation with ±3° rotation over 3-4s
- Added `.scenery-tree` class applied to tree emoji elements
- Each tree gets randomized `--tree-sway-duration` (3-4.5s) and `--tree-sway-delay` (0-3s) via cell dataset seed
- Seeds stored in `cell.dataset.treeSeed` for consistency across re-renders

### T2: Cow Moo Sound
- Added `SFX.moo()` using dual oscillators: sine 140Hz with pitch bend + triangle 280Hz nasal overtone
- Added `checkCowProximity()` function called in `advanceTrainAnim()` when entering new cells
- Checks 3×3 grid around train position for cow scenery tiles
- 3-second cooldown per cow tracked in `anim.mooCooldowns` object
- Only one moo per cell transition to avoid audio overload

### T3: Cow Facing Direction
- Added `.scenery-cow-flipped` CSS class using `scaleX(-1)` transform
- 50% random flip chance on first render, stored in `cell.dataset.cowFlip` for consistency
- Correctly overrides the base translate(-50%, -50%) transform

### T4: House Chimney Smoke
- Added `@keyframes chimney-smoke-rise` CSS animation (slower, smaller than train smoke)
- Added `.chimney-smoke` CSS class
- Created chimney smoke system: `spawnChimneySmoke()`, `startChimneyLoop()`, `stopChimneyLoop()`
- Spawns every 1.2s with 30% probability per house per tick
- Max 2 particles per house active at once (tracked via `data-house` attribute)
- Particles positioned above house cell center, drift upward with random horizontal offset
- Night mode: lighter shade, lower opacity for visibility
- Always active (not just during play)

### T5: Visibility API Pause
- Added `visibilitychange` listener in `init()`
- When hidden: stops chimney smoke interval, adds `.animations-paused` class to grid
- When visible: restarts chimney smoke, removes class
- CSS pauses tree sway, duck drift, and water wave animations via `animation-play-state: paused`

## Files Modified
- `index.html` — all changes in single file

## Commits
- Ready for commit
