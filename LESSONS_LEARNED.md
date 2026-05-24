# Lessons Learned — Train Tracks

## Code Patterns
- LESSON-DAY63-A: Cycle 3 Build Day 5 (Sticker Book) — the cleanest way to add a *secondary* achievement system on top of an existing milestone/stats system is a separate, parallel storage key (`trainTracks_stickers` next to `trainTracks_stats`) with its own state object, its own checker, and its own modal. Don't try to fold stickers into MILESTONES — they serve a different UX: milestones gate piece unlocks, stickers are collectibles that drive return visits. Two storages, two checkers, ONE shared hook point: `incrementStat()` calls both `checkAndUnlockMilestones()` *and* `checkAndAwardStickers()`. Adding the second call cost 3 lines; trying to merge the two systems would have meant rewriting the stats modal and the unlocks logic both. The two systems happily co-exist.
- LESSON-DAY63-B: Meta achievements ("earn all other achievements") need a two-pass evaluator, not a recursive condition. First pass awards every non-meta sticker. Second pass evaluates the meta sticker's predicate (`STICKERS.every(s => s.id === 'train-master' || stickerState.earned[s.id])`) against the *just-updated* `stickerState.earned`. If you try to use a single pass with the meta sticker in the same loop, the predicate reads stale state and the meta sticker never fires in the same tick as its last prerequisite. Same shape as a classic SQL recursive CTE — keep the levels separate.
- LESSON-DAY63-C: Implicit-progress flags for existing players: a fresh sticker-book release should retroactively award what users already did, even if the *trigger event* happened pre-release. Pattern: on init(), call `recordSoundPackTried(currentSoundPack)` once (seeds whatever pack is currently set) and `if (isNightMode()) recordNightToggled()` once. Existing players boot up, the seed flag fires, `checkAndAwardStickers()` runs immediately after `loadGameStats()`, and they see retroactive sticker toasts on day-one. No "unfair" feeling for veteran players. Cost: 4 lines in init().
- LESSON-DAY63-D: For "unearned" UI states, fade + greyscale + `?` emoji beats a solid silhouette. Earned stickers get `background: linear-gradient(180deg, #FFF8E1, #FFE0B2)` + a `box-shadow` glow + a `stickerPop` keyframe animation; unearned get `filter: grayscale(0.95); opacity: 0.55` and `❓` instead of the real emoji. Same DOM structure both states. CSS transitions between them feel like the sticker is "developing" into existence when earned. The grayscale-filter approach is fully driven by CSS, so awarding a sticker mid-modal-open just toggles the `.earned` class via `renderStickerContent()` and the animation runs automatically.
- LESSON-DAY62-A: Cycle 3 Build Day 4 (Replay Sharing) — the cleanest way to add a brand-new payload to an existing share-link format is a fresh **version byte**, not a flag bit in the v2 header. v1=fixed-12×8, v2=`[ver,rows,cols,grid,trains,switches]`, v3=`[v2 layout + 2-byte action count + per-action bytes]`. Decoders branch on the version byte once and the rest of the parse is identical — old v1/v2 links keep working forever, new v3 readers handle both new and old, and there's no "is this bit set" parsing ambiguity. The 2-byte little-endian action count gives 65,535 actions per link — vastly more than any kid will record (typical recordings are 5-50 actions, ~178 chars b64url).
- LESSON-DAY62-B: Action encoding cheat — each replay action gets a 1-byte kind discriminator followed by a kind-specific payload (place=3 bytes, remove=2, rotate=2, placeTrain=3, clearAll=0). Reusing the existing `(typeId<<2)|rotIdx` cell packing for the `place` action means the byte format is symmetric with the v2 grid cell encoding, so writing the encoder and decoder feels like the same code in mirror image. Total per-action cost: 2-3 bytes raw → ~3-4 chars base64. A 30-step replay fits in ~120 chars (URL safe, no escaping).
- LESSON-DAY62-C: When decoding a v3 share-link, the decoded grid/trains/switches IS the replay baseline — don't snapshot live `state` after applying it, because (a) `state` gets mutated by side-effect during decode and (b) the baseline needs to match exactly what was originally recorded. Cloning the just-decoded `newGrid`/`newTrains`/`newSwitchStates` into `state.replayBaseline` before they're assigned to `state.*` keeps the baseline pristine. Side channel: a module-level `pendingReplayFromShare` flag that `decodeGridState` sets to true and `init()` consumes (sets false + setTimeout to autoplay). Cleaner than threading return values up through `loadFromShareHash` → `init`.
- LESSON-DAY62-D: Autoplay timing for a shared replay needs a small delay (1500ms in our case) so the visitor can: (1) see the baseline state painted, (2) read the toast `🎬 Shared replay loaded — watch it build!`, (3) absorb that this is a replay and not their own track. Jumping straight into the ghost rebuild is jarring. The 1500ms delay also gives the browser time to settle after the initial render (autoload, palette init, tutorial check) so the ghost step cadence (600ms each) doesn't compete with init work.
- LESSON-DAY61-A: Cycle 3 Build Day 3 (Whistle Songs) — adding a *per-color musical identity* on top of an existing per-pack SFX system is cheapest when you separate the two axes cleanly. Sound packs (Day 48) live on the timbre dimension (waveform / freq multiplier / gain) shared across all trains. Whistle songs (Day 61) live on the **color** dimension (note sequence + per-color waveform). Concretely: `const WHISTLE_SONGS = { red:{notes,type,label}, blue:..., ... }` plus a 12-line `playWhistleSong(color)` that loops over notes and calls the existing `playNote(freq, dur, type, vol, delay)` helper. No new oscillator code, no audio context plumbing — just config + a tiny scheduler. +37 LOC for 5 distinct melodies. The two systems don't interact: a Toy-pack red train still sings the red melody with a sawtooth (the song picks waveform, not the pack). Documented this trade-off in the comment block: "color *is* the identity."
- LESSON-DAY61-B: When layering a new audio event on top of an existing one (SFX.station's two-tone horn ~0.7s tail), schedule the new event with a `delay` offset baked into the `playNote` call rather than using `setTimeout`. Three reasons: (1) sample-accurate scheduling via the Web Audio API's currentTime is glitch-free, (2) it auto-respects the `soundEnabled` guard inside `playNote` so muting the master kills everything together, (3) no zombie timers if the train crashes / play stops between the schedule and the actual sound. Concrete params that ended up sounding right: offset=0.60s (after horn body, during horn tail), per-note dur=0.24s, step=0.19s (≈80% overlap → legato), vol=0.075 (sits under the horn's 0.10–0.12 peaks). Total whistle-song length ≈ 0.81s, station arrival now ~1.4s start-to-silence.
- LESSON-DAY61-C: Pentatonic-only frequency choice (C, D, E, G, A in two octaves) is the lowest-risk way to add new melodies to a project that already runs an ambient-music loop in the same key. Day 27's MUSIC_ENGINE picks notes from `PENTA_FREQS`. Whistle songs draw from the exact same scale. Result: a station chime mid-bar never produces a dissonant clash, no matter where the music engine happens to be in its 16-bar pattern. Worth the 30 seconds it takes to write the scale comment next to the freqs so future-me doesn't reach for a F# or Bb "because it sounds bluesier" — that's how cross-system audio bugs get born.
- LESSON-DAY61-D: `function foo(){}` at script top-level attaches to `window` in non-module scripts, but `const FOO = {...}` does NOT. Counter-intuitive — both feel "top-level" but only function declarations are hoisted onto the global object. Consequence: I can wrap `window.playWhistleSong` from a Playwright `evaluate` call for live integration testing, but I cannot read `window.WHISTLE_SONGS` directly. If a config object needs to be inspectable from devtools / e2e tests, declare it as `window.FOO = {...}` or use a `var`. (Index.html is not a module — we keep it that way for the share-link compactness, see ROADMAP.)
- LESSON-001: The game is a single `index.html` file (~10,335 lines after Day 44 build). All changes go here.
- LESSON-DAY60-A: Cycle 3 Build Day 2 (Animal Passengers) — when a new gameplay system needs a visible **per-train accessory** (badge above the loco), the cleanest pattern is to mirror Day 46's cargo-badge plumbing exactly: (1) one CSS class `.train-animal-badge` with a transform-friendly `translate(-50%, -50%)` anchor + small wiggle keyframe, (2) one DOM element appended to `#grid-container` and stored on the anim state as `anim.animalBadgeEl`, (3) one positioning block in `renderTrainAtProgress` that copies the loco's `locoX/locoY + offset`, (4) one `refreshTrainAnimalBadge(anim)` helper that creates / updates / removes the element based on a state lookup. Same shape as cargo, so the two badges happily coexist (cargo top-right, animal top-left of the loco).
- LESSON-DAY60-B: Scenery cells with persistent transient state (an animal that is "away" on a train) should mark their state via `cell.dataset.animalBoarded = '1'` rather than mutating the rendered `.scenery-emoji` directly. Reason: `renderCell()` strips and re-creates the `.scenery-emoji` div on every call (night-mode toggle, focus styling, undo, etc.), but the cell's `dataset` survives those re-renders. Style targets the data attribute via CSS (`.cell[data-animal-boarded="1"] .scenery-emoji { opacity: 0.22; filter: grayscale(0.85); }`), so the faded look survives any re-render automatically. Cleanup happens by walking `Object.keys(animalState.boarded)` in `resetAnimalState()` and deleting the dataset key on each cell.
- LESSON-DAY60-C: For "reuses Day 25 passenger pipeline + Day 30 animal SFX" features, the implementation is two integration points — `(passenger system bottom + cargo system bottom) → animalState block`, then one `advanceTrainAnim` station-handler tail that calls `handleTrainAtAnimalStation(...)`. The order at the station matters: cargo first (most setup), passengers second (toggle-gated), animals third (auto-on, no setup). All three return `boolean` so the fallback `Toot toot!` toast only fires when NONE of them produced an event. Reading old systems' signatures + matching them in the new one is faster than inventing a parallel design.
- LESSON-DAY48-A: Cycle 2 Build Day 5 (Sound Packs) — the cheap way to add timbral variety to a Web Audio app is a `SOUND_PACKS = {classic, toy, diesel}` config object containing **only** the per-pack parameters (waveform `type`, frequency multipliers, gain levels, filter cutoffs). The SFX *functions* themselves stay shared — they just read `getSoundPack().whistle.f1` instead of hard-coding `880`. This kept the diff to ~120 net lines for four distinct sound surfaces (whistle, chug noise + accent note, station horn + overtone, HONK button horn + harmonic + noise burst) instead of triplicating the synthesis code per pack.
- LESSON-DAY48-B: When swapping audio params doesn't take effect on the *next* event, the bug is almost always that you read the param ONCE at engine init time and cached it in a closure. Reading `getSoundPack()` *inside* the playback function (every call) is the right default — Web Audio cost is negligible and it lets users hear the change instantly without a Stop/Play cycle. Verified live: cycling pack mid-play swaps the chug filter freq + horn waveform for the very next chug beat / HONK without restarting.
- LESSON-DAY48-C: For settings that have 3+ discrete states (not boolean), a Settings *cycle button* (click → next → next → wrap) is friendlier on a 5-year-old's UX than a `<select>` dropdown. The button label shows the current value (`Sound: Classic`), the click rolls forward, a tiny preview whistle plays so they hear the difference, and a toast confirms the new pack name. No keyboard, no menus-within-menus, no scroll wheel — just thump the button and listen.
- LESSON-DAY48-D: Multi-state UI labels go through ONE update helper (`updateSoundPackSettingsLabel`) called from THREE places: the setter (`setSoundPack`), the menu-opener (`openSettingsMenu`), and — if it ran in init — a restore hook. Same pattern as Day 45's `updateBigGridLabel`. Missing the menu-opener call is the most common bug: stale label on first menu open after page load.
- LESSON-DAY48-E: When persisting a setting whose values map to a static config object, store the *key* (`'toy'`) not the resolved object. Validate on restore (`if (saved && SOUND_PACKS[saved])`) so a future schema change or corrupted localStorage falls back to the default cleanly instead of throwing. Same pattern as biome restoration.
- LESSON-DAY45-A: Cycle 2 Build Day 2 (Big Grid Mode) — when a value used everywhere as a `const` needs to become reactive, the cheapest path is `const → let` and a single `applyGridSize()` swapper. ROWS/COLS are referenced 60+ times in this codebase; converting them to `let` made every `for (r<ROWS; c<COLS)` loop, every render, every random-gen, every save/load, and every cellSize calculation instantly responsive — zero call-site edits needed. The only places that needed surgery were (1) the share-link byte format (had to add an explicit grid-dim header for round-tripping) and (2) the auto-save deserialize path (call `normalizeStateGridToCurrent()` to clip/pad loaded grids that don't match current dims).
- LESSON-DAY45-B: Migration-friendly share-link versioning — keep version-byte=1 readable as the legacy fixed-dim format, and bump to version-byte=2 for `[version,rows,cols,...grid]` going forward. Old share links keep working, new ones encode dims, and the decoder just branches on the version byte. Cheap forward-compat.
- LESSON-DAY45-C: Ordering matters in `init()`. Restore-from-localStorage helpers that change ROWS/COLS (or any layout-affecting global) must run BEFORE `calculateSize()` and `initGrid()`, or the first paint uses stale dims and you get mismatched DOM-vs-state on reload. Pattern: any future feature that changes layout dims should restore its localStorage at the very top of `init()`.
- LESSON-DAY45-D: Modal text labels that reflect localStorage state (e.g., `Big Grid: 16x10` vs `12x8`, `Music: On` vs `Off`) need refresh hooks at THREE sites: (1) the toggle function itself, (2) the `openSettingsMenu()` (or equivalent menu-opener) so a fresh menu paint shows the right value, and (3) the restore function called in init() so the page-load state matches the persisted setting. Missing #2 or #3 → label drifts from reality and confuses users.
- LESSON-DAY44-A: Cycle 2 Build Day 1 (Train Name Labels) — adding an optional `name` field to train objects worked transparently with all existing serialization paths because they use `JSON.stringify(state.trains)` or `state.trains.map(t => ({...t, ...}))` — both naturally include the new field. The ONE place that needed an explicit guard was the Settings/Customization modal (and the truthy check in renderTrainAtProgress) because random-gen and puzzle-init build train objects via raw object literals (`{row,col,color,cars}`) without going through `placeTrain`. A defensive `normalizeTrainsName()` helper called at modal-open + after deserializeState fixes this without touching every literal site. **Pattern:** when adding optional fields to a state object that's built in 5+ places, add a single normalize() helper and call it at the choke points (read-back paths) rather than back-filling all the literal sites.
- LESSON-DAY44-B: Floating UI elements that follow a transformed sprite should NOT be children of the sprite — they'd inherit its `rotate()` and read upside-down on a south-bound train. Make them sibling DOM elements appended to the same `grid-container`, then update their absolute `left/top` in the same render pass that updates the sprite. The label (`.train-name-label`) uses `transform: translate(-50%, -100%)` so the position you write is the *bottom-center anchor* — easy to compute as `locoY - cellSize*0.55`.
- LESSON-002: SVG rendering for all track pieces — clean, scales to any size.
- LESSON-DAY41-A: Single-source-of-truth palette — desktop sidebar (#sidebar) is the canonical palette HTML; mobile drawer (#drawer-content) is now built at boot via `buildMobileDrawer()` which clones sidebar children. `<h2>` headers map to `<span class="drawer-section-label">` automatically. ALWAYS edit ONLY the sidebar markup when adding/removing palette pieces — the drawer mirrors automatically. Run `buildMobileDrawer()` BEFORE the SVG render loop in `init()` so both sets get SVGs in one pass.
- LESSON-DAY41-B: Inline button styles (`style="background:...;color:white;box-shadow:..."`) belong in CSS utility classes (`.btn-random`, `.btn-share`, `.btn-settings`, etc.). It's the same number of HTML lines but ~50% fewer characters per button, easier to theme, and survives a future palette restyle without touching every button in HTML.
- LESSON-DAY41-C: Dead-function audit pattern — `awk -F'function ' '/^function /{split($2,a,"("); print a[1]}' index.html | while read fn; do total=$(grep -cE "\b${fn}\b" index.html); [ "$total" -le 1 ] && echo "$fn dead"; done`. Total=1 means defined-but-never-called. Day 41 caught: `getCurrentBiome`, `isConnectedAt`, `updateAllConnectionDots`, `startLongPress` (orphaned), `cyclePaletteTrainColor` (only called itself via `setPaletteTrainColor`).
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

## Biome System Patterns (Day 20)
- LESSON-126: Biome CSS classes must appear BEFORE night-mode in the stylesheet — night mode overrides ALL biomes, ensuring dark theme always works regardless of biome selection.
- LESSON-127: Use a `getSceneryEmoji(type)` function as a single abstraction layer for all scenery emoji display — this makes it trivial to add biome-specific emoji overrides without modifying every call site.
- LESSON-128: Biome is a global visual preference (like night mode), not per-layout state. Store in its own localStorage key, not in serializeState(). This avoids breaking save/load compatibility.
- LESSON-129: When changing biomes, both `renderAllCells()` AND `rerenderPalette()` must be called to update emoji in both the grid and the sidebar/drawer palettes.
- LESSON-130: Biome-specific random generator weights should keep trees as the dominant type (~35-40%) in all biomes for visual consistency. Vary the animal/flower mix per biome for character.
- LESSON-131: For biome CSS, use the existing CSS custom properties + transition system. No new animation or transition properties needed since all themed elements already use `var(--grass)` etc. with 0.5s transitions.

## Tutorial Overlay Patterns (Day 21)
- LESSON-132: Use box-shadow: 0 0 0 3000px rgba() on a positioned spotlight element to create a dark overlay with a cutout — simpler and more compatible than clip-path approaches.
- LESSON-133: Tutorial overlay z-index (400) must be higher than all other modals (300) and toast (200). Spotlight z-index (399) is just below overlay so the bubble sits on top.
- LESSON-134: Escape key handler must check highest z-index layer first — tutorial before puzzle/save/shortcuts modals.
- LESSON-135: First-visit tutorial should show with a delay (800ms) to avoid competing with initial toast and let the UI settle visually.
- LESSON-136: Mobile tutorial uses mobileTargetSelector to highlight the bottom drawer instead of the hidden sidebar — check isMobileLayout() for target selection.
- LESSON-137: Re-trigger pop animation on step change by resetting animation property to 'none', forcing reflow with offsetHeight, then clearing it.

## Screenshot Canvas Patterns (Day 22)
- LESSON-138: For screenshots, use programmatic canvas rendering (not DOM capture) to produce clean output without UI chrome. Read CSS custom properties via `getComputedStyle()` for theme-awareness.
- LESSON-139: Use canvas transform (translate + rotate + translate-back) to render rotated track pieces. This mirrors the SVG rotation approach used in the DOM.
- LESSON-140: Scale factor of 4x produces crisp screenshots even on retina displays. Canvas dimensions: COLS * 60 * 4 by ROWS * 60 * 4.
- LESSON-141: When adding new modals, ALWAYS add them to: (1) Escape key handler chain, (2) modal guard that blocks keyboard shortcuts, and (3) click-outside-to-close handler. These are three separate insertion points and easy to miss.
- LESSON-142: For download, use `canvas.toBlob()` → `URL.createObjectURL()` → anchor click → `URL.revokeObjectURL()`. Don't use `toDataURL()` which has memory issues with large canvases.
- LESSON-143: Clipboard write requires `ClipboardItem` API — not universally supported. Always provide a download fallback and graceful error handling.
- LESSON-144: When running multiple Python text replacement scripts in sequence, later scripts may overwrite earlier changes if they read the file fresh. Always verify all changes are in the final file.

## Share Link Patterns (Day 23)
- LESSON-145: Use 1 byte per cell (type << 2 | rotIdx) for grid encoding — simpler than bit-packing and still compact enough (< 200 chars base64 for full grid). Premature optimization isn't needed when URL length is already well under limit.
- LESSON-146: Base64url encoding (RFC 4648 §5) avoids URL encoding issues: replace + with -, / with _, strip trailing =. Always decode by reversing these substitutions + re-adding padding.
- LESSON-147: Hash detection must run BEFORE autoLoad in init() — share links take priority over saved state. Use history.replaceState to clear the hash after loading to prevent re-loading on refresh.
- LESSON-148: Always provide a fallback clipboard method (document.execCommand('copy') via temporary input) since navigator.clipboard.writeText requires secure context and may not be available in all browsers.
- LESSON-149: When encoding variable-length data (trains with varying car counts), use count-prefixed format (trainCount, then per-train: row, col, color, carCount, ...cars) rather than fixed-size records.
- LESSON-150: The type map (SHARE_TYPE_MAP / SHARE_TYPE_REVERSE) must cover ALL piece types including scenery. If a new type is added to SCENERY_TYPES or TRACK_TYPES, the share link type map must be updated too.

## Train Customization Patterns (Day 24)
- LESSON-151: Use `pointerdown` with `stopPropagation` on color selector dots to prevent parent palette drag handlers from firing. This is critical for small interactive elements inside draggable containers.
- LESSON-152: Color selector dots must be preserved across `rerenderPalette()` and window resize — exclude `.color-selector` and `.color-dot` from querySelectorAll cleanup selectors.
- LESSON-153: When adding new train colors, update ALL color maps in parallel: TRAIN_COLORS, TRAIN_COLOR_ORDER, colorToIdx (share encode), idxToColor (share decode), trainColorMap (thumbnail), trainColorMap (screenshot). Missing any one creates a silent bug.
- LESSON-154: MAX_TRAINS should match the number of available colors to avoid confusing UX where a color exists in the palette but can't be placed.
- LESSON-155: Color dot `active` state uses CSS class toggle — simpler than tracking state separately. The dot's `data-color` attribute provides the lookup key.
- LESSON-156: Yellow train needs high-contrast detail colors (#F57F17) to remain visible in both day and night modes. Light body colors require darker accents.

## Passenger Delivery Patterns (Day 25)
- LESSON-157: Session-only state (like passenger delivery) should NOT persist to save/load or share links. Reset on stopPlay to keep things clean.
- LESSON-158: Use `lastPickupTrain` per station to prevent delivering passengers at the same station they were picked up from. This prevents trivial 0-distance deliveries.
- LESSON-159: Gate all new feature code behind an `enabled` flag so the feature is truly togglable with zero side effects when off.
- LESSON-160: When hooking into advanceTrainAnim for station events, replace the toast-only path conditionally (`if enabled → feature; else → original toast`) to avoid double-toasting.
- LESSON-161: Mini confetti reuses the existing `.confetti-particle` CSS class — no need for new keyframes when the visual style is the same.
- LESSON-162: Passenger emoji positions use `right`/`top` percentages relative to the cell, keeping them near the station platform regardless of cell size or zoom level.

## Progression & Unlock Patterns (Day 26)
- LESSON-163: Use a separate `allUnlocked` boolean flag for the unlock-all override — simpler than adding every piece to unlockedPieces set, and makes save/restore trivial.
- LESSON-164: Auto-detect returning players (have saves but no stats) and auto-unlock everything to avoid frustrating existing users with a new gating system.
- LESSON-165: Gate palette drags in `onPaletteDown` early (before dragInfo is set) to prevent locked pieces from entering the drag system at all.
- LESSON-166: Milestone unlock toasts should be staggered (1.5s apart) when multiple unlock at once — prevents toast overwrite where only the last one is visible.
- LESSON-167: `isPieceUnlocked` should return true during puzzle mode (`puzzleState.active`) so players can use all pieces. Also remove lock CSS in `loadPuzzle` and restore in `exitPuzzle`.
- LESSON-168: Stats increment points must be chosen carefully: `tracksPlaced` increments in `placePiece` (covers drag, keyboard, and puzzle), not in `onPointerUp` which only covers drag.
- LESSON-169: Long-press unlock-all needs both `pointerup` and `pointerleave` cleanup to handle the case where the user drags off the element before releasing.

## Ambient Music Patterns (Day 27)
- LESSON-170: Use look-ahead scheduling (schedule next bar 0.5s before current bar ends) with recursive setTimeout for gapless music playback. setInterval can't handle dynamic tempo changes.
- LESSON-171: Route music through its own GainNode → masterGainNode chain. This gives independent music volume while still respecting the global master mute/volume.
- LESSON-172: Music-box timbre: sine wave (fundamental) + triangle wave at 2x frequency (sparkle harmonic, quieter at 0.3x volume). Fast attack (10ms linear ramp) + exponential decay creates bell-like envelope.
- LESSON-173: Default music OFF and require explicit user action to start. Browser autoplay policies block audio without user gesture. For returning users, listen for first pointerdown/keydown with `{ once: true }` to auto-start.
- LESSON-174: Pentatonic scale (C, D, E, G, A) avoids dissonance — any note combination sounds pleasant. Ideal for ambient background music that shouldn't distract.
- LESSON-175: Tempo changes work naturally with bar-level scheduling: `getMusicTempo()` is called fresh for each new bar, so state changes (play/idle, day/night) smoothly take effect at the next bar boundary without any explicit transition logic.
- LESSON-176: Pause music on `visibilitychange` (tab hidden) to avoid background CPU usage and prevent audio surprises when user returns. Resume on visible if still enabled.

## Accessibility Patterns (Day 28)
- LESSON-177: Add `role="gridcell"` and `aria-label` to grid cells in initGrid(), then update labels dynamically in renderCell() via a separate `updateCellAriaLabel()` function. This keeps the ARIA state in sync with visual state.
- LESSON-178: Palette pieces need `tabindex="0"` and `role="button"` for keyboard accessibility. Use `:focus-visible` for the focus ring (not `:focus`) to avoid showing it on mouse clicks.
- LESSON-179: Grid keyboard navigation (arrow keys + Enter) should use a visible `.grid-focus` CSS class — not browser focus — since grid cells aren't focusable elements. The focus indicator needs to adapt for night mode and high-contrast mode.
- LESSON-180: Keyboard shortcuts for visual toggles (fullscreen, high-contrast, night mode) must be placed BEFORE the `if (state.playing) return;` guard in handleKeyDown — these should work during play.
- LESSON-181: Clear keyboard grid focus on mouse interaction (`clearGridFocus()` in `onGridDown`) to prevent stale focus indicators lingering after the user switches to mouse.
- LESSON-182: For colorblind accessibility, use shape + color for connection dots: connected = circle (round), disconnected = diamond (rotated square). Never rely on color alone.
- LESSON-183: `@media (prefers-reduced-motion: reduce)` CSS block should target decorative animations only (particles, sway, confetti). Keep functional transitions (modal open/close) intact. Also gate JS particle spawning with `prefersReducedMotion()` utility function.
- LESSON-184: High-contrast mode uses `body.high-contrast` class with thicker borders, larger dots, and boosted contrast filter. Must work alongside biome AND night mode — order matters in CSS (biome < night-mode < high-contrast for overrides).
- LESSON-185: Fullscreen toggle via `requestFullscreen` needs a `fullscreenchange` listener to recalculate grid size. Add 100ms delay before recalc to let the browser finish the transition.

## Train Horn Patterns (Cycle 1, Day 1)
- LESSON-186: Use staggered setTimeout per train for horn sounds (i * 80ms) to avoid simultaneous oscillator overload when multiple trains exist.
- LESSON-187: Steam puff particles reuse the smoke-particle pattern but with larger size (8-18px) and stronger opacity. Key difference: stagger spawning (i * 60ms) for a natural eruption feel.
- LESSON-188: Per-color pitch variation uses a lookup table (HORN_PITCHES) mapping color to base frequency and sweep target. Red=low (220Hz), Yellow=high (400Hz). Makes each train sound distinct.
- LESSON-189: Horn cooldown (1s boolean flag with setTimeout reset) is simpler than timestamp-based cooldown for single-event buttons. No need for per-train cooldowns since the horn is a global action.
- LESSON-190: Button bounce animation requires force-reflow trick (void btn.offsetHeight) between classList.remove and classList.add to restart the CSS animation on rapid presses.
- LESSON-191: Three-layer horn sound design: triangle oscillator (body) + sine harmonic at 2x frequency (richness) + bandpass-filtered noise burst (steam hiss). Each layer has independent gain envelope.
- LESSON-192: H key context-switching (horn during play, tutorial when stopped) replaces the fixed H=tutorial binding. Check state.playing before the state.playing guard that blocks build shortcuts.

## Animal Reaction Patterns (Cycle 1, Day 2)
- LESSON-193: Use CSS class on the CELL element (not the emoji) for reaction animations, with `.animal-react-{type} .scenery-emoji` selectors. This lets the animation override the emoji's default animation (sway/waddle) via !important, and the cell class is easy to add/remove.
- LESSON-194: Flipped animals need separate keyframe animations that include the scaleX(-1) in every keyframe state. Without it, the flip gets reset at the start of the reaction animation.
- LESSON-195: Reaction animations should be very fast (0.5-0.8s) — short enough that they feel like a startled reflex, not a slow dance. Kids love the quick snap-back.
- LESSON-196: Reuse the existing mooCooldowns system for reaction timing — visual reactions trigger at the same time as sound effects, keeping them perfectly in sync without a separate cooldown tracker.
- LESSON-197: Always clean up reaction CSS classes in stopPlay() using regex-based class removal: `className.replace(/animal-react-\S+/g, '')`. This prevents stale animation classes lingering on cells.
- LESSON-198: Force-reflow trick (void el.offsetHeight) between class remove/add is needed to restart CSS animation when the same animal gets triggered again within the animation duration.

## Weather System Patterns (Cycle 1, Day 3)
- LESSON-199: Weather is a global visual preference (like biome/night mode) — store in its own localStorage key, not in game state. This keeps save/load compatibility intact.
- LESSON-200: Weather particles spawn into the grid-viewport element (not grid-container) so they're clipped to the visible game area and unaffected by zoom/pan transforms.
- LESSON-201: Use CSS custom properties (--rain-speed, --snow-drift, etc.) to randomize each particle's behavior without creating separate keyframes per particle. Same pattern as smoke particles.
- LESSON-202: Weather ambient sound uses filtered noise buffers (brown noise for rain, soft wind for snow). Route through a dedicated weatherAmbientGain → masterGainNode chain for independent volume control that still respects global mute.
- LESSON-203: Fade-in ambient sound (linearRampToValueAtTime over 1.5-2s) prevents jarring audio starts when toggling weather. Always fade in, never snap.
- LESSON-204: Weather overlay tinting uses a dedicated #weather-overlay div with CSS class-based background transitions. Separate from grid to avoid z-index conflicts with game elements.
- LESSON-205: Visual toggle keyboard shortcuts (weather W, fullscreen F, high-contrast A) must be placed BEFORE the `state.playing` return guard in handleKeyDown so they work during play mode.
- LESSON-206: Rain particles use thin 2px-wide linear-gradient strips with fast animation (0.4-0.7s). Snow particles use round dots (3-8px) with slow drift animation (2.5-5s) including horizontal sway via multi-stage keyframes.
- LESSON-207: Stop weather particles and ambient sound on visibilitychange (tab hidden) and restart on visible, matching the pattern for chimney smoke and music.
- LESSON-208: MAX_WEATHER_PARTICLES (60) provides good visual density without DOM bloat. Rain spawns every 40ms, snow every 200ms — matched to their visual density needs.

## Railroad Crossing Patterns (Cycle 1, Day 4)
- LESSON-209: Crossing is a track piece with same connections as straight (N-S at rot 0). Use the same exit logic — no special through-route handling needed.
- LESSON-210: Gate activation uses Manhattan distance (|dr| + |dc| <= 2) for proximity detection — simpler and more predictable than Euclidean distance for grid-based games.
- LESSON-211: Gate deactivation needs an 800ms delay timer to prevent flickering when trains pass through the crossing cell itself. Use per-crossing timers in a `crossingActiveTimers` map.
- LESSON-212: Crossing bell sound reuses the existing `SFX.crossingBell()` function (originally for crossover pieces) with a separate per-crossing cooldown map (`anim_crossingBellCooldowns`).
- LESSON-213: Gate arm CSS animation uses `transform-origin` (right center for left arm, left center for right arm) with `rotate(-90deg)` as default (up) and `rotate(0deg)` as active (down). The `transition: transform 0.5s` handles smooth lowering/raising.
- LESSON-214: Signal flash uses CSS `animation: alternate` for a natural oscillation between bright red and dark red, with `box-shadow` for the glow effect.
- LESSON-215: The `updateCrossingGates()` function runs every animation frame via `animateFrame()`. It scans all crossing cells and all active trains — O(crossings × trains) but both are small numbers in practice.
- LESSON-216: Clean up all crossing state (`clearCrossingGates()`) in `stopPlay()` — timers, cooldown maps, and CSS classes must all be reset to prevent stale state.
- LESSON-217: When adding new track types that behave like straight, add them to: BASE_CONNECTIONS, createTrackSVG switch, SHARE_TYPE_MAP, TOOL_KEY_MAP, placeTrainOnLoop valid types, ARIA label typeNames, and the MILESTONES unlock list. Missing any one creates a subtle bug.

## Rainbow Track Patterns (Cycle 1, Day 5)
- LESSON-218: Rainbow track uses linearGradient in SVG with 6 color stops (ROYGBV) for the prismatic effect. CSS hue-rotate animation on the SVG element creates the shimmer without needing JS per-frame updates.
- LESSON-219: Train rainbow glow uses CSS animation (rainbow-glow keyframes cycling through 7 colors) applied via classList.add/remove. The 3-second timer is tracked per-anim with rainbowGlowEnd timestamp compared against Date.now().
- LESSON-220: Sparkle particles spawn from the train's current pixel position (locoX, locoY) into grid-container (not grid) to avoid zoom transform issues. 80ms spawn interval with 20-particle cap prevents DOM bloat.
- LESSON-221: SFX.rainbowChime uses ascending pentatonic arpeggio (C5-E5-G5-A5) with staggered oscillator starts (80ms apart). Sparkle harmonics at 2x frequency with triangle wave add the magical shimmer quality.
- LESSON-222: The rainbow glow re-triggers on every rainbow cell entry, resetting the 3-second timer. This means multiple rainbow tracks in sequence extend the glow effect naturally without special handling.
- LESSON-223: New milestone type "Magician" gates rainbow behind puzzle progression (3 puzzles solved). This keeps the rainbow piece as a reward for engagement while being accessible fairly early.
- LESSON-224: When adding new track types to the screenshot canvas, group them with similar types (straight/tunnel/rainbow share the same straight-line rendering base) and use conditional blocks for unique visuals rather than separate case statements.

## Harden Week Patterns (Cycle 2, Day 52)
- LESSON-DAY52-A: **Stale-coordinate latent crashes from dim-shrink toggles.** Any module-level global that stores `(row, col)` coordinates (gridFocusRow/Col, hoveredCell, future: drag positions, click-anchored UI) needs a bounds check at the *consumer* side, not the producer, because dim-shrink paths are diverse: `setBigGrid()`, `decodeGridState()`, `loadPuzzle()`'s auto-shrink, save-load with mismatched bigGrid flag, etc. A single guard at the read site (e.g. `if (row >= ROWS || col >= COLS) return;`) is far more defensible than chasing every dim-changing function to remember to clear every stale-coord global. Cheap defense-in-depth.
- LESSON-DAY52-B: **Extend existing guards rather than adding new ones** when net-LOC budget is tight. Days 15/17 added per-fix lines; Day 52 fixed two P1 bugs with literally 0 LOC delta by extending the existing one-line early-return conditions (`if (state.playing) return;` → `if (state.playing || row < 0 || col < 0 || row >= ROWS || col >= COLS) return;`). Same defensive coverage, fewer indent levels, no growth.
- LESSON-DAY52-C: **Mouse `hoveredCell` global is set on every mouseover but doesn't auto-clear on grid rebuild.** When `initGrid()` recreates the DOM (after setBigGrid or any future re-layout), the old hoveredCell value persists in module-level state until the user moves the mouse and a new mouseover fires. Any kb-shortcut consumer of hoveredCell (Delete, Backspace) is a potential stale-coord crash site. Bounds-check at consumer.
- LESSON-DAY52-D: **Hunt smart, not exhaustively.** Day 52's mandate was "Fix Everything" with 0 open bugs entering. Instead of re-walking every feature, picked 4 specific *areas Day 51 had flagged* (gridFocus+BigGrid, share-link v1/v2, undoStack cap, duplicates). The first 3 came back clean in <5 minutes each; the 4th (gridFocus+BigGrid) produced 2 P1 bugs. Focused hunts > re-running the same audit checklist.

## Harden Week Patterns (Cycle 1, Days 34-37)
- LESSON-225: A naive `grep -c "function loadPuzzle"` will count both `loadPuzzle` and `loadPuzzleProgress`. When auditing for duplicates, use exact word boundaries (`grep -nE "function loadPuzzle\b"`) or eyeball the line numbers — don't trust raw counts blindly.
- LESSON-226: Four consecutive harden audits (full feature, puzzles, platform, code health) yielding only one P2 favicon bug suggests black-box test coverage is mature. Future harden weeks can compress to 2-3 days and free a day for delight polish or refactor experiments.
- LESSON-227: When `BUGS.md` shows zero open issues on a "Fix Everything" day, treat it as a code-health audit day instead: run JS parse, check tag balance, hunt duplicate code, scan for unsafe innerHTML/console patterns, then runtime smoke-test the live deployment. Document everything — a clean audit is still a deliverable.

## Prune Week Patterns (Cycle 1, Day 40 — Simplify)
- LESSON-228: Toolbar prune via "menu modal" preserves all features while reclaiming visual space. Rolling 7 buttons (🎵 music, ⌨️ shortcuts, 🔗 share, 📸 screenshot, 📊 stats, ♿ contrast, ⛶ fullscreen) into ⚙️ Settings + 📤 Share menus dropped visible toolbar from 21 → 13 buttons. Consolidated CSS via shared selectors (`#shortcuts-overlay,#settings-overlay,#share-overlay`) keeps the modal pattern DRY.
- LESSON-229: When deleting toolbar buttons, audit JS for stale `getElementById('btn-...')` references. Existing code already used `if (btn)` guards on most paths — but `toggleMusic()` did not. Fixing that to be DOM-optional made the function safe to call from the new Settings menu without a button element.
- LESSON-230: Two adjacent ☀️ buttons (day/night and "sunny weather") was a 5-yo confusion bug hiding in plain sight. Single-emoji toolbars need explicit visual differentiation; 🌤️ for weather + ☀️/🌙 dynamic for day/night fixes the collision.

## Cargo Delivery Patterns (Cycle 2, Day 46)
- LESSON-DAY46-A: Reuse the station piece type for cargo. Add optional metadata (`cargoType`, `cargoRole`) on the placed piece object. This piggybacks on JSON save/load for free and keeps a single piece type in palette/random/serialization paths. Drawback: byte-encoded share-link doesn't carry it (same constraint as Day 44 train names) — known limitation, not a bug.
- LESSON-DAY46-B: Random-gen `path.forEach((cell) => { state.grid[r][c] = { type, rotation }; })` is an *implicit filter* — only the listed fields make it onto the grid. When adding new metadata to path cells, you must also extend the placement destructure (`const { row, col, type, rotation, cargoType, cargoRole } = cell;`) or the data silently drops. Easy bug, easy fix once spotted.
- LESSON-DAY46-C: Permanent station-side overlays (cargo badges) need three rendering hooks to survive reality: (1) on placement (random gen, manual drop), (2) on `renderCell` (which strips and rebuilds the cell), (3) on cell-clear at random-gen start (`cleanupStationCargoBadges()` before `renderAllCells`). Missing #2 leads to badges vanishing after rotate/undo/load. Missing #3 leads to ghosts from the previous track.
- LESSON-DAY46-D: When stop-play resets state, distinguish *transient* visuals (in-flight train cargo badges → wipe) from *permanent* visuals (station cargo badges → keep). A blanket "remove all cargo elements" reset destroys the latter. Be explicit about which DOM survives.
- LESSON-DAY46-E: Cargo pickup/delivery share the existing `SFX.passengerBoard()` and `SFX.passengerDeliver()` envelopes — no new audio synth needed for Day 46. The role differentiation is purely visual (orange ring = pickup, green ring = delivery). Audio differentiation can come later if kid feedback wants it.
- LESSON-DAY46-F: Cargo "auto-on if any cargo stations exist on the grid" is a better UX than a toggle. Passenger had a toggle because every station can have passengers (always-on would be visual noise); cargo only appears at *specific* stations placed by random gen, so showing the HUD when those exist is unambiguous and zero-config for kids.

## Track Replay / Ghost Train Patterns (Cycle 2, Day 47)
- LESSON-DAY47-A: Action-log replay is way simpler than diff-replay or video-style replay. Capture (1) a baseline snapshot of grid+trains+switchStates+bigGrid taken at REC time, (2) an array of action records `{kind:'place'|'remove'|'rotate'|'placeTrain'|'clearAll', row, col, ...}`. To replay: restore baseline, then re-call the same low-level functions on a fixed cadence. Reuses the entire rendering pipeline — no separate "ghost renderer" needed.
- LESSON-DAY47-B: A single boolean `replayApplying` (NOT in `state` — module-level let) is the right idiom for "the function I'm calling re-enters its own logger and would record itself". Set true around the replay loop, then `if (state.replayRecording && !replayApplying) push(action)` keeps the hooks idempotent during playback.
- LESSON-DAY47-C: An incrementing token (`replayCancelTokenId`) beats a boolean cancel flag for async replays. Each new `playReplay()` call does `++replayCancelTokenId`, captures `myToken`, and bails out if `myToken !== replayCancelTokenId`. This handles double-clicks, restarts, and nested cancels without a cancel-handshake protocol.
- LESSON-DAY47-D: `body.replay-active` class with `pointer-events: none` on `#grid, #sidebar, #drawer-content, #toolbar, #trash-zone` is the cheapest way to lock UI during ghost playback. No need to disable individual handlers or rebuild input gating — CSS does it for free, and `replay-active` class auto-lifts on completion.
- LESSON-DAY47-E: Reduced-motion users need the cadence still slow enough to *see* what's happening (collapsing to 0ms = batch insert, no learning value). 200ms replay step is the sweet spot: faster than 600ms for users who don't want bobs/anims, but still steppable. Don't conflate "no animation" with "no pacing".
- LESSON-DAY47-F: A tight async setTimeout chain (await sleep + setTimeout(startPlay, 500)) gets visibly throttled in unfocused/headless tabs — the 500ms post-replay delay before auto-startPlay measured ~1500-3000ms in CDP smoke tests. Functionally fine for users (page is foregrounded when they kid-test it) but worth knowing when timing-bound regression checks run on background tabs.
- LESSON-DAY47-G: Persisting replay to its own localStorage key (`trainTracks_replay`) instead of merging into the main autosave keeps the autosave format frozen and the replay independently clearable. ~880 bytes for a 5-step recording with baseline; well under any reasonable LS quota even at 100s of steps. JSON-stringify the whole `{baseline, actions}` object — no need for compact byte encoding here, replays aren't shared yet.

## Day 53 (May 12) — Harden Week 2 Regression Pass

- LESSON-DAY53-A: A *fully automated* regression pass via a single big `evaluate` block (13 sequential checks + console feed afterward) is way more reliable than per-step browser actions. Stage all asserts into one return object, then read the dictionary. One downside: getting localStorage key names wrong silently fails an assertion (I checked `trainTracks_save_1` when the real key is `trainTracks_slot_1` — flagged a "saveSlot.saved=false" until I peeked at `Object.keys(localStorage)` directly). Lesson: when an assertion fails, always dump the *neighborhood* (`Object.keys(localStorage)`, function existence, etc.) before declaring it a bug. False-positive regression failures cost trust.
- LESSON-DAY53-B: `browser.console` poll AFTER the full evaluate block is the cleanest way to confirm "zero console errors" — wrapping `console.error` capture inside the evaluate also works but loses native warnings. Do both: in-evaluate capture for synchronous errors thrown inside the test, post-evaluate `console.messages.length` for async / external errors.
- LESSON-DAY53-C: Harden weeks shine when **2 of 5 days find latent bugs** (Day 51 and Day 52 this cycle, in the same gridFocus + Big-Grid neighborhood). The audit-then-hunt-then-fix-then-regress rhythm catches exactly the kind of bugs you can't see while building. Don't skip Harden weeks even when no bugs are visible — Day 51 entered with 0 known issues and ended with 2 P1 crash fixes shipped.
- LESSON-DAY53-D: Zero net LOC growth across an entire 5-day Harden week (11,192 lines on Day 48 → 11,192 lines on Day 53) is achievable when every fix extends an existing guard's condition instead of adding a new line. "Make the existing if-statement smarter" beats "add a new defensive check" for both readability and code-budget.

## Day 56 (May 15) — Prune Week 2 Code Cleanup

- LESSON-DAY56-A: **The "9 nearly-identical event-handler functions" pattern often dissolves into a single inline expression.** All 9 `closeXxxModalOutside(e)` wrappers were just `if (e.target === overlayEl) closeXxx()`. Replacing the `onclick="closeFooModalOutside(event)"` attribute with `onclick="if(event.target===this)closeFoo()"` deletes the entire indirection. Each modal's HTML grows ~18 chars; the JS shrinks by 31 lines. Net win: -31 LOC, no DRY helper required. Whenever you see N tiny wrapper functions that exist *only* to be referenced from one HTML `onclick`, look at the HTML — the inline form is usually shorter, clearer, and obviates the function entirely.
- LESSON-DAY56-B: **Single-call helper-removal is safer than helper-extraction during prune week.** `cleanupStationPassengers`, `cleanupStationCargoBadges`, `cleanupTrainCargoBadges` were each one line (`document.querySelectorAll('.foo').forEach(el => el.remove())`) and each had exactly one caller. Inlining at the call site (3 × -3 = -9 LOC) was a deterministic win with no API change. Extracting *another* helper like `removeAllByClass(cls)` would have left the LOC budget roughly flat. Rule of thumb: prune week prefers `1-caller helpers → inline` over `N-caller helpers → DRY consolidate`, because inlining is locally reasonable while consolidation requires global call-site refactor and risks behavior changes.
- LESSON-DAY56-C: **Test the inline-conditional dismissal pattern by directly invoking `overlay.onclick({target: overlay})` and `overlay.onclick({target: inner})` instead of synthesizing real `MouseEvent`s.** Headless browser MouseEvent dispatching went through `addEventListener` paths that bypassed the inline `onclick=` attribute. Calling the attribute-installed handler directly with a fake-target object exercises the actual `if(event.target===this)` predicate. 9/9 modals verified in one evaluate block this way; would have been 9 false-negatives via dispatchEvent.
- LESSON-DAY56-D: **Stale `cleanupStationCargoBadges()` call slipped past the first grep pass.** I deleted the *function definition* in the same edit pass as one of its callers (resetCargoState) but missed a second caller hidden in `generateRandomTrack` (line 7902, comment "// Day 46: clear any stale cargo badges before re-render"). Caught by a second `grep -nE "cleanupStation(Cargo)?Passengers|cleanupTrainCargoBadges"` *after* the first commit. Lesson: when inlining a helper used "once," `grep` again after the edit to confirm — single-call counts can be wrong if a caller is inside a long function and you only spot-checked the most obvious one. Add a verify-grep step to the inline-helper workflow.

## Day 59 (May 18) — Cycle 3 Build Day 1: Time-of-Day Sky

- LESSON-DAY59-A: **Pure CSS animation drives the "Time-of-Day sky cycle during play".** A 60s loop on a gradient overlay (`@keyframes sky-tint-cycle`) + a sun/moon emoji that arcs left→right via keyframe `left:` + `top:` percentages. Zero new JS loop required — only a `vp.classList.add('sky-cycling')` in `startPlay()` and `.remove()` in `stopPlay()`. Auto-respects night mode by gating a separate keyframe (`sky-tint-cycle-night`) with `body.night-mode`. Same pattern that the Day 27 ambient-music feature should have used: let CSS animate, JS just toggles the on/off class.
- LESSON-DAY59-B: **Mid-play night-mode toggle must sync the sun↔moon emoji.** A single `updateSkySunEmoji()` call from `toggleNightMode()` handles it. This is the same "label sync at the choke points" pattern as Day 45 (Big Grid label) and Day 48 (Sound Pack label) — except the three sites collapse to two here: `startPlay()` reads current state on activation, `toggleNightMode()` handles the change. No restore hook needed because the cycle is play-only state and never persists across sessions.
- LESSON-DAY59-C: **Centering an emoji on a percentage `left:` value is a `margin-left: -<halfFontSize>px` trick.** I wanted the sun to ride the arc visually centered on, say, 50% across, but `left: 50%` puts the *left edge* of the 28px emoji at 50%, so it appears 14px right of center. `margin-left: -14px` (half the font-size) compensates without needing transform-origin or translate math. Useful any time you want a fixed-size element to follow a percentage-driven path through its parent.
- LESSON-DAY59-D: **CSS `top:`/`left:` animations are not GPU-composited** (they trigger layout), but for a single 28px emoji animated over 60s at 30fps the cost is negligible. `will-change: transform, top, left` is added as a hint though browsers typically ignore it for non-composited props. The alternative (transform-based arc via translateX percentages of element width) is more complex and harder to read. For low-frequency single-element animations, prefer the simpler property animation — readability > micro-performance.
- LESSON-DAY59-E: **Live verification rhythm for visual-only features:** (1) write CSS+JS surgical edit, (2) JS parse + HTML balance + dup grep — catch structural bugs *before* push, (3) push + wait 30s for GitHub Pages cache, (4) navigate to live URL with `?v=N&fresh=1` cache-buster, (5) `localStorage.clear()` + reload, (6) `evaluate` block reads computed-style `animationName` and `opacity` to confirm CSS is wired live (NOT just "loaded"), (7) wait several seconds of real time, sample sun position + overlay tint mid-cycle to confirm the loop is actually animating, (8) screenshot for visual evidence. Steps 6-7 catch the most common failure mode: animation declared but not triggered because the class toggle is wired to the wrong element.

## Day 57 (May 16) — Prune Week 2 Delight Polish

- LESSON-DAY57-A: **"First-of-session" counter bugs are easy to ship if you increment before you read.** I added `let randomTrackCount = 0` and a `cargoChance = randomTrackCount === 0 ? 0.95 : 0.7` check, but my first version incremented the counter immediately at function entry (long before the cargo check). Result: the counter was always 1 by the time the check ran, so the 95% boost never fired — cargo rate stayed at the 70% baseline. Spot-tested with 30 simulations (got 60%, expected 95%) which caught it; without the simulation I'd have shipped a no-op. **Rule: when adding a `firstCallOnly` boost, put the increment AFTER all reads in the same function, OR use an explicit "didFireOnce" boolean named for the gate it controls (e.g. `firstCargoBoostUsed`).** Inline comment at the increment site explaining "do this AFTER the X check" prevents future re-orderings from quietly breaking the boost.
- LESSON-DAY57-B: **Verify session-scoped boosts via a simulation loop, not a one-shot trial.** A single first-random can hit cargo at 70% baseline by chance — indistinguishable from a working 95% boost. Running 30 simulated first-randoms (`randomTrackCount = 0; generateRandomTrack(); await sleep(1500)`) bounded the actual rate tightly enough to see the bug (60% vs 97% post-fix is a 37-point delta). Build a sampling test into the verification step for any probabilistic-feature change.
- LESSON-DAY57-C: **Emoji icons read very differently to kids than to adults.** 👻 is "a friendly ghost" to an adult who's read the modal copy and "a spooky Halloween thing" to a 5-year-old who hasn't. 🎬 (clapperboard) reads as "movie / replay this" universally. Keeping the ghost personality in the in-flight toast (`👻 Ghost rebuilding track...`) is fine — by that point the kid is already inside the feature and the friendly framing lands. The entry-point icon (settings button + modal h2) is what needs to be unambiguously inviting.

## Day 64 (May 23) — Harden Week 3 Day 1: Full Feature Audit

- LESSON-DAY64-A: **Cycle-3 Harden anchor: 11,873 lines.** This becomes the zero-growth target for Days 64-68 (Harden 3) and the not-to-exceed line for Days 69-73 (Prune 3). Each cycle the anchor grows — 10,089 (Cycle 1) → 11,192 (Cycle 2) → 11,873 (Cycle 3) — because the build week always nets new features, and the prune-week mandate is *net-zero or net-negative* relative to the cycle's own start, not relative to the prior cycle. The Cycle-2 Prune Week did achieve -36 LOC, but the Cycle-3 Build Week added 814 LOC over five days. Worth a Prune-3 stretch goal: -50 to -100 LOC, with the Sticker Book and Animal Passengers as the two biggest "look for inline opportunities" candidates (217 + 303 LOC respectively).
- LESSON-DAY64-B: **`placeTrain` silently no-ops on bare ground** — `if (!piece || SCENERY_TYPES.includes(piece.type)) return;` is the early-return guard. My first Day-64 audit pass tried to place 5 trains in row 2 (empty) and got `state.trains.length === 0` with no thrown errors. Not a bug — defensive design for "drag train onto grass" UX. Lesson: any audit that asserts "trains placed" must place track *first*, then trains atop. Same pattern applies to puzzle audits with locked cells — verify the cell is a valid placement target before asserting placement succeeded.
- LESSON-DAY64-C: **Sticker side-effects make Day-60 + Day-63 audit a two-for-one.** The `first-train` and `animal-friend` stickers auto-earned during a single 9-second play session of the random-generated track, without my needing to construct controlled scenarios. Reading the post-play `localStorage.trainTracks_stickers.earned` keys is a single assertion that proves *both* the sticker hook system (Day 63) AND the underlying stat-tracking it observes (`trainsRun` count, `animalsDelivered` count from Day 60). When two features are layered as "tracker → reactor," audit the reactor — passing the reactor implies the tracker fired correctly.
- LESSON-DAY64-D: **Replay-share v3 round-trip is identifiable by base64 first byte.** `encodeReplayShareState()` produces a hash starting with `Aw…` — first byte 0x03 in base64 is `A` (most-significant bits 000000) followed by `w` (next 6 bits 110000), giving the byte `00000011` = 3. Quick parse: read the version byte directly with `hash.charCodeAt(0)` is wrong (that's the *char* code of the base64 letter, not the decoded byte); instead `b64urlDecode(hash.slice(0,2))[0]` gives the actual version byte. For sanity, just eyeballing `Aw…` as the v3 prefix vs `Ag…` as v2 vs `AQ…` as v1 works for fast visual identification of which decoder branch a hash will take.
- LESSON-DAY64-E: **All 11 modal overlays now exist in DOM** (was 10 through Day 53). Sticker Book (Day 63) added `#sticker-overlay` as the 11th. Modal-presence audit should keep a running inventory — when a new modal lands in a build day, the next Harden audit's modal-list grows by 1. If it *doesn't* grow, that's a smell (modal was inlined into another overlay, or its overlay element name doesn't match the project convention). Project convention is strict: `<feature-name>-overlay` for every modal. Day 63 followed it (`sticker-overlay`); future builds should too.


---

## Day 65 — Harden Week 3 Day 2: Puzzle & Mode Testing

### Lesson — Puzzle 5 "Grand Station" topology is non-obvious

The naive rectangle-perimeter solution for Puzzle 5 needs 13 straights + 4 curves, but the puzzle budget is 9 straights + 8 curves. **The actual solution is a small rectangle on rows 2-3 (visiting both top stations) with a vertical stem dropping through cols 4 and 6 to capture the row-5 station** — uses all 8 curves and exactly 9 straights for a total of 17 player pieces. This is the only puzzle where the optimal topology isn't a rectangle.

For future audits: if "Puzzle 5 unsolvable" comes up, it's NOT a bug — re-read the topology above. The puzzle is intentionally hard ("Hard" difficulty in puzzle data) and forces creative use of curves to avoid the straight-budget bottleneck.

### Lesson — `setCell()` direct-write bypasses puzzle budget

When verifying puzzle solvability via console, using `state.grid[r][c] = {type, rotation}` directly bypasses `puzzleState.pieceCounts` accounting. This is fine for "does the validator accept the topology" tests but can hide budget-fit issues. **Always validate the final solution by re-running with `placePiece()` (which enforces budget)** to confirm the puzzle is actually solvable within its `available` constraints.

### Lesson — Station rotation matters

Stations have `BASE_CONNECTIONS = ['N','S']`. Most puzzles ship stations with `rotation: 90`, which rotates to `['E','W']` — i.e., **stations are HORIZONTAL** in puzzles 5 and 6 (and most cases). The path must enter and exit horizontally. T-junctions (puzzle 6) bridge the station from W/E sides via row-3 horizontal corridor — not from N/S.

### Lesson — Toast `openEnds` is halved in the displayed message

`checkPuzzleSolution()` increments `openEnds` once per direction-mismatch (each broken edge is counted twice — once from each side). The user-facing toast shows `Math.floor(openEnds/2)`. So "1 disconnected edges" means 2-3 raw `openEnds`. Good to know when debugging puzzle failures from a console replay of the validator.

### Lesson — Auto-solver verification approach

For puzzle-batch verification: build a generic auto-solver that places obvious-topology solutions for rectangular puzzles, then iteratively refine for special cases (figure-8, tunnel-substitutes, T-junctions). The validator's `openEnds` count + `toast.match(/(\d+) disconnected/)` is the fastest signal — each mismatch points at a specific cell pair that doesn't connect. Iterate by inspecting cell connections vs neighbors in a single pass; the issue is almost always a wrong rotation on a curve (a curve at the wrong rotation looks identical to a correct one in the UI but mismatches direction). The systematic approach is 10× faster than guess-and-check.
