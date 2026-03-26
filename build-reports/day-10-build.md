# Day 10 Build Report — Water Tiles & Functional Bridges

**Date:** 2026-03-26
**Builder:** Factory Orchestrator

## Changes Made

### 1. Water Type Added to Data Model
- Added `'water'` to `SCENERY_TYPES` array
- Added `water: '💧'` to `SCENERY_EMOJI`
- Water palette piece added to sidebar under Scenery section

### 2. Water Tile CSS Rendering
- `.cell.water-cell` class with blue gradient background (not emoji-based)
- `::before` pseudo-element with radial gradient ripples + `water-wave` keyframe animation
- Night mode variant: darker blue with moonlight shimmer via `::after` pseudo-element
- `moonlight-shimmer` keyframe for subtle reflection effect in night mode

### 3. Animated Ducks
- `water-duck` class with `duck-drift` keyframe animation
- ~40% of water cells get a duck (seeded per cell via `dataset.duckSeed`)
- Random position, duration (3.5-5.5s), and delay per duck for natural feel
- Small size (32% of cell) to not overwhelm the tile

### 4. Track Placement Prevention on Water
- Early check in `onPointerUp` before any placement logic
- Blocks track, train, and car types from being placed on water cells
- Shows "🌊 Tracks can't go on water!" toast
- Returns grid-source pieces to original position
- Snap-back animation for train-only drags

### 5. Scenery-on-Scenery Replacement
- Updated scenery drag-drop to allow placing scenery on other scenery (including water→tree, tree→water, etc.)
- Previous behavior only allowed scenery on empty cells

### 6. Bridge Over Water Enhancement
- `bridge-over-water` class with enhanced drop-shadow on SVG + water-colored underlay via `::after`
- Detection runs in `renderCell()` for bridge type — checks all 4 neighbors for water
- Night mode variant for the underlay
- Neighboring bridges re-render when water is placed/removed (via `placePiece` update)

### 7. Random Generator River Feature
- New `generateRiver()` function: creates vertical or horizontal strip of 3-6 water tiles
- Called from `addRandomScenery()` with ~40% probability
- Avoids cells already occupied by track pieces
- Water tiles excluded from random scenery scatter (only appear via river)

## Files Modified
- `index.html` — All changes (single-file architecture)
- `specs/day-10-spec.json` — New spec file

## Lines Added/Changed
- ~310 lines added, ~20 lines modified
