# Day 19 Build Report — More Scenery + Expanded Palette

## Date: 2026-04-07

## Changes Made

### 1. New Scenery Types (Constants)
- Added `flower`, `sheep`, `horse`, `duck-land`, `people` to `SCENERY_TYPES`
- Added emoji mappings: 🌻 flower, 🐑 sheep, 🐴 horse, 🦆 duck-land, 👨‍👩‍👦 people
- Used `duck-land` to differentiate from existing water-duck decoration

### 2. Palette Additions
- Added 5 new palette pieces to sidebar (after water)
- Mirrored all 5 in mobile bottom drawer
- Labels: Flower, Sheep, Horse, Duck, People

### 3. CSS Animations
- **Flower sway**: gentle 2-3deg rotation with subtle scale pulse
- **People wave**: subtle vertical bounce (2px translateY)
- **Land duck waddle**: 3deg rotation with 1px horizontal shift
- **Animal flipped**: shared `.scenery-animal-flipped` class for sheep/horse random facing
- All new animations pause when tab hidden (`.animations-paused`)

### 4. Sound Effects (Web Audio API)
- `SFX.sheep()`: nasal sawtooth bleat with pitch wobble + triangle overtone
- `SFX.horse()`: descending sawtooth whinny with sine overtone
- `SFX.duckQuack()`: double quack using square wave
- `SFX.peopleCheer()`: ascending sine notes + noise burst

### 5. Animal Proximity System
- Renamed `checkCowProximity` → `checkAnimalProximity`
- Now checks for cow, sheep, horse, duck-land, and people within 1 cell
- Each type triggers its own SFX with per-cell 3s cooldown
- Only one sound per cell transition (early return after first match)

### 6. renderCell Updates
- Flower: adds `.scenery-flower` class with randomized duration/delay via cell dataset seed
- Sheep/Horse: random facing via `.scenery-animal-flipped` class using cell dataset seed
- Duck-land: adds `.scenery-land-duck` class with randomized waddle
- People: adds `.scenery-people` class with randomized wave

### 7. Random Generator
- Updated `addRandomScenery()` weighted distribution:
  - Tree: 35%, House: 15%, Cow: 10%, Flower: 12%, Sheep: 10%, Horse: 6%, Duck-land: 6%, People: 6%
  - Trees still dominant, new types provide variety

## Verification
- JS parse: clean ✅
- HTML div balance: 152/152 ✅
- No duplicate code blocks ✅
- All palette types appear exactly 2x (sidebar + drawer) ✅
