# 🚂 Train Tracks — Cycle 5 Prune Review (Day 104)

**Review date:** July 2, 2026
**Build:** Day 104 (close-out of Prune Week 5 — Cycle 5 of the post-90-day extension)
**Codebase:** Single `index.html`, **12,718 lines / 455,567 bytes / 354 functions**
**Site under review:** https://mikedyan.github.io/train-tracks/?v=104&fresh=1&cb=cycle5closeout
**Reviewer:** Mochi (factory orchestrator, fresh-eyes panel of one)
**Baselines:** `reviews/prune-cycle-1-review.md` (Day 43), `-2-` (Day 58), `-3-` (Day 73), `-4-` (Day 88), `PRUNE_REPORT.md` (Day 99)

---

## 🎯 Executive Summary

**Cycle 5 is the asymptote cycle Cycle 4's review predicted — and that's the honest headline.** For four straight cycles the prune got deeper (+55 → −36 → −76 → −95 LOC) and the score climbed (8.3 → 8.4 → 8.6 → 8.7). Cycle 5 breaks both trends *on purpose*: the prune is the smallest net-negative of the disciplined era (**−15 LOC, −69 bytes**), and the overall score **holds at 8.7** rather than reflexively ticking up. Both outcomes are correct, and both were foreseeable.

**Why the prune shrank.** The Day 99 Fresh-Eyes Audit opened at 12,733 LOC with the classic prune veins already near-exhausted — 1 blank run ≥2, 0 dead functions, 6-cycle-flat chrome. The factory had spent Cycles 2–4 harvesting the fat (DRY meat, comment preambles, closing-fence dedup, blank runs). Entering Cycle 5, there simply wasn't 95 lines of honest cut left. The week's four working days (Simplify / Code Cleanup / DRY / Delight) returned −8 / −4 / −6 / +3 LOC — every one an *honest* number below its own estimate, because LESSON-DAY71 says don't force cuts that hurt readability. **A −15 net-negative on a codebase this lean is a pass, not a miss.** The hard rule (≤12,733) cleared by 15; the stretch (≤12,690) was missed by 28 and correctly not chased.

**Why the score held.** Build Week 5 shipped five more polish-tier delights — 🐾 Conductor Companion, 🎈 Floating Balloons, 👋 Waving Stationmasters, ⭐ Shooting Stars, 🎵 Cargo Jingles — all additive play-time behavior, **zero** new toolbar buttons / settings tiles / modals (**6-cycle chrome-stability streak**). They deepen the "alive in motion" feeling (the color-matched companion pet is the strongest single kid-magnet of the set — a 5-year-old *will* squeal that their red train has a kitty riding it, and cargo jingles finally give each cargo type an audio identity). But — exactly as the Cycle 4 review warned — polish layered on polish asymptotes. Uniqueness, Replayability, and Addictiveness are structurally unchanged because Cycle 5, like Cycle 4, made **no reshape move** (no co-op, no campaign, no level editor). Honest scoring means holding, not inflating.

**Harden Week 5 found 1 bug** — BUG-020, a `stopShootingStars()` teardown that was defined (Day 92) but never wired into `stopPlay()`, leaking the night-mode spawn interval + lingering star nodes. Day 97 fixed it same-day with a one-line call (+1 LOC), and the build-week close anchored at 12,732 → Harden close 12,733 (+1 net). Reachable only in night-mode play, bounded, self-healing next play — a P2, found and closed inside the window.

**Overall score: 8.7/10** (= Day 88, vs Day 73: 8.6, Day 58: 8.4, Day 43: 8.3). Held, not gained. The delight layer is genuinely richer; the structural ceiling is genuinely unmoved.

---

## 📊 Scoring (1–10) vs Day 88 baseline

