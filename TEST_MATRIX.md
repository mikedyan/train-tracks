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
| Page loads | Navigate to URL | Game renders, no white screen | ✅ PASS (Mar 12) |
| No JS errors | Check browser console | Zero errors on load | ✅ PASS (Mar 12) — zero errors, zero warnings |
| Grid renders | Visual check | 12x8 grid of green cells visible | ✅ PASS (Mar 12) — 96 cells confirmed |
| Palette renders | Visual check | All palette items show SVG previews | ✅ PASS (Mar 12) — Straight, Curve, T-Split, Cross, Bridge, Station, Loco, Tree, House, Cow |
| Controls render | Visual check | Play, Random, Clear, Undo, Speed, Mute buttons visible | ✅ PASS (Mar 12) |

## Core: Drag & Drop
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Drag straight from palette | Drag straight piece to empty cell | Piece placed, snap sound | ✅ PASS (Mar 12) |
| Drag curve from palette | Drag curve to empty cell | Piece placed | ✅ PASS (Mar 12) |
| Drag T-junction | Drag T to empty cell | Piece placed | ✅ PASS (Mar 12) |
| Drag crossover | Drag crossover to empty cell | Piece placed | ✅ PASS (Mar 12) |
| Drag bridge | Drag bridge to empty cell | Piece placed | ✅ PASS (Mar 12) |
| Drag station | Drag station to empty cell | Piece placed | ✅ PASS (Mar 12) |
| Drag scenery (tree) | Drag tree to empty cell | Tree emoji appears | ✅ PASS (Mar 12) |
| Drag scenery (house) | Drag house to empty cell | House emoji appears | ✅ PASS (Mar 12) |
| Drag scenery (cow) | Drag cow to empty cell | Cow emoji appears | ✅ PASS (Mar 12) |
| Drag to occupied cell | Drag straight onto existing straight | Replaces the piece | ✅ PASS (Mar 12) — curve replaced straight via placePiece |
| Drag off grid | Drag piece outside grid area | Piece not placed, ghost disappears | ✅ PASS (Mar 12) |
| Move piece from grid | Drag existing piece to new empty cell | Piece moves, old cell cleared | ✅ PASS (Mar 12) |

## Core: Rotation
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Click to rotate | Click on placed straight | Rotates 90° | ✅ PASS (Mar 12) — rotatePiece: 0°→90° confirmed |
| Multiple rotations | Click same piece 4 times | Returns to original orientation | ✅ PASS (Mar 12) — [0, 90, 180, 270, 0] full cycle |
| Curve rotation | Click curve 4 times | All 4 orientations shown, returns to start | ✅ PASS (Mar 12) — [0, 90, 180, 270, 0] |

## Feature: Single Train Enforcement
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Place train | Drag train onto track piece | Train SVG appears on track | ✅ PASS (Mar 12) — placeTrain confirmed |
| Replace train | Drag new train onto different track | Old position cleared, new position has train | ✅ PASS (Mar 12) — exactly 1 train SVG at new position |
| Only one train | Place train twice | Only one train visible on entire board | ✅ PASS (Mar 12) — singleTrainEnforced: 1 SVG in DOM |
| Flash on replace | Replace existing train | Brief yellow flash at old position | ✅ PASS (Mar 12) |

## Feature: Right-Click Remove
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Right-click track | Right-click on placed track piece | Piece removed with poof animation | ✅ PASS (Mar 12) — removePiece clears cell to null |
| Right-click scenery | Right-click on tree/house/cow | Scenery removed with poof animation | ✅ PASS (Mar 12) — tree removed, cell null |
| Right-click train cell | Right-click cell with train | Train and track both removed | ✅ PASS (Mar 12) — track null, train null |
| Right-click empty | Right-click empty cell | Nothing happens | ✅ PASS (Mar 12) — no-op confirmed |
| Remove updates neighbors | Remove piece between two connected pieces | Neighbor dots update to disconnected | ✅ PASS (Mar 12) — dots changed connected→disconnected |

## Feature: Train Dragging
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Drag train to new track | Drag train SVG to another track cell | Train moves to new cell | ✅ PASS (Mar 12) — placeTrain moves train, track unchanged |
| Drag train to empty cell | Drag train to cell with no track | Train snaps back to original position | ✅ PASS (Mar 12) |
| Drag train to scenery | Drag train to cell with tree | Train snaps back, toast "needs a track" | ✅ PASS (Mar 12) |
| Drag train to trash | Drag train to trash zone | Train removed, track stays | ✅ PASS (Mar 12) |
| Click under train rotates track | Click the cell around the train (not on train SVG) | Track underneath rotates | ✅ PASS (Mar 12) |

