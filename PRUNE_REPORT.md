# PRUNE Report — Cycle 2 (May 13, 2026)

**Auditor:** Mochi (fresh-eyes audit, Day 54 of factory cycle / Day 1 of Prune Week 2)
**Site under review:** https://mikedyan.github.io/train-tracks/?v=54&fresh=1
**Code size entering Prune week:** **11,192 lines / 297,740 bytes** (single index.html)
**Baseline to beat (HARD RULE):** end of prune week ≤ **11,192 lines** (net negative code = pass)
**Previous prune (cycle 1):** missed the file-size target by +55 lines. This time we **do not** miss.

---

## TL;DR

The game is in **genuinely good shape**. The toolbar simplification from cycle 1 held — 15 visible buttons (10 row 1 + 5 row 2 + HONK during play). Tutorial auto-opens on a fresh visit. All 26 palette pieces present across 4 well-labeled sections. Zero console errors on the deployed site. Harden Week 2 closed with 0 open bugs.

But cycle 2 build week put **+1,103 lines on the file** (10,089 → 11,192) without much visible bloat to a 5-year-old — the cost is hidden in the **⚙️ Settings drawer**, which has grown from 5 items → 9 items. Settings is becoming the "feature shelf" kids never open.

The audit-priority cuts are **code-side**, not UX. The toolbar passed the fresh-eyes test. The 9 `closeXxxModalOutside(e)` handlers, 5 `updateXxxSettingsLabel` functions, and 2 cargo/passenger cleanup pairs are obvious DRY targets totaling **~80–110 lines saveable** with zero feature loss. That clears the hard rule with margin.

One **non-prune flag for the next Harden week**: on a freshly cleared `localStorage`, **0/26 palette pieces are visually locked**. Cycle 1 had ~20 pieces locked at start (the unlock-as-you-play hook). This may be a quiet regression worth checking — but it is **out of scope for prune week** (no behavior change).

---

## 1. Fresh Eyes Walk-Through (the 5-year-old test, take 2)

Cleared `localStorage` → reloaded `?v=54&fresh=2`. Captured a full-page screenshot. Here's what a 5-year-old sees:

| Element | First impression | Verdict |
|---|---|---|
| Big "🚂 Train Tracks" header | Friendly, on-brand | ✅ Keep |
| Tutorial overlay auto-pops ("Drag a Track Piece!") with Skip/Next | Welcoming, age-appropriate, dismissible | ✅ Keep |
| Left palette: TRACKS / TRAINS / CARS / SCENERY sections | Clear grouping, chunky pieces | ✅ Keep |
| Grid (8×12 default, green felt aesthetic) | "I can put things there" | ✅ Keep |
| Row 1 toolbar (▶️ Play · 🎲 Random · 🗑️ Clear · ↩️ ↪️ · slider · 🔊 · ☀️ · 💾 Save · 🧩 Puzzles) | Reads as "the buttons that matter" | ✅ Keep |
| Row 2 round cluster (🌤️ · 🌸 · 🧑 · 📤 · ❓ · ⚙️) | Visually distinct, lower-stakes, well-grouped | ✅ Keep |
| 📯 HONK (only when playing) | Still chef's kiss | ✅ Sacred |

**Verdict:** Cycle 1's UX prune held. Nothing new to cut in the chrome.

---

## 2. Inventory & Counts (vs Cycle 1 baseline)

### Toolbar (visible: 15 + HONK while playing)
**Row 1 (rectangular, 9 buttons + slider):**
1. ▶️ Play
2. 🎲 Random
3. 🗑️ Clear
4. ↩️ Undo
5. ↪️ Redo
6. _Speed slider (🐢↔️🐰)_
7. 🔊 Sound mute
8. ☀️ Day / Night
9. 💾 Save
10. 🧩 Puzzles

**Row 2 (round cluster, 5 buttons):**
11. 🌤️ Weather (sunny / rain / snow)
12. 🌸 Biome (spring / desert / winter / autumn)
13. 🧑 Passengers ON/OFF
14. 📤 Share menu (Copy Link / Save Image)
15. ❓ Help (tutorial)
16. ⚙️ Settings

