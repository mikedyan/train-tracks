# Day 5 Build Report — Train Cars

**Date:** 2026-03-18
**Feature:** Train Cars (Freight, Passenger, Caboose)

## Tasks Completed

### T3: Car persistence (completion)
- Added `cars` to `serializeState()` and `deserializeState()`
- Added `cars` to `saveToSlot()` and `loadFromSlot()`
- `deserializeState` gracefully handles missing cars field (defaults to [])

### T4: Drop cars onto locomotive
- Added `CAR_TYPES.includes()` branch in `onPointerUp` handler
- Drop on locomotive cell → appends car, sorts caboose to end, plays couple SFX
- Drop on non-locomotive cell → "Drop on the locomotive! 🚂" toast
- No locomotive placed → "Place a locomotive first! 🚂" toast
- Max 5 cars enforced with toast

### T6: Animated car following with position history
- Added `positionHistory`, `cumulativeDistance`, `lastRenderPos`, `carEls` to animState
- Pre-seeds position history with static car positions at negative distances
- Creates animated car DOM elements in `startPlay()`
- `renderTrainAtProgress()` records locomotive position each frame, updates car positions via `findHistoryEntry()` binary search
- `findHistoryEntry()` interpolates between history entries for smooth positioning
- `lerpAngle()` handles angle wrapping for smooth rotation through curves
- History capped at 600 entries to prevent memory growth
- Car spacing: `cellSize * 0.85` pixels between each car
- Cars cleaned up in `stopPlay()`

### T8: Ghost preview and drag handling for cars
- Added car SVG ghost cursor in `showGhost()` (65% cell size)
- Added locomotive cell highlighting in `showCellGhostPreview()` — green on loco, red elsewhere

### Additional
- Added `SFX.couple()` — metallic coupling clank sound
- Added static car/badge cleanup when play starts
- Removed static car SVGs/badges before animated play begins

## Edits Made
12 surgical edits to index.html. No file rewrites.

## Verification
- JavaScript syntax: valid ✅
- HTML DIV balance: 47/47 ✅
- All 39 key functions present ✅
- All 15 SFX methods present ✅
- All car-specific code terms present ✅
