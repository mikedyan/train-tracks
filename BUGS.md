# Train Tracks — Bug Log

Bugs found by QA agent. Should usually be empty — QA fixes everything it finds.
Only logged here if a bug was found, for tracking purposes.

## Status Key
- 🔴 OPEN — Not yet fixed
- 🟡 IN PROGRESS — Being worked on
- 🟢 FIXED — Fixed and verified
- ⚪ WON'T FIX — Accepted behavior

---

## Known Issues (Pre-Roadmap)

### BUG-001 | 🟢 FIXED | Random track generator curve rotations 180° off
- **Found:** Mon Mar 9 by Mike
- **Fixed:** Mon Mar 9 (commit d10b3a2)
- **Details:** All hardcoded corner rotations in generateSimpleRectLoop and generateSpiralLoop were 180° off. getTrackRotation was using travel directions instead of edge connections.

### BUG-002 | 🟢 FIXED (partial) | Wobbly loop generator doesn't close path
- **Found:** Mon Mar 9 during code review
- **Fixed:** Mon Mar 9 (commit 979e016) — QA Agent
- **Severity:** Medium
- **Root cause:** `generateWobblyLoop` walks randomly but has no mechanism to route back to start. After the walk, the fallback condition only checked `path.length < 8`, not whether the path actually closed. Open paths of 8+ cells were returned as valid loops.
- **Fix applied:** Added closure check to fallback: `if (path.length < 8 || !(row === startRow && col === startCol))` — now falls back to `generateSimpleRectLoop` when the wobbly path doesn't close.
- **Verification:** 50/50 generations produce valid closed loops after fix. 0 failures.
- **Remaining:** The wobbly loop algorithm itself still can't close paths — it always falls back to rect. Day 1 builder task will implement proper BFS pathfinding to create truly wobbly closed loops.

---

## Bugs Found During Roadmap

