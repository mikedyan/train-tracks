# Day 21 Build Report — Tutorial Overlay

## Date: 2026-04-09

## What Was Built

### Tutorial CSS (~105 lines)
- Full overlay with backdrop blur
- Tutorial bubble card with pop animation
- Emoji bounce animation for each step
- Step indicator dots with active state styling
- Next/Skip button styles
- Spotlight ring with cutout (box-shadow: 0 0 0 3000px technique)
- Animated arrows (bouncing right and down)
- Pulse ring animation for play button highlight
- Night mode variants for all elements
- Mobile responsive adjustments

### Tutorial HTML
- `#tutorial-overlay` with click handler (prevents dismiss on backdrop click)
- `#tutorial-bubble` card with dynamic content areas (emoji, title, desc, dots, actions)
- `#tutorial-spotlight` positioned div for cutout highlight
- `.tutorial-arrow` animated directional arrow
- `❓` help button added to controls bar (after biome button)

### Tutorial JavaScript (~170 lines)
- `TUTORIAL_KEY` localStorage constant
- `TUTORIAL_STEPS` array with 3 steps:
  1. **"Drag a Track Piece!"** — highlights sidebar (desktop) / drawer (mobile), arrow pointing right
  2. **"Click to Rotate!"** — highlights grid viewport, arrow pointing down
  3. **"Press ▶ to Go!"** — highlights play button with pulse animation
- `showTutorial()` — activates overlay, renders step 0
- `renderTutorialStep(n)` — updates bubble content, dots, button text, repositions spotlight/arrow
- `positionSpotlight(step)` — calculates target element rect, applies with padding
- `positionArrow(step)` — positions animated arrow near target
- `nextTutorialStep()` — advances or completes
- `skipTutorial()` / `completeTutorial()` — dismisses overlay, saves to localStorage
- `isTutorialDone()` / `markTutorialDone()` — localStorage read/write

### Integration
- `init()`: After restoration check, if not tutorial done AND not restored, show tutorial after 800ms delay
- Keyboard shortcut `H` — triggers `showTutorial()`
- Shortcuts modal — added "Show tutorial / H" row under Display section
- Mobile-aware: uses `mobileTargetSelector` for step 1 (drawer instead of sidebar)

## Files Modified
- `index.html` — CSS (105 lines), HTML (16 lines), JS (170 lines) + init integration

## Technical Decisions
- Used box-shadow cutout for spotlight instead of clip-path (simpler, better browser support)
- Tutorial bubble centered in overlay rather than positioned near target (more reliable across screen sizes)
- 800ms delay on auto-show prevents competing with initial toast
- Arrow positioned relative to spotlight target via getBoundingClientRect()
- Overlay does NOT dismiss on backdrop click (intentional — guides user through steps)