| Dimension | D58 | D73 | D88 | D104 | Δ vs 88 | Notes |
|---|---|---|---|---|---|---|
| **First Impression** | 9 | 9 | 9 | **9** | 0 | Tutorial still auto-opens on fresh `localStorage` (verified live `?v=104&fresh=1` — only `trainTracks_stickers` written, tutorial `.open`). The new Day-103 hero balloon (first floating balloon of each session spawns 1.6× as the classic red 🎈) adds a first-seconds delight, but the *opening* — cold grid + tutorial — is intentionally unchanged. |
| **Clarity** | 9 | 9 | 9 | **9** | 0 | Toolbar shape unchanged from Day 73: Play / Random / Clear / Undo / Redo / speed + second row of round icons. Settings 8 tiles / 3 groups. Palette 52 pieces (40 locked fresh). **6-cycle chrome stability** — five more features, still 0 toolbar buttons / 0 settings tiles / 0 modals added. |
| **Core Loop** | 9 | 9 | 9 | **9** | 0 | Drag → place → ▶️ → 📯 → 📦 → 🛤️. Cargo Jingles now play a 3-note pickup melody per cargo type, but it's a reward layered onto pickup, not a new step. |
| **Difficulty Curve** | 8 | 9 | 9 | **9** | 0 | Progression healthy: 40/52 palette items locked on fresh `localStorage` (verified live, identical to D88). No regression from the 5 stat-neutral ambient features. |
| **Juice/Polish** | 9 | 9 | 10 | **10** | 0 | Held at ceiling. Cycle 5 stacks companion pets (color-matched per train) + drifting balloons (poppable) + waving stationmasters + night-mode shooting stars + per-cargo jingles on top of the Cycle-4 alive-in-motion base. Every train, every station, every cargo now has its own feedback layer. Zero jank across today's flow. Already a 10 at D88; even richer now, but the scale caps here. |
| **Replayability** | 8 | 9 | 9 | **9** | 0 | Sticker Book + Replay Sharing v3 still carry this. Cycle 5's additions are ambient delight, not new replay hooks. Hold. |
| **Uniqueness** | 7 | 8 | 8 | **8** | 0 | The Cycle-3 combo (stickers + replay-share + whistles + sound packs) remains the differentiator. Cycle 5 is polish, not a new axis. Hold. |
| **Bug-Free** | 9 | 9 | 9 | **9** | 0 | Harden Week 5 found 1 bug (BUG-020, night-mode teardown leak), fixed same-day Day 97, verified through Day 98 regression (14/14). 0 open bugs entering this review, 0 console errors across today's full 11-action flow. |
| **Visual Design** | 9 | 9 | 9 | **9** | 0 | Today's post-random screenshot (rectangular loop, red train, 2 tunnels, 2 stations with green signal dots, milk-can cargo, full scenery field of houses/trees/sheep/sunflowers/horses/cow, stationmaster figures) reads as a kid's storybook. Companion pet + balloons add life without clutter. |
| **Addictiveness** | 7 | 8 | 8 | **8** | 0 | Sticker Book still the hook. The companion pet is a genuine "I want to see all 5 animals" micro-pull (red🐱/blue🐶/green🐸/yellow🐤/purple🦄), but no UI surfaces it as a collection goal — kids discover it by swapping train colors. A real nudge, not enough to move the composite. Hold. |

### **Overall: 8.7/10** (= D88, vs D73: 8.6, D58: 8.4, D43: 8.3)

**Net change: 0.0 — the first flat cycle-over-cycle score.** This is the honest read, not a stumble. Cycle 4's review said plainly: *"eventually the next gain will require a structural move (a true co-op mode, a campaign, or a level editor)."* Cycle 5 shipped another polish cycle instead — beautiful, disciplined, kid-delighting polish — but polish-on-polish asymptotes. The Juice/Polish dimension has been maxed at 10 since D88; the structural dimensions (Uniqueness/Replayability/Addictiveness) can't move without a reshape. **Holding at 8.7 with reasons beats inflating to 8.8 without them.**

---

## 🏆 The headline metric: code health (5-cycle view)

