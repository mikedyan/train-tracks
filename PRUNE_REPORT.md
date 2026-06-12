# PRUNE Report — Cycle 4 (June 12, 2026)

**Auditor:** Mochi (fresh-eyes audit, Day 84 of factory cycle / Day 1 of Prune Week 4)
**Site under review:** https://mikedyan.github.io/train-tracks/?v=84&fresh=1&cb=prune4d1
**Code size entering Prune Week 4:** **12,485 lines / 448,624 bytes / 343 functions** (single `index.html`)
**Hard rule (end of Prune Week 4):** ≤ **12,485 lines** (net negative code = pass)
**Stretch goal:** ≤ **12,449 lines** (Cycle 2 parity, −36)
**Aspirational goal:** ≤ **12,409 lines** (Cycle 3 parity, −76)
**Byte rule:** ≤ **448,624 bytes** (added in Cycle 3 — both axes must shrink)
**Previous prune outcomes:** Cycle 1 missed (+55). **Cycle 2 first net-negative (−36).** **Cycle 3 best so far (−76 LOC, −3,404 bytes, +0.2 score).**

---

## TL;DR

Cycle 4 shipped the most ambitious build week in the 90-day factory's life: **+691 LOC across 5 features** (Ambient Critters 🦋, Station Arrival Signal 🚦, Confetti Cannon 🎉, Puddle Splashes 🌧️, Train Trail 🛤️). Harden Week 4 added +4 net (BUG-019 re-entry guard +5, dead-fn `resetDeliveryStreak` −1). Entering Prune Week 4 at **12,485 / 448,624 / 343** — the largest game the factory has ever pruned.

The good news: the **UX surface stayed disciplined**. All 5 Cycle-4 features are auto-on or auto-trigger, **zero new toolbar buttons**, **zero new settings tiles**, **zero new modals** added vs. Cycle 3 exit. Build Week 4 followed LESSON-DAY46-F and LESSON-DAY59-A — *add behavior, not chrome*. The toolbar still reads as **15 visible buttons + HONK during play**, the same shape it had at the end of Cycle 1. The settings drawer is still **8 tiles in 3 groups** (Audio/Display/Game). The palette is still **26 pieces in 4 sections**, and progression is healthy — **20/26 locked** on a fresh `localStorage` page load.

The cuts this week are **code-side, not UX-side**. The closing-fence dedup pattern from Cycle 3 Day 70 is exhausted (0 redundant fences remain), and the consecutive-blank-run pattern from Cycle 3 Day 71 is exhausted (0 runs ≥2 blanks). But Cycle 4's three big additions (Puddle Splashes, Confetti Cannon, Train Trail) each shipped with verbose Day-NN preamble comment blocks (~30 LOC combined), and 4 of the original 10 puzzles still carry **kid-comprehension scaffolding comments from the development phase** (~46 LOC across puzzles 6/7/9/10) that are no longer needed for understanding — the actual `pieces:` array is the source of truth. A new DRY target also appears in the audio engine: **15 SFX functions share a 3-line prelude** (`if (!soundEnabled) return; const ctx = getAudioCtx(); if (!ctx) return;`) that can be collapsed via a single `audioBegin()` helper.

**Realistic prune budget for the week: −60 to −90 LOC** across (A) verbose preamble comment trim, (B) puzzle dev-scaffold comment trim, (C) audio prelude DRY. That comfortably clears the hard rule (≤12,485) and beats the stretch goal (≤12,449); the aspirational goal (≤12,409, Cycle 3 parity) is in reach if all 3 targets land cleanly.

**One non-prune UX flag for the (hypothetical) next Build week:** the **🦋 Ambient Critters** are subtle enough that some kids may not notice them — they're scoped to scenery-adjacent cells, animated via pure CSS, and only spawn during play. Consider a "first session, draw one bigger" surfacing or a settings tile to bump the count. Out of scope for prune week — flagging only.

---

## 1. Fresh Eyes Walk-Through (the 5-year-old test, take 4)

