# Day 21 QA Report — Tutorial Overlay

## Date: 2026-04-09

## Acceptance Criteria Results

| ID | Criterion | Status |
|----|-----------|--------|
| AC1 | Tutorial shows on first visit | ✅ PASS |
| AC2 | 3 animated steps with highlights | ✅ PASS |
| AC3 | Step 1 highlights palette | ✅ PASS |
| AC4 | Step 2 shows rotation | ✅ PASS |
| AC5 | Step 3 highlights play button with pulse | ✅ PASS |
| AC6 | Skip button on every step | ✅ PASS |
| AC7 | Next/Done button | ✅ PASS |
| AC8 | localStorage persistence | ✅ PASS |
| AC9 | ❓ help button re-triggers | ✅ PASS |
| AC10 | TUTORIAL_KEY saved | ✅ PASS |
| AC11 | Desktop and mobile support | ✅ PASS |
| AC12 | Semi-transparent overlay | ✅ PASS |
| AC13 | Step indicator dots | ✅ PASS |
| AC14 | H keyboard shortcut | ✅ PASS |

## Bugs Found & Fixed

### QA-FIX-1: Escape key handler ordering
- **Issue**: Tutorial check was inserted after puzzle modal check in Escape handler. Since tutorial has higher z-index (400 vs 300), it should be checked first.
- **Fix**: Swapped lines so tutorial dismissal comes before puzzle modal check.
- **Severity**: Low (tutorial would still dismiss, just in wrong priority order)

## Regression Checks

- ✅ JavaScript syntax: zero parse errors
- ✅ HTML tag balance: 162 open divs / 162 close divs, 25 open buttons / 25 close buttons
- ✅ All 17+ core functions present (no duplicates, no missing)
- ✅ No duplicate code blocks from this build
- ✅ Night mode CSS variables unaffected
- ✅ Biome system unaffected
- ✅ Puzzle system unaffected
- ✅ Keyboard shortcuts maintain correct behavior
- ✅ Save/Load modal still accessible
- ✅ Zoom/Pan system unaffected

## New Lessons Learned
- 6 new lessons (LESSON-132 through LESSON-137)

## Summary
- **Status**: SHIPPED ✅
- **Bugs found**: 1 (ordering issue — fixed immediately)
- **Regressions**: 0
- **New test cases**: 35+ added to TEST_MATRIX.md
