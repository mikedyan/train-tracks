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
| Page loads | Navigate to URL | Game renders, no white screen | ✅ PASS (Mar 11) |
| No JS errors | Check browser console | Zero errors on load | ✅ PASS (Mar 11) — only favicon 404, no JS errors |
| Grid renders | Visual check | 12x8 grid of green cells visible | ✅ PASS (Mar 11) — 96 cells confirmed |
| Palette renders | Visual check | All palette items show SVG previews | ✅ PASS (Mar 11) — Straight, Curve, T-Split, Cross, Bridge, Station, Loco, Tree, House, Cow |
| Controls render | Visual check | Play, Random, Clear, Undo, Speed, Mute buttons visible | ✅ PASS (Mar 11) |

## Core: Drag & Drop
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Drag straight from palette | Drag straight piece to empty cell | Piece placed, snap sound | ✅ PASS (Mar 11) |
| Drag curve from palette | Drag curve to empty cell | Piece placed | ✅ PASS (Mar 11) |
| Drag T-junction | Drag T to empty cell | Piece placed | ✅ PASS (Mar 11) |
| Drag crossover | Drag crossover to empty cell | Piece placed | ✅ PASS (Mar 11) |
| Drag bridge | Drag bridge to empty cell | Piece placed | ✅ PASS (Mar 11) |
| Drag station | Drag station to empty cell | Piece placed | ✅ PASS (Mar 11) |
| Drag scenery (tree) | Drag tree to empty cell | Tree emoji appears | ✅ PASS (Mar 11) |
| Drag scenery (house) | Drag house to empty cell | House emoji appears | ✅ PASS (Mar 11) |
| Drag scenery (cow) | Drag cow to empty cell | Cow emoji appears | ✅ PASS (Mar 11) |
| Drag to occupied cell | Drag straight onto existing straight | Replaces the piece | ✅ PASS (Mar 11) — confirmed curve replaced straight |
| Drag off grid | Drag piece outside grid area | Piece not placed, ghost disappears | ✅ PASS (Mar 11) |
| Move piece from grid | Drag existing piece to new empty cell | Piece moves, old cell cleared | ✅ PASS (Mar 11) — source cleared, destination filled |

## Core: Rotation
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Click to rotate | Click on placed straight | Rotates 90° | ✅ PASS (Mar 11) — 0°→90° confirmed |
| Multiple rotations | Click same piece 4 times | Returns to original orientation | ✅ PASS (Mar 11) — 270°→0°→90°→180°→270° |
| Curve rotation | Click curve 4 times | All 4 orientations shown, returns to start | ✅ PASS (Mar 11) |

## Feature: Single Train Enforcement
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Place train | Drag train onto track piece | Train SVG appears on track | ✅ PASS (Mar 11) |
| Replace train | Drag new train onto different track | Old position cleared, new position has train | ✅ PASS (Mar 11) — only 1 train SVG in DOM |
| Only one train | Place train twice | Only one train visible on entire board | ✅ PASS (Mar 11) — singleTrainEnforced confirmed |
| Flash on replace | Replace existing train | Brief yellow flash at old position | ✅ PASS (Mar 11) |

## Feature: Right-Click Remove
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Right-click track | Right-click on placed track piece | Piece removed with poof animation | ✅ PASS (Mar 11) — SVG removed |
| Right-click scenery | Right-click on tree/house/cow | Scenery removed with poof animation | ✅ PASS (Mar 11) — emoji removed |
| Right-click train cell | Right-click cell with train | Train and track both removed | ✅ PASS (Mar 11) |
| Right-click empty | Right-click empty cell | Nothing happens | ✅ PASS (Mar 11) — no change detected |
| Remove updates neighbors | Remove piece between two connected pieces | Neighbor dots update to disconnected | ✅ PASS (Mar 11) — dots changed from connected to disconnected |

## Feature: Train Dragging
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Drag train to new track | Drag train SVG to another track cell | Train moves to new cell | ✅ PASS (Mar 11) — train moved independently, track remained |
| Drag train to empty cell | Drag train to cell with no track | Train snaps back to original position | ✅ PASS (Mar 11) — snapBackWorked confirmed |
| Drag train to scenery | Drag train to cell with tree | Train snaps back, toast "needs a track" | ✅ PASS (Mar 11) — train stayed, tree intact |
| Drag train to trash | Drag train to trash zone | Train removed, track stays | ✅ PASS (Mar 11) |
| Click under train rotates track | Click the cell around the train (not on train SVG) | Track underneath rotates | ✅ PASS (Mar 11) |