| Metric | C1 Prune | C2 Prune | C3 Prune | C4 Prune | C5 Prune | Verdict |
|---|---|---|---|---|---|---|
| Lines start | 10,089 | 11,192 | 11,866 | 12,485 | **12,733** | — |
| Lines end | 10,144 (**+55**) | 11,156 (**−36**) | 11,790 (**−76**) | 12,390 (**−95**) | **12,718 (−15)** | ✅ net-negative |
| Hard rule | ≤9,900 | ≤11,192 | ≤11,866 | ≤12,485 | **≤12,733** | ✅ cleared by 15 |
| Stretch | — | — | ≤11,830 | ≤12,449 | **≤12,690** | ❌ missed by 28 (not chased) |
| Bytes start | ~345 KB | 297 KB | 422,935 | 448,624 | **455,636** | — |
| Bytes end | 349 KB (+4 KB) | 391 KB (+94 KB) | 419,531 (**−3,404**) | 443,247 (**−5,377**) | **455,567 (−69)** | ✅ net-negative |
| Functions start | ~270 | 317 | 325 | 343 | **352** | — |
| Functions end | 274 (+4) | 306 (−11) | 325 (0) | 343 (0) | **354 (+2)** | DRY helper +1, honest |
| Harden bugs found | 14 | 4 | 0 | 1 | **1** | fixed same-day |
| Open bugs exiting | 0 | 0 | 0 | 0 | **0** | ✅ |
| Console errors live | 0 | 0 | 0 | 0 | **0** | ✅ |
| New toolbar buttons | +2 | 0 | 0 | 0 | **0** | ✅ 6-cycle stability |
| New settings tiles | +1 | 0 | +1 | 0 | **0** | ✅ |
| New modals | +3 | +2 | 0 | 0 | **0** | ✅ |

**Five observations:**

1. **The prune floor is real.** Four cycles of deepening cuts drained the classic veins (DRY meat harvested C2, comment preambles C3–C4, closing-fence dedup C3+C5, blank runs C3+C5). Cycle 5 opened with 1 blank run ≥2 and 0 dead functions — there was no 95-line seam left. −15 is the honest floor of a mature codebase, not a discipline lapse. **The right lesson: net-negative is the win; the *magnitude* is a function of how much fat the previous cycles left behind, and they left very little.**
2. **Function count ticked +2 — and that's fine.** Day 102's `playNoteSequence(notes,type,dur,vol,offset,step)` DRY helper consolidated the identical melody loop from `playWhistleSong` (Day 61) + `playCargoJingle` (Day 93). It *added* a function while *removing* duplicated loop bodies (−6 LOC net). Function count is not the metric; duplication is. This was a genuine de-dupe (Rule 3), verified byte-identical on SFX smoke-test.
3. **Chrome stability is now a 6-cycle, 25-feature streak.** Cycles 2/3/4/5 each added 0 toolbar buttons. Five Cycle-5 features, all auto-on play-time behavior. The "feature = behavior, not chrome" architecture (LESSON-DAY46-F) is the single most durable win of the whole run.
4. **Harden bugs steady at 1.** C3=0, C4=1, C5=1. The bug surface densifies with each cycle's feature stack, but both C4 and C5 bugs were reachable in a narrow path, found in-window, fixed same-day with single-digit LOC. The factory doesn't make many bugs and closes them fast — that muscle is mature.
5. **Bytes net-negative for the 3rd straight cycle** (−3,404 → −5,377 → −69). The −69 is razor-thin, but it's under the transferred byte ceiling (≤455,636), and Day 103 *trimmed its own hero-balloon comment ~93 B to land honestly under* rather than pad the report. **Honesty over vanity margin.**

---

## ✂️ What Prune Week 5 Specifically Achieved

### Day-by-day haul

| Day | Theme | LOC Δ | Bytes Δ | Highlights |
|---|---|---|---|---|
| 99 (Sat) | Fresh Eyes Audit | 0 | 0 | PRUNE_REPORT.md. Hard ≤12,733, stretch ≤12,690, aspirational ≤12,657. Targets A/B/C/D scoped; classic veins flagged near-exhausted. |
| 100 (Sun) | Simplify (Target A) | **−8** | −269 | 8 redundant Cycle-5 inline comments (6 balloon + 2 shooting-star) collapsed. Comment-only, zero functional change. |
| 101 (Mon) | Code Cleanup (Target B+C) | **−4** | −175 | 3 redundant closing fences + last blank run (2→1). 0 blank runs ≥2 remain — consecutive-blank vein fully exhausted. |
| 102 (Tue) | DRY Eval (Target D) | **−6** | +92 | `playNoteSequence` helper de-dupes Whistle + Cargo melody loops. Conditional-ship gate (LESSON-DAY71) honored — SFX smoke-test green, byte-identical freqs/waveforms/timing. |
| 103 (Wed) | Delight Polish | +3 | +283 | 🎈 Hero Balloon — first floating balloon of each play session spawns 1.6× as the classic red 🎈 (mirrors Day-87 hero critter). 3 surgical lines. Trimmed own comment ~93 B to land under byte ceiling. |
| 104 (Thu) | Validation | 0 | 0 | This review. Live smoke test, scoring, push, report. |

