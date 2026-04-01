# Day 15 Build Report — Challenge Puzzles (Set 1)

**Date:** 2026-04-01
**Builder:** Factory Orchestrator (Mochi)

## Critical Bug Fix (P0)

### 6x Duplicate Code Blocks
Day 14 introduced 6 copies of keyboard shortcuts code across CSS, HTML, and JS:
- **CSS:** 5 extra copies of `PALETTE SELECTED` + `KEYBOARD SHORTCUTS OVERLAY` (554 lines)
- **HTML:** 5 extra copies of `Keyboard Shortcuts Modal` (150 lines)
- **JS:** 5 extra copies of `selectedTool`, `TOOL_KEY_MAP`, `handleKeyDown`, modal functions (849 lines)

**Fix:** Removed all 5 duplicate copies in each section (1553 lines removed).
**Result:** File reduced from 6936 → 5383 lines. JS parses cleanly, all keyboard shortcuts work.

## Feature: Challenge Puzzles (Set 1)

### CSS Added (~100 lines)
- Puzzle overlay/modal styles with night mode support
- Puzzle card components with difficulty badges (Easy/Medium/Hard)
- Puzzle HUD (fixed position, translucent, shows piece counts)
- Piece badge system (green for available, red for depleted)
- Locked cell indicator (🔒 emoji overlay)

### HTML Added
- 🧩 Puzzles button in controls bar (orange #FF5722)
- Puzzle HUD with name, piece badges, Check + Sandbox buttons
- Puzzle select modal with closable overlay

### JS Added (~250 lines)
- `PUZZLES` array: 5 puzzle definitions with locked pieces, water, available pieces
- `puzzleState`: active flag, locked cells map, piece counts, saved sandbox state
- `loadPuzzle()`: saves sandbox state, clears board, places locked/water pieces
- `checkPuzzleSolution()`: validates all connections + single connected loop
- `exitPuzzle()`: restores saved sandbox state
- `updatePuzzleHUD()`: real-time piece count badges

### Guards Added to Existing Functions
- `placePiece()`: blocks locked cells, enforces piece count limits
- `removePiece()`: blocks locked cells, returns pieces to count
- `rotatePiece()`: blocks locked cells
- `handleRemoveCell()`: blocks locked cells
- `clearAll()`: blocked during puzzle mode
- `generateRandomTrack()`: blocked during puzzle mode
- `autoSave()`: skipped during puzzle mode
- `handleKeyDown()`: Escape closes puzzle modal
- `renderCell()`: applies/removes locked-cell class

### Puzzles Defined
1. **First Loop** (Easy) — 4 curves locked, add 4 straights
2. **Around the Lake** (Easy) — 4 curves locked, water in center, 10 straights
3. **Figure Eight** (Medium) — crossover locked, add 6 curves
4. **Tunnel Run** (Medium) — 4 curves locked, water in center, 6 straights + 2 tunnels
5. **Grand Station** (Hard) — 3 stations locked, 9 straights + 8 curves

All puzzles verified solvable via automated connection-checking script.
