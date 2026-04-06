# Day 18 Build Report — Pinch-to-Zoom + Pan

**Date:** 2026-04-06
**Feature:** Pinch-to-Zoom + Pan
**Lines changed:** ~280 lines added (6103 → 6382)

## Changes Made

### CSS (lines 217-256)
1. **New `#grid-viewport` wrapper**: Inherits `border-radius`, `overflow: hidden`, `box-shadow`, and `touch-action: none` from old `#grid-container`
2. **`#grid-container` simplified**: Now only has `position: relative`, `transform-origin: 0 0`, `will-change: transform`
3. **`#zoom-indicator` badge**: Absolute-positioned in bottom-right of viewport, shows zoom level when != 1.0x

### HTML (lines 1397-1403)
1. **Wrapped `#grid-container` in `#grid-viewport`**: New parent div for overflow clipping
2. **Added `#zoom-indicator` div**: Inside viewport, shows "1.5×" etc.

### JavaScript — Zoom State (lines 2058-2143)
1. **State vars**: `zoomLevel`, `panX`, `panY`, `zoomTouchState`, constants `ZOOM_MIN=0.5`, `ZOOM_MAX=2.0`
2. **`applyZoomTransform()`**: Sets CSS transform on grid-container
3. **`enforcePanBounds()`**: Prevents grid from being panned off-screen, centers when smaller than viewport
4. **`updateZoomIndicator()`**: Shows/hides zoom badge
5. **`resetZoom()`**: Resets to 1.0x with no pan
6. **`setZoomAtPoint()`**: Zooms toward a specific screen point (cursor/finger midpoint)

### JavaScript — getCellUnder fix
- Now converts screen coords to grid-container local space using viewport rect + zoom/pan values instead of raw `getBoundingClientRect()`

### JavaScript — Animation offset fixes
- **`renderTrainAtProgress`**: Uses `grid.offsetLeft/offsetTop` instead of `getBoundingClientRect()` diff
- **`startPlay` car pre-seeding**: Same fix
- **`spawnChimneySmoke`**: Same fix
- **Puzzle confetti**: Converted to grid-local coords instead of screen-space `getBoundingClientRect()`

### JavaScript — Event Handlers (lines 6185-6300)
1. **`onViewportWheel`**: Mouse wheel zoom toward cursor, `passive: false` to prevent page scroll
2. **`onViewportTouchStart/Move/End`**: Two-finger pinch-to-zoom + pan. Tracks initial distance, scales proportionally, pans with midpoint movement
3. **`onViewportDoubleTap`**: Double-tap within 300ms resets zoom (or zooms to 1.5x if already at 1.0x)
4. **Desktop dblclick**: Same behavior, but only fires on viewport (not on grid cells, to avoid interfering with rotation)

### JavaScript — Keyboard Shortcuts
- **`+`/`=`**: Zoom in 0.1x
- **`-`**: Zoom out 0.1x
- **`0`**: Reset zoom to 1.0x
- Updated shortcuts overlay HTML

### JavaScript — Misc
- **`initGrid()`**: Sets viewport width/height to match grid natural dimensions
- **`init()`**: Calls `initZoomPan()` after `initDragAndDrop()`
- **Window resize**: Calls `resetZoom()` before recalculating sizes

## Architecture Notes
- Zoom uses CSS `transform: translate(panX, panY) scale(zoomLevel)` on `#grid-container` — GPU-accelerated, no reflow
- All children of grid-container (animated trains, particles, headlights) automatically scale with the container
- `grid.offsetLeft/offsetTop` used for local-space positioning instead of `getBoundingClientRect()` diffs (zoom-safe)
- Single-finger touch still works for drag-and-drop (zoom handlers only activate on 2+ fingers)
