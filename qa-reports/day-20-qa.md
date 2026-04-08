# Day 20 QA Report — Terrain Biomes

**Date:** 2026-04-08
**QA Agent:** Factory Agent

## Acceptance Criteria Verification

### T1: Biome CSS Custom Property Overrides
- ✅ `body.biome-winter` sets white/ice-blue grass (#E3EFF5), cold sky (#D6E8F0), frosty sidebar
- ✅ `body.biome-desert` sets tan/sand grass (#D4B896), warm sky (#F5E6C8), warm sidebar
- ✅ `body.biome-autumn` sets orange-brown grass (#A67B52), warm orange sky (#F0D9B5), earthy sidebar
- ✅ Night mode CSS (line 72) appears AFTER biome CSS (lines 35-70) — night always wins
- ✅ All biome colors use CSS custom properties → inherit existing 0.5s transitions
- ✅ Winter water: ice-blue (#B3E5FC) with slower wave animation
- ✅ Desert water: teal oasis (#4DB6AC)
- ✅ Autumn water: darker muted (#4E97A8)

### T2: Biome State, Constants, Emoji Overrides
- ✅ `BIOMES = ['spring', 'winter', 'desert', 'autumn']`
- ✅ Winter overrides: tree→🎄, flower→❄️
- ✅ Desert overrides: tree→🌵, flower→🌾
- ✅ Autumn overrides: tree→🍂, flower→🍁
- ✅ `getSceneryEmoji(type)` checks overrides then falls back to SCENERY_EMOJI
- ✅ localStorage key `trainTracks_biome` for persistence

### T3: SCENERY_EMOJI Display References
- ✅ renderCell: `getSceneryEmoji(piece.type)` — line 2927
- ✅ createPaletteSVG: `getSceneryEmoji(type)` — line 2853
- ✅ Ghost preview: `getSceneryEmoji(type)` — line 3973
- ✅ Toast (removal): `getSceneryEmoji(piece.type)` — line 3489
- ✅ Drop rendering: `getSceneryEmoji(type)` — line 4047
- ✅ Only 1 remaining `SCENERY_EMOJI[` (inside `getSceneryEmoji` fallback)

### T4: Biome Cycle Button
- ✅ Button in controls bar with id `btn-biome`, shows 🌸 by default
- ✅ `cycleBiome()` cycles spring→winter→desert→autumn→spring
- ✅ `renderAllCells()` called to refresh all cell emoji
- ✅ `rerenderPalette()` rebuilds palette visuals
- ✅ Toast with biome icon + name on switch
- ✅ Keyboard shortcut 'B' wired up

### T5: Biome-Aware Random Generator
- ✅ Desert: river chance 0% (no rivers generated)
- ✅ Winter: river chance 10% (rare)
- ✅ Spring/Autumn: river chance 40% (default)
- ✅ Per-biome scenery weighting with appropriate distributions

### T6: Init Restore + Shortcuts
- ✅ `restoreBiome()` called in `init()` after `restoreNightMode()`, before `renderAllCells()`
- ✅ 'B' keyboard shortcut added to `handleKeyDown()` — fires `cycleBiome()`
- ✅ Biome row added to shortcuts overlay between Night mode and Toggle sidebar
- ✅ Input guard (tagName check) prevents shortcut in text fields

## Regression Checks
- ✅ JS syntax: `new Function()` parse check passed
- ✅ HTML tags balanced: 153 open / 153 close `<div>`s
- ✅ All core functions present (1 each): renderCell, renderAllCells, createTrackSVG, createPaletteSVG, togglePlay, stopPlay, clearAll, generateRandomTrack, addRandomScenery
- ✅ No duplicate function declarations for new functions
- ✅ Night mode CSS still works (class added to body, overrides biome)
- ✅ Water placement blocking is type-based (not visual), unaffected by biome
- ✅ Serialization unchanged — biome is a global preference (like night mode), not per-layout

## Bugs Found
None. Clean implementation.

## QA Result: PASSED ✅