**Hidden until playing:** 📯 HONK

**vs Cycle 1 close-out:** 13 + 6 → 10 + 5. Same total. Same shape. ✅

### Palette (26 pieces, 4 sections)
- 🛤 TRACKS (9): straight · curve · t-split · cross · bridge · tunnel · station · crossing · rainbow
- 🚂 TRAINS (5): red · blue · green · yellow · purple
- 🚃 CARS (3): freight · passenger · caboose
- 🌳 SCENERY (9): tree · house · cow · water · flower · sheep · horse · duck-land · people

**vs Cycle 1:** identical. ✅

### Settings menu (9 items — ⚠️ grew from 5)
1. 🎵 Music: Off
2. ♿ High Contrast
3. 📊 Stats & Milestones
4. ⌨️ Keyboard Shortcuts
5. ⛶ Fullscreen
6. 🏷️ Name Your Trains *(NEW Day 44)*
7. 🟦 Big Grid: 12×8 *(NEW Day 45)*
8. 👻 Track Replay *(NEW Day 47)*
9. 🔊 Sound: Classic *(NEW Day 48)*

**Verdict:** Settings is the new toolbar-row-2 problem. It's not visible-chrome bloat (still one click deep), but it has gone from "a handful of advanced toggles" to a "feature wall."

### Modals (10 functional)
tutorial · save · puzzle · share · settings · screenshot · stats · shortcuts · train-names · track-replay

