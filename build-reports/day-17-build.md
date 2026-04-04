# Day 17 Build Report — Mobile Touch Overhaul

## Bug Fixes
- **BUG-013 (FIXED):** Removed 5 duplicate copies of the "Quick-select tool" block in `onGridDown` (98 lines of duplicated code). Only 1 copy remains.

## Features Built

### 1. Mobile Detection
- Added `isMobileLayout()` function that checks `window.innerWidth <= 768`
- calculateSize() now has separate mobile/desktop branches
- Mobile: grid cells size 32-60px, accounts for bottom drawer height
- Desktop: unchanged behavior

### 2. Bottom Drawer Palette
- New HTML element `#mobile-drawer` with all palette pieces in horizontal scroll
- Collapsible via toggle handle (`▲ Pieces` / `▼ Pieces`)
- Section labels: Tracks, Trains, Cars, Scenery
- Smooth CSS transition for collapse/expand
- Hidden by default; shown only via `@media (max-width: 768px)`
- Palette dividers render as vertical bars in horizontal layout
- Auto-collapses during play state

### 3. Mobile CSS Layout
- Desktop sidebar hidden on mobile (`display: none !important`)
- Sidebar toggle button hidden on mobile
- `#app` switches to `flex-direction: column` 
- `#main` gets bottom padding for drawer height
- Controls bar wraps nicely with compact button sizing
- Toast and puzzle HUD repositioned above drawer
- Trash zone positioned above drawer
- Modal dialogs sized to 95vw
- Speed/volume sliders compact

### 4. Touch Target Sizing
- Drawer palette pieces: 56px (comfortable touch target)
- Control buttons: min-height 40px
- Compact font sizes for mobile controls

### 5. Haptic Feedback
- `hapticPlace()` — `navigator.vibrate(10)` on track/scenery placement
- `hapticRemove()` — `navigator.vibrate([5,5,5])` on removal
- Graceful fallback: try/catch guards for unsupported devices

### 6. Anti-Zoom
- Body already had `touch-action: none` and `user-scalable=no` viewport meta
- No additional changes needed — existing setup prevents accidental zoom

### 7. Sidebar Toggle Integration
- `toggleSidebar()` on mobile now delegates to `toggleMobileDrawer()`
- Tab keyboard shortcut works on both layouts

## Code Changes
- Replaced single `@media (max-width: 768px)` with two blocks:
  - `@media (max-width: 900px) and (min-width: 769px)` — desktop small
  - `@media (max-width: 768px)` — full mobile layout
- Added ~150 lines of mobile CSS
- Added ~40 lines of mobile JS (isMobileLayout, calculateSize mobile branch, drawer toggle, haptics)
- Added mobile drawer HTML (~30 lines)
- Removed 98 lines of duplicated quick-select code (BUG-013)
