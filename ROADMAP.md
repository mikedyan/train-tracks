# Train Tracks — 14-Day Feature Roadmap

One feature per day. Builder agent ships at 8 AM PST, QA agent tests at 11 AM PST.

## Status Key
- ⬜ TODO — Not started
- 🔨 IN PROGRESS — Builder is working on it
- ✅ SHIPPED — Implemented and pushed
- 🧪 QA PASSED — Tested and verified by QA agent
- ❌ FAILED — QA found issues, fixes pending

## Completed Features (Pre-Roadmap)
| # | Date | Feature | Status |
|---|------|---------|--------|
| 1 | Fri Mar 6 | Single Train Enforcement | ✅ 🧪 |
| 2 | Sat Mar 7 | Right-Click to Remove | ✅ 🧪 |
| 3 | Sun Mar 8 | Train Dragging (independent of tile) | ✅ 🧪 |
| 4 | Mon Mar 9 | Random Track Generator + rotation fix | ✅ 🧪 |

## 14-Day Schedule

| Day | Date | Feature | Status |
|-----|------|---------|--------|
| 1 | Tue Mar 10 | Fix Wobbly Loop + Figure-8 Generator | ⬜ (Builder not shipped; QA ran full regression, fixed 2 bugs) |
| 2 | Wed Mar 11 | Train Cars (multi-car train) | ⬜ (Builder not shipped; QA ran full regression, 57/57 pass, 0 bugs) |
| 3 | Thu Mar 12 | Smoke & Steam Particles | ⬜ |
| 4 | Fri Mar 13 | Smart Auto-Connect | ⬜ |
| 5 | Sat Mar 14 | Save & Load Layouts | ⬜ |
| 6 | Sun Mar 15 | Night Mode | ⬜ |
| 7 | Mon Mar 16 | Tunnel Piece | ⬜ |
| 8 | Tue Mar 17 | Animated Scenery | ⬜ |
| 9 | Wed Mar 18 | Mobile & Touch Polish | ⬜ |
| 10 | Thu Mar 19 | Water Tiles & River | ⬜ |
| 11 | Fri Mar 20 | Horn Variations & Ambient Audio | ⬜ |
| 12 | Sat Mar 21 | Speed Signs & Signals | ⬜ |
| 13 | Sun Mar 22 | Challenge Puzzles | ⬜ |
| 14 | Mon Mar 23 | Share & Screenshot | ⬜ |

---

## Feature Specs

### Day 1: Fix Wobbly Loop + Figure-8 Generator (Mar 10)
**Problem:** The wobbly loop algorithm often fails to close back to start, producing disconnected open paths. Also, all random layouts are simple shapes — needs more variety.
**Solution:**
- Fix `generateWobblyLoop`: when the random walk wants to stop, use BFS pathfinding to find a route back to the start cell that avoids occupied cells. Place the appropriate track pieces along the return path.
- Handle the closure piece correctly: the first cell of the path needs its entry edge to match the last cell's exit direction.
- Add `generateFigure8Loop`: uses a crossover piece in the center where two loops intersect. Creates more interesting layouts.
- Ensure all generators validate connectivity before returning (every piece has all connections satisfied with green dots).
**Acceptance criteria:**
- Hit Random 20 times — every single layout must be a fully connected loop (all green dots, zero red dots)
- At least 3 visually distinct layout shapes appear across 20 presses
- Train completes full loop on every generated layout without crashing

### Day 2: Train Cars (Mar 11)
**Problem:** Train is a single locomotive. Should support additional cars trailing behind for a more satisfying train experience.
**Solution:**
- Train becomes a linked chain: locomotive + N trailing cars
- New palette items: Freight Car (🟫), Passenger Car (🔵), Caboose (🔴)
- Drag car from palette onto the locomotive to append it to the train
- During animation: maintain a path history ring buffer. Locomotive writes positions. Each car reads from the buffer at an offset (car 1 is 1 cell-length behind, car 2 is 2, etc.)
- Car SVG designs (top-down, same style as locomotive):
  - Freight: brown rectangle with cargo boxes
  - Passenger: blue rectangle with window rows
  - Caboose: red rectangle with rear platform (always last if present)
- Static display: when not playing, cars sit on consecutive track cells behind the loco
- Ordering: cars append in drag order, but caboose always snaps to end
- Max 5 cars (locomotive + 5 = 6 total)
- Remove a car: right-click on it, or drag to trash
**Acceptance criteria:**
- Can add all 3 car types from palette
- Cars follow locomotive smoothly through curves without jitter
- Cars maintain consistent spacing
- Right-click removes individual cars
- Caboose always stays at the end regardless of add order

