# 🚂 Build Week — Cycle 1 Roadmap

**Cycle:** 1 (April 18–22, 2026)
**Theme:** Kid Delight — Make the World Come Alive

These 5 features are all about moments that make a 5-year-old squeal. The game already has great building mechanics and visuals — now we make the world *react* to the player and create magical discovery moments.

---

## Day 1: Train Horn — "CHOO CHOO!" Button 🚂💨

A big, bouncy, irresistibly pressable horn button that appears during play. Press it and EVERY running train blasts its horn with a satisfying doppler-shifted whistle sound. Visible steam puff clouds erupt from each locomotive's smokestack. Different train colors = different horn pitches. The button bounces when pressed with a ripple animation. Also works via 'H' key.

**Why kids love it:** Big button that makes a loud fun noise. They'll press it 500 times.

**Implementation:**
- Add horn button to controls (visible during play, hidden when stopped)
- Web Audio horn sound (frequency sweep oscillator + noise burst)
- Per-color pitch variation (red=low, blue=medium, etc.)
- Steam puff CSS particle animation from each train's position
- Button bounce animation on press
- 'H' keyboard shortcut
- 1-second cooldown to prevent audio stacking

---

## Day 2: Animal Reactions to Trains 🐄

When a train passes within 1 cell of an animal, the animal reacts! Cows jump with a startled bounce, sheep hop sideways in their cell, horses rear up, ducks fly up briefly, people wave excitedly. Each reaction has a unique CSS animation and sound effect. Creates magical cause-and-effect discovery moments.

**Why kids love it:** "Look! The cow jumped! Do it again!" — discovery + repetition = joy.

**Implementation:**
- Proximity detection in advanceTrainAnim (check adjacent cells for animals)
- Per-animal CSS keyframe animations (jump, scatter, rear, fly, wave)
- Sound effects per animal type
- Cooldown per animal per train to prevent spam
- Works with all train colors and speeds

---

## Day 3: Weather System 🌧️

Three weather modes: ☀️ Sunny (default), 🌧️ Rainy, ❄️ Snowy. Rainy: falling raindrop CSS particles, slightly darker sky tint, gentle rain patter sound loop. Snowy: falling snowflake particles, white-tinted ground, soft wind sound. Toggle via new weather button or 'W' key. Persists in localStorage.

**Why kids love it:** Seasons! Snow! Rain! The world changes and it's cozy.

**Implementation:**
- Weather state + toggle button + 'W' keyboard shortcut
- CSS particle systems for rain/snow (like existing smoke particles)
- CSS variable overrides for sky/grass tinting per weather
- Ambient sound loops (rain patter, wind)
- localStorage persistence
- Works with all biomes + night mode

---

## Day 4: Railroad Crossing Gates 🚧

New track piece: Railroad Crossing. Looks like a straight track with crossing gates and signal lights on both sides. When a train approaches (within 2 cells), gates animate down with a rhythmic "ding ding ding" bell sound and alternating red flashing lights. Gates rise smoothly after train passes. The crossing is a new palette item.

**Why kids love it:** The anticipation! The bells! The gates moving! Pure mechanical delight.

**Implementation:**
- New piece type 'crossing' with straight connections (N-S at rot 0)
- SVG rendering: track + gate arms + signal lights
- Gate animation: CSS transform for arm lowering/raising
- Proximity detection to trigger gate sequence
- "Ding ding" bell sound via Web Audio oscillator
- Flashing red lights via CSS animation
- Add to palette, share link type map, all relevant systems

---

## Day 5: Magic Rainbow Track 🌈

New track piece: Rainbow Track (straight variant). The track itself shimmers with animated prismatic rainbow colors. When a train passes over it, the train temporarily glows with a rainbow aura + sparkle particles trail behind for 3 seconds. A magical chime sound plays (ascending pentatonic arpeggio). The rainbow track piece is unlocked after completing 3 puzzles.

**Why kids love it:** It's MAGIC. The train GLOWS. Sparkles follow it. Pure wonder.

**Implementation:**
- New piece type 'rainbow' with straight connections
- Animated rainbow gradient SVG for track rendering
- Train rainbow glow: CSS class with animated box-shadow + hue-rotate
- Sparkle trail particles spawned in advanceTrainAnim when glow active
- Chime sound: ascending C-E-G-A pentatonic using Web Audio
- 3-second glow timer per train
- Unlock gate (3 puzzles completed) — free in sandbox if allUnlocked
- Add to palette, share links, all systems
