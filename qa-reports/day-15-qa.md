# Day 15 QA Report — Challenge Puzzles (Set 1)

**Date:** 2026-04-01
**QA Agent:** Factory Orchestrator (Mochi)

## Critical Bug Fix Verification

### Duplicate Code Removal
- ✅ JS parses cleanly (Node.js `new Function()` test)
- ✅ Only 1 instance of: `selectedTool`, `TOOL_KEY_MAP`, `openShortcutsModal`, shortcuts CSS, shortcuts HTML
- ✅ DIV tags balanced (88 open / 88 close)
- ✅ Zero JS console errors on page load

## Feature Testing

### Puzzle System
- ✅ 🧩 Puzzles button visible in controls bar
- ✅ Puzzle select overlay opens with 5 puzzle cards
- ✅ Difficulty badges: Easy (green), Medium (yellow), Hard (red)
- ✅ Clicking puzzle card loads the puzzle
- ✅ Puzzle HUD appears with name, piece counts, Check + Sandbox buttons
- ✅ Locked pieces placed at correct positions with correct rotations
- ✅ Board cleared from sandbox state on puzzle load
- ✅ Water tiles rendered in water-bearing puzzles

### Locked Cells
- ✅ `locked-cell` class applied during renderCell (persists through re-renders)
- ✅ 🔒 icon visible on locked cells (CSS ::after pseudo-element)
- ✅ Locked cells cannot be rotated (rotatePiece guard)
- ✅ Locked cells cannot be removed (handleRemoveCell guard)
- ✅ Locked cells block placement (placePiece guard)

### Piece Counting
- ✅ HUD shows correct initial counts
- ✅ Count decrements on piece placement
- ✅ Count increments on piece removal
- ✅ Cannot place when count reaches 0 (toast shown)
- ✅ Depleted badges show red styling

### Check Button
- ✅ Reports disconnected edges when incomplete
- ✅ Reports success when loop is complete
- ✅ Bridge/crossover tolerance in check (don't fail on unused connections)
- ✅ Confetti + celebrate sound on success
- ✅ Progress saved to localStorage

### Sandbox Restoration
- ✅ Exit Puzzle button restores previous sandbox state
- ✅ All tracks, scenery, train position preserved
- ✅ Puzzle HUD disappears

### Mode Guards
- ✅ Clear button blocked during puzzle (toast)
- ✅ Random button blocked during puzzle (toast)
- ✅ Auto-save skipped during puzzle
- ✅ Escape key closes puzzle modal

### Puzzle Solvability (Automated Verification)
- ✅ Puzzle 1 (First Loop): 8 tracks, fully connected, single loop
- ✅ Puzzle 2 (Around the Lake): 14 tracks, fully connected, single loop
- ✅ Puzzle 3 (Figure Eight): 7 tracks, fully connected, figure-8
- ✅ Puzzle 4 (Tunnel Run): 12 tracks, fully connected, single loop with tunnels
- ✅ Puzzle 5 (Grand Station): 20 tracks, fully connected, visits all 3 stations

## Regression Testing

### Core Features
- ✅ Random → Play → full loop runs continuously
- ✅ Zero JS errors during play (only benign favicon 404)
- ✅ Keyboard shortcuts work (Space, R, Z, N, etc.)
- ✅ Night mode toggle works
- ✅ Save/Load modal works
- ✅ Drag and drop works
- ✅ Click-to-rotate works
- ✅ Undo/Redo functional
- ✅ Smoke particles during play
- ✅ All 22 key functions present exactly once

## Bugs Found & Fixed
1. **Locked cell class not persisting** — `renderCell()` removes classes but didn't re-apply `locked-cell`. Fixed by adding `isPuzzleLocked()` check in `renderCell()`.

## Summary
- **Tests run:** 30+ (manual + automated)
- **Bugs found:** 1
- **Bugs fixed:** 1
- **Status:** SHIPPED ✅
