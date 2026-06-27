# PRUNE Report — Cycle 5 (June 27, 2026)

**Auditor:** Mochi (fresh-eyes audit, Day 99 of factory / Day 1 of Prune Week 5)
**Site under review:** https://mikedyan.github.io/train-tracks/?v=99&fresh=1&cb=prune5d1
**Code size entering Prune Week 5:** **12,733 lines / 455,636 bytes / 352 functions** (single `index.html`)
**Hard rule (end of Prune Week 5):** ≤ **12,733 lines** (net negative code = pass)
**Stretch goal:** ≤ **12,690 lines** (−43, ~Cycle 2 parity)
**Aspirational goal:** ≤ **12,657 lines** (−76, Cycle 3 parity)
**Byte rule:** ≤ **455,636 bytes** (both axes must shrink — held in C3 and C4)
**Previous prune outcomes:** C1 missed (+55). **C2 first net-negative (−36).** **C3 (−76 LOC, −3,404 B).** **C4 best ever (−95 LOC, −5,377 B, 8.7/10).**

---

## TL;DR

Cycle 5 shipped the **leanest build week in factory history**: **+342 LOC across 5 features** (🐾 Conductor Companion, 🎈 Floating Balloons, 👋 Waving Stationmasters, ⭐ Shooting Stars, 🎵 Cargo Jingles) — 68 LOC/feature, well under Cycle 4's +691 and the +360–520 roadmap estimate. Harden Week 5 added **+1 net LOC** — a single deliberate correctness fix (BUG-020: `stopShootingStars()` was defined Day 92 but never wired into `stopPlay()`, leaking a night-mode interval; one-line teardown wiring on Day 97). Entering Prune Week 5 at **12,733 / 455,636 / 352**.

The discipline held again. All 5 Cycle-5 features are **auto-on / play-time behavior** — **zero new toolbar buttons, zero new settings tiles, zero new modals** vs. Cycle 4 exit. This is the **5th consecutive cycle with zero chrome growth**. Live fresh-load this morning: toolbar unchanged, settings still **3 sections (Audio / Display / Game)**, palette still **26 logical pieces** (52 DOM nodes = sidebar + mobile drawer), **40 locked on fresh** `localStorage` — progression healthy.

The honest news for prune week: **the classic veins are nearly mined out.** The closing-fence dedup (C3 Day 70) and consecutive-blank-run dedup (C3 Day 71) are exhausted — **exactly 1 blank run ≥2 remains** in the whole file. Dead-function audit came back **empty** (0 orphans). Cycle 5's code is already tight: the build scribe wrote terse 1-line preambles, not the verbose Day-NN blocks that fed Cycles 3–4. So Cycle 5's cuts are **smaller and more surgical** than prior cycles.

**Realistic prune budget for the week: −40 to −60 LOC** across (A) Cycle-5 inline redundant-comment trim, (B) a handful of 3-line section-fence sandwiches the new sections re-introduced, (C) the last blank run + intra-function blank trims in the 5 new functions, and (D — OPTIONAL/risk-flagged) DRY the Cargo-Jingle / Whistle-Song "play N notes" pattern into one helper. That comfortably clears the hard rule (≤12,733) and beats the stretch (≤12,690, −43). The aspirational goal (≤12,657, −76 Cycle 3 parity) is **only reachable if Target D lands clean** — and per LESSON-DAY71, we do **not** force DRY where the duplication is cheap micro-optimization. If D feels lossy, we bank a smaller honest win rather than a fragile big one.

**One non-prune note for a hypothetical next Build week:** Waving Stationmasters are persistent per-station residents (verified: 4 stations → 4 `.stationmaster` nodes, 0 waving at rest). They only wave on train arrival, which means on a fresh single-train loop a kid might not catch the wave. Not a defect — flagging as a possible Build-week "first arrival = guaranteed wave + tiny toot" surfacing. Out of prune scope.

---

## 1. Fresh Eyes Walk-Through (the 5-year-old test, take 5)

Cleared `localStorage` → reloaded `?v=99&fresh=1&cb=prune5d1b`. Live DOM probe results:

| Element | First impression | Verdict |
|---|---|---|
| 🚂 Train Tracks header | Friendly, on-brand | ✅ Keep |
| Tutorial overlay auto-pops | `#tutorial-overlay` display≠none on cold boot | ✅ Keep |
| Left palette: TRACKS · TRAINS · CARS · SCENERY | 26 logical pieces, 6 unlocked at fresh | ✅ Keep |
| Locked pieces dim with `.palette-locked` | **40/52 DOM nodes locked** (20/26 logical) | ✅ Keep — progression healthy |
| Grid (12×8 green felt) | "I can put things there" | ✅ Keep |
| Toolbar (row 1 rect + row 2 round) | Same shape as Cycle 1 exit | ✅ Keep |
| Settings drawer | **3 sections: 🔊 Audio / 🖼️ Display / 🎮 Game** | ✅ Keep |
| 📯 HONK (play-only) | Hidden until ▶️ | ✅ Sacred |

**Verdict:** The UX prune work from Cycles 1–4 survived a 5th build week. Cycle 5's additions are *invisible in the chrome* on fresh load — they live entirely in play-time behavior (conductor rides the loco, balloons drift up, stationmasters wave on arrival, shooting stars arc in night mode, cargo jingles play on pickup). **Nothing new to cut from the chrome.** The chrome has now survived **5 consecutive build cycles** without growing.

---

## 2. Inventory & Counts (vs Cycle 4 baseline)

### Toolbar — **15 + HONK while playing** (unchanged 5 cycles)
Row 1 (rect): ▶️ · 🎲 · 🗑️ · ↩️ · ↪️ · speed · 🔊+vol · ☀️ · 💾 · 🧩
Row 2 (round): 🌤️ · 🌸 · 🧑 · 📤 · ❓ · ⚙️
Play-only: 📯 HONK
→ **No change from Cycle 4.** 5-cycle streak.

### Settings Drawer — **8 tiles in 3 sections** (unchanged)
- 🔊 AUDIO: 🎵 Music, 🔊 Sound pack (Classic / Toy / Diesel)
- 🖼️ DISPLAY: ♿ High Contrast, ⬛ Big Grid
- 🎮 GAME: 🏷️ Name Trains, 🎬 Track Replay, 📊 Stats, ⭐ Sticker Book
→ Identical to Cycle 4. Cycle 5 shipped 5 features with **zero settings growth**.

### Palette — **26 logical pieces, 4 sections** (unchanged)
TRACKS (9), TRAINS (5), CARS (3), SCENERY (9). **20/26 locked at fresh** (40/52 DOM nodes counting the mobile drawer mirror). Verified live.

### Modals — **13 overlays** (unchanged)
`weather-overlay`, `sky-overlay`, `save-overlay`, `settings-overlay`, `track-replay-overlay`, `train-names-overlay`, `share-overlay`, `shortcuts-overlay`, `puzzle-overlay`, `screenshot-overlay`, `stats-overlay`, `sticker-overlay`, `tutorial-overlay`. All use the C2 Day 56 delegated outside-click pattern. No new modal in Cycle 5.

### Code health (entering Prune Week 5)

| Metric | C4 entry (D84) | C4 exit (D88) | C5 entry (D99) | Δ vs C4 exit |
|---|---|---|---|---|
| Lines | 12,485 | 12,390 | **12,733** | **+343** |
| Bytes | 448,624 | 443,247 | **455,636** | **+12,389** |
| Functions | 343 | ~343 | **352** | **+9** |
| Modals | 11 (+2 sub) | 11 | **13** | 0 net new feature-modals |
| Toolbar buttons | 15+HONK | 15+HONK | **15+HONK** | 0 |
| Settings tiles | 8 | 8 | **8** | 0 |
| Palette pieces | 26 | 26 | **26** | 0 |
| Open bugs | 0 | 0 | **0** | 0 |
| Console errors live | 0 | 0 | **0** | 0 |

**The chrome held; the engine grew by the smallest build-week delta yet.** Cycle 5 added 9 functions across 5 behavior features (avg ~2/feature) without spending a byte of UX real estate.

---

## 3. Audit Targets — Code-Side Cuts

The C3 prune veins are spent: **1** consecutive-blank run ≥2 remains (lines 7830–7831), **0** dead functions, and the legitimate section fences are real multi-line delimiters. Cycle 5's cuts are smaller and must be surgical.