### Day 3: Smoke & Steam Particles (Mar 12)
**Problem:** Train animation feels static. No visual feedback that the locomotive is "alive."
**Solution:**
- CSS-only particle system spawning from the locomotive's smokestack position
- Small gray/white circles (3-6px) that drift upward, expand, fade to transparent
- Spawn rate: ~3-5 particles per second at speed 1x, scales with train speed
- Particles are absolutely positioned in the grid container, not tied to the train element
- Each particle: random x-offset (±5px), upward drift (30-60px), lifetime 0.8-1.5s
- Use CSS @keyframes for the animation (translateY + scale + opacity)
- Particles only active during play state
- Performance: max 30 particles alive at once (recycle old ones)
**Acceptance criteria:**
- Visible smoke puffs trailing from the locomotive during play
- Smoke rate visually increases when speed slider is higher
- No performance degradation (steady 60fps)
- Particles disappear cleanly when stopping play
- No particles when train is stationary

### Day 4: Smart Auto-Connect (Mar 13)
**Problem:** Placing track pieces requires manual rotation to connect to neighbors. Tedious.
**Solution:**
- When a piece is dropped from the palette, before placing it, check all 4 rotations (0°, 90°, 180°, 270°)
- Score each rotation: +1 for each connection that matches a neighbor's open connection
- Pick the rotation with the highest score
- Tie-breaking: prefer rotation that creates the most connections
- Only auto-rotate pieces from palette (not when moving existing pieces, to preserve user intent)
- Pieces are still manually rotatable by clicking after placement
- Visual feedback: brief green pulse on auto-connected edges
**Acceptance criteria:**
- Drop a curve next to a straight — it auto-rotates to connect
- Drop a straight between two existing pieces — connects to both
- Clicking a piece still rotates it manually
- Moving a piece from the grid preserves its current rotation
- Works correctly with all piece types (straight, curve, T, crossover, bridge, station)

### Day 5: Save & Load Layouts (Mar 14)
**Problem:** Layouts are lost on page refresh. No way to keep favorite builds.
**Solution:**
- 5 named save slots stored in localStorage
- Save button (💾) opens a modal with 5 slots showing:
  - Slot name (editable, default "Slot 1" through "Slot 5")
  - Tiny thumbnail preview of the saved layout (render grid to a small canvas)
  - Timestamp of when it was saved
  - Save / Load / Delete buttons per slot
- Auto-save: save current state to a special "autosave" key on page unload (beforeunload event)
- Auto-restore: on page load, restore from autosave if it exists
- State to save: full grid array, train position, train cars (if Day 2 is done)
- Modal styling: matches the game's warm wood/green aesthetic
**Acceptance criteria:**
- Save to slot 1, refresh page, load from slot 1 — identical layout restored
- All 5 slots work independently
- Thumbnails show a recognizable mini version of the layout
- Auto-save/restore works on page refresh
- Delete clears the slot completely
- Works with all piece types and train position

### Day 6: Night Mode (Mar 15)
**Problem:** Visual experience is one-dimensional. No atmospheric variety.
**Solution:**
- Toggle button: ☀️/🌙 in the controls bar
- Night mode changes:
  - Grass: #7CB342 → #2E4A1E (dark green)
  - Sky/background: #E8F5E9 → #1A1A2E (dark blue)
  - Sidebar: darker wood tones
  - Grid gap: darker
  - Stars: scattered small white dots on background (CSS radial-gradient or pseudo-elements)
  - Train headlight: radial gradient glow (yellow, 2-cell radius) that moves with the train during animation
  - House windows: warm yellow glow (small CSS box-shadow)
  - Firefly particles: tiny yellow-green dots that float randomly in empty cells (CSS animation)
- Smooth transition: all color changes use CSS transitions (0.5s ease)
- Preference saved in localStorage
**Acceptance criteria:**
- Toggle switches between day and night smoothly (no flash)
- Headlight glow follows the train during animation
- House windows glow in night mode
- Stars visible on background
- Preference persists across page refreshes
- All track pieces remain clearly visible in night mode

### Day 7: Tunnel Piece (Mar 16)
**Problem:** Track set is limited. No elevation or hidden sections.
**Solution:**
- New track type in palette: Tunnel
- SVG design: mountain/hill with a dark oval opening, track entering into darkness
- Behavior: connects N-S (like a straight), but train fades to opacity 0 when entering and fades back when exiting
- Entry animation: train shrinks slightly + fades out over first 30% of cell
- Exit animation: train grows + fades in over last 30% of cell
- Sound: "whoosh" echo effect on entry, return whoosh on exit
- Works with night mode (tunnel entrance glows slightly)
- Multiple tunnels on a track: train disappears and reappears at each one
**Acceptance criteria:**
- Tunnel appears in palette, can be dragged and placed
- Train visually disappears inside the tunnel and reappears on the other side
- Sound effect plays on entry/exit
- Tunnel connects correctly with adjacent straight/curve pieces
- Works with train cars (each car disappears/appears independently)
- Rotatable like other pieces (can be horizontal or vertical)

