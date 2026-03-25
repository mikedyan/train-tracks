# Train Tracks — Development Roadmap (Council Synthesis)

*Generated Mar 12, 2026 from 4-model council review (Claude, GPT-5.2, Gemini 3 Pro, Grok 4.1)*
*Each model played the live game and produced independent suggestions.*
*This roadmap synthesizes ~90 suggestions into 28 prioritized days.*

---

## Phase 2: Council Roadmap

### Week 1: Core Polish & Satisfaction (Days 1–7)

The foundation is solid but missing the "juice" — the micro-feedback that makes every interaction satisfying. Week 1 adds the polish that transforms a prototype into a product.

---

#### Day 1 — Save & Load + Auto-Save
**Council consensus: 4/4 models flagged this as critical**

The game has zero persistence — refresh and everything is gone. A toddler who spent 20 minutes building will be devastated.

**Tasks:**
1. Auto-save grid state to localStorage on every change (place, remove, rotate)
2. Auto-restore on page load (seamless — user never notices)
3. Add 💾 Save button that opens modal with 3 named slots
4. Each slot shows: name (editable), mini thumbnail (render grid to small canvas), timestamp
5. Save/Load/Delete buttons per slot
6. Toast confirmation: "💾 Saved!" / "📂 Loaded!"

**Acceptance criteria:**
- Build a track, refresh page → identical layout restored
- All 3 slots work independently
- Thumbnails show recognizable mini layout
- Works with all piece types, scenery, and train position

---

#### Day 2 — Smart Auto-Connect
**Council consensus: 3/4 models (Claude, Gemini, Grok)**

Manually clicking to rotate pieces is frustrating for a toddler. When a piece drops near existing tracks, auto-rotate it to connect.

**Tasks:**
1. On palette drop: try all 4 rotations, score each by number of matching connections
2. Pick highest-scoring rotation (tie-break: most total connections)
3. Only auto-rotate pieces from palette (not when moving existing pieces)
4. Brief green pulse animation on auto-connected edges
5. Fall back to default rotation if no connections exist nearby

**Acceptance criteria:**
- Drop a curve next to a straight → auto-rotates to connect
- Drop a straight between two pieces → connects to both
- Manual click-to-rotate still works after placement
- Moving existing pieces preserves their current rotation

---

#### Day 3 — Smoke/Steam Particles + Loop Celebration
**Council consensus: 3/4 models each**

Two high-impact visual additions. Smoke makes the train feel alive. Loop celebration gives the builder a moment of triumph.

**Tasks:**
1. **Smoke:** CSS particle system from locomotive smokestack during play
2. Small gray/white circles (3-6px) that drift upward, expand, fade
3. Spawn rate scales with speed slider (~3-5/sec at 1x)
4. Max 30 particles alive (recycle old ones), CSS @keyframes only
5. **Celebration:** Detect when train completes full loop (returns to start cell)
6. On first loop completion: confetti burst + triumphant sound + "🎉 Full Loop!" toast
7. Confetti particles: 20-30 colored dots that burst outward and fade

**Acceptance criteria:**
- Visible smoke puffs trailing from locomotive during play
- Smoke rate increases with speed slider
- No performance degradation (steady 60fps)
- Confetti triggers once per play session on loop completion
- Satisfying sound accompanies the celebration

---

#### Day 4 — Ghost Preview + Placement Sounds
**Council consensus: 3/4 models (ChatGPT, Gemini, Grok)**

Show what you're about to place. Make every placement feel tactile.

**Tasks:**
1. When dragging a piece over the grid, show translucent "ghost" preview at target cell
2. Ghost shows auto-connected rotation (if Day 2 is done)
3. Green border if connections will match, red if mismatches
4. Satisfying wooden "thunk" sound on every track placement (Web Audio)
5. Softer "click" for scenery placement
6. Different pitch for rotation clicks

**Acceptance criteria:**
- Ghost preview visible during drag (50% opacity)
- Ghost shows correct rotation for auto-connect
- Green/red border accurately reflects connection state
- Placement sound plays on every successful drop
- No audio glitches or clicks