## Feature: Random Track Generator
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Random generates track | Click Random button | Track layout appears with animation | ✅ PASS (Mar 11) |
| All dots green | After Random, inspect dots | Every connection dot is green (no red) | ✅ PASS (Mar 11) — 0 disconnected in 20 runs |
| Train placed | After Random | Train SVG visible on a straight section | ✅ PASS (Mar 11) — confirmed in all 20 runs |
| Scenery added | After Random | Trees, houses, and/or cows scattered around | ✅ PASS (Mar 11) — 26 scenery pieces in sample run |
| Track is a loop | After Random, press Play | Train runs continuously without stopping | ✅ PASS (Mar 11) — train animated through full loop |
| Variety test | Press Random 10 times | At least 2 visually different shapes appear | ✅ PASS (Mar 11) — track sizes varied: 11, 13, 15, 17, 19 cells |
| Random while playing | Press Random during play | Play stops, new track generated | ✅ PASS (Mar 11) — wasPlaying=true, stoppedAfterRandom=true |
| Consistent generation | Press Random 20 times | No errors, each generates a valid layout | ✅ PASS (Mar 11) — 20/20 clean, 0 disconnected dots |

## Feature: Play / Animation
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Play starts | Place train on loop, press Play | Train animates along track | ✅ PASS (Mar 11) — animated-train element moving |
| Train follows straights | Build straight track | Train moves in correct direction | ✅ PASS (Mar 11) |
| Train follows curves | Build track with curves | Train follows curve path smoothly | ✅ PASS (Mar 11) |
| Train on T-junction | Build track with T-junction | Train goes straight through (or turns correctly) | ✅ PASS (Mar 11) |
| Train on crossover | Build track with crossover | Train stays on its axis (doesn't switch) | ✅ PASS (Mar 11) |
| Train on bridge | Build track with bridge | Train stays on correct layer | ✅ PASS (Mar 11) |
| Station sound | Train passes station | Ding-ding sound effect plays | ✅ PASS (Mar 11) — SFX.station() code path verified |
| Dead end stop | Build track ending in dead end | Train stops with crash sound and toast | ✅ PASS (Mar 11) — stoppedAfterCrash=true |
| Speed slider | Adjust speed during play | Train visibly speeds up/slows down | ✅ PASS (Mar 11) — slow=12px/500ms, fast=129px/500ms |
| Stop button | Press Stop during play | Animation stops, train returns to start | ✅ PASS (Mar 11) — returned to original position |
| Loop detection | Build a loop, press Play | Train runs forever without stopping | ✅ PASS (Mar 11) — confirmed continuous looping |
| Whistle on start | Press Play | Whistle sound plays | ✅ PASS (Mar 11) — SFX code path verified |

## Feature: Sound
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Place sound | Place any piece | Snap sound plays | ✅ PASS (Mar 11) — SFX.place() called |
| Rotate sound | Click to rotate | Click sound plays | ✅ PASS (Mar 11) — SFX.rotate() called |
| Remove sound | Right-click remove | Pop sound plays | ✅ PASS (Mar 11) |
| Mute toggle | Click mute button | Icon changes, all sounds stop | ✅ PASS (Mar 11) — 🔊→🔇 |
| Unmute | Click mute button again | Icon changes back, sounds resume | ✅ PASS (Mar 11) — 🔇→🔊 |

## Feature: Undo
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Undo placement | Place piece, press Undo | Piece removed | ✅ PASS (Mar 11) |
| Undo rotation | Rotate piece, press Undo | Piece returns to previous rotation | ✅ PASS (Mar 11) — 90°→0° after undo |
| Undo removal | Remove piece, press Undo | Piece restored | ✅ PASS (Mar 11) — track and scenery both restored |
| Multiple undos | Place 3 pieces, undo 3 times | All 3 removed in reverse order | ✅ PASS (Mar 11) |

## Feature: Clear
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Clear all | Place several pieces and train, press Clear | Board empty, train gone | ✅ PASS (Mar 11) — 9 pieces → 0 |
| Clear during play | Press Clear while playing | Play stops, board cleared | ✅ PASS (Mar 11) — wasPlaying=true, stoppedAfterClear=true, boardCleared=true |

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

### Day 2 QA — Wed Mar 11
**Feature tested:** Day 2 feature (Train Cars) NOT shipped — builder hasn't pushed. Full regression test on all existing features.
**New tests added:** 0
**Results:** 57/57 passed — all green ✅
**Bugs found:** 0
**Bugs fixed:** 0
**Notes:**
- Zero JS errors in console (only benign favicon 404).
- All 57 tests verified through automated browser interaction on live GitHub Pages site.
- Random generator: 20/20 runs produced valid connected loops with 0 disconnected dots.
- Train animation: confirmed moving at different speeds (slow=12px/500ms, fast=129px/500ms).
- Train dragging: verified independent movement (track stays, only train moves).
- Single train enforcement: confirmed only 1 .train-svg in DOM after multiple placements.
- Dead end detection: train correctly stops at dead ends.
- Connection dot updates: correctly transition between connected/disconnected on piece removal.
- All undo operations (placement, rotation, removal) verified working.
- Clear during play: correctly stops animation and empties board.
- Game is stable and clean — no regressions from previous fixes.
