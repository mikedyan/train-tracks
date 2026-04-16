# Day 27 QA Report — Ambient Background Music

**Date:** 2026-04-16
**QA Agent:** Factory Agent

## Code Review Results

### Structural Integrity
- ✅ JS parse check: Clean (no syntax errors)
- ✅ HTML tag balance: All div, button, span, script, style tags balanced
- ✅ No duplicate code blocks (all key identifiers appear exactly once)
- ✅ File size: 8797 lines (up from 8527, clean +270 line addition)

### Music Engine Review
- ✅ All 16 melody bars sum to exactly 4 beats each
- ✅ All note indices valid (0-4 or -1 for rest)
- ✅ Pentatonic scale frequencies correct (C5-A5 day, C4-A4 night)
- ✅ Look-ahead scheduling prevents gaps between bars
- ✅ Oscillators self-stop via `osc.stop()` — no memory leak risk
- ✅ `musicGainNode` routes through `masterGainNode` — master mute works

### Volume Control Independence
- ✅ `musicGainNode` → `masterGainNode` → `audioCtx.destination` chain
- ✅ SFX notes connect to `getMasterGain()` directly (separate path)
- ✅ `musicVolume` and `volumeLevel` are independent variables
- ✅ Separate localStorage keys for music vs SFX settings

### State Transitions
- ✅ `startPlay()` calls `updateMusicTempo()` — play state variation triggers
- ✅ `stopPlay()` calls `updateMusicTempo()` — idle state restoration
- ✅ `toggleNightMode()` calls `updateMusicTempo()` — night variation triggers
- ✅ Visibility API handler pauses/resumes music on tab change

### Tempo Logic Verification
| State | Tempo | Expected |
|-------|-------|----------|
| Day idle | 100 BPM | ✅ |
| Day play | 120 BPM | ✅ |
| Night idle | 80 BPM | ✅ |
| Night play | 95 BPM | ✅ |

### Default State
- ✅ `musicEnabled = false` on initialization
- ✅ Button starts with opacity 0.6 (visually "off")
- ✅ Volume slider hidden (`display:none`) when music is off
- ✅ Auto-start listeners only added when music was previously enabled

### Keyboard Shortcuts
- ✅ 'M' shortcut added to handleKeyDown with proper guards
- ✅ Modal shown in shortcuts overlay (Display section)
- ✅ Input/textarea guard prevents firing while typing

### Regression Checks
- ✅ All existing sound functions present: playNote, playNoise, SFX.*, toggleMute, onVolumeChange
- ✅ All core functions present: init, togglePlay, startPlay, stopPlay, toggleNightMode, generateRandomTrack, clearAll, handleKeyDown
- ✅ No modifications to existing audio routing (masterGainNode chain unchanged)
- ✅ Night mode toggle still updates house glows and headlight

## Bugs Found
None.

## New Lessons Learned
7 lessons added (LESSON-170 through LESSON-176) covering look-ahead scheduling, gain node routing, music-box timbre synthesis, autoplay policy compliance, pentatonic scale benefits, bar-level tempo transitions, and visibility API music pausing.

## Verdict: SHIPPED ✅
