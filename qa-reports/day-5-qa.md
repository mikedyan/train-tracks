# Day 5 QA Report — Train Cars

**Date:** 2026-03-19
**Feature:** Train Cars (Freight, Passenger, Caboose)
**QA Agent:** Mochi (opus)

## Summary

✅ **ALL TESTS PASS** — 0 bugs found. Feature is complete and working correctly.

## Test Environment

- Live site: https://mikedyan.github.io/train-tracks/
- Browser: Chromium (OpenClaw browser profile)
- Console errors: 0 JS errors (only benign favicon.ico 404)

## Feature Verification

### T1: Car SVGs ✅
- `createCarSVG('freight')` → valid SVG with brown body, sliding door, door handle
- `createCarSVG('passenger')` → valid SVG with blue body, 8 windows, center stripe
- `createCarSVG('caboose')` → valid SVG with red body, cupola, tail light
- All 3 return proper SVG elements with matching locomotive aesthetic

### T2: Car Palette Items ✅
- CARS header visible in sidebar between TRAIN and SCENERY sections
- 3 car palette pieces with SVG previews and labels (Freight, Passenger, Caboose)
- Palette-car CSS styling (green dashed border) distinguishes from track pieces
- Total 13 palette items: 6 tracks + 1 train + 3 cars + 3 scenery

### T3: Car State Management ✅
- `state.cars` array properly initialized as `[]`
- `CAR_TYPES = ['freight', 'passenger', 'caboose']` defined
- `MAX_CARS = 5` enforced
- Cars included in `serializeState()` and `deserializeState()` — verified via localStorage inspection
- Cars included in `saveUndo()` — verified undo restores car state
- `clearAll()` resets cars to `[]` — verified
- `deserializeState` handles missing `cars` field gracefully (defaults to `[]`)

### T4: Drop Cars onto Locomotive ✅
- Drop on locomotive cell → appends car, plays `SFX.couple()` (metallic clank)
- Toast: "🚃 Freight car added!" / "🚃 Passenger car added!" / "🚃 Caboose car added!"
- Drop on non-locomotive cell → toast "Drop on the locomotive! 🚂"
- No locomotive placed → toast "Place a locomotive first! 🚂"
- Max 5 enforced → toast "🚃 Train is full! (max 5 cars)"

### T5: Static Car Rendering ✅
- Cars render on track cells behind locomotive in stopped state
- Car count badge ("🚃×3", "🚃×5") displays on locomotive cell
- Cars oriented correctly along track direction (matching `facingDir`)
- Cars trace backward through connected track from locomotive
- Screenshot verified: freight (brown), passenger (blue), caboose (red) all correct

### T6: Animated Car Following ✅
- Position history ring buffer working — `positionHistory` grows during play
- `findHistoryEntry()` binary search interpolation provides smooth positions
- `lerpAngle()` handles angle wrapping for smooth curve rotation
- Car spacing: `cellSize * 0.85` pixels — consistent during play
- 5 car animated elements created and visible (`carElsCount: 5`, `allCarsVisible: true`)
- History capped at 600 entries (memory protection)
- Pre-seeded position history from static car positions for seamless play start
- Cars cleaned up in `stopPlay()`

### T7: Right-Click Car Removal ✅
- Right-click on car cell → removes that specific car (car removal takes priority over track)
- `handleRemoveCell` checks `getCarCellPositions()` first
- Tested: 5 cars → right-click → 4 cars (freight removed at index 0)
- Poof animation + SFX.remove() + toast "🚃 Freight car removed!"
- Right-click on locomotive with cars → removes locomotive and all cars
- Toast: "🚂 Train + N cars removed!"

### T8: Ghost Preview and Drag Handling ✅
- Car SVG ghost cursor shown when dragging from palette (65% cell size)
- Locomotive cell shows green highlight (ghost-match), other cells show red (ghost-mismatch)
- Car types handled in `showGhost()` and `showCellGhostPreview()`

### Caboose Sorting ✅
- `sortCarsWithCabooseEnd()` moves caboose to end regardless of add order
- Verified: adding caboose first, then freight → order becomes [freight, caboose]
- Verified: [freight, passenger, caboose] maintains caboose at end

### Save/Load Integration ✅
- Auto-save includes cars in serialized state
- `localStorage.getItem('trainTracks_autosave')` contains `cars` array
- Save slots include cars — verified via `saveToSlot()` / `loadFromSlot()`
- `clearAutoSave` removes cars from persistence

## Regression Tests

### Core Features ✅
- **Page Load:** 96 cells, 13 palette pieces, all controls rendered
- **Drag & Drop:** All 6 track types + 3 scenery place correctly
- **Rotation:** Full 0→90→180→270→0 cycle for all track types
- **Single Train:** Exactly 1 .train-svg in DOM after placement
- **Right-Click Remove:** Track, scenery, train removal all work
- **Connection Dots:** Update correctly on placement/removal
- **Random Generator:** Valid closed loops with 0 disconnected dots (single-run test)
- **Train Animation:** Smooth loop playback, smoke particles active
- **Speed Slider:** Affects animation and smoke rate
- **Station Sound:** Triggers on train passing station
- **Undo:** Restores state including cars
- **Clear:** Empties board and removes all cars
- **Sound/Mute:** All 15 SFX methods present, mute toggle works

### Code Integrity ✅
- **JS syntax:** Valid (Node.js parse check)
- **HTML structure:** 47 open DIVs, 47 close DIVs — balanced
- **Core functions:** 37/37 present (0 missing)
- **SFX methods:** 15/15 present (0 missing)
- **Car-specific code:** 7/7 key functions present
- **Total lines:** 3433
- **Console errors:** 0 JS errors

## Bugs Found

None.

## Performance Notes

- Train + 5 cars animation runs smoothly at 60fps
- Position history buffer capped at 600 entries
- Smoke + car animation coexist without degradation
- No memory leaks observed during extended play
