# Train Tracks — Product Requirements Document

## 1. What Is It
A browser-based train track building game. Drag and drop track pieces onto a grid, connect them into loops, place a train, and watch it chug around. Think wooden Brio train set, but digital.

## 2. Target Audience
- **Primary:** A toddler (Mark, ~2 years old) and his dad (Mike) playing together on iPad
- **Secondary:** Anyone who wants a relaxing, creative sandbox toy

## 3. Current State (as of Mar 12, 2026)
Single-file HTML game (`index.html`, ~2200 lines). Deployed on GitHub Pages.

**Working features:**
- 8×6 grid with drag-and-drop placement
- Track pieces: Straight, Curve, T-junction, Crossover, Bridge, Station
- Scenery: Trees 🌲, Houses 🏠, Cows 🐄
- Train placement and animation (follows connected tracks)
- Click to rotate pieces
- Right-click or long-press to remove
- Connection dots (green = connected, red = open)
- Random track generator (3 algorithms: rect, wobbly, spiral)
- Speed slider (turtle to rabbit)
- Sound effects (Web Audio API, no files): place snap, rotation click, whistle, chug, station ding, crash
- Undo (50-deep stack)
- Single train enforcement

## 4. Tech Stack
- Single `index.html` file (HTML + CSS + JS, no build step)
- SVG track rendering
- Web Audio API for all sounds
- Pointer events (works on desktop and touch)
- Hosted on GitHub Pages (push to main → auto-deploy)

## 5. Design Principles
1. **Toddler-first:** Big touch targets, forgiving interactions, delightful feedback
2. **No frustration:** Auto-connect, smart snapping, clear visual feedback
3. **Alive world:** Animations, sounds, reactions — everything should feel living
4. **Dad-friendly depth:** Puzzles, optimization, keyboard shortcuts for power users
5. **Single file:** Keep it as one `index.html` for simplicity (no build pipeline)

## 6. Success Criteria
- Mark (toddler) can build a track and run the train with minimal help
- Mike (dad) finds it genuinely fun to play alongside
- Someone who discovers it shares it with friends
- Works flawlessly on iPad Safari
