# Train Tracks — Test Matrix

QA agent runs ALL tests every day. This file grows as features are added.
Mark each test with the result after running.

## How to Test
1. Open https://mikedyan.github.io/train-tracks/ in the browser
2. Check browser console for JS errors first
3. Run each test section below
4. Take screenshots as evidence
5. If a test fails: fix the bug, re-test, push the fix
6. Update status column with today's date and result

## Test Results Key
- ✅ PASS (date)
- ❌ FAIL (date) — description of failure
- 🔧 FIXED (date) — was failing, now fixed
- ⬜ NOT YET — feature not implemented yet

---

## Core: Page Load
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Page loads | Navigate to URL | Game renders, no white screen | |
| No JS errors | Check browser console | Zero errors on load | |
| Grid renders | Visual check | 12x8 grid of green cells visible | |
| Palette renders | Visual check | All palette items show SVG previews | |
| Controls render | Visual check | Play, Random, Clear, Undo, Speed, Mute buttons visible | |

## Core: Drag & Drop
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Drag straight from palette | Drag straight piece to empty cell | Piece placed, snap sound | |
| Drag curve from palette | Drag curve to empty cell | Piece placed | |
| Drag T-junction | Drag T to empty cell | Piece placed | |
| Drag crossover | Drag crossover to empty cell | Piece placed | |
| Drag bridge | Drag bridge to empty cell | Piece placed | |
| Drag station | Drag station to empty cell | Piece placed | |
| Drag scenery (tree) | Drag tree to empty cell | Tree emoji appears | |
| Drag scenery (house) | Drag house to empty cell | House emoji appears | |
| Drag scenery (cow) | Drag cow to empty cell | Cow emoji appears | |
| Drag to occupied cell | Drag straight onto existing straight | Replaces the piece | |
| Drag off grid | Drag piece outside grid area | Piece not placed, ghost disappears | |
| Move piece from grid | Drag existing piece to new empty cell | Piece moves, old cell cleared | |

## Core: Rotation
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Click to rotate | Click on placed straight | Rotates 90° | |
| Multiple rotations | Click same piece 4 times | Returns to original orientation | |
| Curve rotation | Click curve 4 times | All 4 orientations shown, returns to start | |

## Feature: Single Train Enforcement
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Place train | Drag train onto track piece | Train SVG appears on track | |
| Replace train | Drag new train onto different track | Old position cleared, new position has train | |
| Only one train | Place train twice | Only one train visible on entire board | |
| Flash on replace | Replace existing train | Brief yellow flash at old position | |

## Feature: Right-Click Remove
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Right-click track | Right-click on placed track piece | Piece removed with poof animation | |
| Right-click scenery | Right-click on tree/house/cow | Scenery removed with poof animation | |
| Right-click train cell | Right-click cell with train | Train and track both removed | |
| Right-click empty | Right-click empty cell | Nothing happens | |
| Remove updates neighbors | Remove piece between two connected pieces | Neighbor dots update to disconnected | |

## Feature: Train Dragging
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Drag train to new track | Drag train SVG to another track cell | Train moves to new cell | |
| Drag train to empty cell | Drag train to cell with no track | Train snaps back to original position | |
| Drag train to scenery | Drag train to cell with tree | Train snaps back, toast "needs a track" | |
| Drag train to trash | Drag train to trash zone | Train removed, track stays | |
| Click under train rotates track | Click the cell around the train (not on train SVG) | Track underneath rotates | |

## Feature: Random Track Generator
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Random generates track | Click Random button | Track layout appears with animation | |
| All dots green | After Random, inspect dots | Every connection dot is green (no red) | |
| Train placed | After Random | Train SVG visible on a straight section | |
| Scenery added | After Random | Trees, houses, and/or cows scattered around | |
| Track is a loop | After Random, press Play | Train runs continuously without stopping | |
| Variety test | Press Random 10 times | At least 2 visually different shapes appear | |
| Random while playing | Press Random during play | Play stops, new track generated | |
| Consistent generation | Press Random 20 times rapidly | No errors, each generates a valid layout | |

## Feature: Play / Animation
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Play starts | Place train on loop, press Play | Train animates along track | |
| Train follows straights | Build straight track | Train moves in correct direction | |
| Train follows curves | Build track with curves | Train follows curve path smoothly | |
| Train on T-junction | Build track with T-junction | Train goes straight through (or turns correctly) | |
| Train on crossover | Build track with crossover | Train stays on its axis (doesn't switch) | |
| Train on bridge | Build track with bridge | Train stays on correct layer | |
| Station sound | Train passes station | Ding-ding sound effect plays | |
| Dead end stop | Build track ending in dead end | Train stops with crash sound and toast | |
| Speed slider | Adjust speed during play | Train visibly speeds up/slows down | |
| Stop button | Press Stop during play | Animation stops, train returns to start | |
| Loop detection | Build a loop, press Play | Train runs forever without stopping | |
| Whistle on start | Press Play | Whistle sound plays | |

## Feature: Sound
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Place sound | Place any piece | Snap sound plays | |
| Rotate sound | Click to rotate | Click sound plays | |
| Remove sound | Right-click remove | Pop sound plays | |
| Mute toggle | Click mute button | Icon changes, all sounds stop | |
| Unmute | Click mute button again | Icon changes back, sounds resume | |

## Feature: Undo
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Undo placement | Place piece, press Undo | Piece removed | |
| Undo rotation | Rotate piece, press Undo | Piece returns to previous rotation | |
| Undo removal | Remove piece, press Undo | Piece restored | |
| Multiple undos | Place 3 pieces, undo 3 times | All 3 removed in reverse order | |

## Feature: Clear
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Clear all | Place several pieces and train, press Clear | Board empty, train gone | |
| Clear during play | Press Clear while playing | Play stops, board cleared | |

---

## Daily QA Notes
*(QA agent appends notes here after each run)*

### Template:
```
### Day N — Date
**Feature tested:** [name]
**New tests added:** [count]
**Results:** X/Y passed
**Bugs found:** [count]
**Bugs fixed:** [count]
**Screenshots:** [attached to topic message]
**Notes:** [any observations]
```
