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

## Day/Night Mode Patterns (Day 6)
- LESSON-044: Use CSS custom properties for all theme-dependent colors — makes night mode a simple body class toggle.
- LESSON-045: Stars via CSS radial-gradient on background-image avoids extra DOM elements and canvas overhead.
- LESSON-046: Headlight glow as a positioned div with radial-gradient is simpler and performs better than canvas-based approaches.
- LESSON-047: House glow uses text-shadow on emoji elements — works across browsers, no extra markup needed.
- LESSON-048: restoreNightMode() must run before renderAllCells() in init() so house glows and theme colors are correct on first render.
- LESSON-049: When toggling night mode during play, updateHeadlightVisibility() activates the headlight div, but position is only set on next animation frame in renderTrainAtProgress() — this is fine since it's <16ms.
- LESSON-050: Smoke particles get their color at spawn time (inline style), so particles spawned before a mode toggle keep their original color — acceptable since they last <1s.
- LESSON-051: CSS transitions on custom property changes work through the cascade — setting transition on the element that reads var(--prop) is sufficient.

## Switch/T-Junction Patterns (Day 8)
- LESSON-052: Switch state uses "row,col" string keys in a flat object — simple and fast lookup during animation.
- LESSON-053: Lever pointerdown handler must call stopPropagation() to prevent cell rotation from firing.
- LESSON-054: During play, onGridDown should check for T-junction cells and allow toggling — requires .has-switch class and CSS cursor override.
- LESSON-055: getExitDir for T-junctions: "straight" prefers opposite exit (bar through), "branch" prefers non-opposite (stem). When entering from the stem, both modes pick the same exit — acceptable for gameplay.
- LESSON-056: CSS custom property (--lever-angle) with transition gives smooth lever animation without JavaScript per-frame updates.

## Water & Terrain Patterns (Day 10)
- LESSON-057: Water tiles use CSS rendering (class-based .water-cell) instead of emoji for richer visual effects — wave animations via ::before pseudo-element.
- LESSON-058: Duck presence is seeded per cell via dataset.duckSeed to maintain consistency across re-renders of the same cell.
- LESSON-059: When blocking placement on occupied cells, check whether the drag source piece was already removed from grid. Grid-source drags don't remove the piece until drop — so "cancel" is just hiding the ghost, no restoration needed.
- LESSON-060: Bridge-over-water detection must trigger re-renders of neighboring bridges when water is placed/removed, and vice versa.
- LESSON-061: Scenery-on-scenery replacement should be allowed (water→tree, tree→water) — don't restrict scenery to empty-cells-only.
- LESSON-062: River generation in random tracks must run BEFORE random scenery scatter to avoid placing scenery on water cells.
- LESSON-063: Night mode water uses separate ::after pseudo-element for moonlight shimmer — keeps wave animation on ::before independent.

## Tunnel Patterns (Day 11)
- LESSON-064: Tunnel is a track piece with same connections as straight (N-S at rotation 0). Uses simple piece exit logic in getExitDir (not crossover/bridge through-route logic).
- LESSON-065: Locomotive tunnel fade uses anim.progress (always 0→1 regardless of direction) — naturally direction-aware.
- LESSON-066: Car tunnel fade must be direction-agnostic since cars use pixel positions from history buffer. Use distance from cell center (0=hidden, 1=visible at edges) instead of directional progress.
- LESSON-067: Suppress smoke particles when train is inside tunnel (check anim.inTunnel flag in smoke spawn loop).
- LESSON-068: Headlight glow must be hidden inside tunnel — check isInTunnel in the headlight update section.
- LESSON-069: Random generator tunnel conversion should happen BEFORE the animation loop (before delay variable is used), not after.
- LESSON-070: When new track types share connections with straight but have special visual behavior, add them to placeTrainOnLoop valid types.

## Animated Scenery Patterns (Day 12)
- LESSON-071: CSS animations on scenery emojis must include the base translate(-50%, -50%) in all keyframe states, otherwise the element shifts off-center during animation.
- LESSON-072: Use cell.dataset seeds (treeSeed, cowFlip, duckSeed) to maintain visual consistency across re-renders of the same cell. renderCell clears child elements but preserves dataset.
- LESSON-073: Ambient particle systems (chimney smoke) should be always-active, not tied to play state. Use visibility API to pause when tab is hidden.
- LESSON-074: Max particles per source (2 per house) prevents DOM bloat when many scenery items exist. Track via data attributes on particles, not via counting in an array.
- LESSON-075: Cow moo cooldowns should be per-cow-per-train (keyed by cell coordinates) to prevent the same cow mooing repeatedly when a train loops past it.
- LESSON-076: Only one sound effect per cell transition (early return after first cow moo) prevents audio overload when multiple cows are nearby.
- LESSON-077: Cleanup functions for ambient systems (cleanupChimneySmoke) must be called in clearAll() even if particles self-remove — user expects immediate visual reset.
- LESSON-078: The .animations-paused class on the grid container pauses all CSS animations in descendants via animation-play-state: paused — cleaner than stopping each individually.

