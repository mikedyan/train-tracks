# 🚂 Train Tracks — Phase 2 Roadmap (Days 15-44)

**Phase Start:** Day 15  
**Philosophy:** Fun first. Every day should ship something a kid would notice and love.  
**Priority Order:** Fix critical bugs → Core delight → Goals/Progression → New content → Polish

---

## Day 15 — Critical Bug Fix: Deduplicate Code & Restore Functionality

**Summary:** Remove all duplicate code blocks so the game actually runs.

**Items:**
1. Remove 5 duplicate "KEYBOARD SHORTCUTS + QUICK SELECT" sections (keep only one `let selectedTool`, `let hoveredCell`, `TOOL_KEY_MAP`, `selectTool`, `clearSelectedTool`, `initHoverTracking`, `handleKeyDown`)
2. Remove 5 duplicate "SHORTCUTS MODAL" sections (keep one `openShortcutsModal`, `closeShortcutsModal`, `closeShortcutsModalOutside`)
3. Remove 5 duplicate `#shortcuts-overlay` HTML blocks (keep one)
4. Remove 5 duplicate CSS blocks for `.palette-selected`, `#shortcuts-overlay`, `#shortcuts-modal`, `.shortcut-row`, `.shortcut-key`, `.shortcut-desc`, `.shortcut-section`
5. Fix `onGridDown` to only have the `selectedTool` click-to-place logic once (currently duplicated 6 times inside the function body)
6. Verify game loads and all features work in Chrome, Safari, Firefox
7. Verify deployed version at mikedyan.github.io works after push
8. Run through full test: place tracks, place train, play, stop, save, load, night mode, random generate
9. File size should drop from ~124KB to ~65-70KB
10. Add `console.log('🚂 Train Tracks v0.14 loaded')` in init() for easier debugging

## Day 16 — Welcome Tutorial Overlay

**Summary:** 3-step animated tutorial that appears on first visit, teaching drag-place-play.

**Items:**
1. Create a semi-transparent overlay with 3 tutorial steps
2. Step 1: "Drag a track piece to the board!" with animated arrow pointing from palette to grid
3. Step 2: "Place a train on the track!" with arrow from train palette to a track cell
4. Step 3: "Press Play and watch it go!" with arrow to the Play button
5. Each step advances on click/tap with smooth transition
6. "Skip Tutorial" button visible at all times
7. Store `tutorialComplete` flag in localStorage so it only shows once
8. "?" button in header re-triggers tutorial anytime
9. Tutorial adapts to mobile (touch language) vs desktop (drag language)
10. Confetti burst when tutorial completes with "Let's build!" toast

## Day 17 — Resizable Grid (Small / Medium / Large)

**Summary:** Let users choose grid size for small quick builds or sprawling layouts.

**Items:**
1. Add grid size selector: Small (8×5), Medium (12×8, current default), Large (16×10)
2. Grid size buttons in header or a dropdown near the title
3. Changing grid size offers to keep current layout (centered) or clear
4. `calculateSize()` adapts cell size to fit the chosen grid in the viewport
5. Save/Load preserves grid size alongside grid data
6. Random generator adapts algorithm to grid dimensions
7. Auto-save includes grid size
8. Keyboard shortcut: `G` cycles through grid sizes
9. Smooth animation when grid resizes (scale transition)
10. Large grid enables pan/scroll if cells get too small (minimum cell size: 35px)

## Day 18 — Horn Button & Interactive Sound During Play

**Summary:** Big satisfying horn button kids can press during play, plus clickable cows.

**Items:**
1. Add floating "🎺 HONK!" button visible during play mode (big, colorful, impossible to miss)
2. Pressing it plays a loud, satisfying train horn (different from the auto-whistle)
3. Horn button has a press animation (scale bounce) and brief visual flash
4. Clicking a cow during play triggers a moo sound with the cow doing a jump animation
5. Clicking a tree during play makes birds fly out (small particle emoji "🐦" rising)
6. Horn button can be held down for extended horn (up to 2 seconds)
7. Add haptic feedback on mobile (navigator.vibrate) for horn press
8. Horn sound has slight Doppler variation based on nearest train speed
9. Keyboard shortcut: `H` or `Enter` for horn during play
10. Horn creates a visible "sound wave" ring emanating from the nearest train

## Day 19 — Station Arrival Celebrations

**Summary:** Trains stopping briefly at stations with visible passenger activity.

