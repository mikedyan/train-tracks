# Day 28 Build Report — Accessibility + Final Polish

**Date:** 2026-04-17
**Builder:** Factory Agent

## Changes Implemented

### T1: ARIA Labels
- Added `role="toolbar"` and `aria-label="Piece palette"` to sidebar
- Added `role="button"`, `aria-label`, and `tabindex="0"` to all 22 palette pieces (tracks, trains, cars, scenery) — in both sidebar and mobile drawer
- Added `role="grid"` and `aria-label="Track building grid"` to the grid element
- Added `role="gridcell"` and `aria-label` to each cell in `initGrid()`
- Added `updateCellAriaLabel()` function called from `renderCell()` to dynamically update cell descriptions (e.g., "Row 3, column 5, Curve track, red train")
- Added `aria-label` attributes to all control buttons (play, random, clear, undo, redo, speed slider, volume slider, music volume slider, stats, high-contrast, fullscreen)

### T2: Keyboard Navigation
- Added `gridFocusRow`/`gridFocusCol` state variables
- Added `.grid-focus` CSS class with bright blue outline (adapts for night mode and high-contrast)
- Added `setGridFocus()`, `clearGridFocus()` functions
- Added `handleGridKeyAction()` — Enter places selectedTool at focused cell (with auto-connect), or rotates existing track pieces
- Arrow keys move grid focus in `handleKeyDown`
- Enter key triggers placement/rotation at focused cell
- Added `:focus-visible` styling for palette pieces

### T3: Colorblind Connection Dots
- Disconnected dots now render as rotated diamond/square shapes (border-radius: 1px, rotate(45deg)) instead of circles
- Connected dots remain circles
- Added 1px border to disconnected dots for extra visual distinction
- Per-direction transform overrides for disconnected dot positioning

### T4: High-Contrast Mode
- Added `body.high-contrast` CSS class with:
  - 2px solid borders on grid cells
  - Larger connection dots (9px) with 2px borders
  - Boosted SVG contrast (filter: contrast(1.3))
  - 2px gap in grid
  - Bordered buttons
  - Night-mode-aware cell border color
- Added ♿ toggle button in controls bar
- `toggleHighContrast()`, `restoreHighContrast()` functions
- Stored in `localStorage` key `trainTracks_highContrast`
- Keyboard shortcut: `A`

### T5: Fullscreen Mode
- Added ⛶ button in controls bar
- `toggleFullscreen()` using requestFullscreen/exitFullscreen API
- `onFullscreenChange()` listener updates button text and recalculates layout
- Keyboard shortcut: `F`

### T6: Reduced Motion Preference
- Added `@media (prefers-reduced-motion: reduce)` CSS block disabling:
  - Smoke/chimney/confetti particle animations
  - Tree sway, flower sway, duck waddle, people wave
  - Water duck animation, water wave/shimmer animations
  - Connection dot pulse animations
  - Switch lever transitions
- Added `prefersReducedMotion()` JS utility function
- Guards on: `spawnSmokeParticle()`, `spawnChimneySmoke()`, `triggerLoopCelebration()` (confetti section)

### T7: Final Polish
- Added F, A, Arrows, Enter to shortcuts modal
- New "Grid Navigation" section in shortcuts modal
- All modals have Escape handler entries (verified)
- Zero duplicate code blocks (verified with grep)
- JS parses cleanly (verified with `new Function()`)
- HTML tag balance verified: div(195), button(37), span(73)

## Files Modified
- `index.html` (all changes)

## Verification
- JS parse: ✅ OK
- HTML balance: ✅ OK (div, button, span, script, style all balanced)
- Duplicate check: ✅ All new functions have exactly 1 definition
- Function references: ✅ All called functions exist