---

#### Day 5 — Train Cars
**Council consensus: 2/4 models but both gave detailed specs**

Toddlers love long trains. The single locomotive should support trailing cars.

**Tasks:**
1. New palette items: Freight Car (brown box), Passenger Car (blue windows), Caboose (red)
2. Drag car from palette onto the locomotive to append
3. Path history ring buffer: locomotive writes positions, each car reads at offset
4. Car SVGs: top-down style matching locomotive aesthetic
5. Caboose always snaps to end regardless of add order
6. Max 5 cars (locomotive + 5 = 6 total)
7. Right-click on a car to remove it
8. Cars follow smoothly through curves (interpolated positions)

**Acceptance criteria:**
- Can add all 3 car types
- Cars follow locomotive smoothly through curves without jitter
- Consistent spacing between cars
- Caboose stays at end
- Right-click removes individual cars

---

#### Day 6 — Day/Night Mode
**Council consensus: 3/4 models**

A dramatic visual transformation that kids love and makes the game feel premium.

**Tasks:**
1. Toggle button: ☀️/🌙 in controls bar
2. Night palette: dark blue-green grass, dark sky, darker sidebar
3. Stars: scattered white dots on background (CSS radial-gradient)
4. Train headlight: radial gradient glow (yellow, 2-cell radius) moves with train
5. House windows: warm yellow glow (CSS box-shadow)
6. All transitions use CSS custom properties + 0.5s transition
7. Save preference to localStorage

**Acceptance criteria:**
- Smooth toggle (no flash, 0.5s transition)
- Headlight follows train during animation
- House windows glow at night
- Stars visible on background
- All track pieces remain clearly visible
- Preference persists across refreshes

---

#### Day 7 — Crash/Derail Feedback
**Council consensus: 2/4 models (ChatGPT, Grok) + Gemini**

When something goes wrong, make it fun — not frustrating.

**Tasks:**
1. When train hits an open track end (red dot): bouncy "Boing!" sound + dust cloud
2. Star burst animation at crash point (10-15 yellow stars that scatter and fade)
3. Train bounces backward slightly before stopping
4. Toast: "💥 Oops! Connect more tracks!" (friendly, not punishing)
5. If train derails at speed > 1.5x: exaggerated wobble before crash
6. Crash sound varies by speed (louder at higher speed)

**Acceptance criteria:**
- Crash animation plays at open track ends
- Sound is comical/fun, not jarring
- Toast message appears with helpful hint
- Animation doesn't block gameplay (auto-clears in 2s)
- Works with train cars (cars pile up comedically behind locomotive)

---

### Week 2: Gameplay Depth (Days 8–14)

Now the sandbox feels alive. Week 2 adds mechanics that give players reasons to build more complex layouts.

---

#### Day 8 — Clickable Switches (Interactive T-Splits)
**Council consensus: 3/4 models (ChatGPT, Gemini, Grok)**

The most-requested gameplay feature. Click T-junctions to toggle direction while the train is moving.

**Tasks:**
1. T-junction pieces get a clickable lever indicator (small arrow showing active direction)
2. Click during play to toggle: train takes the other path next time
3. Visual: lever animates from one side to the other (CSS transition)
4. Click sound: mechanical "clunk"
5. Works during play AND while paused (pre-set routes)
6. Default direction: straight-through (the non-branching path)

**Acceptance criteria:**
- Clicking T-junction toggles direction during play
- Train follows the toggled path on next pass
- Lever visually indicates current direction
- Works with multiple T-junctions in same layout
- Pre-setting during pause works correctly

---

#### Day 9 — Multiple Trains ✅ *(completed: 2026-03-25)*
**Council consensus: 3/4 models (ChatGPT, Gemini, Grok)**

Multiple trains = chaos for toddler, strategy for dad.