**Items:**
1. Trains slow down and pause for 1.5 seconds when entering a station cell
2. During pause, show tiny emoji passengers (👤) appearing/disappearing at the platform
3. Station pause shows a "Arriving at Station!" toast with a ding-dong sound
4. Passenger count badge on station: "👤 ×3" incrementing with each visit
5. Different station visit counts trigger celebrations (5 visits = confetti, 10 = fanfare)
6. Station doors animate (open/close) during passenger boarding
7. Speed slider still affects the pause duration proportionally
8. Multiple trains can't occupy the same station simultaneously (queue system)
9. Station statistics persist in save data
10. Station plays a unique 2-note jingle (re-use and enhance existing `SFX.station`)

## Day 20 — Challenge Mode (Track Puzzles)

**Summary:** Pre-built puzzles where players must connect points with limited track pieces.

**Items:**
1. New "🧩 Challenges" button in controls area
2. Challenge overlay shows a list of 10 starter puzzles with difficulty stars (1-3)
3. Each puzzle defines: fixed scenery/stations, required connections, available pieces
4. Player must connect Station A to Station B using only the given pieces
5. Puzzle grid renders with locked cells (can't modify) shown in a different color
6. "Check Solution" button validates all required connections are made
7. Star rating: ★ = solved, ★★ = solved with pieces left over, ★★★ = optimal solution
8. Completion unlocks next puzzle + triggers confetti celebration
9. Progress saved to localStorage
10. "Back to Sandbox" button to return to free play mode

## Day 21 — Animated Scenery Reactions

**Summary:** Animals and scenery react to passing trains — cows flee, birds scatter, trees shake.

**Items:**
1. Cows within 1 cell of a passing train run away (brief translate animation away from track)
2. Cows return to position after train passes (2-second delay, slow drift back)
3. Trees adjacent to a passing train shake more vigorously (amplitude doubles briefly)
4. Birds (🐦) scatter from trees when train passes adjacent cell (3-4 particles rising)
5. Houses' chimney smoke increases when train passes (more particles, faster)
6. Ducks on water paddle away from the nearest track cell when train is near
7. All reactions have a cooldown per cell (3 seconds) to avoid spam
8. Reactions scale with train speed (faster = more dramatic)
9. Night mode: house windows flicker when train passes (simulating people looking out)
10. Sound effects accompany reactions: birds chirping, cow startled moo (higher pitch)

## Day 22 — Track Drawing Mode (Click & Drag to Paint)

**Summary:** Hold and drag across cells to paint a continuous track path — the #1 UX improvement.

**Items:**
1. When a track tool is selected (1-7 keys), clicking and dragging across cells places tracks continuously
2. Auto-detect whether to place straight or curve based on drag direction changes
3. If dragging straight horizontally → horizontal straight pieces; vertically → vertical straight pieces
4. If drag changes direction → automatically insert a curve piece at the turn
5. Ghost preview shows the entire pending path while dragging
6. Release to confirm placement (all pieces placed as single undo-able action)
7. Path validates connectivity in real-time (green preview = valid, red = invalid)
8. Maximum drag path: 20 cells (prevents accidental massive placements)
9. Sound: rapid "build build build" sounds as each cell is previewed
10. Works on mobile with touch-drag gesture

## Day 23 — Cargo Delivery System

**Summary:** Pick up cargo at one station, deliver to another. First real "goal" in sandbox mode.

**Items:**
1. Stations can be designated as "pickup" (📦) or "delivery" (🏠) with a click toggle
2. When a freight car passes a pickup station, it visually "loads" (color change + particle burst)
3. When a loaded freight car reaches a delivery station, cargo is "delivered" (confetti + coin sound)
4. Running delivery counter in the header: "📦 Deliveries: 5"
5. Milestone celebrations: 5 deliveries = small confetti, 25 = big confetti, 100 = fireworks
6. Passenger cars pick up/drop off passengers at any station (counter per car)
7. Cargo types: boxes (📦), mail (✉️), food (🍎) — randomly assigned to pickup stations
8. Delivery animation: package emoji flies from car to station platform
9. Sound: cash register "cha-ching" on successful delivery
10. Delivery stats persist in save data; shown in a "📊 Stats" popup

## Day 24 — Weather System

**Summary:** Rain, snow, and sunshine with visual/audio effects that change the vibe.

**Items:**
1. Weather button cycles: ☀️ Sunny → 🌧️ Rain → ❄️ Snow → ☀️ Sunny
2. Rain: CSS animated droplets falling across the grid (30-50 small blue lines)
3. Rain: puddle reflections appear on grass tiles (subtle blue shimmer)
4. Rain: water tiles have stronger wave animation
5. Rain: ambient rain sound loop using filtered noise (Web Audio)
6. Snow: white particle dots falling gently across the grid (CSS animation)
7. Snow: grass tiles gradually turn white over 10 seconds (CSS transition)
8. Snow: train moves 20% slower (snow on tracks!)
9. Weather persists through save/load
10. Weather transitions smoothly (5-second crossfade between states)

## Day 25 — Train Customization & Naming

**Summary:** Name your trains and pick their color from a wider palette.

**Items:**
1. Click a stopped train to open a "Train Info" popup
2. Editable name field (default: "Red Express", "Blue Bullet", "Green Local")
3. Train name shows as a tooltip on hover and in the car-count badge
4. Color picker with 8 colors: red, blue, green, yellow, purple, orange, pink, black
5. Custom color changes both the train SVG and the palette indicator
6. Train speed override: each train can have its own speed multiplier (0.5x - 2x)
7. Train info popup shows stats: distance traveled, stations visited, deliveries made
8. "Reverse" button: flip train direction without moving it
9. Name appears above train during play mode (small floating label)
10. All customization saved in state and persisted

## Day 26 — Signal Towers & Traffic Lights

**Summary:** New track piece that controls train flow — stop/go signals at intersections.

**Items:**
1. New palette piece: Signal (🚦) — places a signal tower on any track cell
2. Signal has two states: green (go) and red (stop), toggled by clicking during play
3. Trains approaching a red signal slow down and stop before the cell
4. Train waiting at red signal plays an idle animation (slight rocking)
5. Signal changes: visual transition (green→yellow→red, 0.3s each)
6. Signal click sound: mechanical "clank" (similar to switch toggle)
7. Auto-signal mode: signals cycle automatically every 5 seconds
8. Multiple signals on a layout enable traffic management puzzles
9. Keyboard shortcut: clicking signal while holding Shift sets it to auto-cycle
10. Trains resume with a whistle when signal turns green

## Day 27 — Terrain: Hills & Elevation

**Summary:** Add elevation to the grid — hills that trains climb over with speed changes.

**Items:**
1. New palette piece: Hill (⛰️) — an elevated terrain tile that tracks can cross
2. Hill tiles render with a raised 3D-perspective effect (darker shadow, lighter top)
3. Trains slow down going uphill (0.7x speed) and speed up going downhill (1.3x speed)
4. Uphill: train tilts slightly (3° angle) and smoke increases
5. Downhill: train tilts the other way, less smoke, slight acceleration sound
6. Hills adjacent to tunnels create a natural mountain range visual
7. Hill-to-flat transitions show a gentle slope in the SVG
8. Random generator can include hill sections
9. Hill cells have a subtle height shadow cast on adjacent grass cells
10. Challenge puzzles can use hills as constraints (limited uphill pieces)

## Day 28 — Share & Export System

**Summary:** Export your layout as a shareable URL or downloadable image.

**Items:**
1. "📤 Share" button in controls area
2. Serialize layout to compact base64 string appended as URL hash
3. Loading the URL auto-imports the layout (with "Someone shared a track!" toast)
4. "📸 Screenshot" button: renders grid to canvas and downloads as PNG
5. Screenshot includes train positions, scenery, and night/day mode
6. "Copy Link" button with clipboard API + success toast
7. Shared links work without any server — purely client-side
8. Import validation: reject corrupt/tampered share strings gracefully
9. Optional: QR code generation for the share URL (using a tiny inline QR library)
10. Share modal shows a preview thumbnail of the layout being shared

## Day 29 — Turntable & Roundhouse

**Summary:** New track piece that rotates trains 90°/180° — enabling complex track designs.

**Items:**
1. New palette piece: Turntable — a circular rotating platform that redirects trains
2. Turntable connects to all 4 directions (like a crossover) but actively rotates
3. When a train enters, the turntable rotates to the designated exit (animated spin)
4. Click turntable during play to change its exit direction (cycles N→E→S→W)
5. Turntable SVG: circular platform with visible rails and rotation mechanism
6. Rotation animation: 0.5 second spin with mechanical sound effect
7. Train pauses on turntable during rotation (visible on the spinning platform)
8. Turntable state (current direction) saved and restored
9. Turntable can be set to "auto" mode — alternates exits each time a train arrives
10. Random generator occasionally includes turntables in complex layouts

## Day 30 — Multiple Sound Themes

**Summary:** Switchable audio themes — Steam, Diesel, Bullet Train, and a silly mode.

**Items:**
1. Sound theme selector in settings: Steam (default), Diesel, Bullet, Silly
2. Steam: current sounds (chug-chug, whistle) — already implemented
3. Diesel: deeper engine rumble, air horn, mechanical brake sounds
4. Bullet: electric hum, pneumatic doors at stations, high-pitched whistle
5. Silly: cartoon boings, slide whistles, rubber duck squeaks, rim shots on crashes
6. Each theme changes: chug sound, whistle/horn, station arrival, crash, place/remove
7. Sound theme persists in localStorage
8. Smooth crossfade when switching themes during play
9. Theme preview: clicking a theme plays a short sample before applying
10. Silly mode also changes toast messages to be extra goofy ("BONKERS CRASH!" etc.)

## Day 31 — Seasons & Time Progression

**Summary:** Automated day/night cycle with seasonal visual changes.

**Items:**
1. "Auto Cycle" toggle that transitions day→sunset→night→sunrise every 30 seconds
2. Sunset mode: orange/pink sky gradient, warm shadows, golden hour lighting
3. Sunrise mode: pale blue/pink gradient, dew sparkle on grass cells
4. Spring: flowers appear on grass tiles (small colored dots), birds more frequent
5. Summer: brighter greens, sun glare effect on water
6. Autumn: trees change to 🍂 orange/brown, leaves particle effect on wind
7. Winter: snow on ground, frozen water (blue-white), bare trees
8. Season selector button or auto-cycle through seasons (each 2 minutes)
9. Season affects weather: winter = snow default, spring = rain more likely
10. Season-appropriate ambient sounds: crickets in summer night, wind in winter

## Day 32 — Expandable Grid & Pan/Zoom

**Summary:** Grid expands as you build near edges; pinch-to-zoom on mobile.

**Items:**
1. When player places a piece on an edge cell, grid automatically adds a row/column on that side
2. Maximum expanded grid: 24×16 (4x the original area)
3. When grid exceeds viewport, enable click-drag panning (hold middle mouse or two-finger touch)
4. Pinch-to-zoom gesture on mobile (0.5x to 2x zoom range)
5. Zoom controls: "+" / "−" buttons and scroll wheel
6. Mini-map in corner showing full grid with current viewport highlighted
7. Auto-center on train during play (gentle camera follow, toggleable)
8. "Fit to screen" button: zoom/pan to show entire layout
9. Grid expansion is reversible (shrinks back when edge cells are cleared)
10. Pan/zoom state is NOT saved (always resets to centered view on load)

## Day 33 — Freight Yard & Switching Puzzles

**Summary:** Dedicated switching puzzle mode where you sort train cars using sidings.

**Items:**
1. "🔀 Switching Yard" mode accessible from challenges menu
2. Scenario: 5 colored freight cars must be sorted into correct order on a siding
3. Player controls switch junctions in real-time to route cars
4. Cars can be decoupled from train by clicking during play (click car → detach)
5. Decoupled cars coast to a stop after 2 cells (realistic momentum)
6. Re-coupling: train can back up into stopped cars to pick them up
7. 5 switching puzzles of increasing complexity
8. Timer and move counter for competitive scoring
9. "Hint" button shows optimal solution path (grayed out track highlighting)
10. Completion unlocks a special "Yard Master" badge shown in train info

## Day 34 — Ambient Music System

**Summary:** Procedural background music that responds to gameplay state.

**Items:**
1. Soft generative background music using Web Audio API (pentatonic scale, slow arpeggios)
2. Music intensity increases when trains are running (add bass, more notes)
3. Night mode: shift to minor key, slower tempo, softer dynamics
4. Music volume independent from SFX (separate slider)
5. Music layers: base melody + harmony + bass, each toggled by game state
6. Station visits add a brief melodic flourish
7. Crash: music briefly drops out then returns
8. "🎵" button toggles music on/off (separate from SFX mute)
9. Multiple music "moods": Peaceful, Adventurous, Silly (matches sound theme)
10. Music cross-fades smoothly between day/night and play/build modes

## Day 35 — River Crossings & Drawbridges

**Summary:** Rivers that block tracks and drawbridges that open/close for boats.

**Items:**
1. New terrain: River — a connected strip of water tiles that flows (directional wave animation)
2. Rivers are 1 cell wide and must be crossed with a bridge or drawbridge
3. New piece: Drawbridge — a bridge that opens to let boats pass
4. Drawbridge toggles open/closed by clicking (like a switch)
5. When drawbridge is open: trains stop and wait, small boat emoji passes through
6. When drawbridge closes: boat animation ends, train proceeds
7. Drawbridge open/close animation: bridge halves tilt up/down (0.8 second)
8. Sound: creaking mechanical sound for drawbridge, boat horn when boat passes
9. Random generator creates rivers with bridge crossings
10. Challenge puzzles can require timing drawbridge operations

## Day 36 — Achievements & Progression System

**Summary:** Persistent achievements that reward experimentation and mastery.

**Items:**
1. Achievement system with 20 achievements unlockable through play
2. "🏆 Achievements" button opens a grid of locked/unlocked badges
3. Starter achievements: "First Track", "First Loop", "Night Owl" (use night mode), "Speed Demon" (max speed)
4. Advanced: "Bridge Builder" (build 5 bridges), "Tunnel Vision" (3 tunnels in one layout), "Full House" (all 3 trains + cars)
5. Secret achievements: "Moo-ve Over" (pass 10 cows), "Duck Duck Train" (bridge over 5 ducks)
6. Achievement unlock: golden notification banner + achievement-specific sound + confetti
7. Achievement progress tracked persistently in localStorage
8. "🌟 New!" indicator on achievements button when new achievement unlocked
9. Each achievement has a fun description and emoji icon
10. Meta-achievement: "Completionist" for unlocking all others

## Day 37 — Scenery Expansion: Farms, Factories, Lakes

**Summary:** More scenery types for richer world-building.

**Items:**
1. New scenery: Farm (🌾) — wheat field with swaying grain animation
2. New scenery: Factory (🏭) — smokestack with heavier smoke (day), red glow (night)
3. New scenery: Lake — 2×2 water area with a dock and fishing boat
4. New scenery: Windmill (🏗️) — animated spinning blades
5. New scenery: Signal Post (🚩) — decorative crossing sign
6. Each new scenery has night mode variant
7. Factory reacts to train proximity: smoke increases, assembly sounds
8. Farm: harvest particles when train passes (golden grain sprinkle)
9. Scenery palette gets scroll or second column for expanded options
10. Random generator uses all new scenery types with appropriate density

## Day 38 — Mobile-First Controls Overhaul

**Summary:** Touch-optimized controls, gesture support, and responsive layout for phones.

**Items:**
1. Palette becomes a bottom drawer on screens < 768px (slide up to reveal)
2. Touch-drag with larger hit targets (72px minimum)
3. Double-tap cell to rotate piece (instead of single tap which conflicts with place)
4. Swipe-right from left edge to open palette; swipe-left to close
5. Floating action button (FAB) for Play/Stop — always accessible
6. Pinch-to-zoom on grid (uses CSS transform scale)
7. Long-press context menu: Rotate / Remove / Info (replaces right-click)
8. Haptic feedback on placement, rotation, and train start
9. Grid cells slightly larger on mobile (minimum 50px)
10. Test on iPhone SE, iPhone 15 Pro, iPad, Samsung Galaxy S24

## Day 39 — Train Racing Mode

**Summary:** Competitive mode: build a track for 2-3 trains and see which completes the loop first.

**Items:**
1. "🏁 Race!" button starts all trains simultaneously from their positions
2. Each train's lap counter displayed in the header (🔴 Laps: 2 / 🔵 Laps: 1 / 🟢 Laps: 0)
3. Race is 3 laps (configurable)
4. First train to complete 3 laps wins → victory fanfare + winner's confetti
5. "🏆 Red wins!" banner across the screen with celebration animation
6. Each train can have different speed (see Day 25 customization)
7. Race timer shows elapsed time
8. Photo finish: if trains are within 0.5 cells of each other → "PHOTO FINISH!" toast
9. Race results screen: place, time, top speed, stations visited
10. Race history saved in localStorage for bragging rights

## Day 40 — Scenario Builder / Level Editor

**Summary:** Create and save custom challenge puzzles to share with others.

**Items:**
1. "✏️ Create Puzzle" mode enters puzzle editor
2. Place fixed pieces that solvers can't move (rendered with a lock icon)
3. Define "start" and "goal" stations with colored markers
4. Set which piece types are available to the solver (piece budget)
5. Add hints: "Connect the two stations" text, suggested piece count
6. Test puzzle: instantly solve your own puzzle to validate it's solvable
7. Save puzzle to a slot (separate from sandbox saves)
8. Export puzzle as URL hash for sharing
9. Import puzzles from URL — "Someone shared a puzzle!" toast
10. Puzzle metadata: title, author name, difficulty rating

## Day 41 — Smoke & Particle System Upgrade

**Summary:** GPU-accelerated particle system for richer visual effects.

**Items:**
1. Refactor all particles (smoke, confetti, crash stars, dust) to use a unified particle engine
2. Particle engine uses CSS `will-change: transform` and composite-only properties
3. Double smoke density at no performance cost (fewer DOM elements via canvas rendering)
4. New particle types: sparks on curves (when train turns), steam puffs at stations
5. Fireworks effect for major celebrations (100+ particles, multi-color, gravity physics)
6. Snow and rain particles (from Day 24) integrated into unified system
7. Particle color palette adapts to night mode
8. Performance budget: cap at 100 active particles, recycle oldest
9. Particles respect tunnel visibility (hidden inside tunnels)
10. Profile on low-end devices (reduce particle count if FPS < 30)

## Day 42 — Sound Spatialization & Immersive Audio

**Summary:** Stereo panning based on train position and distance-based volume.

**Items:**
1. Train sounds pan left/right based on position in the grid (Web Audio StereoPanner)
2. Volume attenuates with distance from grid center (simulating listener perspective)
3. Multiple trains: each has its own audio panning, creating a spatial soundscape
4. Tunnel echo effect uses ConvolverNode with generated impulse response
5. Station announcements have a "PA system" filter (bandpass + slight distortion)
6. Cow moos come from the cow's grid position (spatial direction)
7. Crash sounds have reverb proportional to how many tiles are around (open field vs. dense)
8. Crossing bells have a repetitive stereo ringing pattern
9. Master audio compressor to prevent clipping with multiple trains + effects
10. Audio visualization: optional "sound waves" icon near active sound sources

## Day 43 — Community Gallery (Server-Optional)

**Summary:** Gallery of featured layouts that can be loaded and played.

**Items:**
1. "🌍 Gallery" button opens a curated list of pre-built layouts
2. Ship 10 hand-crafted showcase layouts in the HTML (compressed JSON data)
3. Each layout has: thumbnail, title, author, track count, train count
4. "Play" button loads a layout and automatically starts trains
5. "Copy to Sandbox" imports the layout for editing
6. Layouts sorted by category: Simple, Complex, Scenic, Racing, Puzzle
7. "Featured Layout of the Day" rotates through the 10 built-in layouts
8. Each layout has a short description: "A mountain railway with 3 tunnels and a lake"
9. Gallery renders thumbnails using the existing `renderThumbnail` function
10. Future: add a lightweight server endpoint for user-submitted layouts (optional)

## Day 44 — Performance Audit & Grand Polish

**Summary:** Final optimization pass, accessibility improvements, and delight details.

**Items:**
1. Performance audit: profile with Chrome DevTools, target 60fps with 3 trains + full scenery
2. Reduce DOM element count: virtualize off-screen cells if grid is large
3. Accessibility: ARIA labels on all interactive elements, keyboard-only navigation through palette
4. Accessibility: high-contrast mode option for colorblind users
5. Reduce file size: minify inline CSS/JS, remove all dead code
6. Add PWA manifest for "Add to Home Screen" on mobile (offline play!)
7. Add `<meta>` tags for social sharing (og:title, og:image, og:description)
8. Easter egg: Konami code (↑↑↓↓←→←→BA) spawns a golden train with rainbow smoke
9. Loading screen: brief train animation while fonts/page load (replaces flash of unstyled content)
10. Version number in footer: "Train Tracks v1.0 — Made with ❤️"

---

## 📊 Phase 2 Summary

| Week | Days | Theme | Key Deliverables |
|------|------|-------|-----------------|
| 1 | 15-18 | **Foundation** | Bug fix, tutorial, grid sizes, horn button |
| 2 | 19-22 | **Delight** | Station celebrations, challenges, scenery reactions, track drawing |
| 3 | 23-26 | **Depth** | Cargo delivery, weather, train customization, signals |
| 4 | 27-30 | **Expansion** | Hills, sharing, turntables, sound themes |
| 5 | 31-34 | **Immersion** | Seasons, pan/zoom, switching yard, ambient music |
| 6 | 35-38 | **World** | Drawbridges, achievements, new scenery, mobile UX |
| 7 | 39-42 | **Competition** | Racing, level editor, particle upgrade, spatial audio |
| 8 | 43-44 | **Polish** | Gallery, performance, accessibility, Easter eggs |

**Target:** Transform a promising sandbox into a game kids beg to play and adults find genuinely relaxing.
