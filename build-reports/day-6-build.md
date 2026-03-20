# Day 6 Build Report — Day/Night Mode

## What Was Built

### T1: CSS Custom Properties for Night Theme
- Added new custom properties: `--grass-hover`, `--sky-gradient-start`, `--sky-gradient-end`, `--sidebar-top`, `--sidebar-bottom`, `--header-color`, `--house-glow`, `--star-bg`
- Defined `body.night-mode` selector overriding all theme variables
- Night palette: dark green grass (#2E4A3A), dark blue sky (#0D1B2A), dark sidebar (#1A2332/#0F1923)

### T2: Toggle Button (☀️/🌙)
- Added `btn-night` button in controls bar between mute and save
- `toggleNightMode()` toggles `body.night-mode` class
- Button text switches between ☀️ (day) and 🌙 (night)
- Preference saved to localStorage key `trainTracks_nightMode`
- `restoreNightMode()` called during init before first render

### T3: Night Sky with Stars
- 16 CSS radial-gradient dots as `--star-bg` custom property
- Applied as `background-image` on `#main`
- Stars are subtle white dots (0.4-0.9 opacity, 1-1.5px size)
- Only visible in night mode (day mode `--star-bg: none`)

### T4: Train Headlight Glow
- Added `#train-headlight` div inside `#grid-container`
- During night play: radial gradient glow (warm yellow, 2-cell radius)
- Position updated every frame in `renderTrainAtProgress()`
- CSS opacity transition for smooth appear/disappear
- Activated in `startPlay()`, deactivated in `stopPlay()`

### T5: House Window Glow
- Houses get warm yellow text-shadow in night mode
- Applied during `renderCell()` for initial render
- `updateHouseGlows()` updates all existing houses on toggle
- Glow: `0 0 12px rgba(255,200,50,0.7), 0 0 24px rgba(255,180,30,0.4)`

### T6: Darker Sidebar and Grid
- Sidebar uses `var(--sidebar-top)` and `var(--sidebar-bottom)` for gradient
- Sidebar toggle button uses same custom properties
- Grid gaps use `var(--grass-dark)`, cells use `var(--grass)`
- Header text, speed control labels use `var(--header-color)`
- Grid container gets stronger shadow in night mode

### T7: Smooth Transitions
- All color properties have `transition: 0.5s ease`
- Applied to: body, sidebar, grid, cells, header, speed control, grid-container
- Headlight has `opacity 0.3s ease` transition
- Smoke particles adapt opacity for night visibility

## Files Modified
- `index.html` — all changes

## Technical Notes
- No external files, no new dependencies
- All star rendering via CSS radial-gradient (no canvas/JS)
- Headlight is a simple positioned div with radial-gradient
- Night mode variable saved as '1'/'0' in localStorage
- Thumbnail rendering respects current mode
