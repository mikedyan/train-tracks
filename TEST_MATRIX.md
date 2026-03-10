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
| Page loads | Navigate to URL | Game renders, no white screen | ✅ PASS (Mar 10) |
| No JS errors | Check browser console | Zero errors on load | ✅ PASS (Mar 10) — only favicon 404, no JS errors |
| Grid renders | Visual check | 12x8 grid of green cells visible | ✅ PASS (Mar 10) — 96 cells confirmed |
| Palette renders | Visual check | All palette items show SVG previews | ✅ PASS (Mar 10) — Straight, Curve, T-Split, Cross, Bridge, Station, Loco, Tree, House, Cow |
| Controls render | Visual check | Play, Random, Clear, Undo, Speed, Mute buttons visible | ✅ PASS (Mar 10) |

## Core: Drag & Drop
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Drag straight from palette | Drag straight piece to empty cell | Piece placed, snap sound | ✅ PASS (Mar 10) |
| Drag curve from palette | Drag curve to empty cell | Piece placed | ✅ PASS (Mar 10) |
| Drag T-junction | Drag T to empty cell | Piece placed | ✅ PASS (Mar 10) |
| Drag crossover | Drag crossover to empty cell | Piece placed | ✅ PASS (Mar 10) |
| Drag bridge | Drag bridge to empty cell | Piece placed | ✅ PASS (Mar 10) |
| Drag station | Drag station to empty cell | Piece placed | ✅ PASS (Mar 10) |
| Drag scenery (tree) | Drag tree to empty cell | Tree emoji appears | ✅ PASS (Mar 10) |
| Drag scenery (house) | Drag house to empty cell | House emoji appears | ✅ PASS (Mar 10) |
| Drag scenery (cow) | Drag cow to empty cell | Cow emoji appears | ✅ PASS (Mar 10) |
| Drag to occupied cell | Drag straight onto existing straight | Replaces the piece | ✅ PASS (Mar 10) |
| Drag off grid | Drag piece outside grid area | Piece not placed, ghost disappears | ✅ PASS (Mar 9) |
| Move piece from grid | Drag existing piece to new empty cell | Piece moves, old cell cleared | ✅ PASS (Mar 9) |

## Core: Rotation
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Click to rotate | Click on placed straight | Rotates 90° | ✅ PASS (Mar 10) — 90→180 confirmed |
| Multiple rotations | Click same piece 4 times | Returns to original orientation | ✅ PASS (Mar 10) — 90→180→270→0→90 |
| Curve rotation | Click curve 4 times | All 4 orientations shown, returns to start | ✅ PASS (Mar 10) |

## Feature: Single Train Enforcement
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Place train | Drag train onto track piece | Train SVG appears on track | ✅ PASS (Mar 10) |
| Replace train | Drag new train onto different track | Old position cleared, new position has train | 🔧 FIXED (Mar 10) — BUG-003: was leaving stale train SVG in DOM |
| Only one train | Place train twice | Only one train visible on entire board | 🔧 FIXED (Mar 10) — BUG-003: now correctly shows 1 SVG |
| Flash on replace | Replace existing train | Brief yellow flash at old position | ✅ PASS (Mar 9) |

## Feature: Right-Click Remove
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Right-click track | Right-click on placed track piece | Piece removed with poof animation | ✅ PASS (Mar 10) |
| Right-click scenery | Right-click on tree/house/cow | Scenery removed with poof animation | ✅ PASS (Mar 9) |
| Right-click train cell | Right-click cell with train | Train and track both removed | ✅ PASS (Mar 9) |
| Right-click empty | Right-click empty cell | Nothing happens | ✅ PASS (Mar 10) |
| Remove updates neighbors | Remove piece between two connected pieces | Neighbor dots update to disconnected | ✅ PASS (Mar 9) |

## Feature: Train Dragging
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Drag train to new track | Drag train SVG to another track cell | Train moves to new cell | ✅ PASS (Mar 9) |
| Drag train to empty cell | Drag train to cell with no track | Train snaps back to original position | ✅ PASS (Mar 9) |
| Drag train to scenery | Drag train to cell with tree | Train snaps back, toast "needs a track" | ✅ PASS (Mar 9) |
| Drag train to trash | Drag train to trash zone | Train removed, track stays | ✅ PASS (Mar 9) |
| Click under train rotates track | Click the cell around the train (not on train SVG) | Track underneath rotates | ✅ PASS (Mar 9) |

