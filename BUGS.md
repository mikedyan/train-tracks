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

*(QA agent adds entries here as bugs are found)*