**Net: −15 lines, −69 bytes. Hard rule cleared by 15. Stretch (−43) missed by 28 and not chased.**

### Wins

1. **Every day returned an honest number below its own estimate — and none were padded.** −8 (est −12..18), −4 (est −13..22), −6 (est −8..12), +3 (est +0..8). LESSON-DAY71 held every single day: don't force phase-separating blanks or why-comment removals that hurt readability just to hit a number. The factory *chose* the smaller honest cut four times running.
2. **Genuine DRY, not cosmetic churn (Day 102).** The `playNoteSequence` extraction is the first real de-duplication since Cycle 2's function harvest — two independently-written melody loops (Whistle Day 61, Cargo Day 93) collapsed to one helper, smoke-tested byte-identical. That's the Target-D risk gate from the PRUNE_REPORT paying off: ship only if green, and it was.
3. **Delight inside a closet for the 3rd cycle running (Day 103).** Hero balloon is +3 LOC / +283 B, lives entirely inside the balloon system (module flag + reset + one guard in `spawnBalloon`), surfaces nothing new on the chrome. Verified live today: with `heroPending=true`, a forced `spawnBalloon()` rendered a **29.46px red 🎈** (base ×1.6 = 28.8px threshold cleared) — hero mechanism confirmed working on the deployed build.
4. **Both axes net-negative, byte ceiling respected to the byte.** −15 LOC / −69 B, exit 455,567 under the 455,636 ceiling. Day 103 chose to trim its own verbosity rather than pad — the honesty discipline is now reflexive.
5. **The PRUNE_REPORT correctly forecast the floor.** Day 99 wrote: *"Classic veins near-exhausted… Win = honest net-negative, not a record chase."* The week executed exactly that thesis. The report is now a genuine strategic instrument (3rd cycle running), not a to-do list.

### Misses

1. **Stretch goal (≤12,690) missed by 28 lines.** Not chased — correctly. But it's the first stretch miss since the goal was introduced, and it signals the codebase has hit its lean floor under the current comment/blank/DRY toolkit. **Future prune weeks should set the stretch relative to available seams, not relative to prior-cycle magnitudes.** Chasing −95 again would require inventing cuts that hurt the code.
2. **The 🧑 Passengers-button discoverability debt is now flagged in 4 consecutive PRUNE_REPORTs (C3, C4, C5) and still unactioned.** It's correctly out of scope for prune weeks (it's a UX-surface change), but it's the longest-standing carried item. **Must be a Build-week priority if the factory runs Cycle 6.**
3. **Tutorial still 3 steps for a now-13-feature play surface.** The hero critter (D87) and hero balloon (D103) partially address "kids may miss the ambient features," but a returning-player tour for Companions / Stationmasters / Shooting Stars / Cargo Jingles / Stickers / Sound Packs remains unbuilt. Carried from C4.

---

## 🐛 Bug & Code Health Detail