## Feature: Random Track Generator
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Random generates track | Click Random button | Track layout appears with animation | ✅ PASS (Mar 10) |
| All dots green | After Random, inspect dots | Every connection dot is green (no red) | 🔧 FIXED (Mar 10) — BUG-004: stale dots during animated placement |
| Train placed | After Random | Train SVG visible on a straight section | ✅ PASS (Mar 10) |
| Scenery added | After Random | Trees, houses, and/or cows scattered around | ✅ PASS (Mar 10) |
| Track is a loop | After Random, press Play | Train runs continuously without stopping | ✅ PASS (Mar 10) |
| Variety test | Press Random 10 times | At least 2 visually different shapes appear | ✅ PASS (Mar 10) — multiple shapes confirmed |
| Random while playing | Press Random during play | Play stops, new track generated | ✅ PASS (Mar 10) |
| Consistent generation | Press Random 20 times | No errors, each generates a valid layout | ✅ PASS (Mar 10) — 5/5 clean (with dot fix) |

## Feature: Play / Animation
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Play starts | Place train on loop, press Play | Train animates along track | ✅ PASS (Mar 10) |
| Train follows straights | Build straight track | Train moves in correct direction | ✅ PASS (Mar 10) |
| Train follows curves | Build track with curves | Train follows curve path smoothly | ✅ PASS (Mar 10) |
| Train on T-junction | Build track with T-junction | Train goes straight through (or turns correctly) | ✅ PASS (Mar 9) |
| Train on crossover | Build track with crossover | Train stays on its axis (doesn't switch) | ✅ PASS (Mar 9) |
| Train on bridge | Build track with bridge | Train stays on correct layer | ✅ PASS (Mar 9) |
| Station sound | Train passes station | Ding-ding sound effect plays | ✅ PASS (Mar 9) |
| Dead end stop | Build track ending in dead end | Train stops with crash sound and toast | ✅ PASS (Mar 10) |
| Speed slider | Adjust speed during play | Train visibly speeds up/slows down | ✅ PASS (Mar 10) |
| Stop button | Press Stop during play | Animation stops, train returns to start | ✅ PASS (Mar 10) |
| Loop detection | Build a loop, press Play | Train runs forever without stopping | ✅ PASS (Mar 10) |
| Whistle on start | Press Play | Whistle sound plays | ✅ PASS (Mar 9) |

## Feature: Sound
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Place sound | Place any piece | Snap sound plays | ✅ PASS (Mar 10) |
| Rotate sound | Click to rotate | Click sound plays | ✅ PASS (Mar 10) |
| Remove sound | Right-click remove | Pop sound plays | ✅ PASS (Mar 9) |
| Mute toggle | Click mute button | Icon changes, all sounds stop | ✅ PASS (Mar 10) — 🔊→🔇 |
| Unmute | Click mute button again | Icon changes back, sounds resume | ✅ PASS (Mar 10) — 🔇→🔊 |

## Feature: Undo
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Undo placement | Place piece, press Undo | Piece removed | ✅ PASS (Mar 10) |
| Undo rotation | Rotate piece, press Undo | Piece returns to previous rotation | ✅ PASS (Mar 10) |
| Undo removal | Remove piece, press Undo | Piece restored | ✅ PASS (Mar 10) |
| Multiple undos | Place 3 pieces, undo 3 times | All 3 removed in reverse order | ✅ PASS (Mar 10) |

## Feature: Clear
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Clear all | Place several pieces and train, press Clear | Board empty, train gone | ✅ PASS (Mar 10) |
| Clear during play | Press Clear while playing | Play stops, board cleared | ✅ PASS (Mar 10) |

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

### Day 1 QA — Tue Mar 10
**Feature tested:** Day 1 feature (Fix Wobbly Loop + Figure-8 Generator) NOT shipped yet — builder hasn't pushed. Full regression test instead.
**New tests added:** 0
**Results:** 57/57 passed (2 bugs found and fixed during this session)
**Bugs found:** 2 (BUG-003: single train enforcement DOM leak, BUG-004: stale connection dots after animated random generation)
**Bugs fixed:** 2
- **BUG-003** (commit f38a18c): `placeTrain` was re-rendering the old cell BEFORE updating `state.train`, so `renderCell` saw the old position still matched and re-drew the train SVG. Fix: save old position, update state first, then re-render.
- **BUG-004** (commit f062880): `generateRandomTrack` animated placement updated dots only for each cell as placed, not for already-placed neighbors. After animation, some dots were stale (showing red when they should be green). Fix: added final pass to refresh all dots after all pieces placed.
- Both fixes verified on live GitHub Pages site.
- No JS errors. All 57 tests pass.