**Tasks:**
1. Allow placing up to 3 trains (palette shows 3 colored trains: red, blue, green)
2. Each train runs independently on connected tracks
3. Collision detection: if two trains meet on same cell, play crash animation
4. Each train has independent car attachments
5. Speed slider affects all trains equally
6. Play/Stop controls all trains simultaneously

**Acceptance criteria:**
- Can place 3 trains on different track segments
- All trains animate simultaneously during play
- Collision triggers crash animation for both trains
- Each train can have its own car chain
- Removing one train doesn't affect others

---

#### Day 10 — Water Tiles & Functional Bridges
**Council consensus: 3/4 models (ChatGPT, Gemini, Grok)**

Terrain variety that gives bridges a mechanical purpose.

**Tasks:**
1. New scenery: Water 💧 in palette
2. Water tile SVG: blue gradient with animated wave ripples (CSS keyframe)
3. Can't place track on water (toast: "🌊 Tracks can't go on water!")
4. Bridge piece placed adjacent to water visually spans over it (z-index layering)
5. Duck: tiny SVG duck that slowly drifts on water tiles
6. Random generator: sometimes includes a "river" strip of water through the layout
7. Night mode: darker blue water, moonlight reflection

**Acceptance criteria:**
- Water tiles show animated waves
- Can't place track directly on water
- Bridge placed near water looks natural
- Ducks drift on water (decorative)
- Random generator occasionally produces rivers
- Works in both day and night modes

---

#### Day 11 — Tunnels
**Council consensus: 2/4 models (ChatGPT, Claude)**

Hide-and-reveal mechanics are magical for kids.

**Tasks:**
1. New track piece in palette: Tunnel (mountain with dark oval opening)
2. Connects N-S like a straight (rotatable for E-W)
3. Train entry: shrinks + fades to opacity 0 over first 30% of cell
4. Train exit: grows + fades back in over last 30%
5. Sound: "whoosh" echo on entry, return whoosh on exit
6. Each car fades independently when entering
7. Night mode: tunnel entrance has subtle glow

**Acceptance criteria:**
- Tunnel in palette, draggable and placeable
- Train disappears inside, reappears on other side
- Sound effects on entry/exit
- Connects with adjacent straight/curve pieces
- Works with train cars (staggered fade)
- Rotatable (horizontal or vertical)

---

#### Day 12 — Animated Scenery
**Council consensus: 3/4 models (ChatGPT, Claude, Grok)**

Make the world feel alive even when the train is stopped.

**Tasks:**
1. Trees: gentle CSS sway (rotate ±3°, 3-4s loop, randomized delay per tree)
2. Cows: emit "moo" sound (low-frequency oscillator) when train passes nearby
3. Cows: occasionally face different direction (CSS flip, random timer)
4. Houses: chimney smoke (small CSS particles from roof, slower than train smoke)
5. Animations pause when tab hidden (visibility API)
6. All animations subtle — enhance, don't distract

**Acceptance criteria:**
- Trees visibly sway (subtle)
- Cows moo when train passes within 1 cell
- House chimneys emit tiny smoke wisps
- Animations don't affect performance
- Animations stop when tab hidden

---

#### Day 13 — Richer Soundscape
**Council consensus: 3/4 models (ChatGPT, Claude, Grok)**

Layer the audio for immersion.

**Tasks:**
1. Train horn upgrade: proper two-tone horn at stations (frequency sweep)
2. Crossing bell: rapid ding-ding-ding at crossover pieces
3. Tunnel echo: reverb/delay on chug sound inside tunnel
4. Speed-synced chug rhythm (currently exists, refine timing)
5. Volume slider in settings area
6. Sound state icon: 🔊 → 🔉 → 🔇 (cycle on click)
7. All sounds synthesized via Web Audio (no external files)

**Acceptance criteria:**
- Horn sounds satisfying at stations
- Crossing bell audible at crossovers
- Tunnel modifies chug sound
- Volume slider controls all audio
- Mute silences everything
- No audio glitches

---

#### Day 14 — Keyboard Shortcuts + Undo/Redo Polish
**Council consensus: 2/4 models (Claude, Gemini)**