- **Open bugs:** 0 (Harden Week 5 closed clean Day 98 after BUG-020 same-day fix Day 97; Prune Week 5 introduced 0 new bugs).
- **JS parse:** clean (`node --check` on extracted script block, verified today).
- **Functions in file:** 354 (352 entering prune + `playNoteSequence` DRY helper Day 102; net +2 across the extension via genuine de-dup).
- **File size:** 12,718 LOC / 455,567 bytes (was 12,733 / 455,636 entering Prune Week 5; **−15 LOC, −69 bytes**).
- **HTML balance:** div 188/188, button 55/55, script 1/1, style 1/1.
- **Console errors live:** 0 (across the full Day-104 flow below).
- **Live smoke test summary (verified today on `?v=104&fresh=1&cb=cycle5closeout`, `localStorage.clear()` + reload):**
  - ✅ Served build current: char-count 454,540 (= 455,567 bytes; multi-byte emoji), 4 `balloonHeroPending` matches (Day-103 ship confirmed on Pages)
  - ✅ Cold boot: tutorial auto-opens, 96 grid cells, only `trainTracks_stickers` in `localStorage`
  - ✅ Progression: 52 palette pieces, 40 locked (`.palette-locked`) fresh
  - ✅ `generateRandomTrack()` → occupied track + train render; all 15 key functions present (`startBalloonSystem`, `spawnBalloon`, `playNoteSequence`, `startShootingStars`, `stopShootingStars`, etc.)
  - ✅ **Conductor Companion:** `startPlay()` → 1 🐱 conductor on the red train (color-matched)
  - ✅ **Floating Balloons + Hero:** balloons drift during play; on fresh play with `balloonHeroPending=true`, forced `spawnBalloon()` → **29.46px red 🎈** (>28.8px base×1.6 = hero confirmed)
  - ✅ **Waving Stationmasters:** 2 🧍 during play; persist per-station after stop (4 total, not a leak — matches Day 98)
  - ✅ **Shooting Stars:** night-mode play arms `shootingStarInterval` (true); forcing `maybeSpawnShootingStar()` ×20 → 7 `.shooting-star` nodes rendered
  - ✅ **Cargo Jingles:** `playCargoJingle('logs')` fires clean (no throw); `playNoteSequence` DRY helper live
  - ✅ Ambient critters (6, incl. Day-87 hero) + 8 station signals spawn during play
  - ✅ **BUG-020 hold:** `shootingStarInterval` set during play → **null after stop**; all ephemerals (conductor/balloons/critters/signals/stars/trails) drain to 0 on `stopPlay()`
  - ✅ Puzzles modal: 10 puzzles (First Loop, Around the Lake, Figure Eight, Tunnel Run, Grand Station…), cards render
  - ✅ `encodeGridState()` → 140-char share hash (v2 protocol length intact)
  - ✅ Save → clearAll → load round-trip: 16 cells → 0 → 16, byte-identical, `trainTracks_slot_1` written
  - ✅ Zero console errors across the entire 11-action sequence
  - ✅ Post-random screenshot: red train on a loop, 2 tunnels, 2 stations with green signal dots, milk-can cargo, full storybook scenery field

---

## 🔮 The 5-cycle arc — and what the flat score means

| Cycle | Build features | Harden bugs | Prune LOC Δ | Prune bytes Δ | Score |
|---|---|---|---|---|---|
| 1 (D29–43) | Horn, Animal Reactions, Weather, Crossings, Rainbow | 14 | +55 | +4 KB | 8.3 |
| 2 (D44–58) | Train Names, Big Grid, Cargo Missions, Track Replay, Sound Packs | 4 | −36 | +94 KB | 8.4 |
| 3 (D59–73) | Sky, Animal Passengers, Whistle Songs, Replay Sharing v3, Sticker Book | 0 | −76 | −3,404 | 8.6 |
| 4 (D74–88) | Critters, Station Signal, Confetti Cannon, Puddle Splashes, Train Trail | 1 | −95 | −5,377 | 8.7 |
| 5 (D89–104) | Conductor Companion, Floating Balloons, Waving Stationmasters, Shooting Stars, Cargo Jingles | 1 | **−15** | **−69** | **8.7** |

**The arc reads honestly now:**

1. **Score curve: 8.3 → 8.4 → 8.6 → 8.7 → 8.7.** The +0.1/+0.2/+0.1 gains slowed to +0.0. This is the asymptote, not a plateau of failure. Five cycles of polish have maxed every dimension that polish can touch (Juice hit 10 at C4; First Impression / Core Loop / Visual all at 9 ceilings). **The next 0.1 requires a reshape, not another delightful ambient behavior.**
2. **Prune curve: +55 → −36 → −76 → −95 → −15.** The deepening reversed because the fat ran out. −15 on a codebase with 0 dead functions and 0 blank runs ≥2 is a *healthy* floor, not regression. The metric that matters — *net-negative* — held for the 4th straight cycle.
3. **Chrome: flat through 25 features.** The durable architectural win. 6 cycles, 0 toolbar creep.
4. **Bugs: 14 → 4 → 0 → 1 → 1.** Steady-state low. The factory builds features that don't break the game.

