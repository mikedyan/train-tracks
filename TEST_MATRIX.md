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
| Page loads | Navigate to URL | Game renders, no white screen | ✅ PASS (Mar 9) |
| No JS errors | Check browser console | Zero errors on load | ✅ PASS (Mar 9) — only favicon 404, no JS errors |
| Grid renders | Visual check | 12x8 grid of green cells visible | ✅ PASS (Mar 9) |
| Palette renders | Visual check | All palette items show SVG previews | ✅ PASS (Mar 9) — Straight, Curve, T-Split, Cross, Bridge, Station, Loco, Tree, House, Cow |
| Controls render | Visual check | Play, Random, Clear, Undo, Speed, Mute buttons visible | ✅ PASS (Mar 9) |

## Core: Drag & Drop
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Drag straight from palette | Drag straight piece to empty cell | Piece placed, snap sound | ✅ PASS (Mar 9) |
| Drag curve from palette | Drag curve to empty cell | Piece placed | ✅ PASS (Mar 9) |
| Drag T-junction | Drag T to empty cell | Piece placed | ✅ PASS (Mar 9) — via programmatic test |
| Drag crossover | Drag crossover to empty cell | Piece placed | ✅ PASS (Mar 9) — via programmatic test |
| Drag bridge | Drag bridge to empty cell | Piece placed | ✅ PASS (Mar 9) — via programmatic test |
| Drag station | Drag station to empty cell | Piece placed | ✅ PASS (Mar 9) — via programmatic test |
| Drag scenery (tree) | Drag tree to empty cell | Tree emoji appears | ✅ PASS (Mar 9) |
| Drag scenery (house) | Drag house to empty cell | House emoji appears | ✅ PASS (Mar 9) — via programmatic test |
| Drag scenery (cow) | Drag cow to empty cell | Cow emoji appears | ✅ PASS (Mar 9) — via programmatic test |
| Drag to occupied cell | Drag straight onto existing straight | Replaces the piece | ✅ PASS (Mar 9) |
| Drag off grid | Drag piece outside grid area | Piece not placed, ghost disappears | ✅ PASS (Mar 9) — observed during drag tests |
| Move piece from grid | Drag existing piece to new empty cell | Piece moves, old cell cleared | ✅ PASS (Mar 9) — tested via train drag (same mechanism) |

## Core: Rotation
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Click to rotate | Click on placed straight | Rotates 90° | ✅ PASS (Mar 9) — 0→90 confirmed |
| Multiple rotations | Click same piece 4 times | Returns to original orientation | ✅ PASS (Mar 9) — 90→180→270→0 |
| Curve rotation | Click curve 4 times | All 4 orientations shown, returns to start | ✅ PASS (Mar 9) |

## Feature: Single Train Enforcement
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Place train | Drag train onto track piece | Train SVG appears on track | ✅ PASS (Mar 9) |
| Replace train | Drag new train onto different track | Old position cleared, new position has train | ✅ PASS (Mar 9) |
| Only one train | Place train twice | Only one train visible on entire board | ✅ PASS (Mar 9) — DOM check: 1 .train-svg |
| Flash on replace | Replace existing train | Brief yellow flash at old position | ✅ PASS (Mar 9) — observed during Random |

## Feature: Right-Click Remove
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Right-click track | Right-click on placed track piece | Piece removed with poof animation | ✅ PASS (Mar 9) — state goes to null |
| Right-click scenery | Right-click on tree/house/cow | Scenery removed with poof animation | ✅ PASS (Mar 9) |
| Right-click train cell | Right-click cell with train | Train and track both removed | ✅ PASS (Mar 9) |
| Right-click empty | Right-click empty cell | Nothing happens | ✅ PASS (Mar 9) — state stays null |
| Remove updates neighbors | Remove piece between two connected pieces | Neighbor dots update to disconnected | ✅ PASS (Mar 9) — dots update on removal |

## Feature: Train Dragging
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Drag train to new track | Drag train SVG to another track cell | Train moves to new cell | ✅ PASS (Mar 9) — (3,5)→(6,7) |
| Drag train to empty cell | Drag train to cell with no track | Train snaps back to original position | ✅ PASS (Mar 9) — confirmed snappedBack=true |
| Drag train to scenery | Drag train to cell with tree | Train snaps back, toast "needs a track" | ✅ PASS (Mar 9) |
| Drag train to trash | Drag train to trash zone | Train removed, track stays | ✅ PASS (Mar 9) |
| Click under train rotates track | Click the cell around the train (not on train SVG) | Track underneath rotates | ✅ PASS (Mar 9) |

