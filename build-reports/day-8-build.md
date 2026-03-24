# Day 8 Build Report — Clickable Switches (Interactive T-Splits)

## Date: 2026-03-24

## Summary
All 7 spec tasks implemented. T-junction pieces now have interactive switch levers that toggle the train's path between straight-through and branch directions. Works during play and while paused.

## Implementation Details

### Task 1: Switch State Tracking
- Added `switchStates: {}` to state object (maps "row,col" → true for branch mode)
- Included in `saveUndo()` and `undo()` for full undo support
- Included in `serializeState()` / `deserializeState()` for auto-save and save slots
- Reset in `clearAll()` 
- Cleaned up in `removePiece()` (delete entry) and `placePiece()` (delete if not T-junction)

### Task 2: getExitDir Switch Logic
- Added optional `row, col` parameters to `getExitDir(type, rotation, entryEdge, row, col)`
- T-junction logic reads `state.switchStates[row+','+col]`:
  - **Default (straight):** prefers opposite exit (straight-through N↔S, E↔W)
  - **Branch mode:** prefers the non-opposite exit (the branching direction)
- All 3 call sites updated: `startPlay()`, `animateFrame()`, `getCarCellPositions()`

### Task 3: CSS Styles
- `.switch-lever` — 18px orange circle, centered, z-index 7, pointer-events auto
- `.switch-lever:hover` — enlarged (scale 1.15)
- `.switch-lever.branch` — green variant (#66BB6A)
- `.lever-arm` — 4px×14px arm with `--lever-angle` CSS custom property, 0.3s transition
- `#app.playing .cell.has-switch` — cursor:pointer override during play
- `#app.playing .cell.has-switch:hover` — grass hover color during play

### Task 4: Visual Lever in renderCell
- For T-junction cells, creates `.switch-lever` div with `.lever-arm` child
- Computes arm angle: `straightAngle = piece.rotation`, `branchAngle = (piece.rotation + 90) % 360`
- Lever has pointerdown handler with `stopPropagation()` to prevent rotation
- Cell gets `.has-switch` class
- Cleanup in renderCell removes `.switch-lever` and `.has-switch` class

### Task 5: toggleSwitch and updateSwitchLever
- `toggleSwitch(row, col)`: flips between straight/branch, plays `SFX.switchToggle()`, updates lever, calls `autoSave()`
- `updateSwitchLever(row, col)`: finds lever element, updates `--lever-angle` and `.branch` class

### Task 6: Play-Mode Click Handler
- `onGridDown` during play: checks if clicked cell is T-junction → calls `toggleSwitch()`
- Non-T-junction cells: no action during play (existing behavior)

### Task 7: SFX.switchToggle Sound
- Low triangle wave (180Hz, 0.1s) + square wave (120Hz, 0.1s) + noise burst
- Mechanical railway lever clunk effect

## Lines Changed
~173 lines added/modified in index.html

## Commit
`a7244d5 Day 8: Switches & Signals (builder only — QA pending)`