### Day 8: Animated Scenery (Mar 17)
**Problem:** Scenery is static decoration. World feels lifeless.
**Solution:**
- Trees: gentle sway animation (CSS transform: rotate ±3°, 3-4s loop, randomized delay per tree so they don't sway in sync)
- Cows: wander to adjacent empty cells every 5-10 seconds (random timer per cow). Movement: slide transition over 1s. Only move to adjacent empty cells (not onto tracks). If no empty neighbor, stay put.
- Houses: chimney smoke — tiny CSS particle (same system as train smoke but smaller, slower, from the house roof)
- All animations are subtle and non-distracting
- Animations pause when browser tab is not visible (requestAnimationFrame/visibility API)
- Performance: stagger cow movement checks, max 1 cow moving at a time
**Acceptance criteria:**
- Trees visibly sway (subtle, not wild)
- Cows occasionally move to adjacent empty cells
- Cows never walk onto tracks or other scenery
- House chimneys emit tiny smoke wisps
- Animations don't affect game performance
- Animations stop when tab is hidden

### Day 9: Mobile & Touch Polish (Mar 18)
**Problem:** Game works on mobile but isn't optimized. Small targets, no zoom, awkward layout.
**Solution:**
- Responsive grid: recalculate cell size to fill available screen space
- Portrait mode: move palette to a bottom drawer (horizontal scrolling strip) instead of side panel
- Larger touch targets: palette pieces 72px on mobile (up from 54px)
- Pinch-to-zoom on the grid area (CSS transform: scale, with boundaries)
- Double-tap to zoom to 1:1
- Haptic feedback: `navigator.vibrate(10)` on place, `navigator.vibrate([5,5,5])` on remove
- Prevent accidental zoom/scroll of the whole page
- Controls: make buttons larger on mobile, wrap to two rows if needed
- Test at 375px wide (iPhone SE) through 768px (iPad)
**Acceptance criteria:**
- Game fills the screen on iPhone SE (375px) — no horizontal scroll
- Palette accessible on portrait orientation
- Can build and play a full track layout on mobile without frustration
- Pinch-to-zoom works smoothly
- No accidental page zoom or scroll
- Haptic feedback fires on supported devices

### Day 10: Water Tiles & River (Mar 19)
**Problem:** Landscape is just grass. No terrain variety.
**Solution:**
- New scenery type in palette: Water 💧
- Water tile SVG: blue gradient with animated wave ripples (CSS keyframe on SVG paths)
- Bridge interaction: when bridge is placed adjacent to water, it looks like it's spanning over the water (z-index layering)
- Duck: tiny SVG duck that slowly drifts on water tiles (random direction, 10-15s per tile, wraps to adjacent water)
- Random generator update: sometimes generates a "river" — a 1-wide strip of water tiles through empty space
- Water is impassable for track (can't place track on water, only bridges over water)
- Lily pads: small green circles randomly placed on some water tiles
**Acceptance criteria:**
- Water tiles show animated waves
- Can place water from palette
- Can't place track directly on water (shows toast warning)
- Bridge placed next to water looks natural
- Ducks drift on water tiles
- Random generator occasionally includes a river
- Water works in both day and night mode (darker blue at night)

### Day 11: Horn Variations & Ambient Audio (Mar 20)
**Problem:** Sound is minimal and repetitive. No atmosphere.
**Solution:**
- Train horn upgrade: proper two-tone horn at stations (Web Audio API frequency sweep)
- Crossing bell: rapid ding-ding-ding when train passes through crossover piece
- Tunnel echo: reverb/delay effect on chug sound inside tunnel
- Ambient sounds (separate toggle):
  - Day: bird chirps (random intervals, 10-30s), gentle breeze (filtered noise)
  - Night: cricket chirps, owl hoot (rare, every 30-60s)
- Volume control: slider in settings (affects all sound equally)
- Sound icon shows current state: 🔊 (all on), 🔉 (ambient off), 🔇 (all off) — cycle through
**Acceptance criteria:**
- Horn sounds different and more satisfying than current whistle
- Crossing bell audible at crossovers
- Tunnel modifies the chug sound
- Ambient sounds play during idle (not just during play)
- Volume slider works
- Mute properly silences everything
- No audio glitches or clicks

### Day 12: Speed Signs & Signals (Mar 21)
**Problem:** Train speed is global. No way to create interesting speed dynamics in the layout.
**Solution:**
- New palette item: Speed Sign (trackside decoration, not a track type)
- Speed sign types: 🐢 Slow (0.5x), 🚂 Normal (1x), 🐇 Fast (2x)
- Place on any track cell (overlays on the track, doesn't replace it)
- When train passes a speed sign, train speed transitions to the sign's speed over 0.3s
- Visual: speed signs are small SVG elements positioned at the edge of the track cell
- Sign SVG: circular sign on a pole, with speed icon inside
- Multiple signs on a layout create speed zones
- Works with cars: whole train transitions together
- Clicking a placed sign cycles through speed levels (slow → normal → fast → slow)
**Acceptance criteria:**
- Can place speed signs on track cells from palette
- Train visibly speeds up and slows down when passing signs
- Speed transitions are smooth (not jarring)
- Signs are clearly visible but don't obscure the track
- Clicking cycles the speed level
- Right-click removes the sign (not the track underneath)
- Works correctly with train cars

### Day 13: Challenge Puzzles (Mar 22)
**Problem:** Game is freeform only. No goals or structured play.
**Solution:**
- New mode: Puzzles (🧩 button in controls)
- 5 hand-crafted puzzles of increasing difficulty:
  1. "Simple Loop" — Connect 2 stations with 4 pre-placed curves (just add straights)
  2. "Bridge Builder" — Cross a river of water tiles to connect two sides
  3. "Figure 8" — Create a figure-8 using a crossover (limited pieces)
  4. "Mountain Pass" — Navigate through tunnels and around obstacles
  5. "Grand Station" — Connect 3 stations in a single loop (hardest)
- Puzzle mode UI:
  - Puzzle select screen (overlay) with thumbnail + difficulty stars
  - Locked cells (pre-placed pieces can't be moved, shown with a subtle lock icon)
  - Limited palette (only the pieces needed, shown with count)
  - "Check" button validates the solution (all connections green + train can complete loop)
  - Star rating: ⭐ = solved, ⭐⭐ = solved with fewer pieces, ⭐⭐⭐ = optimal solution
  - Completion saved to localStorage
- "Back to Sandbox" button to return to freeform mode
**Acceptance criteria:**
- All 5 puzzles are solvable
- Locked pieces can't be moved or removed
- Limited palette correctly restricts available pieces
- Check button accurately validates (no false positives/negatives)
- Star rating works correctly
- Progress persists across refreshes
- Can freely switch between puzzle and sandbox modes

### Day 14: Share & Screenshot (Mar 23)
**Problem:** No way to show off your creations.
**Solution:**
- 📸 Screenshot button in controls bar
- Captures the grid (without UI chrome) as a PNG image:
  - Use OffscreenCanvas or html2canvas to render the grid
  - Include scenery, track, train, and all visual effects
  - Clean render without connection dots or UI overlays
- Actions after capture:
  - Download as PNG (auto-named "train-tracks-YYYY-MM-DD.png")
  - Copy to clipboard (navigator.clipboard.write)
  - Toast confirmation: "📸 Saved!" or "📋 Copied!"
- Share link: encode the grid state in a URL hash
  - Compress grid to compact format: type (4 bits) + rotation (2 bits) = 6 bits per cell
  - Base64 encode → append to URL as hash fragment
  - Opening a share link auto-loads the layout
  - "🔗 Copy Link" button after screenshot
- URL detection: on page load, check for hash → decode and load if present
**Acceptance criteria:**
- Screenshot produces a clean PNG of the grid
- Download works in Chrome, Firefox, Safari
- Copy to clipboard works
- Share link correctly encodes and decodes a layout
- Complex layouts (all piece types, scenery, train) survive encode/decode
- Share links work when opened in a new browser/incognito

---

## Architecture Notes

### Cron Agents
- **Builder Agent**: Daily 8:00 AM PST, Opus with high thinking. Reads this ROADMAP.md, implements today's feature, pushes, updates status.
- **QA Agent**: Daily 11:00 AM PST, Opus with high thinking. Tests EVERYTHING in TEST_MATRIX.md. Fixes ALL bugs found (unlimited budget). Pushes fixes. Updates TEST_MATRIX.md with new feature tests.

### Priority Rules
1. QA agent fixes everything it finds. No time limits. Ship quality.
2. If QA is still fixing when Builder runs next morning, Builder checks git log to avoid conflicts.
3. Builder checks BUGS.md on startup — if QA logged anything it couldn't fix (rare), Builder addresses it before new feature.
4. Working product > new features. If the game is broken, fix it first.

### File Responsibilities
- `ROADMAP.md` — Feature schedule, specs, status (this file)
- `TEST_MATRIX.md` — Cumulative test checklist, grows daily
- `BUGS.md` — Bug tracking log (should usually be empty if QA is doing its job)
- `index.html` — The product (single file)
