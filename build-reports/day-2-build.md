# Day 2 Build Report — Smart Auto-Connect

**Date:** 2026-03-14
**Builder:** Factory Orchestrator (Opus)

## What Was Built

### T1: `findBestRotation(row, col, type)` function (line ~790)
- Evaluates all 4 rotations (0°, 90°, 180°, 270°) for a given track piece type
- For each rotation, counts how many of the piece's connection directions have a compatible neighbor (neighbor has OPPOSITE[dir] in its connections)
- Returns `{ rotation, score }` — best rotation and its match count
- Score 0 = no neighbors have matching connections → defaults to rotation 0°
- Skips scenery neighbors (only matches track pieces)

### T2: Palette drop integration (line ~1628)
- Modified `onPointerUp()` to call `findBestRotation()` for palette-sourced track pieces
- Grid-sourced drags still use `dragInfo.rotation` (preserving existing rotation)
- Train drops and scenery drops are unaffected
- After placing with auto-rotation, triggers pulse if score > 0

### T3: CSS pulse animation (line ~213)
- Added `@keyframes connect-pulse` for N/S dots (translateX-based)
- Added `@keyframes connect-pulse-y` for E/W dots (translateY-based)
- Separate keyframes needed because dots use different transform bases (translateX vs translateY)
- Duration: 0.6s ease-out, scales up to 2.2x with green glow

### T4: `showAutoConnectPulse(row, col)` function (line ~1160)
- Finds all `.connection-dot.connected` elements in the placed cell
- Also finds matching dots on connected neighbors
- Adds `pulsing` class, removes on `animationend` event
- Uses `{ once: true }` listener to auto-cleanup

## Verification
- All 20 core functions confirmed present via automated check
- HTML div tag balance: 40/40 ✅
- Script tag balance: 1/1 ✅
- No whole-file rewrites — 4 surgical edits only