Cleared `localStorage` → reloaded `?v=84&fresh=1&cb=prune4d1`. Captured full-viewport screenshot. Here's what a 5-year-old sees:

| Element | First impression | Verdict |
|---|---|---|
| 🚂 Train Tracks header | Friendly, on-brand | ✅ Keep |
| Tutorial overlay auto-pops ("Drag a Track Piece!") | Step 1 of 3, welcoming dot 1/3, Skip + Next visible | ✅ Keep |
| Left palette: TRACKS · TRAINS · CARS · SCENERY | 4 clear sections, 6 unlocked items visible at fresh start (Straight, Curve, Red train, Tree, House, Cow) | ✅ Keep |
| Locked pieces dim to opacity 0.35 with `palette-locked` class | 20/26 dimmed — reads as "earn this later" | ✅ Keep — progression healthy |
| Grid (12×8 default, green felt) | "I can put things there" | ✅ Keep |
| Row 1 toolbar (▶️ · 🎲 · 🗑️ · ↩️ · ↪️ · speed · 🔊 · ☀️ · 💾 · 🧩) | 9 rectangular buttons + 2 sliders | ✅ Keep |
| Row 2 round cluster (🌤️ · 🌸 · 🧑 · 📤 · ❓ · ⚙️) | 6 round buttons (lower-stakes) | ✅ Keep |
| 📯 HONK (play-only) | Hidden until ▶️ is hit — surprise reward | ✅ Sacred |

**Verdict:** The UX prune work from Cycles 1, 2, and 3 held through a 5-feature build week. Cycle 4's additions are *invisible in the chrome* on fresh load — they live entirely in play-time behavior (critters spawn during play, station signals appear on stations during play, puddles spawn during rain, confetti cannon fires at delivery #5, train trails appear behind running trains). **Nothing new to cut from the chrome.** The chrome has now survived 4 consecutive build cycles without growing.

---

## 2. Inventory & Counts (vs Cycle 3 baseline)

### Toolbar (visible: **15** + HONK while playing — unchanged for 4 cycles)
**Row 1 (rectangular, 9 buttons + speed slider + volume slider):**
1. ▶️ Play
2. 🎲 Random
3. 🗑️ Clear
4. ↩️ Undo
5. ↪️ Redo
6. _Speed slider (🐢↔🐰)_
7. 🔊 Sound (mute) + volume slider
8. ☀️ Day/Night
9. 💾 Save
10. 🧩 Puzzles

**Row 2 (round, 6 buttons):**
1. 🌤️ Weather (sunny / rain / snow)
2. 🌸 Biome (spring / summer / autumn / winter / desert)
3. 🧑 Passengers toggle (Off / On — *still flagged from Cycle 3*)
4. 📤 Share / Save image
5. ❓ How to play
6. ⚙️ Settings

**Play-only:** 📯 HONK (appears bottom-right while a train is running)

→ **No change from Cycle 3 end (Day 73).** Cycle 4 shipped 5 features without adding a single toolbar button. **4-cycle streak.**

### Settings Drawer (**8 tiles + music volume slider — unchanged**)
- 🔊 AUDIO: 🎵 Music (Off/On), 🔊 Sound pack (Classic / Toy / Diesel)
- 🖼️ DISPLAY: ♿ High Contrast, ⬛ Big Grid (12×8 / 16×10)
- 🎮 GAME: 🏷️ Name Your Trains, 🎬 Track Replay, 📊 Stats & Milestones, ⭐ Sticker Book

→ **Identical to Cycle 3 end.** Cycle 4 shipped 5 features without adding a single settings tile. **First cycle ever with zero settings-drawer growth.**

### Palette (**26 pieces, 4 sections** — unchanged)
- TRACKS (9): Straight, Curve, T-Split, Cross, Bridge, Tunnel, Station, Crossing, Rainbow
- TRAINS (5): Red, Blue, Green, Yellow, Purple
- CARS (3): Freight, Passenger, Caboose
- SCENERY (9): Tree, House, Cow, Water, Flower, Sheep, Horse, Duck, People

