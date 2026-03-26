# Day 10 QA Report — Water Tiles & Functional Bridges

**Date:** 2026-03-26
**QA Agent:** Factory Orchestrator

## Acceptance Criteria Results

| AC | Description | Result |
|----|-------------|--------|
| AC1 | Water tile in palette under Scenery | ✅ PASS — `data-type="water"` palette piece added after Cow |
| AC2 | Animated wave ripples on water tiles | ✅ PASS — CSS `water-wave` keyframe on `::before` pseudo-element |
| AC3 | Can't place track/train/car on water | ✅ PASS — Guard in `onPointerUp` blocks non-scenery types with toast |
| AC4 | Bridge over water visual enhancement | ✅ PASS — `bridge-over-water` class with enhanced shadow + water underlay |
| AC5 | Animated drifting ducks on water | ✅ PASS — ~40% of water cells get `water-duck` element with `duck-drift` animation |
| AC6 | Random generator creates river strips | ✅ PASS — `generateRiver()` called ~40% of the time from `addRandomScenery()` |
| AC7 | Water correct in both day/night modes | ✅ PASS — Night mode has darker blue gradient + moonlight shimmer |
| AC8 | No regressions on existing features | ✅ PASS — All core functions verified, HTML balanced, JS syntax OK |
| AC9 | Water removable like other scenery | ✅ PASS — Water in `SCENERY_TYPES`, right-click/long-press triggers `handleRemoveCell` |
| AC10 | Save/load preserves water tiles | ✅ PASS — Water stored as `{type:'water', rotation:0}` in grid state, serialized normally |

## Bugs Found & Fixed

### BUG-QA-010-1 | Water placement guard incorrectly re-placed source pieces
- **Found:** During QA code review
- **Severity:** Medium
- **Root cause:** When dragging a track from grid onto water, the guard called `placePiece()` to "restore" the source piece. But the source piece was never removed during drag — it was still in `state.grid`. This would have caused a duplicate `saveUndo()` call and potential state corruption.
- **Fix:** Simplified the guard to just cancel the drag. For grid-source drags, no restoration is needed since the piece never left. For train-only drags, `animateSnapBack()` handles visual restoration.
- **Verified:** Logic traced through all drag source types (palette, grid, train-only).

## Regression Checks

| Check | Status |
|-------|--------|
| HTML div balance (open=close) | ✅ 54/54 |
| JS syntax validation | ✅ No errors |
| Core functions present | ✅ All 17 checked |
| Train animation paths | ✅ No changes to animation logic |
| Switch/T-junction logic | ✅ No changes |
| Car coupling system | ✅ No changes |
| Night mode toggle | ✅ Water has night mode styles |
| Save/Load system | ✅ Water serialized as standard grid entry |
| Crash/derail system | ✅ No changes |
| Auto-connect system | ✅ No changes |

## New Patterns & Notes

- Water tiles use CSS rendering (class-based) instead of emoji, providing richer visual effects
- Duck seed stored in `cell.dataset.duckSeed` to maintain consistency across re-renders
- Bridge-over-water detection runs in `renderCell()` with neighbor re-renders when water/bridge placed nearby
- Scenery-on-scenery replacement now allowed (was previously empty-cells-only)
- River generation avoids track cells by checking `!state.grid[r][c]`