Power user features for dad.

**Tasks:**
1. `Space` = Play/Stop
2. `R` = Random track
3. `Z` / `Ctrl+Z` = Undo
4. `Shift+Z` / `Ctrl+Shift+Z` = Redo (new!)
5. `1-6` = Quick select track type
6. `Delete` = Remove selected/hovered piece
7. `N` = Night mode toggle
8. Small "⌨️" button showing keyboard shortcuts overlay
9. Redo stack: mirror undo architecture, clear on new action

**Acceptance criteria:**
- All shortcuts work
- Redo correctly reverses undo operations
- Shortcuts overlay shows all bindings
- No conflicts with browser defaults
- Only active when not in a modal/input

---

### Week 3: Modes & Mobile (Days 15–21)

The sandbox is polished. Week 3 adds structured play and ensures mobile is first-class.

---

#### Day 15 — Challenge Puzzles (Set 1)
**Council consensus: 4/4 models — top request**

**Tasks:**
1. 🧩 Puzzles button in controls opens puzzle select overlay
2. 5 puzzles with increasing difficulty:
   - "First Loop" — 4 pre-placed curves, add 4 straights to complete
   - "Bridge Over Water" — Cross a river using bridge pieces
   - "Figure Eight" — Create figure-8 using crossover (limited pieces)
   - "Tunnel Run" — Route through 2 tunnels around obstacles
   - "Grand Station" — Connect 3 stations in one loop