**Locked at fresh start: 20 / 26** (opacity 0.35 + `.palette-locked` class)
Unlocked: Straight, Curve, Red train, Tree, House, Cow.

→ **Progression system held through Cycle 4 Harden.** Verified live this morning. **Difficulty Curve score should stay at 9.**

### Modals (**11 total + tutorial-overlay = 12 — unchanged**)
`save-overlay`, `settings-overlay`, `track-replay-overlay`, `train-names-overlay`, `share-overlay`, `shortcuts-overlay`, `puzzle-overlay`, `screenshot-overlay`, `stats-overlay`, `sticker-overlay`, plus the persistent `tutorial-overlay` and `replay-rec-indicator`. All use the Cycle 2 Day 56 delegated `event.target===this` outside-click pattern.

### Code health (entering Prune Week 4)

| Metric | Cycle 3 entry (Day 69) | Cycle 3 exit (Day 73) | Cycle 4 entry (Day 84) | Δ vs C3 exit |
|---|---|---|---|---|
| Lines | 11,866 | 11,790 | **12,485** | **+695** |
| Bytes | 422,935 | 419,531 | **448,624** | **+29,093** |
| Functions | 325 | 325 | **343** | **+18** |
| Modals | 11 | 11 | **11** | 0 |
| Toolbar buttons | 15 + HONK | 15 + HONK | **15 + HONK** | 0 |
| Settings tiles | 8 | 8 | **8** | 0 |
| Palette pieces | 26 | 26 | **26** | 0 |
| Open bugs | 0 | 0 | **0** | 0 |
| Console errors live | 0 | 0 | **0** | 0 |

**The chrome held; the engine grew.** Cycle 4 added 5 behavior features (critters, station signals, confetti cannon, puddle splashes, train trail) without spending one byte of UX real estate. That's the right architecture, and it's the reason Cycle 4 was the heaviest build week (+691 LOC) in factory history — every feature is internal behavior with no UI cost.

---

## 3. Audit Targets — Code-Side Cuts

The Cycle 3 prune patterns (closing-fence dedup, blank-run dedup) are **exhausted**: 0 redundant fences in the codebase today, 0 multi-blank runs. The Cycle 4 cuts have to come from new sources.

### Target A — Verbose Day-NN preamble comments (~30 LOC)

The 3 biggest Cycle-4 features each shipped with explanatory preamble comment blocks intended to document *why* the feature exists. The kid-pitch context is already in FACTORY_STATE.json history entries; the code-level "why" can be 1-2 lines per feature.

Identified:
- **Lines 4301–4307: Day 77 PUDDLE SPLASHES preamble** (7 lines) → collapse to 2.
- **Lines 4403–4412: Day 78 TRAIN TRAIL preamble** (10 lines) → collapse to 2.
- **Lines 4886–4891: Day 77 puddle module-state preamble** (6 lines) → collapse to 1.
- **Lines 4227–4230: Day 75 STATION SIGNAL preamble** (4 lines) → leave (already terse).
- **Lines 8403–8420: Day 47 TRACK REPLAY preamble** (18 lines) → collapse to 4. *Earlier-cycle code, fair game now that the system is mature and bug-free across 2 harden weeks.*
- **Lines 3205–3213: Day 61 WHISTLE SONGS preamble** (9 lines) → collapse to 2.
- **Lines 3126–3131: Day 48 SOUND PACKS preamble** (6 lines) → collapse to 2.
- **Lines 8280–8285: Day 44 TRAIN NAMES preamble** (6 lines) → collapse to 1.

**Estimated savings: 33 LOC.** Zero functional change, zero readability loss (the *what* the code does is obvious from the function names; the *why* was scaffolding for the build-week scribe).

### Target B — Puzzle dev-scaffold comments (~46 LOC)

Puzzles 6, 7, 9, and 10 each ship with multi-line "here's how I designed this puzzle" comment blocks left over from the Day 16 build session. The actual puzzle is defined by the `pieces:` array right below the comment; the comments are obsolete development notes.

