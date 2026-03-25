# Build Report — Day 9: Multiple Trains

**Date:** 2026-03-25
**Feature:** Multiple Trains (up to 3, independently colored)

## What Changed

### State Architecture (Major Refactor)
- `state.train` (single object) → `state.trains` (array of `{row, col, color, cars}`)
- `state.cars` (single array) → per-train `train.cars`
- `animState` (single object) → `animStates` (array of per-train animation states)
- Added helper functions: `getTrainAt()`, `getTrainIndex()`, `getTrainByColor()`, `isTrainType()`, `getTrainColor()`
- Added constants: `MAX_TRAINS=3`, `TRAIN_COLORS`, `TRAIN_COLOR_ORDER`

### Palette
- Single "Loco" → 3 colored trains: Red, Blue, Green
- Each has distinct CSS (colored border/background matching train color)
- `data-type="train-red"` / `"train-blue"` / `"train-green"`

### Train SVG
- `createTrainSVG()` → `createTrainSVG(color)` with TRAIN_COLORS map
- Red preserves original look; Blue and Green use complementary color schemes
- Neutral elements (wheels, headlight, smokestack, windows) unchanged across colors

### Drag & Drop
- Train dragging preserves color identity via `dragInfo.trainColor`
- Palette drops use color from data-type
- Car drops target any locomotive (finds train at drop cell)
- Ghost preview uses correct train color

### Animation System
- `startPlay()` creates animState per valid train
- `animateFrame()` iterates all active animStates
- New `advanceTrainAnim(anim, timestamp)` handles single train advancement
- Per-train headlight divs (night mode)
- Smoke spawns for all active trains
- Shared chug rhythm

### Collision Detection
- After each frame, checks all pairs of active trains for same-cell overlap
- `triggerCollision(anim1, anim2)` triggers crash sequence for both
- New `SFX.collision()` sound effect
- Fun collision toast messages

### Persistence
- Serialization saves `trains` array
- Deserialization handles both old format (`train` + `cars`) and new format (`trains`)
- Save slots use new format
- `renderThumbnail()` shows colored dots per train

## Files Modified
- `index.html` — All changes (single-file app)

## Lines of Code
- ~30 distinct code sections modified
- ~200 lines added (new functions, collision, constants)
- ~100 lines modified (adapted to multi-train)

## Testing
- Manual browser testing: page load, random, play/stop, 3-train animation
- JavaScript syntax validation (Node.js)
- Brace balance check: 615/615
- Console error check: 0 JS errors
- Persistence round-trip test (serialize → deserialize → verify)
- Old format migration test: verified `{train, cars}` → `{trains}` conversion
