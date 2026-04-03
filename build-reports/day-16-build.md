# Day 16 Build Report — Puzzle Star Rating + 5 More Puzzles

## Date: 2026-04-03

## Changes Made

### 1. Star Rating System (T1, T2)
- Added `par` and `optimal` fields to all 10 puzzle definitions
- New `getPuzzleStars()` function — backwards-compatible with old boolean completions (treated as 1 star)
- New `renderStarDisplay()` function — renders ⭐⭐⭐ with .star-empty class for unearned stars
- Modified `checkPuzzleSolution()` to count player-placed pieces and calculate stars (1=solved, 2=under par, 3=optimal)
- Stars stored as `{ stars: N }` in puzzleState.completed — old `true` values treated as 1 star
- Only saves if new stars > previous stars (can't lose stars)
- Updated `openPuzzleModal()` to show star display on puzzle cards
- Added `.puzzle-card-stars` and `.puzzle-card-stars .star-empty` CSS classes

### 2. Puzzle 6: Switchyard (T3)
- Theta-shaped layout: outer rectangle with station crossbar connected by T-junctions
- Locked: 4 corner curves + 1 station
- Player places: 7 straights + 2 T-junctions = 9 pieces
- Difficulty: Medium

### 3. Puzzle 7: Speed Run (T4)
- Large oval rectangle requiring many straights
- Locked: 4 corner curves spread wide (cols 2-9)
- Player places: 18 straights (given 20, optimal=18)
- Difficulty: Medium

### 4. Puzzle 8: Cow Pasture (T5)
- Rectangle loop around 4 pre-placed cows
- New `scenery` field on puzzle definition for pre-placed scenery
- Modified `loadPuzzle()` to handle `puzzle.scenery` array
- Player places: 12 straights (given 14, optimal=12)
- Difficulty: Easy

### 5. Puzzle 9: Night Express (T6)
- Rectangle with tunnels, forces night mode on load
- New `forceNight` flag on puzzle definition
- Modified `loadPuzzle()` to toggle night mode when `forceNight` is true
- Modified `exitPuzzle()` to restore previous night mode state
- Added `savedNightMode` to puzzleState
- Locked: 4 curves + 1 tunnel, Player: 8 straights + 1 tunnel = 9 pieces
- Difficulty: Hard

### 6. Puzzle 10: Twin Loops (T7)
- Two separate small rectangles, each with its own train
- New `trains` field on puzzle definition for pre-placed trains
- Modified `loadPuzzle()` to place trains from puzzle.trains array
- Modified `checkPuzzleSolution()` connectivity check to support multi-loop puzzles (BFS finds all components, allows N components for N-train puzzles)
- Locked: 8 corner curves (4 per loop), Player: 8 straights
- Pre-placed: red train + blue train
- Difficulty: Hard

## Verification
- All 10 puzzles validated with automated connection-checking script
- JS parse check: OK
- No duplicate code blocks
- HTML tag balance: OK (88 div open/close)
- Total lines: 5918 (was 5744, +174 net)
