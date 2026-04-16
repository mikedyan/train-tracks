# Day 27 Build Report — Ambient Background Music

**Date:** 2026-04-16
**Feature:** Ambient Background Music
**Builder:** Factory Agent

## What Was Built

### 1. Music Synthesis Engine (T1)
- Pentatonic music-box melody using Web Audio API (100% synthesized, no external files)
- Scale: C5, D5, E5, G5, A5 (day mode) / C4, D4, E4, G4, A4 (night mode - lower octave)
- Music-box timbre: sine oscillator + triangle harmonic at octave above (sparkle layer)
- Fast attack (10ms), medium exponential decay for bell-like envelope
- 16-bar melody across 3 themes (A, B, A', C) with varied rhythm patterns
- Rests interspersed for breathing room and natural feel

### 2. Separate Music Volume Control (T2)
- 🎵 button in controls bar toggles music on/off
- Separate music volume slider (purple accent, 40px) appears when music is enabled
- Music has its own `musicGainNode` routed through `masterGainNode`
- Master mute (🔇) still silences everything including music
- Separate localStorage keys: `trainTracks_musicEnabled`, `trainTracks_musicVolume`

### 3. Play State Variation (T3)
- Idle tempo: 100 BPM (gentle, ambient)
- Play tempo: 120 BPM (slightly more upbeat when trains are running)
- Tempo changes apply on next bar boundary via `getMusicTempo()` called fresh each bar
- No audio glitches on state transitions

### 4. Night Mode Variation (T4)
- Night idle: 80 BPM with lower octave (PENTA_LOW frequencies)
- Night + play: 95 BPM (moderate, between night idle and day play)
- Lower note volume in night mode (0.06 vs 0.09)
- Smooth transition — frequency table switches on next bar

### 5. Default Off + Autoplay Compliance (T5)
- Music defaults to OFF on first visit
- Enabled via 🎵 button click (user interaction satisfies autoplay policy)
- Returning users with `musicEnabled` saved get auto-start on first interaction (pointerdown/keydown)
- Uses `{ once: true }` listeners for clean auto-start

### 6. M Keyboard Shortcut (T6)
- `M` key toggles music on/off
- Added to shortcuts modal under Display section
- Respects input/textarea focus guard

### 7. Integration Points
- `startPlay()` → calls `updateMusicTempo()` for faster tempo
- `stopPlay()` → calls `updateMusicTempo()` for idle tempo
- `toggleNightMode()` → calls `updateMusicTempo()` for night variation
- Visibility API → pauses/resumes music when tab is hidden/shown

## Technical Details
- Look-ahead scheduling: bars scheduled 0.5s ahead for smooth playback
- Recursive `setTimeout` pattern (not `setInterval`) for dynamic tempo changes
- All oscillators self-cleanup via `stop()` calls
- No memory leaks: oscillators are short-lived and auto-disconnect

## Verification
- JS parse: ✅ Clean
- HTML tag balance: ✅ All tags balanced
- No duplicate code blocks: ✅ All key identifiers appear exactly once
- File size: 8797 lines (was 8527, +270 lines)
