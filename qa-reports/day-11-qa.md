# Day 11 QA Report — Tunnels

**Date:** 2026-03-27
**QA Agent:** Factory Orchestrator

## Acceptance Criteria Verification

| AC | Description | Status |
|----|-------------|--------|
| AC1 | Tunnel in palette, draggable and placeable | ✅ PASS — Added between Bridge and Station |
| AC2 | Connects N-S (r0) / E-W (r90) | ✅ PASS — BASE_CONNECTIONS = ['N','S'], rotatable |
| AC3 | Click to rotate works | ✅ PASS — Uses standard rotation logic |
| AC4 | Train fade/shrink in tunnel | ✅ PASS — Progressive opacity/scale via anim.progress |
| AC5 | Whoosh sounds on entry/exit | ✅ PASS — Bandpass-filtered noise, state-tracked |
| AC6 | Car staggered fade | ✅ PASS — Center-distance fade per car |
| AC7 | Night mode tunnel glow | ✅ PASS — CSS .has-tunnel filter |
| AC8 | Integration (save/load/undo/dots) | ✅ PASS — Standard grid piece serialization |
| AC9 | Random generator includes tunnels | ✅ PASS — 20% straight→tunnel conversion |
| AC10 | Both day and night modes | ✅ PASS — CSS custom properties + glow |

## Bugs Found & Fixed

1. **BUG-007** (Low): Car tunnel fade direction-dependent → Fixed with center-distance approach
2. **BUG-008** (Low): Headlight visible inside tunnel at night → Fixed with isInTunnel check
3. **BUG-009** (Low): placeTrainOnLoop skipped tunnel cells → Fixed with additional type check

## Code Quality Checks

- ✅ JavaScript syntax validates (zero parse errors)
- ✅ All critical functions present (renderTrainAtProgress, createTrackSVG, etc.)
- ✅ HTML structure intact
- ✅ New tunnel SVG case has proper `break` statement
- ✅ No orphaned DOM elements (tunnel CSS class removed on cell clear)
- ✅ Tunnel sound effects use proper Web Audio API patterns (consistent with existing SFX)
- ✅ anim.inTunnel state properly initialized in startPlay

## Regression Check

- ✅ getExitDir returns correct exits for tunnel (N→S, S→N, E→W, W→E)
- ✅ TRACK_TYPES order preserved (tunnel between bridge and station)
- ✅ Smoke particle suppression only when inTunnel=true
- ✅ Existing train animation unaffected (opacity/scale only applied when isInTunnel)
- ✅ Random generator tunnel conversion before animation loop (no timing issues)

## Status: SHIPPED ✅