### Target A — Cycle-5 inline redundant comments (~12–18 LOC)
The 5 new functions carry a handful of inline comments that restate the obvious code beneath them. Identified live:
- **Line 8114: `// Randomize properties`** (over 6 self-explanatory `--balloon-*` setProperty calls) → drop.
- **Line 8132: `// Self-cleanup after animation completes`** → the `setTimeout(... remove ...)` says this; drop or 1-word.
- **Line 8143: `// Spawn immediately, then interval`** → obvious from the two lines; drop.
- **Line 8145: `// New balloon roughly every 4.5s`** → the `4500` literal says it; drop.
- **Line 8153: `// Check for balloon collision`** → function is named `checkBalloonCollisions`; drop.
- **Line 8158: `// generous hit area`** → keep (explains the 0.8 magic number) OR shorten.
- Sweep the Conductor / Stationmaster / Shooting-Star / Cargo-Jingle blocks for the same pattern.

**Estimated savings: 12–18 LOC.** Zero functional change. Keep comments that explain *magic numbers* or *non-obvious why*; cut comments that restate the *what*.

### Target B — 3-line section-fence sandwiches re-introduced by Cycle 5 (~5–10 LOC)
Cycle 5 added new sections (`BALLOON SYSTEM` Day 90, `STATIONMASTER` Day 91, `CARGO JINGLES` Day 93) using the 3-line sandwich (top `=====` / title / bottom `=====`). The C3 Day 70 rule: a section needs **one** delimiter, not a closing twin. Candidate redundant-closing fences from the Cycle-5 additions and any survivors: evaluate the bottom `=====` lines at 8104, 11269 and the JS-comment sandwich headers. Collapse only the redundant *closing* fence; preserve the top header.

**Estimated savings: 5–10 LOC.** Identical to the C3 Day 70 pattern that cleared cleanly.

### Target C — last blank run + intra-function blank trims (~8–12 LOC)
- **Lines 7830–7831:** the single remaining ≥2 consecutive-blank run → collapse to 1.
- The 5 new Cycle-5 functions (esp. `spawnBalloon`, `checkBalloonCollisions`) carry generous single-blank separators inside short bodies. Trim the ones that don't separate logical phases — conservatively, preserving readability (LESSON-DAY71: don't strip every blank, only noise).

**Estimated savings: 8–12 LOC.**

### Target D — DRY the note-sequence audio pattern (~8–12 LOC, OPTIONAL / RISK-FLAGGED)
**Cargo Jingles (Day 93)** and **Whistle Songs (Day 61)** both iterate an array of frequencies and schedule oscillator notes on the shared audio context with near-identical scaffolding (`audioBegin`-style prelude → loop → `osc.start/stop` with per-step offset). A single `playNoteSequence(notes, {type, dur, step, vol, offset})` helper could cover both, plus possibly the per-color station melodies.

**BUT:** per LESSON-DAY71, we do **not** force DRY on intentional micro-optimized audio paths, and the two callers differ in envelope/vol/offset. **Ship D only if the diff stays clean and all SFX paths smoke-test green** (cargo logs/milk/mail/coal + all 5 whistle colors + station horn). If it feels lossy, **skip** and bank a smaller honest win. **Estimated savings: 8–12 LOC net.**

### What I'm NOT cutting
- **Legit section fences.** The 58 `=========` delimiters are mostly real multi-line block headers; only the *redundant closing twin* on Cycle-5-added sections is fair game (Target B).
- **Function count.** 352 functions, all named + referenced (0 orphans). Cutting for a count would hurt readability (LESSON-DAY71).
- **Cycle-5 magic-number comments.** Keep the ones explaining `0.8` hit radius, jingle frequencies, BFS depth — they're real *why*.
- **CSS.** No dead-rule suspects; Cycle-5 CSS (`.train-conductor`, `.floating-balloon`, `.stationmaster`, `.shooting-star`) all have live JS paths (verified: conductor/balloon/stationmaster/trail all spawn during play).
- **BUG-020 teardown wiring.** The +1 Harden LOC stays — it's a correctness fix, not flab.