### JavaScript surface
- **317 functions** (vs 270 PRUNE_REPORT cycle 1, 274 end of cycle 1 prune → +43 in cycle 2)
- **53 `<button>` elements** in HTML (vs 39 in cycle 1)
- **49 `palette-piece` references** (vs 75 in cycle 1 — Day 41's DRY drawer cleanup held)
- **9 near-identical `close*Outside(e)` handlers** — biggest DRY target this week
- **5 `updateXxxSettingsLabel` functions** — second-biggest pattern
- **2 cargo/passenger cleanup pairs** — third candidate

### LOC trajectory
- Day 14 (pre-cycle): 8,400 ish
- Day 43 (end cycle 1 prune): 10,144
- Day 48 (end cycle 2 build): **11,192**
- Day 53 (end cycle 2 harden, today's starting point): **11,192** ← zero growth across Harden Week 2, mandate satisfied
- Day 58 target (end cycle 2 prune): **≤ 11,192** ← hard rule

---

## 3. Findings — Where the fat is (code-side, not UX)

### 🚨 Big DRY targets (Wednesday Day 56)

**3A. 9 nearly-identical `closeXxxModalOutside(e)` handlers (~25–30 lines saveable)**

```
closeSettingsMenuOutside, closeShareMenuOutside, closeTrainNamesModalOutside,
closeTrackReplayModalOutside, closeSaveModalOutside, closeScreenshotModalOutside,
closeShortcutsModalOutside, closePuzzleModalOutside, closeStatsModalOutside
```

All 9 follow the same shape:
```js
function closeFooModalOutside(e) {
  if (e.target === document.getElementById('foo-overlay')) closeFooModal();
}
```

**Cut:** Replace with a single delegated handler on `document` that looks at the `.modal-overlay` class on `e.target` and dispatches to a registered closer. Or simpler: one shared `dismissOnOverlayClick(e, overlayId, closerFn)` that all `onclick=` attributes call inline. The inline-attribute footprint goes up slightly (~9 × 30 chars), but the JS function bloat (9 × 3 lines = 27 lines) goes away. Net negative.

**3B. 5+ `updateXxxSettingsLabel` functions (~30–50 lines saveable)**

`updateMusicSettingsLabel`, `updateBigGridLabel`, `updateReplaySettingsLabel`, `updateSoundPackSettingsLabel`, plus implicit ones for High-Contrast / Passengers / Night. Each reads a state variable and writes `.textContent` on a labelled DOM node. Identical shape:
```js
function updateXxxSettingsLabel() {
  const el = document.getElementById('settings-xxx-label');
  if (el) el.textContent = `${EMOJI} ${LABEL}: ${state.xxx}`;
}
```

**Cut:** A single `refreshSettingsLabels()` driven by a config array of `{id, format()}` entries. Called from `openSettingsMenu()` and the individual toggle handlers. ~40 lines net saving.

**3C. Cargo + Passenger badge cleanup duplication (~15 lines saveable)**

`cleanupStationCargoBadges`, `cleanupTrainCargoBadges`, `cleanupStationPassengers` (plus `resetCargoState` and `resetPassengerState`) all do the same conceptual work: walk DOM, query selector, remove nodes; reset module state. Two thirds of this code is structurally identical.

**Cut:** Extract `cleanupBadgesByClass(className)` helper and have the three callers pass `'station-cargo-badge'`, `'train-cargo-badge'`, `'station-passenger'`. ~15 lines net.

### 🟡 Medium prune targets (Wednesday — only if time permits)

**3D. Dead-ish helpers in the long tail**
- `cancelLongPress` (3 refs but all defensive — verify if any actually fires)
- `restoreBigGrid` / `restoreSoundPack` are 1-call helpers — consider inlining at the single call site in `init()`.
- 7 inline `style="…"` attributes still in the HTML (down from 21+ in cycle 1, but a few were re-added in Cycle 2's modal HTML). Move to existing utility classes.

**3E. SOUND_PACKS config could shed comment bulk**
The Day 48 config object has helpful inline comments for each timbral parameter (whistle f1/f2/type/vol/dur/delay, chug filterFreq/filterQ/vol+accents, etc.). Some are descriptive sentences. If we're tight on the LOC budget, tightening these to short tags (or moving the doc to LESSONS_LEARNED.md) yields ~10 lines.

### 🟢 P3 (out of scope for prune; flag for next cycle)
- **0/26 pieces locked on fresh visit.** Either the progression system is now permissive by default (intentional?) or `isPieceUnlocked()` falls through when `state.unlocks.pieces.length === 0`. Cycle 1 review explicitly verified "80%+ pieces locked at start." Day 49 audit notes claim "default 6 unlocked." Today's audit says **0 locked / 26 visible**. This is a behavior change, not a code cleanup, so it doesn't belong in prune week. Flag for Cycle 3 Harden Week 1: explicitly decide and document — "no progression on fresh visit" or "progression broken, restore the lock state."

### ✅ Sacred (do NOT cut)
- HONK 📯 (untouchable)
- All 9 track types, 5 train colors, 3 cars, 9 scenery, 10 puzzles
- Train Names, Big Grid, Cargo Missions, Track Replay, Sound Packs (cycle 2 features all earned their place)
- Tutorial auto-show on first visit (the strongest "first 30 seconds" win)
- Speed slider with bunny+tortoise emojis

---

## 4. Tuesday plan (Day 55 — Simplify, UX-side)

Cycle 1's prune week did UX consolidation; cycle 2's UX is already lean. The cycle-2 simplify pass is **about Settings menu polish**, not menu-tree restructuring:

**Cut #1 — Move ⌨️ Keyboard Shortcuts out of Settings, into ❓ Help.**
Kids who need help look at ❓, not ⚙️. Adults can find it either way. The shortcuts modal stays; only its launcher moves. Saves 1 Settings line + 1 launcher function.

**Cut #2 — Demote ⛶ Fullscreen.**
F11 works in every browser. The launcher costs us ~5 lines of fullscreen-detection/swap code. Either remove or move to keyboard-shortcuts overlay. Saves ~5 lines.

**Cut #3 — Settings auto-grouping.**
Currently a flat list of 9 emoji rows. Group as: **Audio** (🎵, 🔊), **Display** (♿, 🟦, ⛶), **Game** (🏷️, 👻, 📊). Same 9 rows but with 3 short `<h3>` separators. This is **+3 lines of HTML** — counted against the budget but worth the kid-eye win.

**Cut #4 — Drop the redundant 🎵 Music toggle.**
Music belongs in the same place as Sound (🔊 mute). Add a second click on 🔊 mute to cycle "All audio / SFX only / Muted" or expose music as a tiny secondary slider inside the same UI. Saves 1 Settings line, but adds slight UI complexity to the mute control — **revisit Tuesday before committing.**

**Net Tuesday target:** -10 to -15 lines, plus the +3-line Settings header bump.

## 5. Wednesday plan (Day 56 — Code Cleanup)

Execute 3A, 3B, 3C above plus the 3D long-tail.
- **3A** outside-click handlers: -25 to -30 lines
- **3B** settings labels: -30 to -50 lines
- **3C** cleanup helpers: -15 lines
- **3D** misc inlining + dead branches: -10 lines

**Net Wednesday target: -80 to -105 lines.**

## 6. Thursday plan (Day 57 — Delight Polish)

- Verify tutorial 3-step sequence still flows: "Drag a Track Piece! → Hit Play → CHOO CHOO!" (and confirm HONK is taught).
- Make the very-first random track even more delightful: ensure a cargo-mission pair appears (Day 46 said ~70% rate — verify this is still true post-cuts; if not, bump to ~85% on the *first* random of a session).
- Smooth the Settings open-animation timing if the grouping (Cut #3) introduces visible jank.
- Audit Track Replay: kid-test the icon — is 👻 read as "ghost" or as "spooky"? Maybe 🔁 or 🎬 is friendlier.

**Net Thursday target:** 0 to +3 lines (small additions allowed; offset by Wednesday's haul).

## 7. Friday plan (Day 58 — Expert Panel + Validation)

- Open the deployed site cold, score 10 dimensions vs Day 43 baseline (8.3/10).
- **HARD RULE check: file size ≤ 11,192 lines.** If we land at 11,050 → ✅. If we land at 11,193 → ❌, revert until we're under.
- Confirm zero open bugs after this prune (Harden Week 2 closed with 0; cycle-2-prune should not introduce any).
- Write `reviews/prune-cycle-2-review.md` with cycle-1 retrospective comparison.

---

## 8. Risks & non-goals

- **Don't remove features.** Train Names, Big Grid, Cargo Missions, Track Replay, Sound Packs all stay. Track Replay is the closest to "kid-niche" but it earned its 365 lines on Day 47 and the activation pattern (Settings → 👻 → Record / Replay) is clean.
- **Don't change the saved-state schema.** Auto-save format (~9 LS keys), share-link v2 byte format, save-slot keys — all frozen during prune.
- **Don't relitigate cycle 1's UX gains.** The 21 → 15 toolbar trim is good. Don't undo it.
- **Don't fix the missing locked-pieces in this week.** It's a behavior change that needs a Build-week or Harden-week conversation, not a prune-week side-quest.

---

## 9. Friday score commitment (Day 58)

Re-run 10-dimension scoring vs Day 43:

| Dimension | Day 43 | Target Day 58 |
|---|---|---|
| First Impression | 9 | 9 (same) |
| Clarity | 9 | 9 (small Settings grouping win) |
| Core Loop | 9 | 9 |
| Difficulty Curve | 8 | 8 (no progression change this week) |
| Juice/Polish | 9 | 9 |
| Replayability | 7 | 7–8 (cycle-2 features mature) |
| Uniqueness | 7 | 7 |
| Bug-Free | 9 | 9 (don't introduce any) |
| Visual Design | 9 | 9 |
| Addictiveness | 7 | 7 |

Target overall: **8.3–8.5 / 10**, with the **headline metric being code health** — first prune week to land at-or-under the start-of-week LOC ceiling.

---

*Audit complete. On to Tuesday: simplify the Settings drawer.*
*— Mochi, factory orchestrator, Day 54.*