The game grew from 10,089 LOC (Day 29) to **12,718 LOC (Day 104)** — **+2,629 LOC for 25 features + 5 prune weeks** — ~105 LOC/shipped-feature, *down* from 115 at C4 close. The per-feature footprint is still shrinking, which means prune discipline is outpacing feature complexity even as the raw prune magnitude falls.

### If there is a Cycle 6 — the recommendation shifts

Four prune cycles proved the factory can shrink code. Five build cycles proved it can add delight without chrome. **The unexplored axis is structural.** The score won't move again on polish. Concrete C6 candidates, in priority order:

1. **A reshape-tier feature.** Pick ONE: (a) a **puzzle campaign** with a starred world-map progression, (b) a **level editor** with shareable custom puzzles (leverages the existing v3 share codec), or (c) a lightweight **"play a friend's track" co-op/ghost-race** mode. Any of these could move Uniqueness/Replayability/Addictiveness off their 8-ceilings for the first time since C3.
2. **🧑 Passengers-button discoverability** — 4th-time-flagged, finally action it (promote to settings tile or rename). Build-week Day 1.
3. **Tutorial expansion / returning-player tour** for the now-13-feature surface.
4. **Reset the prune stretch goal to seams-available, not prior-magnitude.** Don't set ≤−40 again on a lean codebase — set the stretch by auditing actual harvestable lines in the Fresh-Eyes pass.

---

## 🏁 Verdict

Cycle 5 closes with the factory's **first flat cycle-over-cycle score (8.7 = 8.7)** and its **smallest net-negative prune (−15 LOC, −69 bytes)** — and both are the *correct, honest* outcomes for a fifth consecutive polish cycle on an already-lean, already-maxed-on-juice codebase. The extension exits with a game that:

- Ships **25 features across 5 build weeks**, 20 bugs fixed total, 0 customer-facing regressions
- Has **0 open bugs**, **0 console errors** on live deploy
- Weighs **455,567 bytes / 12,718 LOC** (net-negative prune in 4 of 5 cycles)
- Holds a **6-cycle chrome-stability streak** (0 toolbar buttons across 25 features)
- Auto-opens tutorial for fresh visitors; 40/52 palette pieces gated by progression
- Gives every train a **color-matched companion pet** (🐱🐶🐸🐤🦄), drifts **poppable balloons** (with a hero-sized red 🎈 first each session), waves **stationmasters** on arrival, arcs **shooting stars** in night play, and plays a **per-cargo jingle** on pickup
- Still does everything Cycle 4 did: critters, station signals, confetti cannon, puddle splashes, train trails, 12 stickers, 10 puzzles, v2+v3 share links, save/load, screenshot
- Scores **8.7/10** — Juice/Polish at a perfect 10, structural dimensions honestly held pending a reshape

**The hard rule worked for the 4th consecutive cycle. The prune discipline is now so effective that the codebase has hit its lean floor — the score can only climb again with a structural move, and the factory now knows it.** Five cycles, 104 days, 25 features, 20 bugs fixed, +26% codebase growth, net-negative prune in 4 of 5 cycles, and a game that a 5-year-old would genuinely squeal at.

**Cycle 5: complete. Game: ship-ready. Factory: has run out of fat to trim and delight to layer — Cycle 6, if it runs, should reshape. 🚂🐾🎈👋⭐🎵**

---

*Review by Mochi, factory orchestrator. Live-tested at https://mikedyan.github.io/train-tracks/?v=104&fresh=1&cb=cycle5closeout with `localStorage.clear()` + reload. Compared against `reviews/prune-cycle-1..4-review.md` and `PRUNE_REPORT.md` (Day 99). All scores are honest assessments — the flat 8.7 is deliberate, not a rubber stamp; polish-on-polish asymptotes and the next gain needs a structural move. Hard rule met on both LOC and bytes because both were written with numbers, not vibes. The stretch goal was missed and correctly not chased — forcing cuts on a lean codebase violates LESSON-DAY71.*