### BUG-003 | 🟢 FIXED | Single train enforcement leaves stale train SVG in DOM
- **Found:** Tue Mar 10 — QA Agent
- **Fixed:** Tue Mar 10 (commit f38a18c) — QA Agent
- **Severity:** Medium (cosmetic/functional — 2 trains visible, only 1 in state)
- **Root cause:** `placeTrain()` called `renderCell()` on the old train's cell BEFORE updating `state.train`. Since `renderCell` checks `state.train.row === row && state.train.col === col` to decide whether to draw the train SVG, the old cell re-drew the train (because `state.train` still pointed there). Result: 2 train SVGs in the DOM, even though state only tracked 1.
- **Fix applied:** Save old train position to local variable, update `state.train` to new position FIRST, then re-render old cell (which now correctly sees it's no longer the train's position and doesn't draw a train SVG).
- **Verification:** Confirmed on live site — placing train twice results in exactly 1 `.train-svg` element at the correct position.

### BUG-005 | 🟢 FIXED | Toast override on auto-restore
- **Found:** Fri Mar 13 — QA Agent (Day 1)
- **Fixed:** Fri Mar 13 (Day 1 QA)
- **Severity:** Low (cosmetic — welcome toast invisible)
- **Root cause:** `init()` showed "Welcome back!" toast followed immediately by "Drag track pieces!" default toast, which overwrote it.
- **Fix applied:** Wrapped default toast in `if (!restored)` condition.

### BUG-006 | 🟢 FIXED | XSS risk in save slot name rendering
- **Found:** Fri Mar 13 — QA Agent (Day 1)
- **Fixed:** Fri Mar 13 (Day 1 QA)
- **Severity:** Low (security — only affects localStorage data the user controls)
- **Root cause:** Slot names inserted via innerHTML with unescaped `value` attribute.
- **Fix applied:** Added `escapeAttr()` function to sanitize `& " < >` characters.

### BUG-004 | 🟢 FIXED | Stale connection dots after animated random track generation
- **Found:** Tue Mar 10 — QA Agent
- **Fixed:** Tue Mar 10 (commit f062880) — QA Agent
- **Severity:** Low-Medium (cosmetic — red dots on a fully-connected loop)
- **Root cause:** `generateRandomTrack()` places pieces with staggered `setTimeout()` calls (40ms apart for animation). Each piece calls `updateConnectionDots(row, col)` only for itself, not for its neighbors. When piece A is placed and checks its east neighbor — that neighbor might not exist yet. Later when the east neighbor IS placed, it updates its own dots but never goes back to update piece A's east dot. Result: after animation completes, some connection dots remain "disconnected" (red) even though the connections are actually valid.
- **Fix applied:** Added a final `setTimeout` after all pieces are placed that refreshes connection dots for every cell in the path. This runs at `delay + 50ms` (after last piece but before scenery/train placement).
- **Verification:** Ran Random 5 times on live site — 0 red dots in all 5 runs.

### BUG-007 | 🟢 FIXED | Car tunnel fade reversed for reverse-direction travel
- **Found:** Thu Mar 27 — QA Agent (Day 11)
- **Fixed:** Thu Mar 27 (Day 11 QA)
- **Severity:** Low (visual — fade direction wrong for one travel direction)
- **Root cause:** Car tunnel fade used pixel-based progress along cell axis, which is direction-dependent. Cars traveling N→S would fade correctly but S→N would fade in at entry and out at exit (reversed).
- **Fix applied:** Changed to direction-agnostic center-distance approach: distance from cell center determines opacity (center=hidden, edges=visible). Works identically regardless of travel direction.

### BUG-008 | 🟢 FIXED | Headlight glow visible inside tunnel in night mode
- **Found:** Thu Mar 27 — QA Agent (Day 11)
- **Fixed:** Thu Mar 27 (Day 11 QA)
- **Severity:** Low (visual — headlight shines through mountain)
- **Root cause:** Headlight update in renderTrainAtProgress didn't check if train was in a tunnel.
- **Fix applied:** Added `!isInTunnel` condition to headlight visibility check.

### BUG-009 | 🟢 FIXED | placeTrainOnLoop skips tunnel cells
- **Found:** Thu Mar 27 — QA Agent (Day 11)
- **Fixed:** Thu Mar 27 (Day 11 QA)
- **Severity:** Low (functional — train might not be placed on generated track)
- **Root cause:** `placeTrainOnLoop` only checked for `cell.type === 'straight'`, but random generator now converts some straights to tunnels. In extreme cases, all straights could be tunnels.
- **Fix applied:** Added `|| cell.type === 'tunnel'` to the placement condition.

### BUG-010 | 🟢 FIXED | cleanupChimneySmoke() defined but never called
- **Found:** Sat Mar 28 — QA Agent (Day 12)
- **Fixed:** Sat Mar 28 (Day 12 QA)
- **Severity:** Low (cosmetic — particles self-clean in ~2s, but clearAll should be immediate)
- **Root cause:** `cleanupChimneySmoke()` function was defined but never invoked during board clear operations.
- **Fix applied:** Added `cleanupChimneySmoke()` call in `clearAll()`.

### BUG-011 | 🟢 FIXED | 6x duplicate code blocks from Day 14
- **Found:** Tue Apr 1 — Factory Day 15
- **Fixed:** Tue Apr 1 (Day 15 critical fix)
- **Severity:** Critical (all JS execution prevented by redeclaration errors)
- **Root cause:** Day 14 builder inserted keyboard shortcuts code 6 times across CSS, HTML, and JS sections.
- **Fix applied:** Removed 5 duplicate copies of each section (1553 lines total).
- **Verification:** JS parses cleanly, all keyboard shortcuts functional.

### BUG-012 | 🟢 FIXED | Locked cell class not persisting in puzzle mode
- **Found:** Tue Apr 1 — QA Day 15
- **Fixed:** Tue Apr 1 (Day 15 QA fix)
- **Severity:** Low (visual — lock icons not visible, but locking still works via JS guards)
- **Root cause:** `renderCell()` removes custom classes but didn't re-apply `locked-cell`. The class was applied once in `loadPuzzle()` but any subsequent `renderCell()` call stripped it.
- **Fix applied:** Added `isPuzzleLocked()` check in `renderCell()` to re-apply `locked-cell` class on every render.


### BUG-013 | 🟢 FIXED | 6x duplicated quick-select blocks in onGridDown
- **Found:** Fri Apr 4 — Factory Day 17
- **Fixed:** Fri Apr 4 (Day 17 build)
- **Severity:** Medium (functional — extra iterations through redundant code, performance waste)
- **Root cause:** Previous build inserted the quick-select tool check block 6 times instead of once in onGridDown.
- **Fix applied:** Removed 5 duplicate copies (98 lines total).
- **Verification:** grep confirms exactly 1 occurrence of "Quick-select tool: click to place".

### Day 27 — No bugs found
- QA: Code review passed. JS parse clean. HTML balanced. No duplicate code blocks.

### Day 28 — QA Fixes Applied
- **Fix 1:** `handleGridKeyAction()` was missing `state.playing` guard — keyboard placement could modify grid during play. Added guard.
- **Fix 2:** Fullscreen (F) and High-contrast (A) shortcuts were placed after `state.playing` return, making them inaccessible during play. Moved before playing guard.
- **Fix 3:** Grid focus indicator wasn't cleared on mouse click — added `clearGridFocus()` call at start of `onGridDown`.
- All 3 fixes applied and committed. JS parse clean. No duplicate code. HTML balanced.

---

## Harden Week 1 — Full Feature Audit (Day 34)

### Audit Date: Thu Apr 23, 2026

**Testing Environment:** Desktop (1200x834 viewport), Chrome-based browser

### Systematic Test Results

| Feature | Status | Notes |
|---------|--------|-------|
| Page Load | ✅ PASS | Zero JS errors, clean console |
| Tutorial Overlay | ✅ PASS | Shows on fresh visit, Skip/Next work, re-trigger via ❓ |
| Random Track Generator | ✅ PASS | Generates valid closed loops with scenery, water, bridges, tunnels |
| Play/Stop | ✅ PASS | Train animates smoothly around loop, Stop returns to build mode |
| Connection Dots | ✅ PASS | All green after random generation, no stale red dots |
| Night Mode | ✅ PASS | Toggle works, house glow, dark theme, moon icon |
| Undo/Redo | ✅ PASS | Both buttons work, Redo enables after Undo |
| Save/Load | ✅ PASS | Modal opens with 3 slots, Save button works |
| Puzzles | ✅ PASS | All 10 puzzles listed, First Loop loads correctly with locked pieces |
| Puzzle Exit | ✅ PASS | Sandbox button restores previous track |
| Keyboard Shortcuts Modal | ✅ PASS | All shortcuts listed: Space, H, 1-8, Del, R, Z, ⇧Z, C |
| Biome: Default (Spring) | ✅ PASS | Green grass, standard trees/flowers |
| Biome: Winter | ✅ PASS | Light blue, Christmas trees, snowflake |
| Biome: Desert | ✅ PASS | Sandy/tan, cacti, rice emoji |
| Biome: Autumn | ✅ PASS | Brown, maple leaves, fallen leaves |
| Weather: Rain | ✅ PASS | Rain particles visible, icon changes |
| Weather: Snow | ✅ PASS | Snow particles drift down |
| Weather: Sunny (off) | ✅ PASS | Particles stop |
| Share Link | ✅ PASS | Button works (copies to clipboard) |
| Screenshot | ✅ PASS | Canvas renders track, Download/Copy buttons present |
| Stats & Milestones | ✅ PASS | All stats tracked, milestones with progress bars |
| High Contrast Mode | ✅ PASS | Thicker grid lines, larger dots |
| Passenger Delivery Toggle | ✅ PASS | Button toggles |
| HONK! Button | ✅ PASS | Appears during play mode |
| Train Animation (Tunnel) | ✅ PASS | Train fades out inside tunnel correctly |
| Water Tiles | ✅ PASS | Blue animated waves, duck decorations |
| Bridge over Water | ✅ PASS | Bridge renders correctly over water |
| ARIA Labels | ✅ PASS | All 96 cells have labels, grid role present |
| Sidebar Palette | ✅ PASS | All 9 track types, 5 trains, 3 cars, 9 scenery items |
| Train Colors | ✅ PASS | Red, Blue, Green, Yellow, Purple all in palette |

### BUG-014 | 🟢 FIXED | Missing favicon causes 404 on every page load
- **Found:** Thu Apr 23 — Harden Day 1
- **Fixed:** Thu Apr 23 (inline SVG favicon added)
- **Severity:** P2 (cosmetic — 404 in console, no visual impact)
- **Root cause:** No `<link rel="icon">` tag in `<head>`. Browser requests `/favicon.ico` by default.
- **Fix applied:** Added inline SVG data URI favicon with 🚂 emoji.

### Code Health Check
- **JS Syntax:** ✅ Clean (node -c passes)
- **HTML Tags:** ✅ All balanced (div: 207/207, span: 79/79, button: 39/39)
- **Duplicate Code:** ✅ None found (all key functions appear exactly once)
- **File Size:** 10,090 lines
- **Console Errors During Play:** Zero (after favicon fix)

### Summary
- **Bugs found:** 1 (P2 favicon 404 — fixed)
- **Bugs remaining:** 0
- **Overall Status:** Game is in excellent shape. All features functional, no JS errors, no duplicate code.

---

## Harden Week 1 — Puzzle & Mode Testing (Day 35)

### Audit Date: Fri Apr 24, 2026

**Testing Environment:** Desktop (1200x834 viewport), Chrome-based browser

### Puzzle Testing Results

All 10 puzzles verified solvable with 3-star solutions.

| # | Puzzle | Difficulty | Stars | Notes |
|---|--------|-----------|-------|-------|
| 1 | First Loop | Easy | ⭐⭐⭐ | 4 straights complete rectangle |
| 2 | Around the Lake | Easy | ⭐⭐⭐ | 10 straights around water |
| 3 | Figure Eight | Medium | ⭐⭐⭐ | 6 curves + crossover, two loops |
| 4 | Tunnel Run | Medium | ⭐⭐⭐ | 6 straights + 2 tunnels |
| 5 | Grand Station | Hard | ⭐⭐⭐ | S-bend connects all 3 stations |
| 6 | Switchyard | Medium | ⭐⭐⭐ | T-junctions route through station |
| 7 | Speed Run | Medium | ⭐⭐⭐ | 18/20 straights used |
| 8 | Cow Pasture | Easy | ⭐⭐⭐ | 12/14 straights, cows pre-placed |
| 9 | Night Express | Hard | ⭐⭐⭐ | Night mode forced correctly |
| 10 | Twin Loops | Hard | ⭐⭐⭐ | Two separate loops, 2 trains |

### Mode & Feature Testing

**Puzzle System:**
- ✅ All 10 puzzles load with correct locked pieces
- ✅ Piece counters decrement on placement
- ✅ Check validates and awards stars
- ✅ Progress persists in localStorage
- ✅ Sandbox restore works on exit
- ✅ Night mode save/restore (Puzzle 9)
- ✅ Multi-train puzzles (Puzzle 10)

**Passenger Delivery:**
- ✅ Toggle enables/disables correctly
- ✅ Counter appears during play ("Delivered: 0")
- ✅ State persists in localStorage

**Progression & Unlocks:**
- ✅ Stats: Tracks 125, Trains 10, Loops 19, Puzzles 10
- ✅ Milestones: Builder/Architect/Engineer/Miner all complete
- ✅ Progress bars and descriptions accurate

**Share Links:**
- ✅ Encodes to 138-char base64url hash
- ✅ Encode/decode functions present and working

**Screenshots:**
- ✅ Canvas renders all elements (tracks, scenery, water, tunnel, train)
- ✅ Download and Copy buttons functional

**Save/Load:**
- ✅ 3 save slots with name inputs and thumbnails

**Play Mode:**
- ✅ Train animates, Full Loop toast, HONK button, Stop button

### Code Health
- **Console Errors:** Zero (throughout all testing)

### Bugs Found: 0

All tested systems working correctly. No bugs found.