Identified:
- **Lines 10673–10691: Puzzle 6 Switchyard design notes** (19 lines) → collapse to 1.
- **Lines 10706–10717: Puzzle 7 Speed Run design notes** (12 lines) → collapse to 1.
- **Lines 10731–10736: Puzzle 8 Cow Pasture design notes** (6 lines) → collapse to 1.
- **Lines 10756–10766: Puzzle 9 Night Express design notes** (11 lines) → collapse to 1.
- **Lines 10782–10789: Puzzle 10 Multi-Train design notes** (8 lines) → collapse to 1.

**Estimated savings: 51 LOC.** Zero functional change. The puzzle definitions are exhaustively unit-tested (Day 65 + Day 80 each auto-solved all 10 puzzles at 3⭐ with `placePiece`).

### Target C — Audio prelude DRY helper (~12-18 LOC)

15 SFX functions share an identical opening:
```js
if (!soundEnabled) return;
const ctx = getAudioCtx();
if (!ctx) return;
// (often followed by) const mg = getMasterGain();
```

Sites: lines 3227, 3498, 3513, 3570, 3680, 3709, 3737, 3771, 3802, 3835, 3877, 3910, 3943, 3975, 4025.

Proposed helper:
```js
function audioBegin() {
  if (!soundEnabled) return null;
  const ctx = getAudioCtx();
  if (!ctx) return null;
  return { ctx, mg: getMasterGain() };
}
```

Each caller collapses to:
```js
const a = audioBegin(); if (!a) return;
const { ctx, mg } = a;
```

That's 2 lines instead of 3-4 per site. With 15 sites and a 6-line helper, net saving is roughly **15 × 1.5 = 22 LOC saved − 6 LOC for the helper = ~16 LOC net**. Conservative estimate. *But:* some callsites only need `ctx` and don't fetch `mg` — we can preserve that micro-optimization by exposing both `audioBegin()` (returns `{ctx,mg}`) and the existing `getAudioCtx()` for the rare ctx-only sites. **Estimated savings: 12-18 LOC.**

Safer alternative if the helper feels lossy: leave the audio engine alone and route the remaining LOC budget elsewhere. Day 71 cycle-3 cleanup taught us that **forcing DRY where the duplication is intentional micro-optimization** hurts readability without saving meaningful bytes.

### Target D — Confetti particle spawn helper (~10-15 LOC, OPTIONAL)

`triggerMiniConfetti` (12-particle loop, line 11539) and the inner loop of `triggerConfettiCannon` (3 × 18-particle bursts, line 11598-ish) share the bulk of the particle setup pattern. Could extract `spawnConfettiParticle(container, cx, cy, colors, sizeMin, sizeMax, distBase, distRand, durMs)`.

But the two patterns differ in *size, distance, dy bias, and lifetime*, so the helper signature gets noisy. **Verdict: skip unless the budget is short.** Day 67's `svgEl` hoist was clean because the inner helper was byte-identical; this one isn't.

### What I'm NOT cutting

- **Closing fences (`// =====`).** All 62 in the file today are legitimate multi-line block delimiters (top fence + section header + bottom fence). The redundant closing fences from Cycle 2 were harvested on Day 70. Don't re-prune dry wood.
- **Consecutive blank-line runs.** Zero ≥2-run blanks remain in the file (verified by python sweep). Day 71 already harvested these.
- **Function count.** Cycle 3 closed flat at 325 because the DRY meat was eaten. Cycle 4 added 18 functions across 5 features (average 3-4 fns/feature, all named, all referenced); cutting them would hurt readability. *Don't force a function-count cut.*
- **CSS classes.** No dead-rule suspects emerged from a quick scan; the Cycle 3 Day 67 dead-CSS audit cleared the file and nothing new looks orphan.
- **Day 75 Station Signal preamble** (4 lines) — already terse, leaves no room.

---

## 4. Day-by-Day Plan