## Audio Infrastructure Patterns (Day 13)
- LESSON-079: Route ALL sound output through a single masterGainNode for volume control. Never connect directly to ctx.destination.
- LESSON-080: Use recursive setTimeout instead of setInterval for rhythmic audio — allows interval recalculation each beat without restart.
- LESSON-081: Delay-based reverb (DelayNode + feedback GainNode) is simpler than ConvolverNode for tunnel echo effects.
- LESSON-082: Per-cell cooldown objects on anim state (e.g., crossingCooldowns, mooCooldowns) prevent sound spam when trains loop.
- LESSON-083: Three-state mute (full/low/mute) needs both soundEnabled flag AND masterGain value — soundEnabled gates sound creation, masterGain controls volume.
- LESSON-084: Audio settings (volume, mute state) should use separate localStorage keys from game state to keep concerns separated.
- LESSON-085: When multiple trains exist, check isAnyTrainInTunnel() before disabling tunnel reverb — one train exiting shouldn't kill reverb for another still inside.

## QA Patterns
- LESSON-015: Random → Play → watch full loop is the core regression test.
- LESSON-016: Test on both desktop (mouse) and mobile (touch) for any interaction changes.
- LESSON-017: Check sound after every audio change — Web Audio can produce clicks/pops if not handled.
- LESSON-023: Verify all core functions still exist after edits (use automated grep/node parse check).
- LESSON-024: Check HTML tag balance (open vs close tags) as a quick structural integrity test.
- LESSON-043: When batch-testing `generateRandomTrack()` in automated tests, each call's setTimeout animation can overlap with the next call. Test single generations with sufficient delay (2-3s) for reliable results. Batch testing requires long delays between runs.

## Duplicate Code Prevention (Day 15)
- LESSON-086: ALWAYS run `grep -c` for key identifiers after building to detect duplicates. Day 14 had 6x duplicated code blocks that broke JS execution.
- LESSON-087: Use `node -e "new Function(scriptContent)"` parse check after every edit to catch syntax errors immediately.

## Puzzle System Patterns (Day 15)
- LESSON-088: When adding custom CSS classes to cells, add/remove them inside `renderCell()` — not externally. External class application gets wiped on re-render.
- LESSON-089: Puzzle piece counting must be bidirectional: decrement on placement, increment on removal/undo.
- LESSON-090: Bridge and crossover pieces have 4 connections in `getConnections()` but only need 2 matched through-routes. Puzzle check must tolerate unmatched connections on these types.
- LESSON-091: Verify puzzle solvability with automated connection-checking script before shipping. Manual verification is error-prone with rotation math.
- LESSON-092: Curve rotation reference: rot 0=N+E, rot 90=E+S, rot 180=S+W, rot 270=W+N. Use `rotateDir()` for correctness.
- LESSON-093: When puzzle mode modifies game state, save sandbox state with `serializeState()` BEFORE clearing, and restore with `deserializeState()` on exit.
- LESSON-094: Block sandbox-specific operations (Clear, Random, AutoSave) during puzzle mode to prevent state corruption.

## Puzzle Star Rating Patterns (Day 16)
- LESSON-095: Store puzzle completion as `{ stars: N }` instead of boolean for richer tracking. Keep backwards-compatibility by treating old `true` values as 1 star.
- LESSON-096: Star calculation: count player-placed pieces only (exclude locked cells from count). Compare against par and optimal thresholds.
- LESSON-097: Only save star progress if new stars > previous stars — players shouldn't lose progress by replaying.
- LESSON-098: When puzzles support pre-placed scenery, add a `scenery` array to puzzle definition and handle in `loadPuzzle()` — scenery items are placed before locked track pieces.
- LESSON-099: Multi-loop puzzles (multiple trains) need BFS connectivity check that finds ALL components, not just one. Allow N components for N-train puzzles.
- LESSON-100: ForceNight puzzles must save night mode state in puzzleState on load and restore it in exitPuzzle() — otherwise users lose their night mode preference.
- LESSON-101: When pre-placing trains in puzzles, add them to state.trains BEFORE renderAllCells() so they render on the first pass.
- LESSON-102: Avoid redundant `const` redeclarations in the same function scope even if they're in separate block scopes (if/else) — can confuse maintainers.


