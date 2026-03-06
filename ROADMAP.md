# Train Tracks — Feature Roadmap

One feature per day, shipped in the morning and pushed to repo.

## Schedule

| # | Date | Feature | Status |
|---|------|---------|--------|
| 1 | Fri Mar 6 | Single Train Enforcement | ✅ DONE |
| 2 | Sat Mar 7 | Right-Click to Remove | ⬜ TODO |
| 3 | Sun Mar 8 | Train Dragging (independent of tile) | ⬜ TODO |
| 4 | Mon Mar 9 | Random Track Generator | ⬜ TODO |
| 5 | Tue Mar 10 | Train Cars (multi-car train) | ⬜ TODO |

---

## Feature Specs

### 1. Single Train Enforcement (Mar 6)
**Problem:** Multiple trains can be placed on the board. Only one should exist.
**Solution:**
- When dragging a new train from the palette, automatically remove any existing train
- `placeTrain()` already handles moving the train, but the palette drag path creates duplicates
- Single change: in the drop handler for train type, remove old train before placing new
- Visual feedback: brief flash or animation when old train is replaced

### 2. Right-Click to Remove (Mar 7)
**Problem:** No easy way to remove pieces. Must drag to trash zone or off-grid.
**Solution:**
- Right-click (or long-press on mobile) on any occupied cell removes the piece
- Works for: track pieces, scenery, and the train
- Show a brief "poof" animation or particle effect on removal
- Context menu is already prevented (`e.preventDefault()` on grid)
- Mobile: long-press (500ms hold) triggers removal

### 3. Train Dragging — Independent of Tile (Mar 8)
**Problem:** Clicking a cell with a train rotates the tile underneath instead of grabbing the train.
**Solution:**
- Train gets its own hit zone (the SVG element itself) with a higher z-index pointer handler
- `pointerdown` on the train SVG starts a train drag (not a tile rotation)
- `pointerdown` on the cell background (around the train) still rotates the tile
- Train can only be dropped on cells that have a track piece (not empty, not scenery)
- If dropped on invalid cell, snaps back to original position
- Dragging train to trash zone or off-grid removes it entirely

### 4. Random Track Generator (Mar 9)
**Problem:** Building tracks from scratch every time is tedious for quick fun.
**Solution:**
- "🎲 Random" button in the controls bar
- Algorithm: random walk path generation
  1. Pick a random starting cell (not edge)
  2. Walk randomly, placing track pieces, ensuring the path connects
  3. Close the loop (path must return to start for infinite play)
  4. Fill 30-50% of remaining empty cells with scenery (trees, houses, cows)
  5. Place train on a straight section of the loop
- Ensure variety: different loop shapes each time (not always rectangles)
- Clear existing board before generating
- Sound effect on generation (fun "building" cascade)

### 5. Train Cars / Multi-Car Train (Mar 10)
**Problem:** Train is a single locomotive. Should support additional cars trailing behind.
**Solution:**
- Train becomes a linked chain: locomotive + N trailing cars
- Cars follow the locomotive's path with a fixed delay (each car is X% behind on the path)
- New palette item: "Car" (🚃) — drag onto the locomotive or any existing car to append
- Cars are NOT tied to individual cells — they float along the path independently
- Implementation approach:
  - During animation, maintain a path history (ring buffer of recent positions)
  - Locomotive writes positions to history as it moves
  - Each car reads from history at an offset (car 1 reads 1 cell-length behind, car 2 reads 2, etc.)
  - Car SVG designs: freight car (brown box), passenger car (blue with windows), caboose (red, always last)
- Static display: when not playing, cars sit on consecutive track cells behind the loco
- Max cars: 5 (locomotive + 5 = 6 total)

---

## Design Principles
- **Kid-friendly**: Everything should feel playful and satisfying
- **Sound matters**: Each action gets a unique, fun sound
- **No dead states**: Random generator always creates a valid, playable loop
- **Progressive complexity**: Each feature builds on the last
