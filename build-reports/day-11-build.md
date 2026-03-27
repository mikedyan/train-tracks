# Day 11 Build Report — Tunnels

**Date:** 2026-03-27
**Builder:** Factory Orchestrator

## Changes Made

### 1. Tunnel Track Type (T1)
- Added `'tunnel'` to `TRACK_TYPES` array
- Added `BASE_CONNECTIONS.tunnel = ['N', 'S']` — connects like straight, rotatable
- Added tunnel palette item in sidebar between Bridge and Station

### 2. Tunnel SVG Rendering (T2)
- New `'tunnel'` case in `createTrackSVG()`
- Mountain/hill shape (green with highlights)
- Dark oval openings at N and S edges
- Brown arch highlights around openings
- Track rails visible entering/exiting
- Snow/rock cap detail on mountain peak

### 3. Train Fade/Shrink Animation (T3)
- Modified `renderTrainAtProgress()` to detect tunnel cells
- First 30%: opacity 1→0, scale 1→0.3 (entering)
- Middle 40%: opacity 0, scale 0.3 (hidden inside)
- Last 30%: opacity 0→1, scale 0.3→1 (exiting)
- Smooth CSS transitions via inline style updates

### 4. Car Fade Animation (T4)
- Each car independently checks its grid cell position
- Determines if car is within a tunnel cell using pixel coordinates
- Applies same fade/shrink logic based on progress within cell
- Uses connection direction to determine primary axis (N-S vs E-W)

### 5. Tunnel Sound Effects (T5)
- `SFX.tunnelEnter()`: Descending bandpass-filtered noise whoosh + low tone
- `SFX.tunnelExit()`: Ascending bandpass-filtered noise + bright exit tone
- Added `inTunnel` state tracking to animation state object
- Sounds trigger on state transitions (entering/exiting tunnel)

### 6. Night Mode Glow (T6)
- CSS rule: `body.night-mode .cell.has-tunnel svg` gets amber drop-shadow glow
- Added `has-tunnel` class toggling in `renderCell()`
- Class removed on cell clear (added to classList.remove)

### 7. Integration (T7)
- Random generator: ~20% of straight pieces converted to tunnels
- Conversion happens before animation loop (no timing issues)
- Smoke particles suppressed when train is inside tunnel
- Auto-connect, save/load, undo, connection dots all work naturally

## Files Modified
- `index.html`: All changes in single file
- `specs/day-11-spec.json`: New spec file

## Commit
`62c603a` — "Day 11: Tunnels — hide-and-reveal track piece with fade/shrink animation"
