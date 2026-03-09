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

### BUG-002 | 🔴 OPEN | Wobbly loop generator doesn't close path
- **Found:** Mon Mar 9 during code review
- **Severity:** Medium — falls back to rect loop, but produces disconnected tracks when it doesn't fall back
- **Details:** generateWobblyLoop walks randomly but has no mechanism to route back to start. When the walk ends without reaching start, it returns an open path. Scheduled for fix on Day 1 (Mar 10).

---

## Bugs Found During Roadmap

*(QA agent adds entries here as bugs are found)*
