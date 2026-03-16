# Day 4 Build Report — Ghost Preview + Placement Sounds

**Date:** 2026-03-16
**Builder:** Factory Orchestrator

## Changes Made

### 1. Ghost Preview in Target Cell (T1, T2, T3)
- **CSS:** Added `.ghost-preview` (50% opacity SVG), `.ghost-preview-emoji` (50% opacity emoji), `.cell.highlight.ghost-match` (green inset border), `.cell.highlight.ghost-mismatch` (red/pink inset border)
- **JS: `showCellGhostPreview(row, col)`** — Renders a translucent preview of the dragged piece at the target cell:
  - **Track pieces from palette:** Uses `findBestRotation()` to show auto-connected rotation
  - **Track pieces from grid:** Uses `dragInfo.rotation` (existing rotation)
  - **Scenery:** Shows translucent emoji
  - **Train:** Shows translucent train SVG oriented to track connections
  - **Border colors:** Computes connection score — green if ≥1 match, red if track neighbors exist but 0 matches
- **JS: `clearCellGhostPreview()`** — Removes ghost preview SVG/emoji and border classes
- **Performance optimization:** Tracks `ghostPreviewRow`/`ghostPreviewCol` to only recreate preview when the cursor enters a different cell

### 2. Modified `highlightCellUnder()` 
- Separated highlight class removal from ghost preview cleanup
- Only updates ghost preview when the target cell changes (avoids per-frame DOM thrashing)
- Clears ghost preview when cursor leaves the grid

### 3. Modified `clearHighlight()`
- Now calls `clearCellGhostPreview()` for full cleanup on drag end

### 4. Differentiated Placement Sounds (T4)
- **SFX.place():** Changed from high-pitched snap (800/1200Hz) to wooden thunk (250Hz triangle + 180Hz sine + noise burst) — deeper, more tactile
- **SFX.placeScenery():** New function — softer click (1000/1400Hz sine) for scenery placement
- **SFX.rotate():** Changed to mechanical click (440/660Hz) — distinctly different from both placement sounds
- **placePiece():** Now branches on type — `SFX.placeScenery()` for scenery, `SFX.place()` for tracks

## Validation
- JS syntax: ✅ Valid (Node.js `new Function()` parse)
- HTML structure: ✅ 40/40 DIV balance
- All 25 core functions: ✅ Present
- All new features: ✅ Verified in code

## Files Modified
- `index.html` — CSS additions (~15 lines), JS additions (~80 lines), sound modifications (~10 lines)
