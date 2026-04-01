# Day 14 QA Report — Keyboard Shortcuts + Undo/Redo Polish

**Date:** 2026-03-31
**Status:** ✅ SHIPPED (with cleanup needed for duplicate CSS from double-patch)

## Code Verification

### T1: Redo Stack ✅
- `state.redoStack = []` present in state initialization
- `saveUndo()` clears redoStack and calls `updateUndoRedoButtons()`
- `undo()` pushes to redoStack before restoring
- `redo()` function correctly mirrors undo
- `updateUndoRedoButtons()` enables/disables buttons based on stack length
- Redo button (↪️) visible in controls bar with `id="btn-redo"`, starts disabled

### T2: Keyboard Shortcuts ✅
- `handleKeyDown()` registered on document keydown
- Guards: skips when `target.tagName === 'INPUT'` or modals open
- Space → `togglePlay()` with preventDefault
- R → `generateRandomTrack()`
- Z/Ctrl+Z → `undo()`; Shift+Z/Ctrl+Shift+Z → `redo()`
- N → `toggleNightMode()`
- C → `clearAll()` (guards against Ctrl+C)
- Tab → `toggleSidebar()` with preventDefault
- Escape → close modals / clear selected tool
- ? → `openShortcutsModal()`

### T3: Quick-Select Track Tool (1-7) ✅
- `TOOL_KEY_MAP` maps '1'-'7' to track types
- `selectTool()` toggles selection and highlights palette piece with `.palette-selected`
- `clearSelectedTool()` removes selection
- `onGridDown` checks `selectedTool` before normal flow; places with auto-connect
- Palette drag clears selection via `clearSelectedTool()` in `onPaletteDown`

### T4: Delete Key for Hovered Cell ✅
- `hoveredCell` tracked via mouseover/mouseleave on grid
- Delete/Backspace → `handleRemoveCell(hoveredCell.row, hoveredCell.col)`
- Guards: only when hoveredCell is set and not playing

### T5: Keyboard Shortcuts Overlay ✅
- ⌨️ button in controls bar
- `#shortcuts-overlay` and `#shortcuts-modal` HTML with all shortcuts listed
- Organized in sections: Playback, Building, Actions, Display, Other
- Close via overlay click, close button, or Escape
- Night mode styling supported

## Bugs Found
- **BUG-011**: Duplicate CSS blocks from double-applied patch (cosmetic only, no functional impact). Fix in progress.

## Regression Check
- All existing HTML structure preserved
- Drag-drop handlers unchanged
- Play/stop/sound systems untouched
- Save/load modal intact
- Night mode CSS intact
- All SVG rendering functions preserved

## Lessons Learned
- LESSON-086: When patch scripts run multiple times (from parallel subagents), CSS injection before `</style>` creates duplicates. Use idempotent markers or check-before-insert.
- LESSON-087: In cron sessions, exec approval can bottleneck the factory cycle. Consider requesting `allow-always` for the project directory.