3. Locked cells (pre-placed pieces can't be moved, subtle lock icon)
4. Limited palette (count badges on available pieces)
5. "Check" button validates solution

**Acceptance criteria:**
- All 5 puzzles are solvable
- Locked pieces can't be moved or removed
- Limited palette enforced correctly
- Check button accurately validates
- "Back to Sandbox" button returns to freeform

---

#### Day 16 — Puzzle Star Rating + 5 More Puzzles
**Tasks:**
1. Star rating: ⭐ = solved, ⭐⭐ = under par pieces, ⭐⭐⭐ = optimal
2. Completion saved to localStorage
3. Puzzle select shows stars earned per puzzle
4. 5 more puzzles (total: 10):
   - "Switchyard" — Use T-junctions to route train to correct station
   - "Speed Run" — Use speed signs to accelerate through long track
   - "Cow Pasture" — Build loop that passes all 4 cows
   - "Night Express" — Build in night mode, train has only headlight
   - "Multi-Train" — Route 2 trains without collision

**Acceptance criteria:**
- Star rating works correctly for all 10 puzzles
- Progress persists across refreshes
- New puzzles solvable and fun
- Difficulty ramps appropriately

---

#### Day 17 — Mobile Touch Overhaul
**Council consensus: 4/4 models**

**Tasks:**
1. Detect portrait orientation on screens < 768px
2. Move palette to collapsible bottom drawer (horizontal scroll strip)
3. Palette pieces: 72px touch targets on mobile (up from 54px)
4. Grid fills available space above drawer
5. Larger control buttons on mobile (48px minimum)
6. Prevent accidental page zoom/scroll (touch-action: none on grid)
7. Haptic feedback: `navigator.vibrate(10)` on place, `vibrate([5,5,5])` on remove

**Acceptance criteria:**
- Game fills screen on iPhone SE (375px)
- No horizontal scroll
- Palette accessible on portrait
- Can build and play full layout on mobile
- Haptic feedback on supported devices

---

#### Day 18 — Pinch-to-Zoom + Pan
**Council consensus: 3/4 models**

**Tasks:**
1. Pinch-to-zoom on grid area (CSS transform: scale)
2. Zoom range: 0.5x to 2.0x
3. Two-finger drag to pan (translate)
4. Double-tap to reset to 1:1
5. Mouse wheel zoom on desktop
6. Zoom level indicator in corner
7. Boundaries: can't pan grid off-screen

**Acceptance criteria:**
- Pinch zoom works on iPad/iPhone
- Mouse wheel zoom on desktop
- Pan works with two fingers / middle-mouse
- Double-tap resets zoom
- Grid stays within viewport bounds

---

#### Day 19 — More Scenery + Expanded Palette
**Tasks:**
1. New scenery: 🌻 Flowers, 🐑 Sheep, 🐴 Horse, 🦆 Duck, 👨‍👩‍👦 People
2. Scenery palette: scrollable or categorized (Tracks | Scenery | Special)
3. Each new scenery has a subtle interaction (duck quacks, sheep baas when train passes)
4. Random generator uses expanded scenery pool
5. All new scenery works in day and night modes

**Acceptance criteria:**
- All new scenery items draggable and placeable
- Sound interactions for each animal
- Random generator places varied scenery
- Palette is organized and not cluttered

---

#### Day 20 — Terrain Biomes
**Council consensus: 2/4 models (Gemini, Grok)**

**Tasks:**
1. Biome selector button (cycles through themes)
2. "Spring" (default): green grass, current palette
3. "Winter": white ground, snow-covered trees 🌲❄️, frozen water
4. "Desert": tan/sand ground, cacti 🌵, no water
5. "Autumn": orange-brown grass, colorful trees 🍂
6. Just CSS/emoji swaps — minimal effort, high visual impact
7. Biome affects random generator scenery choices
8. Preference saved to localStorage

**Acceptance criteria:**
- 4 biomes look visually distinct
- All track pieces work in all biomes
- Random generator respects biome
- Toggle is smooth (CSS transition)
- Preference persists

---

#### Day 21 — Tutorial Overlay
**Council consensus: 2/4 models (ChatGPT, Claude)**

**Tasks:**
1. First-visit detection (localStorage flag)
2. 3-step animated tutorial:
   - Step 1: "Drag a track piece!" (arrow from palette to grid, pulse animation)
   - Step 2: "Click to rotate!" (piece rotation animation)
   - Step 3: "Press ▶ to go!" (play button highlight)
3. "Skip" button always visible
4. Semi-transparent overlay (doesn't block the actual UI behind it)
5. Never shows again after completion or skip
6. Manual re-trigger via "❓" help button

**Acceptance criteria:**
- Tutorial shows on first visit only
- 3 steps are clear and animated
- Skip works at any step
- ❓ button re-triggers tutorial
- Tutorial completion saved to localStorage

---

### Week 4: Social & Polish (Days 22–28)

The game is feature-complete. Week 4 adds shareability, personalization, and final polish.

---

#### Day 22 — Screenshot & Download
**Tasks:**
1. 📸 button in controls bar
2. Capture grid (without UI chrome) as PNG
3. Use OffscreenCanvas or html2canvas to render grid
4. Include all visual elements (scenery, tracks, train, effects)
5. Download as "train-tracks-YYYY-MM-DD.png"
6. Also: "📋 Copy" button (navigator.clipboard.write)
7. Toast: "📸 Saved!" or "📋 Copied!"

**Acceptance criteria:**
- Clean PNG of grid produced
- Download works in Chrome/Firefox/Safari
- Clipboard copy works
- All visual elements captured
- No UI chrome in screenshot

---

#### Day 23 — Share Link
**Tasks:**
1. Encode grid state compactly: type (4 bits) + rotation (2 bits) = 6 bits per cell
2. Base64 encode → URL hash fragment
3. "🔗 Copy Link" button
4. On page load: detect hash → decode → load layout
5. Share links work in new browser/incognito
6. Toast: "🔗 Link copied!"

**Acceptance criteria:**
- Complex layouts survive encode/decode
- Share link loads identical layout in new browser
- URL stays reasonably short (< 500 chars for typical layout)
- Backwards compatible (pages without hash still load normally)

---

#### Day 24 — Train Customization
**Tasks:**
1. Click palette train to cycle colors: Red, Blue, Green, Yellow, Purple
2. SVG fill colors update dynamically
3. Each placed train keeps its chosen color
4. Color selector: small color dots below train in palette
5. Multiple trains can be different colors

**Acceptance criteria:**
- 5 train colors available
- Color persists after placement
- Multiple trains can be different colors
- Colors visible in both day and night modes
- Color choice saved with layout

---

#### Day 25 — Passenger Delivery
**Council consensus: 2/4 models (ChatGPT, Claude)**

**Tasks:**
1. Stations generate tiny passengers (emoji 🧑) on a timer (every 10s)
2. Max 3 passengers per station
3. Train picks up passengers when arriving at station (boarding sound)
4. Passengers drop off at next station (disembark sound + confetti)
5. Counter: "🧑 Delivered: 12" in the controls area
6. High score saved to localStorage
7. Optional — doesn't interfere with sandbox (togglable)

**Acceptance criteria:**
- Passengers appear at stations
- Train picks up and delivers
- Counter tracks deliveries
- Satisfying sounds on board/disembark
- Can be toggled off for pure sandbox play

---

#### Day 26 — Progression & Unlocks
**Tasks:**
1. Track play stats: tracks placed, trains run, loops completed, passengers delivered
2. Unlock milestones: "Place 50 tracks" → unlock Tunnel piece
3. 8-10 unlock milestones for special pieces and scenery
4. Unlock notification: "🎉 New piece unlocked: Tunnel!"
5. Stats page (modal): show all stats and unlock progress
6. All pieces available from start in puzzle mode (unlocks = sandbox only)
7. Override: long-press lock icon to unlock everything (for impatient dads)

**Acceptance criteria:**
- Stats track accurately
- Unlocks trigger at correct thresholds
- Notification appears on unlock
- Stats page shows all progress
- Override unlocks everything
- Puzzle mode unaffected

---

#### Day 27 — Ambient Background Music
**Tasks:**
1. Gentle, looping toy-train melody (Web Audio API synthesis)
2. Pentatonic scale, music-box timbre, 16-bar loop
3. Separate music volume slider (independent of SFX)
4. Music starts on first user interaction (browser autoplay policy)
5. Slightly more upbeat variation during play state
6. Night mode: slower, softer variation
7. Default: off (respects users who prefer silence)

**Acceptance criteria:**
- Pleasant, non-repetitive-sounding loop
- Music and SFX volumes independent
- Respects autoplay policy
- Variations for play/idle/night states
- Default off, saved to localStorage

---

#### Day 28 — Accessibility + Final Polish
**Tasks:**
1. ARIA labels on all grid cells, palette items, and buttons
2. Keyboard navigation: Tab through palette, Arrow keys to move grid focus, Enter to place
3. Connection dots: add shape difference (circle vs triangle) for colorblind users
4. High-contrast mode toggle (stronger borders, bolder colors)
5. Fullscreen mode button (requestFullscreen API)
6. Reduce motion preference: disable particles and animations for `prefers-reduced-motion`
7. Final bug sweep across all features

**Acceptance criteria:**
- Screen reader can describe game state
- Keyboard-only play is possible
- Colorblind users can distinguish connected/disconnected
- High-contrast mode works
- Fullscreen works on desktop and mobile
- Reduced motion disables animations

---

## Architecture Notes

### Factory Pipeline
Each day runs through: **PM → Builder → QA** (sequential in one cron session)

### File Responsibilities
- `FACTORY_STATE.json` — Current day, phase, progress tracking
- `PRD.md` — Product requirements (static reference)
- `ROADMAP.md` — Feature schedule + specs (this file)
- `TEST_MATRIX.md` — Cumulative test checklist (grows daily)
- `BUGS.md` — Bug tracking (should be empty if QA does its job)
- `LESSONS_LEARNED.md` — Cross-run knowledge base
- `specs/` — PM-generated specs per day
- `build-reports/` — Builder output per day
- `qa-reports/` — QA output per day

### Priority Rules
1. QA fixes everything. No time limits. Ship quality.
2. Working product > new features. If the game is broken, fix it first.
3. Builder checks BUGS.md on startup — address any open bugs before new feature.
4. LESSONS_LEARNED.md is mandatory reading for all roles.