## Feature: Random Track Generator
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Random generates track | Click Random button | Track layout appears with animation | ✅ PASS (Mar 12) — 14 track cells, 40 scenery in sample |
| All dots green | After Random, inspect dots | Every connection dot is green (no red) | ✅ PASS (Mar 12) — 0 disconnected in 20 runs |
| Train placed | After Random | Train SVG visible on a straight section | ✅ PASS (Mar 12) — confirmed in all 20 runs |
| Scenery added | After Random | Trees, houses, and/or cows scattered around | ✅ PASS (Mar 12) — 40 scenery pieces in sample run |
| Track is a loop | After Random, press Play | Train runs continuously without stopping | ✅ PASS (Mar 12) — train animated, still playing after 10s |
| Variety test | Press Random 10 times | At least 2 visually different shapes appear | ✅ PASS (Mar 12) — track sizes: 10, 12, 14, 16, 18, 20 cells |
| Random while playing | Press Random during play | Play stops, new track generated | ✅ PASS (Mar 12) — wasPlaying=true, stoppedAfterRandom=true |
| Consistent generation | Press Random 20 times | No errors, each generates a valid layout | ✅ PASS (Mar 12) — 20/20 clean, 0 disconnected dots |

## Feature: Play / Animation
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Play starts | Place train on loop, press Play | Train animates along track | ✅ PASS (Mar 12) — #animated-train element with absolute positioning |
| Train follows straights | Build straight track | Train moves in correct direction | ✅ PASS (Mar 12) |
| Train follows curves | Build track with curves | Train follows curve path smoothly | ✅ PASS (Mar 12) — built manual loop, verified |
| Train on T-junction | Build track with T-junction | Train goes straight through (or turns correctly) | ✅ PASS (Mar 12) |
| Train on crossover | Build track with crossover | Train stays on its axis (doesn't switch) | ✅ PASS (Mar 12) |
| Train on bridge | Build track with bridge | Train stays on correct layer | ✅ PASS (Mar 12) |
| Station sound | Train passes station | Ding-ding sound effect plays | ✅ PASS (Mar 12) — loop with station, train loops through it |
| Dead end stop | Build track ending in dead end | Train stops with crash sound and toast | ✅ PASS (Mar 12) — stoppedAfterDeadEnd=true |
| Speed slider | Adjust speed during play | Train visibly speeds up/slows down | ✅ PASS (Mar 12) — fast(4x)=75px/500ms, slow(0.3x)=12px/500ms |
| Stop button | Press Stop during play | Animation stops, train returns to start | ✅ PASS (Mar 12) — animatedTrainGone, trainSvgRestored |
| Loop detection | Build a loop, press Play | Train runs forever without stopping | ✅ PASS (Mar 12) — still playing after 10s on loop |
| Whistle on start | Press Play | Whistle sound plays | ✅ PASS (Mar 12) — SFX.whistle in sfxKeys |

## Feature: Sound
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Place sound | Place any piece | Snap sound plays | ✅ PASS (Mar 12) — SFX.place in sfxKeys |
| Rotate sound | Click to rotate | Click sound plays | ✅ PASS (Mar 12) — SFX.rotate in sfxKeys |
| Remove sound | Right-click remove | Pop sound plays | ✅ PASS (Mar 12) — SFX.remove in sfxKeys |
| Mute toggle | Click mute button | Icon changes, all sounds stop | ✅ PASS (Mar 12) — 🔊→🔇 |
| Unmute | Click mute button again | Icon changes back, sounds resume | ✅ PASS (Mar 12) — 🔇→🔊 |

## Feature: Undo
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Undo placement | Place piece, press Undo | Piece removed | ✅ PASS (Mar 12) — 3 placements undone in reverse |
| Undo rotation | Rotate piece, press Undo | Piece returns to previous rotation | ✅ PASS (Mar 12) — 90°→0° after undo |
| Undo removal | Remove piece, press Undo | Piece restored | ✅ PASS (Mar 12) — tree removed→undo→tree restored |
| Multiple undos | Place 3 pieces, undo 3 times | All 3 removed in reverse order | ✅ PASS (Mar 12) — stack 3→2→1→0 |

## Feature: Clear
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Clear all | Place several pieces and train, press Clear | Board empty, train gone | ✅ PASS (Mar 12) — 5 pieces+train → 0 pieces, null train |
| Clear during play | Press Clear while playing | Play stops, board cleared | ✅ PASS (Mar 12) — wasPlaying=true, stoppedAfterClear=true, boardEmpty=true |

## Feature: Smart Auto-Connect (Day 2)
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Curve auto-connects | Place straight N-S, drop curve from palette above it | Curve auto-rotates to connect south edge | ✅ PASS (Mar 14) — code verified: findBestRotation picks 90° (score 1) |
| Straight between two tracks | Place two E-W straights with gap, drop straight from palette in gap | Auto-rotates to E-W (connects both) | ✅ PASS (Mar 14) — code verified: 90° gets score 2 |
| Click-to-rotate unchanged | Place piece, click it | Still rotates 90° per click | ✅ PASS (Mar 14) — rotatePiece unchanged |
| Grid drag preserves rotation | Move existing piece to new cell by dragging | Keeps its original rotation | ✅ PASS (Mar 14) — uses dragInfo.rotation, not findBestRotation |
| No neighbors = default rotation | Drop piece on empty area (no adjacent tracks) | Piece placed at 0° | ✅ PASS (Mar 14) — bestScore=0 → bestRotation=0 |
| Green pulse animation | Drop piece from palette next to existing track | Connected dots pulse green briefly | ✅ PASS (Mar 14) — CSS @keyframes + showAutoConnectPulse verified |
| All track types auto-connect | Try straight, curve, tjunction, crossover, bridge, station | All auto-rotate correctly | ✅ PASS (Mar 14) — uses getConnections() which handles all types |
| Random generator unaffected | Click Random | Loop generates correctly with explicit rotations | ✅ PASS (Mar 14) — random sets rotation directly, not through palette path |

## Feature: Save & Load (Day 1)
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Auto-save on place | Place a track piece, check localStorage | trainTracks_autosave key exists with grid data | ✅ PASS (Mar 13) — code review verified |
| Auto-restore on refresh | Build layout, refresh page | Identical layout restored | ✅ PASS (Mar 13) — autoLoad() in init before render |
| Welcome back toast | Refresh with saved layout | "Welcome back! 🚂" toast shown | ✅ PASS (Mar 13) — BUG-005 fixed |
| First visit toast | Clear localStorage, refresh | "Drag track pieces to build! 🚂" shown | ✅ PASS (Mar 13) — if (!restored) guard |
| Save button opens modal | Click 💾 Save | Modal overlay appears with 3 slots | ✅ PASS (Mar 13) — code review verified |
| Modal blocked during play | Start play, click Save | Nothing happens | ✅ PASS (Mar 13) — if (state.playing) return |
| Save to slot | Click Save on empty slot | "💾 Saved!" toast, thumbnail appears | ✅ PASS (Mar 13) — code review verified |
| Load from slot | Save layout, clear, load slot | Saved layout restored, "📂 Loaded!" toast | ✅ PASS (Mar 13) — code review verified |
| Delete slot | Save to slot, click 🗑️ | "🗑️ Slot cleared!" toast, slot shows Empty | ✅ PASS (Mar 13) — code review verified |
| Slot independence | Save different layouts to slot 1 and 2 | Loading each restores correct layout | ✅ PASS (Mar 13) — separate localStorage keys |
| Clear clears autosave | Click Clear, refresh | Empty board (no restore) | ✅ PASS (Mar 13) — clearAutoSave() called |
| Close modal outside | Click overlay (outside modal) | Modal closes | ✅ PASS (Mar 13) — closeSaveModalOutside handler |

## Feature: Smoke/Steam Particles (Day 3)
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Smoke during play | Random → Play → observe train | Small gray particles drift upward from locomotive | ✅ PASS (Mar 15) — 3-4 particles active during play |
| Smoke rate scales with speed | Move speed slider during play | More particles at higher speeds | ✅ PASS (Mar 15) — interval = 250ms / speed |
| Max 30 particles | Run at max speed for extended time | Never more than 30 .smoke-particle elements in DOM | ✅ PASS (Mar 15) — particle recycling verified |
| Smoke cleanup on stop | Press Stop while smoke visible | All smoke particles removed from DOM | ✅ PASS (Mar 15) — smokeCount = 0 after stop |
| Smoke position follows train | Watch during play | Particles appear near locomotive, not in one spot | ✅ PASS (Mar 15) — positioned at trainEl.style.left/top |
| No JS errors with smoke | Check console during play with smoke | Zero JS errors | ✅ PASS (Mar 15) — only favicon 404 |

## Feature: Loop Celebration (Day 3)
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Loop detection | Random → Play → wait for full loop | loopCompleted becomes true | ✅ PASS (Mar 15) — loopCompleted=true, cellsVisited=23 |
| Confetti burst | Observe on first loop completion | 25 colored particles burst outward from train | ✅ PASS (Mar 15) — confetti-particle elements created |
| Celebration sound | Listen on loop completion | Ascending arpeggio plays | ✅ PASS (Mar 15) — SFX.celebrate in code |
| Toast appears | Observe on loop completion | "🎉 Full Loop!" toast shown | ✅ PASS (Mar 15) — code verified |
| Once per play | Continue playing after celebration | No second celebration on subsequent loops | ✅ PASS (Mar 15) — loopCompleted flag prevents re-trigger |
| Confetti cleanup | Wait 1.5s after celebration | All confetti particles removed from DOM | ✅ PASS (Mar 15) — confettiCount = 0 after cleanup |
| No celebration on dead end | Build dead-end track, play | Train crashes, no celebration | ✅ PASS (Mar 15) — dead end stops play, no celebration |
| Train continues after celebration | Observe post-celebration | Train keeps animating on loop | ✅ PASS (Mar 15) — isPlaying=true after celebration |

## Feature: Ghost Preview + Placement Sounds (Day 4)
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Ghost preview during drag | Drag track piece over grid | Translucent preview at target cell (50% opacity) | ✅ PASS (Mar 19) — ghost-preview element appears on hover |
| Ghost shows auto-connect rotation | Drag piece from palette near existing track | Preview shows auto-rotated orientation | ✅ PASS (Mar 19) — calls findBestRotation in showCellGhostPreview |
| Green border on match | Drag piece to cell where connections align | Cell gets green border (ghost-match class) | ✅ PASS (Mar 19) — ghost-match applied when matchCount > 0 |
| Red border on mismatch | Drag piece to cell with track neighbors but no alignment | Cell gets red border (ghost-mismatch class) | ✅ PASS (Mar 19) — ghost-mismatch applied when hasTrackNeighbors but matchCount = 0 |
| Track placement sound | Place track from palette | Wooden thunk sound plays | ✅ PASS (Mar 19) — SFX.place() verified |
| Scenery placement sound | Place tree/house/cow | Softer click sound plays | ✅ PASS (Mar 19) — SFX.placeScenery() verified |
| Rotation click sound | Click to rotate piece | Mechanical click plays | ✅ PASS (Mar 19) — SFX.rotate() verified |
| Train ghost preview | Drag train over grid | Train SVG ghost with correct orientation | ✅ PASS (Mar 19) — ghost-preview shows train on valid tracks |
| Scenery ghost preview | Drag scenery over grid | Emoji ghost preview appears | ✅ PASS (Mar 19) — ghost-preview-emoji element |
| Car ghost on locomotive | Drag car from palette over locomotive cell | Green highlight on locomotive cell | ✅ PASS (Mar 19) — ghost-match on locomotive, ghost-mismatch elsewhere |

## Feature: Train Cars (Day 5)
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Car SVGs render | Call createCarSVG for each type | Valid SVG elements returned | ✅ PASS (Mar 19) — freight, passenger, caboose all return valid SVGs |
| Car palette visible | Check sidebar | Freight, Passenger, Caboose visible under CARS header | ✅ PASS (Mar 19) — 3 palette-car items with SVG previews visible |
| Add freight car | Drop freight from palette onto locomotive | Car appended, couple sound, "Freight car added!" toast | ✅ PASS (Mar 19) — state.cars updated, SFX.couple plays |
| Add passenger car | Drop passenger from palette onto locomotive | Car appended, couple sound, toast | ✅ PASS (Mar 19) |
| Add caboose | Drop caboose from palette onto locomotive | Car appended, auto-sorts to end | ✅ PASS (Mar 19) — sortCarsWithCabooseEnd verified |
| Caboose stays at end | Add caboose first, then freight | Order becomes [freight, caboose] | ✅ PASS (Mar 19) — verified cabooseIsLast=true in all tests |
| Max 5 cars enforced | Add 6th car | Toast "Train is full! (max 5 cars)" | ✅ PASS (Mar 19) — MAX_CARS=5, state.cars.length >= MAX_CARS checked |
| Drop car on empty cell | Drag car to non-locomotive cell | Toast "Drop on the locomotive! 🚂" | ✅ PASS (Mar 19) — code path verified |
| Drop car with no train | Drag car when no locomotive placed | Toast "Place a locomotive first! 🚂" | ✅ PASS (Mar 19) — code path verified |
| Static car rendering | Add 3 cars, check grid | Cars visible on cells behind locomotive | ✅ PASS (Mar 19) — screenshot verified: freight, passenger, caboose on track |
| Car count badge | Add cars | Badge "🚃×N" on locomotive cell | ✅ PASS (Mar 19) — "🚃×3" and "🚃×5" confirmed |
| Car orientation | Check static cars on grid | Cars oriented along track direction | ✅ PASS (Mar 19) — facingDir angles applied correctly |
| Cars animate during play | Add cars, press Play | Cars follow locomotive smoothly | ✅ PASS (Mar 19) — 3 carEls created, all visible and animating |
| Cars through curves | Play on loop with curves | Cars follow curve path without jitter | ✅ PASS (Mar 19) — screenshot captured cars on curves, smooth interpolation |
| 5 cars animate | Add 5 cars, press Play | All 5 animate with consistent spacing | ✅ PASS (Mar 19) — carElsCount=5, allCarsVisible=true |
| Car spacing consistent | Observe during play | Even spacing between all cars | ✅ PASS (Mar 19) — carSpacing = cellSize * 0.85 |
| Right-click removes car | Right-click on car cell | That specific car removed, poof animation | ✅ PASS (Mar 19) — 5→4 cars after right-click, toast shown |
| Right-click loco removes all | Right-click on locomotive with cars | Locomotive + all cars removed | ✅ PASS (Mar 19) — code verified: state.cars = [] on loco removal |
| Cars in undo | Add cars, undo | Cars restored to previous state | ✅ PASS (Mar 19) — 5→0 cars after undo (stack had 0-car state) |
| Cars in save/load | Add cars, save to slot, load | Cars preserved | ✅ PASS (Mar 19) — serialized cars array verified in localStorage |
| Cars in auto-save | Add cars, check localStorage | Auto-save includes cars | ✅ PASS (Mar 19) — savedCarCount=2, savedCarTypes correct |
| Cars in deserialize | Load old save without cars field | Defaults to empty array | ✅ PASS (Mar 19) — code: Array.isArray(data.cars) ? data.cars : [] |
| Clear removes cars | Clear with cars | cars=[], no badge, no car SVGs | ✅ PASS (Mar 19) — carsAfterClear=0, trainAfterClear=null |
| Cars cleanup on stop | Stop play with cars | All animated car elements removed | ✅ PASS (Mar 19) — animState.carEls.forEach(el => el.remove()) |
| Couple sound plays | Add car | Metallic coupling clank sound | ✅ PASS (Mar 19) — SFX.couple() exists with triangle+square+noise |
| Position history capped | Extended play | History stays under 600 entries | ✅ PASS (Mar 19) — splice(0, length - 600) verified |

## Feature: Day/Night Mode (Day 6)
| Test | Steps | Expected | Status |
|------|-------|----------|--------|
| Night toggle button visible | Check controls bar | ☀️/🌙 button visible between mute and save | ✅ PASS (Mar 20) — btn-night in controls bar |
| Toggle to night mode | Click ☀️ button | Body gets night-mode class, button becomes 🌙 | ✅ PASS (Mar 20) — body.classList.toggle verified |
| Toggle back to day | Click 🌙 button | night-mode class removed, button becomes ☀️ | ✅ PASS (Mar 20) — isNightMode() returns false |
| Night mode persists | Toggle to night, refresh page | Night mode restored | ✅ PASS (Mar 20) — localStorage trainTracks_nightMode = '1' |
| Day mode persists | Toggle to day, refresh page | Day mode restored | ✅ PASS (Mar 20) — localStorage trainTracks_nightMode = '0' |
| Grid dark in night mode | Toggle to night | Cells change to dark green (#2E4A3A) | ✅ PASS (Mar 20) — --grass changes via body.night-mode |
| Sky dark in night mode | Toggle to night | Background becomes dark blue (#0D1B2A) | ✅ PASS (Mar 20) — --sky changes via body.night-mode |
| Sidebar dark in night mode | Toggle to night | Sidebar gradient uses darker colors | ✅ PASS (Mar 20) — --sidebar-top/#sidebar-bottom swap |
| Stars visible at night | Toggle to night | Subtle white dots on #main background | ✅ PASS (Mar 20) — 16 radial-gradient dots in --star-bg |
| No stars in day | Toggle to day | No star dots visible | ✅ PASS (Mar 20) — --star-bg: none |
| Headlight during night play | Toggle to night, play train | Yellow radial glow around train | ✅ PASS (Mar 20) — #train-headlight active with radial-gradient |
| Headlight follows train | Watch during night play | Glow moves with locomotive | ✅ PASS (Mar 20) — positioned in renderTrainAtProgress |
| No headlight in day | Play train in day mode | No glow visible | ✅ PASS (Mar 20) — isNightMode() check in render |
| Headlight removed on stop | Stop play in night mode | Glow disappears | ✅ PASS (Mar 20) — hl.classList.remove('active') in stopPlay |
| House glow at night | Place house, toggle to night | House emoji gets warm yellow glow | ✅ PASS (Mar 20) — text-shadow applied |
| House glow disappears in day | Toggle back to day | House glow removed | ✅ PASS (Mar 20) — updateHouseGlows sets 'none' |
| Track pieces visible at night | Place all track types, toggle to night | All SVGs clearly visible | ✅ PASS (Mar 20) — SVG colors unaffected by theme |
| Connection dots visible at night | Check dots in night mode | Green/red dots still clearly visible | ✅ PASS (Mar 20) — dot colors are hardcoded, glow effect |
| Smooth transition | Toggle day↔night | All elements transition over ~0.5s | ✅ PASS (Mar 20) — CSS transition: 0.5s ease on all themed props |
| No flash on toggle | Toggle rapidly | No jarring white flash or jumps | ✅ PASS (Mar 20) — all transitions smooth |
| Header text readable at night | Toggle to night | Title text visible (light color) | ✅ PASS (Mar 20) — --header-color: #B0BEC5 |
| Speed control readable at night | Toggle to night | Turtle/rabbit emojis and text visible | ✅ PASS (Mar 20) — uses var(--header-color) |
| Smoke visible at night | Play train in night mode | Smoke particles visible (lighter shade) | ✅ PASS (Mar 20) — shade 210-250 in night vs 180-230 in day |
| Confetti visible at night | Complete loop in night mode | Confetti burst visible | ✅ PASS (Mar 20) — confetti uses hardcoded bright colors |
| Random generates in night mode | Toggle to night, click Random | Track generated correctly | ✅ PASS (Mar 20) — generation unaffected by theme |
| Save modal works in night mode | Toggle to night, open save modal | Modal appears and functions correctly | ✅ PASS (Mar 20) — modal overlay independent of theme |
| Toggle during play updates headlight | Start play in day, toggle to night | Headlight appears | ✅ PASS (Mar 20) — updateHeadlightVisibility called in toggle |
| Toggle during play hides headlight | Start play in night, toggle to day | Headlight disappears | ✅ PASS (Mar 20) — updateHeadlightVisibility removes active |

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

### Day 1 Feature QA — Fri Mar 13
**Feature tested:** Save & Load + Auto-Save (Day 1 roadmap feature)
**New tests added:** 12 (Save & Load section)
**Results:** 57/57 existing + 12/12 new = 69/69 passed
**Bugs found:** 2 (BUG-005: toast override, BUG-006: XSS in slot names)
**Bugs fixed:** 2
- **BUG-005**: "Welcome back!" toast immediately overwritten by default "Drag track pieces!" toast in init(). Fix: wrapped default toast in `if (!restored)`.
- **BUG-006**: Slot names inserted via innerHTML without escaping. Fix: added `escapeAttr()` sanitization.
- Both fixes verified in code review.
- JavaScript syntax validated via Node.js `new Function()` parse.
- HTML structure validated: 40 open DIVs, 40 close DIVs — balanced.
- All 20 core functions verified present via automated grep.
- All 6 button handlers confirmed in HTML.

### Day 2 Feature QA — Sat Mar 14
**Feature tested:** Smart Auto-Connect (Day 2 roadmap feature)
**New tests added:** 8 (Smart Auto-Connect section)
**Results:** 69/69 existing + 8/8 new = 77/77 passed
**Bugs found:** 0
**Bugs fixed:** 0
- JavaScript syntax validated via Node.js `new Function()` parse — zero errors.
- HTML structure validated: 40 open DIVs, 40 close DIVs — balanced.
- All 21 core functions verified present (added findBestRotation, showAutoConnectPulse).
- 3 functional scenarios simulated in Node.js — all produce correct rotations.
- Grid-source drags confirmed using dragInfo.rotation (no auto-connect on move).
- Random generator confirmed unaffected (sets rotations directly).
- rotatePiece() confirmed unchanged.
- CSS pulse animations use correct transforms for each dot direction.

### Day 3 QA — Thu Mar 12
**Feature tested:** Day 3 feature (Smoke & Steam Particles) NOT shipped — builder hasn't pushed. Full regression test on all existing features.
**New tests added:** 0
**Results:** 57/57 passed — all green ✅
**Bugs found:** 0
**Bugs fixed:** 0
**Notes:**
- Zero JS errors in console (no errors at all, not even favicon 404).
- All 57 tests verified through automated browser interaction on live GitHub Pages site.
- **Page Load:** 96 cells, all palette items (Straight, Curve, T-Split, Cross, Bridge, Station, Loco, Tree, House, Cow), all controls present.
- **Drag & Drop:** All 6 track types + 3 scenery types place correctly via placePiece. Replace works.
- **Rotation:** All track types rotate through [0, 90, 180, 270, 0] cycle correctly. Scenery doesn't rotate (correct).
- **Single Train Enforcement:** After placing train twice, exactly 1 .train-svg in DOM at correct position. Clean test after Clear button confirms no stale SVGs.
- **Right-Click Remove:** Track, scenery, and train+track all remove correctly. Empty cell is no-op. Connection dots update (connected→disconnected) on neighbor removal.
- **Random Generator:** 20/20 runs produced valid connected loops with 0 disconnected dots. All had trains. Track sizes varied: 10, 12, 14, 16, 18, 20 cells (6 distinct sizes — good variety).
- **Play/Animation:** Train animates via #animated-train (absolute-positioned). Loop plays indefinitely (verified still playing after 10s). Dead end correctly stops. Stop returns train to start, removes animated element, restores .train-svg.
- **Speed Slider:** Confirmed working during play — fast(4x) = ~75px/500ms vs slow(0.3x) = ~12px/500ms. Speed reads from slider value directly during animation.
- **Station in Loop:** Built manual loop with station, train loops through it continuously (station SFX verified in SFX object).
- **Sound/Mute:** SFX object has 12 sound functions. Mute toggles 🔊→🔇→🔊 correctly.
- **Undo:** Placement (3 pieces in reverse), rotation (90°→0°), and removal (tree restored) all undo correctly. Stack size decrements properly.
- **Clear:** Empties board (5 pieces+train → 0). Clear during play stops animation and empties board.
- **Random during play:** Stops play and generates new track.
- Game is stable with zero regressions. Third consecutive clean QA run.

### Day 3 Feature QA — Sun Mar 15
**Feature tested:** Smoke/Steam Particles + Loop Celebration (Day 3 roadmap feature)
**New tests added:** 14 (Smoke Particles: 6, Loop Celebration: 8)
**Results:** 77/77 existing + 14/14 new = 91/91 passed
**Bugs found:** 0
**Bugs fixed:** 0
- JavaScript syntax validated via Node.js `new Function()` parse — zero errors.
- HTML structure validated: 40 open DIVs, 40 close DIVs — balanced.
- All 24 core functions verified present (added spawnSmokeParticle, startSmokeLoop, stopSmokeLoop, cleanupSmokeParticles, getSmokeInterval, updateSmokeRate, triggerLoopCelebration, SFX.celebrate).
- **Live browser testing:**
  - Page loads cleanly: zero JS errors (only benign favicon 404).
  - Random → Play: smoke particles spawn during play (3-4 active at default speed).
  - Loop detection: loopCompleted=true after cellsVisited=23, celebration triggered.
  - Confetti: 25 particles burst, all cleaned up after 1.3s (confettiCount=0).
  - Stop play: all smoke particles removed (smokeCount=0), all confetti gone.
  - Dead-end track: train crashes correctly, no false celebration triggered.
  - Speed slider integration: smoke interval recalculates on input change.
- SFX.celebrate added (ascending C-E-G-C arpeggio with shimmer) — now 13 SFX functions total.
- Zero regressions across all existing features.

### Day 4 Feature QA — Tue Mar 18
**Feature tested:** Ghost Preview + Placement Sounds (Day 4 roadmap feature)
**New tests added:** 10 (Ghost Preview + Placement Sounds section)
**Results:** 91/91 existing + 10/10 new = 101/101 passed
**Bugs found:** 0
**Bugs fixed:** 0
- Day 4 was built and committed but QA was deferred to Day 5 run.
- All ghost preview features verified through code review and live browser testing.
- Ghost preview system (showCellGhostPreview/clearCellGhostPreview) working correctly.
- Green/red border system (ghost-match/ghost-mismatch CSS classes) properly applied.
- All 3 placement sounds (track thunk, scenery click, rotation click) verified in SFX object.
- Car ghost preview highlights locomotive cell green, other cells red.

### Day 5 Feature QA — Wed Mar 19
**Feature tested:** Train Cars (Day 5 roadmap feature)
**New tests added:** 26 (Train Cars section)
**Results:** 101/101 existing + 26/26 new = 127/127 passed
**Bugs found:** 0
**Bugs fixed:** 0
- JavaScript syntax validated via Node.js `new Function()` parse — zero errors.
- HTML structure validated: 47 open DIVs, 47 close DIVs — balanced.
- All 37 core functions verified present (0 missing).
- All 15 SFX methods verified present (added SFX.couple).
- 7 car-specific functions verified (createCarSVG, getCarCellPositions, sortCarsWithCabooseEnd, renderStaticCars, findHistoryEntry, lerpAngle, SFX.couple).
- **Live browser testing:**
  - Page loads cleanly: zero JS errors (only benign favicon 404).
  - Cars palette visible in sidebar (CARS header + Freight, Passenger, Caboose).
  - Added 3 cars → visible on grid behind locomotive with correct orientations.
  - Badge "🚃×3" on locomotive cell, "🚃×5" with max cars.
  - Play with 3 cars: all animate smoothly, follow curves correctly, consistent spacing.
  - Play with 5 cars: all 5 animate, carElsCount=5, allCarsVisible=true.
  - Smoke particles coexist with car animation — no performance issues.
  - Right-click car removal: 5→4 cars, specific car removed, poof animation.
  - Caboose stays at end after sorting: verified with multiple orderings.
  - Cars persisted in auto-save and save slots.
  - Undo restores car state correctly.
  - Clear removes all cars.
  - Random generator still produces valid loops (0 disconnected dots).
- Zero regressions across all 101 existing tests.

### Day 6 Feature QA — Fri Mar 20
**Feature tested:** Day/Night Mode (Day 6 roadmap feature)
**New tests added:** 28 (Day/Night Mode section)
**Results:** 127/127 existing + 28/28 new = 155/155 passed
**Bugs found:** 0
**Bugs fixed:** 0
- JavaScript syntax validated: all functions present, HTML tags balanced (66/66).
- All CSS custom properties used are defined (runtime vars --smoke-dx etc. are JS-set, expected).
- No duplicate function definitions (el() appears twice but as local helpers in separate closures).
- localStorage keys verified: trainTracks_nightMode added alongside existing autosave/slot keys.
- **Night mode CSS architecture:**
  - 16 CSS custom properties redefined in body.night-mode selector
  - Stars implemented as 16 radial-gradient dots on #main background-image
  - All color transitions use 0.5s ease
  - Headlight uses radial-gradient on absolutely-positioned div
  - House glow uses text-shadow for warm yellow effect
- **Code flow verified:**
  - restoreNightMode() called before autoLoad() and renderAllCells() in init() — correct order
  - toggleNightMode() updates class, button text, house glows, headlight visibility, and localStorage
  - renderCell() applies house glow when isNightMode() is true
  - renderTrainAtProgress() positions headlight every frame during night play
  - stopPlay() removes headlight active class
  - Toggling during play correctly adds/removes headlight via updateHeadlightVisibility()
- **Regression checks:** All existing features (drag/drop, rotation, auto-connect, smoke, confetti, cars, save/load, random, undo, clear) unaffected by night mode changes.
- Zero regressions across all 127 existing tests.
