# PRUNE Report — Cycle 3 (May 28, 2026)

**Auditor:** Mochi (fresh-eyes audit, Day 69 of factory cycle / Day 1 of Prune Week 3)
**Site under review:** https://mikedyan.github.io/train-tracks/?v=69&fresh=1
**Code size entering Prune Week 3:** **11,866 lines / 422,935 bytes** (single `index.html`)
**Hard rule (end of Prune Week 3):** ≤ **11,866 lines** (net negative code = pass)
**Stretch goal:** ≤ **11,830 lines** (match Cycle 2's −36 LOC cut)
**Previous prune outcomes:** Cycle 1 missed (+55 LOC). **Cycle 2 hit (-36 LOC, first net-negative.)** Cycle 3 must match or beat Cycle 2.

---

## TL;DR

The game is in **excellent kid-UX shape** after Cycle 3. Build Week 3 shipped 5 features (Time-of-Day Sky 🌅, Animal Passengers 🐄, Whistle Songs 🎵, Replay Sharing v3 🎬, Sticker Book ⭐) for **+717 net LOC**, but **zero new toolbar buttons** and only **+1 settings tile** (Sticker Book). That's the right discipline — feature surface should be discoverable, but it shouldn't crowd the chrome. Harden Week 3 closed clean with 0 open bugs, 0 console errors, and the first net-negative Harden week in the 90-day plan (-7 LOC, Day 67).

The fresh-eyes audit confirms the toolbar passed (15 visible buttons, same as Cycle 2). Settings drawer at 8 tiles is still walkable for a 5-year-old (and Sticker Book is genuinely a *reward* — kids want to find it). The piece-progression system is working as intended this cycle — **20 of 26 palette pieces are visually locked** on a fresh `localStorage` (Cycle 2's "0/26 locked" flag is no longer a regression). Tutorial auto-opens, step 3 teaches HONK (Day 57), first-random of the session hits cargo missions ~97% (Day 57). All UX wins from prior prunes held.

The audit-priority cuts are **code-side, not UX**. The script section has **107 `// =====` separator lines** with **51 redundant closing fences** (sandwich pattern: header line surrounded by `=====` both above and below). Trimming the closing fences alone clears the hard rule with a ~50-line margin and zero feature/readability loss. Smaller code-health targets (sticker-modal CSS variants, Day 60 verbose comment block, blank-divider runs) round out a realistic **-50 to -65 LOC** budget for the week — comfortably beating Cycle 2.

**One non-prune UX flag for the next Build week** (not actionable this week): the **🧑 Passengers** toolbar button is the only round-row item that holds *state* (Off/On). Kids see a face icon and don't know it's a switch until the tooltip. Consider either (a) making it a settings-drawer tile in a future cycle, or (b) renaming the icon to read more obviously like a toggle. Out of scope for prune week — flagging for the next Build roadmap.

---

## 1. Fresh Eyes Walk-Through (the 5-year-old test, take 3)

Cleared `localStorage` → reloaded `?v=69&fresh=1`. Captured a full-page screenshot. Here's what a 5-year-old sees:

| Element | First impression | Verdict |
|---|---|---|
| Big "🚂 Train Tracks" header | Friendly, on-brand | ✅ Keep |
| Tutorial overlay auto-pops ("Drag a Track Piece!") with Skip/Next | Step 1 of 3, welcoming, dismissible | ✅ Keep |
| Left palette: TRACKS / TRAINS / CARS / SCENERY headers | Clear grouping | ✅ Keep |
| Locked pieces dim to opacity 0.35 + 🔒 emoji overlay | Reads as "earn this later" without being scary | ✅ Keep — **better than Cycle 2** |
| Grid (12×8 default, green felt aesthetic) | "I can put things there" | ✅ Keep |
| Row 1 toolbar (▶️ Play · 🎲 Random · 🗑️ Clear · ↩️ ↪️ · speed slider · 🔊 + volume slider · ☀️ · 💾 Save · 🧩 Puzzles) | Reads as "the buttons that matter" | ✅ Keep |
| Row 2 round cluster (🌤️ · 🌸 · 🧑 · 📤 · ❓ · ⚙️) | Visually distinct, lower-stakes | ✅ Keep — 1 caveat (see §6) |
| 📯 HONK (only when playing) | Still chef's kiss | ✅ Sacred |

**Verdict:** The UX prune work from Cycles 1 and 2 held. Cycle 3's feature additions are *invisible* in the chrome on fresh load — they live in the Settings drawer (Sticker Book) or auto-trigger during gameplay (Sky, Animals, Whistles, Replay-sharing on inbound link). Nothing new to cut.

---

## 2. Inventory & Counts (vs Cycle 2 baseline)

### Toolbar (visible: **15** + HONK while playing — unchanged)
**Row 1 (rectangular, 9 buttons + speed slider + volume slider):**
1. ▶️ Play
2. 🎲 Random
3. 🗑️ Clear
4. ↩️ Undo
5. ↪️ Redo
6. _Speed slider (🐢↔🐰)_
7. 🔊 Sound (mute toggle) + volume slider
8. ☀️ Day/Night
9. 💾 Save
10. 🧩 Puzzles

**Row 2 (round, 6 buttons):**
1. 🌤️ Weather (sunny / rain / snow)
2. 🌸 Biome (spring / summer / autumn / winter / desert)
3. 🧑 Passengers toggle (Off / On — *flagged in §6*)
4. 📤 Share / Save image
5. ❓ How to play
6. ⚙️ Settings

**Play-only:** 📯 HONK (appears bottom-right while a train is running)

→ **No change from Cycle 2 end (Day 58).** Cycle 3 shipped 5 features without adding a single toolbar button.

### Settings Drawer (**8 tiles + music volume slider**)
- AUDIO: 🎵 Music (Off/On), 🔊 Sound pack (Classic / Toy / Diesel)
- DISPLAY: ♿ High Contrast, ⬛ Big Grid (12×8 / 16×10)
- GAME: 🏷️ Name Your Trains, 🎬 Track Replay, 📊 Stats & Milestones, ⭐ Sticker Book

→ **+1 from Cycle 2 end (was 7).** The new Sticker Book is the right addition — collectibles belong in GAME, not floating on the toolbar. Drawer still passes the "scannable in 2 seconds" test.

### Palette (**26 pieces, 4 sections** — unchanged)
- TRACKS (9): Straight, Curve, T-Split, Cross, Bridge, Tunnel, Station, Crossing, Rainbow
- TRAINS (5): Red, Blue, Green, Yellow, Purple
- CARS (3): Freight, Passenger, Caboose
- SCENERY (9): Tree, House, Cow, Water, Flower, Sheep, Horse, Duck, People

**Locked at fresh start: 20 / 26** (opacity 0.35 + 🔒 overlay)
Unlocked: Straight, Curve, Red train, Tree, House, Cow.

→ **Progression is working again this cycle.** Cycle 2's PRUNE_REPORT flagged "0/26 locked" as a quiet regression — verified today that the milestone unlock system is healthy, no action needed.

### Modals (**11 total** — unchanged since Day 64)
`save-modal`, `settings-modal`, `track-replay-modal`, `train-names-modal`, `share-modal`, `shortcuts-modal`, `puzzle-modal`, `screenshot-modal`, `stats-modal`, `sticker-modal`, plus `tutorial-overlay`. Each uses the delegated `event.target===this` outside-click pattern from Cycle 2 Day 56.

### Code health
- **Lines:** 11,866 (entering Prune)
- **Bytes:** 422,935 (~413 KB)
- **Total functions:** 325 (vs 306 end of Cycle 2 — +19 from Cycle 3 build week, of which Sticker Book + Replay-share v3 are the biggest contributors)
- **Duplicate function declarations:** 0 (Day 67 cleared the last one — `svgEl` hoist)
- **CSS classes defined:** 215 unique
- **Dead CSS suspects:** 0 confirmed (`.animal-react-*` and `.difficulty-*` look like dead-rule candidates by lexical count, but verified — all are dynamically applied via `'animal-react-' + animalType` and `'difficulty-' + p.difficulty.toLowerCase()`)
- **Console errors live:** 0
- **Open bugs entering Prune week:** 0

---

## 3. Code-Health Targets (the actual prune budget)

Hard rule: end ≤ 11,866 LOC. Stretch: ≤ 11,830 LOC (Cycle 2 parity at -36).

### 🎯 Target A — Section-divider de-duplication (~50 LOC)

The script section uses a `// ====================` "outer fence" pattern around every section header:

```
// ============================================================
// SECTION LABEL
// ============================================================
```

There are **107 fence-divider lines** in the script section, paired with **~50 section headers**. **51 of those fences are sandwich-closers** (the line *after* a `// LABEL` header). Removing the closing fences keeps every section break visible (each section still starts with `===\nLABEL`) and saves ~50 LOC with **zero readability loss**.

Concretely, transform every:
```
// ============================================================
// LABEL
// ============================================================
```
into:
```
// ============================================================
// LABEL
```

→ **Estimated saving: ~50 LOC.** Day 3 (Code Cleanup) target.

### 🎯 Target B — Verbose Day 60 / Day 63 explainer comments (~5–8 LOC)

Two block comments are *very* prose-heavy (8–10 lines each describing rationale for a single small function). They were useful during build week, but the code itself is now well-named enough that a one-line summary is fine. Specific candidates:
- `// ============================================================` + 8-line essay above `ANIMAL_PASSENGERS` (lines ~11149–11157)
- 6-line preamble above `STICKER_STORAGE_KEY` (lines ~11514–11521)

Tighten to ~2 lines each. → **Estimated saving: ~10 LOC.** Day 3 target.

### 🎯 Target C — Sticker constant array compaction (~2 LOC)

`STICKERS` array (12 entries) currently has the `train-master` meta-sticker on 4 lines (the `check` function takes a multi-line body). Could be inlined to 2 lines with `function () { return STICKERS.every(s => s.id === 'train-master' || stickerState.earned[s.id]); }`. **Marginal but free.**

→ **Estimated saving: ~2 LOC.** Day 3 target.

### 🎯 Target D (defer if margin is comfortable) — Sky CSS variant consolidation

`@keyframes sky-tint-cycle` and `@keyframes sky-tint-cycle-night` are 9 + 4 lines respectively. They could share keyframes via CSS custom properties for the gradient stops, but the cleanup adds ~6 lines of CSS-variable plumbing. **Net wash. Skip.**

### 🎯 Target E (defer) — Modal `.close-btn` rule consolidation

Each modal style block re-declares its `.close-btn` selector with the same 6-property body. There are 8 such repetitions. A single `.modal .close-btn { ... }` rule would save ~24 LOC, but the existing rules use modal-id selectors (`#sticker-modal .close-btn`), and the bodies aren't byte-identical (some override night-mode). **Higher refactor risk for ~15 net LOC. Defer to a future cycle.**

### Realistic Day-3 budget

| Target | Saving | Risk |
|---|---|---|
| A. Section-divider de-dup | ~50 LOC | None |
| B. Verbose comments | ~10 LOC | None |
| C. Sticker meta inline | ~2 LOC | None |
| **Subtotal** | **~62 LOC** | **None** |

→ **Projected end-of-week LOC: 11,866 − 62 = 11,804.** Beats the hard rule (≤11,866) by 62 lines, beats Cycle 2's −36 by ~26 lines. **Stretch goal achievable.**

---

## 4. UX Simplification Targets (Day 2 — Simplify)

The Cycle 2 prune already absorbed the obvious UX wins (settings grouping, Fullscreen demoted to F-key, Track Replay icon 👻→🎬, HONK in tutorial). For Cycle 3, the deck is **mostly clean**. Two small candidates:

### 4a. Sticker Book progress on first-visit modal (delight polish, candidate)
First-time sticker-book visitor sees `0 / 12 stickers earned`. A gentle hint — *"Play to earn your first sticker!"* — under the progress bar would warm up the empty state. **+4 LOC, kid-friendly delight.** (This is actually a Day 4 *Delight Polish* candidate, not a Day 2 cut. Flagged here for visibility.)

### 4b. Settings drawer Sticker Book entry — icon variant
Currently `⭐ Sticker Book`. Considered: leave it. The ⭐ matches the meta-sticker reward and the Stats & Milestones tile already uses 📊, so star is the right read. **No change.**

### 4c. (Defer) Passengers 🧑 button surface
Round-row Passengers button is the only stateful icon in row 2 (Off/On switch). Discoverability nit but **not** a prune target — moving it to settings would *grow* the file (drawer tile + remove toolbar button = net wash or growth). **Flag for Build Week 4 roadmap discussion.**

→ **Day 2 plan: no UX cuts.** Cycle 3 Prune Week is a code-health week, by design.

---

## 5. Delight Polish (Day 4 candidates)

These are *additions*, not cuts — Day 4 of Prune Week is where small kid-magic gets added back inside the saved-LOC margin.

1. **Sticker Book empty-state hint** (~4 LOC, see §4a) — warms up the 0/12 state.
2. **Honk-from-keyboard tells you what train honked** — currently HONK sounds for the active train, but on first run a kid might press it and not see which train made the sound. A 1-frame badge over the active loco when HONK fires? **Optional, ~10 LOC.**
3. **First-sticker celebration upgrade** — Day 63's award path uses `SFX.celebrate()` + toast. For the *first* sticker only, consider a brief whole-screen confetti burst (the function already exists from cargo deliveries). **~5 LOC.**

→ Pick the cheapest one (1) on Day 4. Save the rest for Build Week 4 or beyond.

---

## 6. Non-Prune Flags (for the next Build Week roadmap, not actionable here)

- **🧑 Passengers button discoverability** (§4c) — Off/On state isn't obvious. Consider rename, indicator dot, or settings-drawer relocation in Cycle 4.
- **Tutorial coverage** — Tutorial still has 3 steps. Cycle 3 shipped 5 features. Kids who skip tutorial won't see Sticker Book, Animal Passengers, or Whistle Songs surfaced anywhere. Consider a "What's New" reveal after the 3rd run, or extending the tutorial to 4 steps. **Build Week 4 candidate.**
- **Big Grid + Sky-cycle interaction** — On a 16×10 grid, the sun-arc keyframe percentages still target the viewport, so the sun's trajectory looks fine. Verified in Harden Week. No action.

---

## 7. Day-by-Day Plan for Prune Week 3

| Day | Date | Goal | Specifics |
|---|---|---|---|
| **Day 69 (Mon)** | May 28 | Fresh-Eyes Audit | _(this report)_ |
| **Day 70 (Tue)** | May 29 | Simplify | **Target A executed (closing-fence dedup, −49 LOC).** Hard rule cleared, stretch goal beaten by 13 lines. Game verified live on deploy: 0 console errors, random-track generates 40 cells + train clean. |
| **Day 71 (Wed)** | May 30 | Code Cleanup | **Targets B + C executed + bonus blank-run dedup, −33 LOC.** See Day 71 Result below. |
| **Day 72 (Thu)** | May 31 | Delight Polish | Add Sticker Book empty-state hint (§5.1) |
| **Day 73 (Fri)** | June 1 | Expert Panel + Validation | Cycle 3 close-out review, score vs Day 58 (8.4 baseline), commit to `reviews/prune-cycle-3-review.md` |

### Day 71 Result (May 30)

- **LOC:** 11,817 → **11,784** (−33)
- **Bytes:** 419,799 → **418,970** (−829)
- **Cycle 3 Prune cumulative:** −82 LOC (hard rule ≤11,866 cleared by 82, stretch ≤11,830 beaten by 46 — already past Cycle 2's −36 with 2 days to spare)
- **What changed:**
  - Target B: Day 60 `ANIMAL_PASSENGERS` 10-line preamble → 3-line summary; Day 63 `STICKER_STORAGE_KEY` 8-line preamble → 3-line summary (−15 LOC)
  - Target C: `train-master` meta-check inlined (4 → 1 line, −3 LOC)
  - Bonus: 18 redundant blank lines removed (5 known 3+-run locations plus all 2-blank runs across the file collapsed to a single blank — readability unchanged)
- **Verification:** `node --check` on extracted script: clean. Live deploy at `?v=71`: 0 console errors, 52 palette pieces, 50 buttons, 12 stickers, 4 animal types (cow/sheep/duck-land/horse), `generateRandomTrack()` succeeds.
- **Day 4 / Day 5 plan unchanged:** Delight polish (Sticker Book empty-state hint, §5.1) Thursday; Cycle 3 close-out review Friday. Margin is so generous Day 4 could absorb an extra small polish if one surfaces.

### Day 70 Result (May 29)

- **LOC:** 11,866 → **11,817** (−49)
- **Bytes:** 422,935 → **419,799** (−3,136)
- **Hard rule** (≤11,866): ✅ cleared by 49 lines
- **Stretch goal** (≤11,830): ✅ beaten by 13 lines
- **What changed:** 49 redundant closing `// =====` fences removed from 3-line sandwich section headers. 58 fences remain — all legitimate multi-line block comment delimiters (correctly preserved).
- **Verification:** `node --check` on extracted script clean. Live deploy at v=70 renders grid, palette (52 pieces), 50 buttons. `generateRandomTrack()` produces 40 occupied cells + train with 0 console errors.
- **Schedule impact:** Targets B + C deferred to Day 3 (Code Cleanup). Margin is generous — Day 3 can pursue further code-health wins beyond the original budget.

---

## 8. The Number That Matters

**Entering:** 11,866 lines / 422,935 bytes
**Hard rule end-of-week:** ≤ 11,866
**Realistic projection:** ~11,804 (-62)
**Stretch:** ≤ 11,830 (-36, parity with Cycle 2)

**Prediction:** Cycle 3 Prune will be the **second consecutive net-negative prune** in the 90-day plan. Code-debt momentum compounding.

---

*Auditor: Mochi 🐯
Date: May 28, 2026
File: `PRUNE_REPORT.md`
Cycle: 3 of the 90-day program (Apr 18 – Jul 16, 2026)*
