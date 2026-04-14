# Day 25 Build Report — Passenger Delivery

## Feature Summary
Added a togglable passenger delivery system. Stations generate passengers on a timer during play, trains pick them up and deliver them to the next station, with sound effects, confetti, and a delivery counter.

## Changes Made

### CSS (~50 lines)
- `#passenger-hud`: Fixed-position HUD with delivery counter and high score, night mode support
- `.station-passenger`: Positioned emoji with idle bounce animation
- `@keyframes passenger-board/arrive`: Boarding shrink-and-fade, arrival grow-and-fade
- `.btn-passengers` + `.enabled`: Toggle button styling (brown off, green on)

### HTML (~5 lines)
- Added `🧑` toggle button in controls bar after help button
- Added `#passenger-hud` div with count and best score spans
- Both desktop sidebar and mobile drawer unaffected (no palette changes needed)

### JavaScript (~200 lines)

#### Sound Effects
- `SFX.passengerBoard()`: Ascending ding-ding-ding (cheerful boarding)
- `SFX.passengerDeliver()`: Mini-fanfare with ascending notes (triumphant delivery)

#### Passenger State
- `passengerState` object: enabled flag, stations map, onboard map (per train), delivered count, high score
- localStorage keys for enabled preference and high score

#### Core Functions
- `togglePassengers()`: Toggle on/off, updates button and localStorage
- `startPassengerSystem()`: Scans grid for stations, initializes state, starts spawn timer
- `spawnPassengers()`: Every 10s, 70% chance per station to add a passenger (max 3)
- `handleTrainAtStation()`: Handles pickup + delivery logic
  - If train has onboard passengers and station wasn't the pickup station → deliver + confetti
  - If station has waiting passengers → board them (boarding animation)
- `triggerMiniConfetti()`: 12-particle burst at station on delivery
- `renderStationPassengers()`: Positions emoji near station platform
- `updatePassengerHUD()`: Updates counter and best score display
- `resetPassengerState()`: Cleans up on stop play

#### Integration Hooks
- `startPlay()`: Calls `startPassengerSystem()` after whistle
- `stopPlay()`: Calls `resetPassengerState()` before state reset
- `advanceTrainAnim()`: At station cells, calls `handleTrainAtStation()` when enabled
- `init()`: Calls `loadPassengerSettings()` to restore preference

## Architecture Decisions
- Passenger state is session-only (resets on stop) — not saved to localStorage or share links
- Uses `lastPickupTrain` per station to prevent deliver-at-same-station-as-pickup
- Each train tracks its own onboard count independently
- 70% spawn chance per tick per station creates natural randomness
- Delivery and boarding don't happen in the same visit (return early after delivery)

## Testing Notes
- JS parses cleanly (verified via `new Function()`)
- No duplicate identifiers (verified via grep)
- All new functions have unique names, no collisions with existing code