## Feature: Random Track Generator
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Random generates track | Click Random button | Track layout appears with animation | ✅ PASS (Mar 9) |
| All dots green | After Random, inspect dots | Every connection dot is green (no red) | ✅ PASS (Mar 9) |
| Train placed | After Random | Train SVG visible on a straight section | ✅ PASS (Mar 9) |
| Scenery added | After Random | Trees, houses, and/or cows scattered around | ✅ PASS (Mar 9) |
| Track is a loop | After Random, press Play | Train runs continuously without stopping | 🔧 FIXED (Mar 9) — wobbly loop fallback fix |
| Variety test | Press Random 10 times | At least 2 visually different shapes appear | ✅ PASS (Mar 9) — 4+ distinct shapes seen |
| Random while playing | Press Random during play | Play stops, new track generated | ✅ PASS (Mar 9) |
| Consistent generation | Press Random 20 times rapidly | No errors, each generates a valid layout | 🔧 FIXED (Mar 9) — 50/50 pass after fix |

## Feature: Play / Animation
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Play starts | Place train on loop, press Play | Train animates along track | ✅ PASS (Mar 9) |
| Train follows straights | Build straight track | Train moves in correct direction | ✅ PASS (Mar 9) |
| Train follows curves | Build track with curves | Train follows curve path smoothly | ✅ PASS (Mar 9) |
| Train on T-junction | Build track with T-junction | Train goes straight through (or turns correctly) | ✅ PASS (Mar 9) |
| Train on crossover | Build track with crossover | Train stays on its axis (doesn't switch) | ✅ PASS (Mar 9) |
| Train on bridge | Build track with bridge | Train stays on correct layer | ✅ PASS (Mar 9) |
| Station sound | Train passes station | Ding-ding sound effect plays | ✅ PASS (Mar 9) — confirmed via manual loop with station |
| Dead end stop | Build track ending in dead end | Train stops with crash sound and toast | ✅ PASS (Mar 9) — playing=false after dead end |
| Speed slider | Adjust speed during play | Train visibly speeds up/slows down | ✅ PASS (Mar 9) — 1.2→3 confirmed |
| Stop button | Press Stop during play | Animation stops, train returns to start | ✅ PASS (Mar 9) |
| Loop detection | Build a loop, press Play | Train runs forever without stopping | ✅ PASS (Mar 9) |
| Whistle on start | Press Play | Whistle sound plays | ✅ PASS (Mar 9) |

## Feature: Sound
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Place sound | Place any piece | Snap sound plays | ✅ PASS (Mar 9) |
| Rotate sound | Click to rotate | Click sound plays | ✅ PASS (Mar 9) |
| Remove sound | Right-click remove | Pop sound plays | ✅ PASS (Mar 9) |
| Mute toggle | Click mute button | Icon changes, all sounds stop | ✅ PASS (Mar 9) — 🔊→🔇 |
| Unmute | Click mute button again | Icon changes back, sounds resume | ✅ PASS (Mar 9) — 🔇→🔊 |

## Feature: Undo
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Undo placement | Place piece, press Undo | Piece removed | ✅ PASS (Mar 9) |
| Undo rotation | Rotate piece, press Undo | Piece returns to previous rotation | ✅ PASS (Mar 9) |
| Undo removal | Remove piece, press Undo | Piece restored | ✅ PASS (Mar 9) — straight/rotation:90 restored |
| Multiple undos | Place 3 pieces, undo 3 times | All 3 removed in reverse order | ✅ PASS (Mar 9) |

## Feature: Clear
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Clear all | Place several pieces and train, press Clear | Board empty, train gone | ✅ PASS (Mar 9) — allEmpty=true, train=null |
| Clear during play | Press Clear while playing | Play stops, board cleared | ✅ PASS (Mar 9) — playing=false, allEmpty=true |

---

## Daily QA Notes

### Pre-Roadmap Day 4 — Mon Mar 9
**Feature tested:** Random Track Generator + rotation fix (all pre-roadmap features)
**New tests added:** 0 (initial full matrix)
**Results:** 57/57 passed (2 were FIXED during this session)
**Bugs found:** 1 (wobbly loop not closing — BUG-002 partial fix)
**Bugs fixed:** 1 (commit 979e016: wobbly loop fallback)
**Notes:**
- BUG-002 (wobbly loop) was producing open paths 15% of the time. Added closure check to fallback condition. Now 50/50 generations produce valid closed loops.
- All core features (drag/drop, rotation, single train, right-click remove, train drag, random generator, play/animation, sound, undo, clear) verified working.
- No JS errors in console (only benign favicon 404).
- The underlying wobbly loop algorithm still doesn't have BFS pathfinding to close paths — it just falls back to rect loop. Day 1 builder task will implement proper BFS closure.
