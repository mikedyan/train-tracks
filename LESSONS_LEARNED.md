# Lessons Learned — Train Tracks

## Code Patterns
- LESSON-001: The game is a single `index.html` file (~2200 lines). All changes go here.
- LESSON-002: SVG rendering for all track pieces — clean, scales to any size.
- LESSON-003: Web Audio API for all sounds — no external audio files, everything synthesized.
- LESSON-004: Uses pointer events (not separate mouse/touch) — works on both desktop and mobile.
- LESSON-005: CSS custom properties used for theming — leverage for day/night mode.
- LESSON-006: Connection dots use glowing radial gradients (green/red) at cell edges.

## Common Bugs (Pre-Roadmap)
- LESSON-007: Corner rotation in random generators was 180° off — all fixed in pre-roadmap phase.
- LESSON-008: Connection dots need to refresh after random track animation completes, not during.
- LESSON-009: Train state must be updated before re-rendering cells (race condition with single train enforcement).

## Architecture Decisions
- LESSON-010: Single file is a hard constraint. No splitting into multiple files.
- LESSON-011: No external dependencies (no libraries, no CDN, no build step).
- LESSON-012: All new features must work in both day and night modes (when Day 6 ships).
- LESSON-013: Performance budget: maintain 60fps with max 30 particles active.
- LESSON-014: localStorage for all persistence (save slots, preferences, progress).

## Persistence Patterns (Day 1)
- LESSON-018: Auto-save must hook into ALL state mutation paths — not just the obvious functions, but also drag-and-drop handlers that modify state directly (e.g., train-to-trash, train-off-grid).
- LESSON-019: When adding a new toast in init(), check if it conflicts with existing toasts (only one toast shows at a time).
- LESSON-020: Always sanitize user-provided strings before inserting into innerHTML — use escapeAttr() for attribute values.
- LESSON-021: localStorage operations should always be wrapped in try/catch (storage full, private browsing, etc.).
- LESSON-022: Save slot data serialization must be complete — grid + train + trainDir. Undo stack is session-only and intentionally excluded.

## Auto-Connect Patterns (Day 2)
- LESSON-025: Auto-connect should only apply to palette drops — grid-source drags must preserve existing rotation to avoid surprising the user.
- LESSON-026: findBestRotation() returns { rotation, score } — score > 0 means at least one neighbor matched. Use this to conditionally trigger visual feedback.
- LESSON-027: CSS animations on connection dots need separate keyframes for N/S (translateX-based) and E/W (translateY-based) dots because they use different base transforms.
- LESSON-028: Use `{ once: true }` on animationend listeners to auto-cleanup — prevents listener accumulation on repeatedly-pulsed dots.

## Particle Systems (Day 3)
- LESSON-029: Use CSS @keyframes with `forwards` fill-mode for particle animations — lets the browser handle the animation loop, no JS per frame needed.
- LESSON-030: Smoke particles need manual cleanup via both auto-remove (setTimeout after animation duration) and bulk cleanup in stopPlay(). Don't rely on only one mechanism.
- LESSON-031: Use CSS custom properties (--smoke-dx, --confetti-dx) to vary particle directions without creating separate keyframes for each particle.
- LESSON-032: Particle spawn rate should scale with speed slider. Use `input` event listener on the slider to restart the spawn interval.
- LESSON-033: Loop detection gate (cellsVisited >= 4) prevents false triggers on the starting cell. The `loopCompleted` flag ensures celebration fires only once per play session.
- LESSON-034: Confetti particles should be evenly distributed around a circle (angle = 2π * i / n) with random jitter, not purely random angles. Creates a more uniform burst.

## Train Cars Patterns (Day 5)
- LESSON-035: Position history ring buffer is the right approach for train car following — binary search interpolation gives smooth positions on curves.
- LESSON-036: Pre-seed position history with static car positions at negative distances before play starts — prevents cars snapping from origin to their positions.
- LESSON-037: Cap position history at 600 entries to prevent memory growth during extended play sessions.
- LESSON-038: `sortCarsWithCabooseEnd()` must be called after every car addition to maintain caboose-last invariant.
- LESSON-039: Car removal via right-click should take priority over track removal in `handleRemoveCell` — check `getCarCellPositions()` first.
- LESSON-040: When serializing state, handle missing `cars` field gracefully in `deserializeState` (older saves won't have it) — default to empty array.
- LESSON-041: Clean up animated car DOM elements in `stopPlay()` alongside the train element — don't leave orphaned nodes.
- LESSON-042: Car animation z-index should decrease with car index (49, 48, 47...) so front cars render on top of back cars at overlapping positions.

## QA Patterns
- LESSON-015: Random → Play → watch full loop is the core regression test.
- LESSON-016: Test on both desktop (mouse) and mobile (touch) for any interaction changes.
- LESSON-017: Check sound after every audio change — Web Audio can produce clicks/pops if not handled.
- LESSON-023: Verify all core functions still exist after edits (use automated grep/node parse check).
- LESSON-024: Check HTML tag balance (open vs close tags) as a quick structural integrity test.
- LESSON-043: When batch-testing `generateRandomTrack()` in automated tests, each call's setTimeout animation can overlap with the next call. Test single generations with sufficient delay (2-3s) for reliable results. Batch testing requires long delays between runs.
