# Day 13 Build Report — Richer Soundscape

**Date:** 2026-03-30
**Builder:** Factory Agent (Opus)

## What Was Built

### T1: Station Horn Upgrade
- Replaced simple ding-ding with a proper two-tone train horn
- Triangle wave base with frequency sweeps (520→440Hz and 392→349Hz)
- Sawtooth harmonic overtone for richness
- Two tones overlap for ~0.7s total — sounds like a real horn

### T2: Crossing Bell
- Added `SFX.crossingBell()` — 4 rapid dings at ~1400Hz with alternating frequency
- Metallic overtone at 2.2x fundamental for realistic bell timbre
- Triggered when train enters any crossover piece
- Per-crossover cooldown (2s) prevents retriggering on loops

### T3: Tunnel Echo/Reverb
- Built delay-based reverb system: `createTunnelReverb()`, `isAnyTrainInTunnel()`
- DelayNode (0.1s) with feedback gain (0.3) for echo effect
- Reverb gain activates (0.4) on tunnel entry, deactivates on exit
- Multi-train aware: only disables when NO trains are in tunnel
- Chug sound routed through reverb via `playChugWithEcho()`

### T4: Refined Chug Rhythm
- Replaced `setInterval` with recursive `setTimeout` for cleaner timing
- Added alternating accent pattern: weaker beat at 90Hz (choo), stronger at 110Hz (CHOO)
- Musical interval formula: `280 / speed`, clamped 70-500ms
- Clean restart when speed changes (no double-triggering)

### T5: Volume Slider
- Added range input (0-1, step 0.05) next to mute button
- Created `masterGainNode` in audio context — ALL sounds route through it
- Updated `playNote()`, `playNoise()`, and all direct Web Audio SFX to connect to `getMasterGain()` instead of `ctx.destination`
- Volume persisted to localStorage (`trainTracks_volume`)

### T6: Three-State Sound Icon
- Mute button now cycles: 🔊 (full) → 🔉 (low = 30% of slider) → 🔇 (mute) → 🔊
- `applyVolumeState()` sets masterGain based on state × slider
- State persisted to localStorage (`trainTracks_soundState`)
- `restoreAudioSettings()` called in init to restore both volume and state

## Audio Infrastructure Changes
- All sound output now routes through `masterGainNode` → `ctx.destination`
- Direct `ctx.destination` connections replaced in: playNote, playNoise, station, tunnelEnter, tunnelExit, moo, boing, crossingBell
- New functions: `getMasterGain()`, `applyVolumeState()`, `onVolumeChange()`, `restoreAudioSettings()`, `createTunnelReverb()`, `isAnyTrainInTunnel()`, `playChugWithEcho()`

## Validation
- JS parse: ✅ (zero errors)
- HTML DIVs: 56/56 balanced ✅
- All 13 new functions present ✅
- All 22 SFX methods present ✅
