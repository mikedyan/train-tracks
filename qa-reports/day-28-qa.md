# Day 28 QA Report — Accessibility + Final Polish

**Date:** 2026-04-17
**QA Agent:** Factory Agent

## Summary
Day 28 adds comprehensive accessibility features: ARIA labels, keyboard grid navigation, colorblind-friendly connection dots, high-contrast mode, fullscreen support, and reduced motion preference. All features verified, 3 bugs found and fixed.

## Bugs Found & Fixed

### QA-FIX-1: handleGridKeyAction missing play-state guard
- **Severity:** Medium (functional — could modify grid during play)
- **Root cause:** `handleGridKeyAction()` didn't check `state.playing` before allowing placement/rotation
- **Fix:** Added `if (state.playing) return;` at top of function

### QA-FIX-2: F and A shortcuts blocked during play
- **Severity:** Low (UX — accessibility toggles should work anytime)
- **Root cause:** Fullscreen (F) and High-contrast (A) shortcuts were placed after `if (state.playing) return;` in handleKeyDown
- **Fix:** Moved both shortcut handlers before the playing guard

### QA-FIX-3: Stale grid focus indicator on mouse use
- **Severity:** Low (cosmetic — blue outline persists after switching to mouse)
- **Root cause:** `onGridDown` didn't clear the keyboard focus indicator
- **Fix:** Added `clearGridFocus()` call at start of `onGridDown`

## Acceptance Criteria Verification

### T1: ARIA Labels ✅
- ✅ Grid cells have `role="gridcell"` and dynamic `aria-label`
- ✅ All 22 palette pieces have `role="button"`, `aria-label`, `tabindex="0"` (sidebar + mobile)
- ✅ All control buttons have `aria-label` attributes
- ✅ Labels update via `updateCellAriaLabel()` on every `renderCell()` call

### T2: Keyboard Navigation ✅
- ✅ Arrow keys move grid focus indicator
- ✅ `.grid-focus` class visible in day, night, and high-contrast modes
- ✅ Enter places selectedTool at focused cell with auto-connect
- ✅ Enter rotates existing track pieces
- ✅ Placement blocked during play (QA fix applied)
- ✅ Focus cleared on mouse click (QA fix applied)
- ✅ Palette pieces have `:focus-visible` styling

### T3: Colorblind Connection Dots ✅
- ✅ Connected = circle (border-radius: 50%)
- ✅ Disconnected = diamond (border-radius: 1px, rotate(45deg), with border)
- ✅ Shapes distinguishable without color

### T4: High-Contrast Mode ✅
- ✅ Toggle button (♿) works
- ✅ 2px cell borders, larger 9px dots, boosted SVG contrast
- ✅ Night mode variant (white borders instead of dark)
- ✅ Persists in localStorage
- ✅ Works with all 4 biomes
- ✅ A shortcut works during play (QA fix applied)

### T5: Fullscreen Mode ✅
- ✅ ⛶ button triggers fullscreen
- ✅ Layout recalculates on fullscreen change (100ms delay)
- ✅ Button text toggles ⛶ ↔ 🔲
- ✅ F shortcut works during play (QA fix applied)

### T6: Reduced Motion ✅
- ✅ CSS `@media (prefers-reduced-motion: reduce)` disables all decorative animations
- ✅ JS `prefersReducedMotion()` gates smoke, chimney, confetti spawning
- ✅ Functional UI transitions preserved

### T7: Final Polish ✅
- ✅ Shortcuts modal updated with F, A, Arrows, Enter
- ✅ New "Grid Navigation" section in shortcuts overlay
- ✅ JS parse: clean
- ✅ HTML balance: all tags balanced
- ✅ No duplicate code blocks
- ✅ All new functions have exactly 1 definition

## Regression Check
- ✅ All existing keyboard shortcuts verified present
- ✅ Escape handler chain covers all modals
- ✅ localStorage keys consistent with existing patterns

## Technical Metrics
- Lines added: ~280 (CSS + JS + HTML)
- New functions: 9 (updateCellAriaLabel, setGridFocus, clearGridFocus, handleGridKeyAction, prefersReducedMotion, toggleHighContrast, restoreHighContrast, toggleFullscreen, onFullscreenChange)
- Total file size: 9,079 lines