## Mobile Layout Patterns (Day 17)
- LESSON-103: On mobile (<768px), hide the desktop sidebar entirely and show a horizontal scroll bottom drawer instead. Never try to shrink the sidebar — it doesn't work on small screens.
- LESSON-104: The body's touch-action: none prevents all touch gestures. For scrollable sub-elements (like the drawer), override with touch-action: pan-x to allow horizontal scrolling.
- LESSON-105: Mobile drawer palette pieces share the same .palette-piece class as sidebar pieces. querySelectorAll('.palette-piece') in init picks up both, so no separate init code is needed.
- LESSON-106: Haptic feedback (navigator.vibrate) must be wrapped in try/catch — not all browsers support it, and some throw even when the API exists.
- LESSON-107: When checking for mobile layout, use window.innerWidth (JS) and @media (max-width: 768px) (CSS) consistently. Don't rely on user-agent sniffing.
- LESSON-108: calculateSize() must account for the bottom drawer height on mobile (subtract from available height before computing cell size).
- LESSON-109: Mobile drawer should auto-collapse during play state via CSS (no JS needed) using #app.playing #mobile-drawer { transform: translateY(...) }.
- LESSON-110: Duplicate code blocks from previous builds must be checked with grep -c after each build. Day 14's duplicates survived through Day 16.

## Zoom/Pan Patterns (Day 18)
- LESSON-111: Use a viewport wrapper (#grid-viewport) with overflow:hidden around the grid container. Apply CSS transform on the inner container, not the viewport — this keeps the visible area fixed while the content zooms.
- LESSON-112: CSS transform: scale() with transform-origin: 0 0 is GPU-accelerated and doesn't trigger reflow. All children scale automatically — no per-element adjustment needed.
- LESSON-113: For coordinate conversion with zoom, use viewport.getBoundingClientRect() + panX/panY + zoomLevel to convert screen coords to grid-local coords. Don't use grid.getBoundingClientRect() which returns scaled values.
- LESSON-114: Replace all getBoundingClientRect()-based offset diffs (gridRect.left - containerRect.left) with element.offsetLeft/offsetTop for positioning within the container. These are zoom-safe (always in local space).
- LESSON-115: setZoomAtPoint() must calculate the local-space point BEFORE changing zoom, then adjust pan to keep that point under the cursor. Formula: panX = vpX - localX * newZoom.
- LESSON-116: enforcePanBounds() should center the grid when it's smaller than the viewport (zoom < 1), and clamp pan when larger (zoom > 1).
- LESSON-117: Two-finger pinch handlers (touchstart/touchmove/touchend) must only activate on e.touches.length === 2 to avoid interfering with single-finger drag-and-drop.
- LESSON-118: Double-tap/double-click zoom reset must not fire on grid cells — check e.target.closest('.cell') to avoid interfering with click-to-rotate.
- LESSON-119: Reset zoom on window resize to prevent layout inconsistencies when viewport dimensions change.
- LESSON-120: The wheel event on the viewport must use { passive: false } and e.preventDefault() to prevent page scroll during zoom.

## Expanded Scenery Patterns (Day 19)
- LESSON-121: When adding new scenery types that behave like existing ones (animals with flip, plants with sway), reuse CSS class patterns (e.g., `.scenery-animal-flipped` shared by sheep/horse like `.scenery-cow-flipped` for cow).
- LESSON-122: Use hyphenated type names (`duck-land`) when a new type might collide with existing visual elements (water-duck decoration). Keep the type name distinct and descriptive.
- LESSON-123: When expanding a per-type proximity check (like cow moo), refactor into a lookup table (ANIMAL_SFX map) instead of growing an if-else chain. Scales better with more types.
- LESSON-124: All sound-producing scenery should use the shared `anim.mooCooldowns` object for per-cell cooldowns. The key is "row,col" and works across all animal types.
- LESSON-125: The random scenery weighted distribution should keep trees as the most common type (~35%) to maintain the forest feel. New types should fill in the remaining probability space proportionally.
