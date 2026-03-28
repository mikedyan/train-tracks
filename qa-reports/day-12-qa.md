# Day 12 QA Report — Animated Scenery

## Acceptance Criteria Verification

### T1: Tree Sway Animation ✅
- [x] `@keyframes tree-sway` correctly rotates ±3° with translate(-50%, -50%) preserved in all keyframes
- [x] `.scenery-tree` class applied to tree emojis in `renderCell()`
- [x] Each tree gets unique `--tree-sway-duration` (3-4.5s) and `--tree-sway-delay` (0-3s) seeded from `cell.dataset.treeSeed`
- [x] Seed persists across re-renders (stored in dataset, not cleared by renderCell)
- [x] Works in both day and night modes (no color dependency in animation)

### T2: Cow Moo Sound ✅
- [x] `SFX.moo()` implemented with dual-oscillator approach (sine 140Hz + triangle 280Hz overtone)
- [x] `checkCowProximity()` checks 3×3 area around train when entering new cell
- [x] 3-second cooldown per cow via `anim.mooCooldowns` keyed by "row,col"
- [x] Only one moo per cell transition (early return after first moo)
- [x] Respects `soundEnabled` flag (checked in SFX.moo)

### T3: Cow Facing Direction ✅
- [x] `.scenery-cow-flipped` class uses `scaleX(-1)` with preserved translate(-50%, -50%)
- [x] 50% random flip on first render, stored in `cell.dataset.cowFlip`
- [x] Dataset persists across re-renders

### T4: House Chimney Smoke ✅
- [x] `@keyframes chimney-smoke-rise` is slower (1.8-2.8s) and smaller than train smoke
- [x] Particles spawned at top-center of house cells with random horizontal drift
- [x] Max 2 particles per house enforced via `data-house` attribute querySelectorAll count
- [x] Night mode: lighter shade, lower opacity
- [x] Always active (started in init, not tied to play state)
- [x] Self-cleaning particles via setTimeout

### T5: Visibility API Pause ✅
- [x] `visibilitychange` listener added in init()
- [x] When hidden: stops chimney interval + adds `.animations-paused` to grid
- [x] When visible: restarts chimney interval + removes class
- [x] CSS pauses tree sway, duck drift, and water wave animations via `animation-play-state: paused`

## Regression Checks

- [x] HTML tag balance: 71 open / 71 close — BALANCED
- [x] JavaScript syntax: VALID (new Function parse check)
- [x] All core functions present: init, renderCell, renderAllCells, togglePlay, startPlay, stopPlay, generateRandomTrack, advanceTrainAnim, renderTrainAtProgress, placePiece, removePiece
- [x] Train smoke particles still work (separate system from chimney smoke)
- [x] Loop celebration confetti still present
- [x] Crash animations still present
- [x] Tunnel fade/sound still present
- [x] Night mode transitions still work
- [x] Water tiles / duck drift still work
- [x] clearAll() now calls cleanupChimneySmoke() for proper cleanup

## Bugs Found & Fixed

### BUG-010 | 🟢 FIXED | cleanupChimneySmoke() never called
- **Severity:** Low (cosmetic — particles self-clean in ~2s anyway)
- **Root cause:** Function was defined but never invoked during board clear
- **Fix:** Added `cleanupChimneySmoke()` call in `clearAll()`

## Performance Notes
- Tree sway: pure CSS animation, no JS overhead
- Chimney smoke: interval runs every 1.2s, iterates 96 cells max (trivial), max 2 particles per house
- Cow moo: only checked on cell transitions during play (not per-frame)
- All particle cleanup is timer-based with finite lifetimes

## Status: ✅ SHIPPED