---

## 4. Day-by-Day Plan

| Day | Theme | Target LOC Δ | Notes |
|---|---|---|---|
| **99 Sat** | Fresh Eyes Audit | 0 | This report. Hard ≤12,733, stretch ≤12,690, aspirational ≤12,657. |
| **100 Sun** | Simplify (Target A) | **−12 to −18** | Trim Cycle-5 inline redundant comments. |
| **101 Mon** | Code Cleanup (Target B + C) | **−13 to −22** | Collapse redundant closing fences + last blank run + conservative intra-fn blank trims. |
| **102 Tue** | DRY eval (Target D) | **−8 to −12 or 0** | Build `playNoteSequence` helper; ship ONLY if all SFX smoke-test green, else skip and hold the line. |
| **103 Wed** | Delight Polish | **+0 to +8** | Tiny kid-friendly addition inside an existing surface, within banked margin (LESSON-DAY72/87). |
| **104 Thu** | Validation + Cycle 5 Review | 0 | Live smoke test `?v=104&fresh=1`, full user flow, JS parse, 0 console errors, `reviews/prune-cycle-5-review.md`, commit/push/Telegram. |

**Cumulative target: −40 to −60 LOC.** Clears the hard rule with margin and beats the stretch (≤12,690). Aspirational (≤12,657, C3 parity) requires Target D to land clean — not forced.

> Note: Cycle 5 Prune spans Day 99 (Sat) → Day 104 (Thu), 6 calendar days. If the cron schedule compresses this to a Mon–Fri window, fold Target A+B into one Simplify day and keep the Validation day fixed; the LOC targets and hard rule are unchanged.

---

## 5. Risks & Watch-Items
1. **Target D (audio DRY) is the only risky cut.** Smoke-test every SFX path after refactor (cargo ×4, whistle ×5, station horn, sound-pack switch). If any note timing shifts audibly, revert. Per LESSON-DAY71, a held line beats a fragile DRY.
2. **Don't over-trim Cycle-5 blanks.** The new functions read cleanly *because* of their phase-separating blanks. Cut noise, not structure.
3. **Byte rule.** C3 and C4 both shrank bytes. C5 should too — comment trims are byte-cheap but real; track in build-reports.
4. **Delight polish stays off the toolbar.** Follow C3 Day 72 / C4 Day 87: additions live inside an existing modal or play-time behavior, never new chrome. 5-cycle streak is a feature.
5. **Smaller cut is OK.** This is the leanest codebase the factory has pruned. A clean −40 honest LOC beats a forced −76. The hard rule is net-negative; everything past that is bonus.

---

## 6. Live Smoke Test (this morning, Day 99)

Verified live on `?v=99&fresh=1&cb=prune5d1b` after `localStorage.clear()` + reload:

- ✅ Tutorial overlay auto-opens on cold boot (`display ≠ none`)
- ✅ Palette: 52 DOM nodes / 40 locked (26 logical / 20 locked — progression healthy)
- ✅ Settings: 3 section headers (🔊 Audio / 🖼️ Display / 🎮 Game)
- ✅ 13 overlays present; no new feature-modal vs Cycle 4
- ✅ `localStorage` after fresh load: only `trainTracks_stickers`
- ✅ `generateRandomTrack()` → 1 train
- ✅ Play-time ephemerals spawn: **1 conductor, 1 balloon, 2 stationmasters waving, 6 trail dots, 6 ambient critters**
- ✅ `stopPlay()` drains conductors / balloons / trail dots → **0** (BUG-020 hold: shooting-star interval cleared too)
- ✅ Stationmasters = 4 (one per station cell), 0 waving at rest — persistent decoration, not a leak
- ✅ **0 console errors** across clear → gen → play → stop sequence
- ✅ JS parse clean (`new Function` on inline script), div 188/188, button 55/55, 0 dead functions

**Anchor confirmed: 12,733 LOC / 455,636 bytes / 352 functions. Prune Week 5 is live.**

---

*Audit by Mochi. The hard rule is numbers, not vibes. C2/C3/C4 all cleared their numeric rules and 3 of 4 went net-negative. Cycle 5 is the leanest input yet — the win this week is an honest net-negative, not a record chase.*
