# Cycle 5 Build Roadmap — June 17 → June 21, 2026

**Cycle:** 5 (Days 89–103)
**Build Week:** Days 89–93 (Wed → Sun)
**Theme:** _"The world greets the train."_ Cycle 4 made the world react (puddles splash, signals light, trails fade, critters wander). Cycle 5 makes the world **say hello** — the train picks up a riding pet, balloons float overhead, stationmasters wave, night sky drops shooting stars, and cargo announces itself with a little jingle. Every feature is auto-on, lives in play-time behavior, and adds zero new chrome (toolbar/settings/modal count must stay flat — 4-cycle streak is now 5).

---

## Inputs reviewed

- `reviews/prune-cycle-4-review.md` — 8.7/10 close, polish-tier cycle, Juice/Polish hit 10/10 for the first time.
- `PRUNE_REPORT.md` (Day 84) — Audio prelude DRY (Target C) explicitly held for a hypothetical Cycle 5 Prune Week.
- `LESSONS_LEARNED.md` — LESSON-DAY46-F (*add behavior, not chrome*) is the factory's default mode after 4 cycles.
- `BUGS.md` — 0 open bugs entering Cycle 5.
- Cycle-3/4 priority backlog: 🧑 Passengers button UX, tutorial expansion, performance smoke test, co-op/campaign feature, audio prelude DRY.

## Non-prune flags carried forward

- **🧑 Passengers button** is still the only round-row icon with On/Off state — flagged in C3 + C4 PRUNE_REPORTs. Cycle 5 is the right time to address it, but **as a quiet relocation (settings tile), not a new toolbar surface**.
- **Tutorial covers 3 of 8+ feature surfaces.** Not in Build Week 5 scope — too big for a single day, and not "kid-magic." Defer to Prune Week 5's Delight Polish day if margin allows.
- **Audio prelude DRY.** Defer to Prune Week 5 PRUNE_REPORT, same as C4.

---

## 5-Day Build Plan

| Day | Date | Feature | LOC est. |
|---|---|---|---|
| **89 Wed** | 2026-06-17 | 🐾 **Conductor Companion** — color-coded riding pet on every train | 50–80 |
| **90 Thu** | 2026-06-18 | 🎈 **Floating Balloons** — drift across viewport during play, trains "pop" them | 100–140 |
| **91 Fri** | 2026-06-19 | 👋 **Waving Stationmasters** — tiny figure waves when a train arrives at a station | 80–110 |
| **92 Sat** | 2026-06-20 | ⭐ **Shooting Stars (night)** — occasional arcing star during night-mode play | 70–100 |
| **93 Sun** | 2026-06-21 | 🎵 **Cargo Jingles** — each cargo type plays a tiny 3-note pickup melody | 60–90 |

**Total estimate: +360 to +520 LOC.** Below the Cycle 4 build week's +691 LOC pour. Smaller per-feature footprint is the goal — Cycle 4's per-feature average crept to 138 LOC/feature (LESSON-DAY88-D), and Cycle 5 should hold around the historical 110–115 LOC/feature mean.

---

## Day 89 — 🐾 Conductor Companion (today)

Each train picks up a tiny color-matched pet that rides on the loco for the entire play session.

| Train color | Pet emoji |
|---|---|
| 🔴 Red | 🐱 cat |
| 🔵 Blue | 🐶 dog |
| 🟢 Green | 🐸 frog |
| 🟡 Yellow | 🐤 chick |
| 🟣 Purple | 🦄 unicorn |

- **Pure CSS bob animation** (`conductor-bob`, ±2px sine, ±3° tilt, 1.1s loop).
- **Auto-on at startPlay**, one element per train (`anim.conductorEl`), parallel to existing `nameLabelEl` / `cargoBadgeEl` / `animalBadgeEl` plumbing.
- **Pinned to loco center** with a small upward offset (~0.18 × cellSize), no rotation — pet stays upright as the train curves under it (LESSON-DAY44-B pattern).
- **Tunnel-aware fade** via the existing `locoOpacity` sync — pet disappears with its train.
- **Reduced-motion safe** (`@media (prefers-reduced-motion: reduce) { .train-conductor { animation: none; } }`).
- **Night-mode glow + high-contrast outline.**
- **Cleaned in `stopPlay()`** alongside the other badges.

### Acceptance

- `startPlay` spawns N companion emojis for N trains, each matching `TRAIN_COLORS[color]` to a pet via `CONDUCTOR_COMPANIONS`.
- `stopPlay` drains all `.train-conductor` elements back to 0.
- Companion's `style.left/top` follows loco's `style.left/top` every frame.
- Live ?v=89 smoke test: 1 train placed → play → 1 pet visible bobbing on the loco → stop → 0 pets in DOM.
- 0 console errors.
- JS parse clean.

### Out of scope (today)

- Pet customization (locked to color).
- Pet personality reactions to events (cargo pickup, station arrival).
- Pet selection UI (would require chrome — explicitly out of scope per the no-chrome-growth mandate).

---

## Cycle 5 chrome budget (hard rule)

- **Toolbar:** **15 visible + HONK** (unchanged). Adding a button breaks the 4-cycle streak.
- **Settings tiles:** **8 in 3 groups** (unchanged) — unless 🧑 Passengers gets promoted from the toolbar to here, in which case net = 0 change.
- **Modals:** **11 overlays** (unchanged).
- **Palette:** **26 piece types** (unchanged).

Every Cycle 5 feature must obey this. Add behavior, not chrome — the 5-cycle streak is the prize.
