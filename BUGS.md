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