| Day | Theme | Target LOC Δ | Notes |
|---|---|---|---|
| **84 Mon** | Fresh Eyes Audit | 0 | This report. Hard rule ≤12,485, stretch ≤12,449, aspirational ≤12,409. |
| **85 Tue** | Simplify (Target A) | **−30** | Collapse 7 verbose Day-NN preamble blocks (Puddle/Trail/Module-State/Replay/Whistle/Sound-Pack/Train-Names). |
| **86 Wed** | Code Cleanup (Target B + audio prelude scan) | **−50** | Trim 5 puzzle dev-scaffold comment blocks. Then evaluate Target C feasibility live — only ship it if the diff stays clean. |
| **87 Thu** | Delight Polish | **+0 to +8** | Tiny kid-friendly addition inside a margin we control. Candidates: brighter confetti color palette in night mode; subtle "first puddle ever" sticker; faster initial critter spawn delay. *Polish must stay net ≤ +8 LOC and live inside an existing surface.* |
| **88 Fri** | Validation + Cycle 4 Review | 0 | Live smoke test on the deployed site (`?v=88&fresh=1`), full 9-action user flow, screenshot evidence, JS parse clean, 0 console errors. Write `reviews/prune-cycle-4-review.md`. Commit + push + Telegram report. |

**Cumulative target: −80 to −90 LOC.** Clears the hard rule with a 80-line margin and beats the stretch goal (≤12,449, −36) by 44; aspirational (≤12,409, −76) is achievable if all 3 targets ship clean.

---

## 5. Risks & Watch-Items

1. **The Day 47 Track Replay preamble cut is the riskiest.** That feature has 2 follow-on integrations (Day 62 share-replay v3, Day 67 sticker-book hook). Keep the *implementation* comments inside `playReplay`/`recordAction` intact; only collapse the top-of-section block.
2. **Audio prelude DRY (Target C) needs a live smoke test before push.** Test all 10+ SFX paths after the refactor: station horn, whistle songs, chug, brake, celebrate, mini-confetti party, puddle "kssh", sound-pack switch.
3. **Don't add a Delight Polish that's UX-surface.** Cycle 3 Day 72 nailed this by adding hints *inside* the sticker modal. Cycle 4 Day 87 must follow the same discipline — additions live inside existing modals or inside play-time behavior, never on the toolbar.
4. **Byte rule.** Cycle 3 was the first cycle where both LOC and bytes shrank. Cycle 4 needs to repeat. Tracking byte delta in build-reports/.
5. **Don't relitigate the 90-day plan.** The Cycle 3 review called the 90-day plan complete. Cycle 4 is bonus-content — the factory has demonstrated the build/harden/prune rhythm and is now exploring whether it can sustain a 4th cycle without regressing the kid-UX wins.

---

## 6. Live Smoke Test (this morning, Day 84)

Verified live on `https://mikedyan.github.io/train-tracks/?v=84&fresh=1&cb=prune4d1` after `localStorage.clear()` + reload:

- ✅ Tutorial overlay auto-opens (step 1 of 3, "Drag a Track Piece!", Skip + Next visible)
- ✅ Palette renders 26 pieces; 20 dimmed with `palette-locked` class (Straight/Curve/Red train/Tree/House/Cow unlocked)
- ✅ Toolbar shows 15 visible buttons (9 row-1 + 6 row-2 round), HONK hidden until play
- ✅ Settings modal: 3 section headers (🔊 Audio / 🖼️ Display / 🎮 Game), 8 settings items
- ✅ Share modal: 3 buttons (Copy Link / Replay Link / Save Image — v3 still wired)
- ✅ Drawer sections: Tracks · Trains · Cars · Scenery (4 labels)
- ✅ `localStorage` after fresh load: only `trainTracks_stickers` key (Sticker Book init from Day 63)
- ✅ Zero console errors across page-load + sidebar render + tutorial render

**Anchor confirmed: 12,485 LOC / 448,624 bytes / 343 functions. Prune Week 4 is live.**

---

*Audit by Mochi. The hard rule is numbers, not vibes. Cycle 2 and Cycle 3 both cleared their numeric rules. Cycle 4 will too.*
