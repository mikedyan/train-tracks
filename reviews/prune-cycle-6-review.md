# 🚂 Train Tracks — Cycle 6 Prune Review (Day 119)

**Review date:** July 17, 2026
**Build:** Day 119 (close-out of Prune Week 6 — Cycle 6 of the post-90-day extension)
**Codebase:** Single `index.html`, **12,890 lines / 467,691 bytes / 357 functions**
**Site under review:** https://mikedyan.github.io/train-tracks/?v=119&fresh=1&cb=cycle6closeout2
**Reviewer:** Mochi (factory orchestrator, fresh-eyes panel of one)
**Baselines:** `reviews/prune-cycle-1-review.md` (Day 43) through `-5-` (Day 104), `PRUNE_REPORT.md` (Day 115)

---

## 🎯 Executive Summary

**Cycle 6 is the reshape cycle — and it broke the score asymptote exactly as Cycle 5's review said it would need to.** For two straight cycles the overall score held flat at 8.7 because Cycles 4 and 5 were polish-on-polish, and polish asymptotes. The Cycle 5 review's verdict was blunt: *"The score won't move again on polish. The next gain needs a structural move — a puzzle campaign, a level editor, or a co-op mode."* Cycle 6 built the first of those. The flat 🧩 Challenge-Puzzles card list became the 🗺️ **Adventure Journey** — a winding, star-gated town-to-town map of 12 stops across 5 themed regions, with a riding 🚂 marker, a bouncing "🎫 All aboard!" frontier beckon, a gold route that draws itself in as you progress, a finish-line certificate, and a 🏁 Trailblazer sticker. This is the first structural reshape in six cycles, and it moves three dimensions that five prior polish cycles could not touch: **Uniqueness 8→9, Replayability 9→10, Addictiveness 8→9.**

**Overall score: 8.9/10** (vs Cycle 5 & 4: 8.7, Cycle 3: 8.6). **Net +0.2 — the first gain in three cycles**, and unlike the C3→C4 bump it came from a *structural* axis, not another delightful ambient behavior. The reshape did what the factory had run out of fat and polish to do.

**The reshape was cheap because the bones were stable.** Build Week 6 (Days 105–109) added the entire Adventure Journey for **+174 LOC** — under the +310–540 roadmap estimate — by laying a new spine (`ADVENTURE_STOPS` ordered list, `isAdventureStopUnlocked`, `startAdventureStop`, `renderAdventureMap`) over the *unchanged* puzzle engine. Stops reference existing `PUZZLES` ids, gate on the existing `getPuzzleStars()`, and clicks call the unchanged `loadPuzzle()`. Two brand-new ultra-easy warm-up puzzles (First Track, Round the Bend) were prepended as a gentle on-ramp, and a 4th tutorial step now points first-timers at the journey — quietly closing the 4×-flagged Passengers/discoverability debt with a wayfinder. The reshape spent exactly **one** chrome change in six cycles: the modal heading swap (🧩 Challenge Puzzles → 🗺️ Adventure Journey). That is the whole chrome cost of a structural reshape — the "feature = behavior, not chrome" architecture held even through a spine transplant.

**Harden Week 6 (Days 110–114) was a 5-day clean sheet — 0 bugs, file flat at 12,892 LOC all week.** The new journey system, all 12 stops, passenger delivery, all 10 unlock milestones, the 140-char v2 share round-trip, and every platform/edge case (mobile 375px, pinch-zoom clamps, keyboard-only nav, 4 biomes × night × high-contrast, cold start, stress) all passed with zero console errors. The reshape did not destabilize a single existing surface.

**Prune Week 6 (Days 115–118) returned −2 LOC / −137 bytes** — the smallest net-negative yet, and honestly so. The Day 115 Fresh-Eyes Audit opened at 12,892 LOC with the classic veins already mined out (0 dead functions, 0 blank runs ≥2, 55 file fences with no closing twins), so the only harvestable material was the fresh +174 LOC of reshape code. Day 116 trimmed 4 restate-the-WHAT comments (−4), Day 117 confirmed Targets B/C were empty and shipped one provably-lossless `renderAdventureMap` DRY fold (−2), and Day 118's Delight Polish added the first-loop hero confetti (+4). Both axes stayed net-negative vs the anchor. **On a codebase this lean, −2 is the win; forcing −40 would violate LESSON-DAY71.**

---

## 📊 Scoring (1–10) vs Day 104 baseline

| Dimension | D73 | D88 | D104 | **D119** | Δ vs 104 | Notes |
|---|---|---|---|---|---|---|
| **First Impression** | 9 | 9 | 9 | **9** | 0 | Cold boot unchanged (grid + auto-opening 4-step tutorial, verified live: only `trainTracks_stickers` in `localStorage`, 96 cells, tutorial `.open`). The journey's warm-up on-ramp + the new 4th tutorial step ("🗺️ Go on an Adventure!") strengthen the *second* impression, but the literal first frame is still the grid. Hold. |
| **Clarity** | 9 | 9 | 9 | **9** | 0 | Toolbar shape unchanged. The reshape reused `#puzzle-overlay` and spent exactly one chrome change in six cycles (modal heading 🧩→🗺️). 7-cycle chrome stability. Hold. |
| **Core Loop** | 9 | 9 | 9 | **9** | 0 | Drag → place → ▶️ → 📯 → 📦 → 🛤️ intact. The journey wraps the puzzle loop; it doesn't alter the sandbox loop. Verified live: random track → play (1 animated train + 6 critters + 1 balloon) → stop (all drain to 0). Hold. |
| **Difficulty Curve** | 9 | 9 | 9 | **9** | 0 | Genuinely improved by the 2 warm-up stops (First Track: place 2 straights, auto-orients; Round the Bend: place 2 curves) + 12-stop star-gate — the smoothest onboarding ramp the game has ever had. Held at 9 rather than bumped because palette gating (40/52 locked fresh) is unchanged; the *puzzle* ramp is now excellent. |
| **Juice/Polish** | 9 | 10 | 10 | **10** | 0 | Ceiling. Day 118 added the first-loop hero confetti (42 particles first loop of a session vs 25 after) on top of the drawn-in gold journey route, region bands, riding train, and bouncing beckon. Verified live: first burst 42, consumed, second 25, new session 42. Caps at 10. |
| **Replayability** | 9 | 9 | 9 | **10** | **+1** | The star-gated 12-stop journey gives a real "clear the whole line" arc the flat card list never had: frontier beckon pulls you to the next stop, the gold route draws in behind you, and a completion certificate ("You rode the whole line — 36/36") + 🏁 Trailblazer sticker cap it. Sticker Book + v3 replay-share still carry the sandbox. Genuine new replay hook → 10. |
| **Uniqueness** | 8 | 8 | 8 | **9** | **+1** | The Adventure Journey is a genuine new structural axis — a themed, riding-train progression map — not another ambient delight. First structural reshape in six cycles. Combined with the existing stickers + replay-share + whistles + sound packs, the game now has a *campaign spine* few kid track-builders offer. → 9. |
| **Bug-Free** | 9 | 9 | 9 | **9** | 0 | Harden Week 6 = 5 consecutive clean sheets, 0 bugs, 0 console errors. Reshape introduced 0 bugs. 0 open bugs entering this review; 0 console errors across today's full cold-boot → journey → build → play → stop → confetti → save/load → share → puzzle-load flow. |
| **Visual Design** | 9 | 9 | 9 | **9** | 0 | The journey map screenshot reads as a storybook trail: green pulsing First Track flag with 🚂 + "All aboard!" pill, grey 🔒 locked stops on a dashed rail, translucent 🌱 Warm-Up / 🌳 Meadow / ⛰️ Hills / 🏜️ Desert / 🌙 Night region bands. Gorgeous, but Visual Design was already a mature 9. Hold. |
| **Addictiveness** | 8 | 8 | 8 | **9** | **+1** | The journey's forward pull is real: the frontier beckon literally says "All aboard!", each star opens the next stop, and the certificate is a completion goal. This is the pull-forward hook the flat list lacked. → 9. |

### **Overall: 8.9/10** (vs D104: 8.7, D88: 8.7, D73: 8.6, D58: 8.4, D43: 8.3)

**Net change: +0.2 — the first gain in three cycles, and the first ever driven by a structural reshape rather than polish.** Three structural dimensions moved (Uniqueness/Replayability/Addictiveness), exactly the three the last two reviews said were pinned at their ceilings pending a reshape. The polish dimensions stayed at their (already-maxed) values. This is the honest read: the reshape unlocked the gain that five polish cycles couldn't.

---

## 🏆 The headline metric: code health (6-cycle view)

| Metric | C2 Prune | C3 Prune | C4 Prune | C5 Prune | **C6 Prune** | Verdict |
|---|---|---|---|---|---|---|
| Lines start | 11,192 | 11,866 | 12,485 | 12,733 | **12,892** | — |
| Lines end | 11,156 (−36) | 11,790 (−76) | 12,390 (−95) | 12,718 (−15) | **12,890 (−2)** | ✅ net-negative |
| Hard rule | ≤11,192 | ≤11,866 | ≤12,485 | ≤12,733 | **≤12,892** | ✅ cleared by 2 |
| Stretch | — | ≤11,830 | ≤12,449 | ≤12,690 | **≤12,862** | ❌ not chased (lean floor) |
| Bytes start | 297 KB | 422,935 | 448,624 | 455,636 | **467,828** | — |
| Bytes end | 391 KB | 419,531 (−3,404) | 443,247 (−5,377) | 455,567 (−69) | **467,691 (−137)** | ✅ net-negative |
| Functions end | 306 | 325 | 343 | 354 | **357 (+3)** | 3 Adventure fns, honest |
| Harden bugs found | 4 | 0 | 1 | 1 | **0** | clean sheet week |
| Open bugs exiting | 0 | 0 | 0 | 0 | **0** | ✅ |
| Console errors live | 0 | 0 | 0 | 0 | **0** | ✅ |
| New toolbar buttons | 0 | 0 | 0 | 0 | **0** | ✅ 7-cycle stability |
| New modals | +2 | 0 | 0 | 0 | **0** | ✅ (reshape reused `#puzzle-overlay`) |

**Five observations:**

1. **A structural reshape cost +174 build LOC and 0 net chrome.** The spine-over-bones approach — new ordered-list data + 3 render/gate functions over an untouched puzzle engine — is why the Adventure Journey landed under estimate and without destabilizing anything. The only chrome spend in six cycles was one modal heading swap. This validates the "feature = behavior, not chrome" architecture at reshape scale, not just delight scale.
2. **The prune floor is now bedrock.** −2 LOC is the smallest net-negative of the run, and correctly so: entering Day 115 the codebase had 0 dead functions, 0 blank runs ≥2, and 55 fences with no closing twins. The only material was the fresh reshape code, and Days 116–117 harvested exactly the honest amount from it (comment restatements + one lossless DRY fold). Net-negative held for the 5th straight cycle; magnitude is a function of prior-cycle discipline, and prior cycles left almost nothing.
3. **Harden Week 6 was the cleanest yet — 0 bugs across a post-reshape week.** C2=4, C3=0, C4=1, C5=1, C6=0. A brand-new structural system passed a full 5-day audit (feature, puzzle/mode, platform/edge, fix-everything, regression) with zero findings. The reshape was built right the first time.
4. **Function count +3, all load-bearing.** `isAdventureStopUnlocked`, `startAdventureStop`, `renderAdventureMap` — no dead functions created (renderStarDisplay was reused for node stars). Function count isn't the metric; duplication is, and there's none.
5. **Bytes net-negative for the 4th straight cycle** (−3,404 → −5,377 → −69 → −137). Thin but real, under the ≤467,828 anchor, and Day 118's delight (+395 B) was absorbed while still landing net-negative for the week.

---

## ✂️ What Cycle 6 Specifically Achieved

### Build Week 6 (Days 105–109) — the reshape, +174 LOC

| Day | Feature | LOC Δ |
|---|---|---|
| 105 | 🗺️ Adventure Journey Map (flat card list → star-gated 10-stop spine) | +59 |
| 106 | 🚂 Journey Train marker + region color-coding (Meadow/Hills/Desert/Night) | +40 |
| 107 | 🎫 Next-Stop beckon + 🏁 Trailblazer sticker | +17 |
| 108 | 🌱 Warm-up stops (First Track + Round the Bend) — 12-stop serpentine | +32 |
| 109 | 🎉 Completion certificate + drawn-in gold route + tutorial wayfinder | +26 |

Under the +310–540 roadmap estimate — the bones were stable, so the spine was cheap.

### Prune Week 6 day-by-day haul

| Day | Theme | LOC Δ | Bytes Δ | Highlights |
|---|---|---|---|---|
| 115 (Mon) | Fresh Eyes Audit | 0 | 0 | PRUNE_REPORT.md. Hard ≤12,892, stretch ≤12,862. Targets A–D scoped against the fresh reshape code; classic veins flagged mined-out. |
| 116 (Tue) | Simplify (Target A) | **−4** | −446 | 4 restate-the-WHAT reshape comments merged/cut; every WHY/provenance comment kept. Comment-only, zero functional change. |
| 117 (Wed) | Code Cleanup (Target B+C) | **−2** | −86 | Targets B (closing fences) + C (blank runs) confirmed 0-material. Shipped one provably-lossless `renderAdventureMap` single-pass DRY fold (reached/beckon loops → one forEach), full 3-state browser smoke-test before ship. |
| 118 (Thu) | Delight Polish | +4 | +395 | 🎉 First-loop hero confetti — the first Full Loop of each session bursts 42 particles vs 25 after. Optional Target D honestly skipped (0 LOC available). |
| 119 (Fri) | Validation | 0 | 0 | This review. Live smoke test, scoring, push, report. |

**Net: −2 lines, −137 bytes. Hard rule (≤12,892) cleared by 2. Stretch (≤12,862) not chased — correctly, per LESSON-DAY71.**

### Wins

1. **The reshape the last two reviews demanded — shipped, stable, and score-moving.** C4 and C5 both said the next gain needed a structural move. C6 delivered the Adventure Journey, it passed a 0-bug Harden week, and it moved 3 structural dimensions. The factory read its own review and acted on it.
2. **+174 LOC for a full campaign spine, 0 net chrome.** Data + 3 functions over an untouched engine. The reshape reused `#puzzle-overlay` (no new modal) and reused `renderStarDisplay` (no dead function).
3. **The warm-up on-ramp quietly closed the longest-standing debt.** First Track + Round the Bend are auto-solvable with zero manual rotation (`findBestRotation` orients between locked neighbors), and the new tutorial step points first-timers straight at the journey — addressing the 4×-flagged discoverability item with a wayfinder instead of a new button.
4. **Every prune day returned an honest number.** −4 (est −10..−16), −2 (est −10..−18), +4 (delight). LESSON-DAY71 held: Day 117 refused to invent nonexistent fence/blank cuts and shipped one real lossless fold instead, smoke-tested across all 3 journey states before touching the freshly-shipped reshape (Risk #1 honored).
5. **0 console errors on a full post-reshape live flow.** Cold boot → journey render (12 nodes/1 beckon/5 bands/base rail/train/"0/12 stops") → random track → play → stop-drain → hero confetti (42/25/42) → save-load byte-identical → share encode/decode → puzzle load — all green.

### Misses

1. **Stretch (≤12,862) not reached — but correctly not chased.** Second straight cycle at the lean floor. The stretch should keep being set from seams-available in the Fresh-Eyes pass, not from prior-cycle magnitudes.
2. **First Impression / Difficulty Curve held at 9 despite genuine improvement.** The warm-up ramp and journey wayfinder make the *second* thirty seconds much better, but the literal cold-boot frame (grid + tutorial) and palette gating are unchanged, so the dimensions honestly held.
3. **The 12-stop journey may be long for a true first-timer.** Flagged in the Day 115 audit as carried Build debt — a region-collapse/resume affordance is the natural next refinement, out of scope for prune.

---

## 🐛 Bug & Code Health Detail

- **Open bugs:** 0. Harden Week 6 = 5 consecutive clean sheets (Days 110–114), 0 bugs found; Prune Week 6 introduced 0 new bugs.
- **JS parse:** clean (`node --check` on the 347,349-byte extracted inline script, verified today).
- **Functions in file:** 357 (354 entering Cycle 6 + `isAdventureStopUnlocked` / `startAdventureStop` / `renderAdventureMap`). 0 duplicate function names.
- **File size:** 12,890 LOC / 467,691 bytes (Prune Week 6: −2 LOC / −137 bytes from the 12,892 / 467,828 anchor).
- **HTML balance:** div 197/197, button 55/55, span 104/104, script 1/1, style 1/1, svg 2/2 — all balanced.
- **Console errors live:** 0.
- **Live smoke test summary** (verified today on `?v=119&fresh=1&cb=cycle6closeout2`, `localStorage.clear()` + reload):
  - ✅ Served build current: 466,608 chars (= 467,691 bytes, multi-byte emoji); 4 `loopHeroPending` + 4 `balloonHeroPending` matches (Days 118/103 ships confirmed on Pages)
  - ✅ Cold boot: tutorial auto-opens (4 steps), 96 grid cells, 40 palette pieces locked fresh, only `trainTracks_stickers` in `localStorage`
  - ✅ **Adventure Journey:** heading "🗺️ Adventure Journey", 12 nodes, 1 frontier beckon, 5 region bands, 1 base rail, 1 riding 🚂, "0/12 stops" (screenshot evidence: green pulsing First Track w/ "All aboard!" pill + flag, grey 🔒 locked stops on dashed rail, Warm-Up + Meadow region bands)
  - ✅ **Core loop:** `generateRandomTrack()` → 44 grid entries filled (track + scenery); `startPlay()` → 1 `.animated-train` + 6 critters + 1 balloon; `stopPlay()` → all ephemerals drain to 0, `state.trains` = 1 (BUG-019 guard holds)
  - ✅ **Day-118 hero confetti:** first loop 42 `.confetti-particle` (hero), flag consumed to false, second loop 25 (classic), simulated new session (`loopHeroPending=true`) → 42 again — per-session reset works
  - ✅ **Save/load:** `saveToSlot(1)` → clear → `loadFromSlot(1)` → grid byte-identical (`loadIdentical=true`)
  - ✅ **Share:** `encodeGridState()` → 135-char v2 hash (prefix `AggMAAAA`); `decodeGridState()` → success
  - ✅ **Puzzle load:** `loadPuzzle(11)` (First Track) loads clean, no throw
  - ✅ **Zero console errors** across the entire multi-action session

---

## 🔮 The 6-cycle arc — and what the +0.2 means

| Cycle | Theme | Build features | Harden bugs | Prune LOC Δ | Score |
|---|---|---|---|---|---|
| 1 (D29–43) | Effects | Horn, Animals, Weather, Crossings, Rainbow | 14 | +55 | 8.3 |
| 2 (D44–58) | Systems | Names, Big Grid, Cargo, Replay, Sound Packs | 4 | −36 | 8.4 |
| 3 (D59–73) | Depth | Sky, Passengers, Whistles, Replay v3, Stickers | 0 | −76 | 8.6 |
| 4 (D74–88) | Alive | Critters, Signals, Confetti, Puddles, Trail | 1 | −95 | 8.7 |
| 5 (D89–104) | Polish | Conductor, Balloons, Stationmasters, Stars, Jingles | 1 | −15 | 8.7 |
| 6 (D105–119) | **Reshape** | **🗺️ Adventure Journey** (map, train, beckon, warm-ups, certificate) | **0** | **−2** | **8.9** |

**The arc now reads:**

1. **Score: 8.3 → 8.4 → 8.6 → 8.7 → 8.7 → 8.9.** The flat C4→C5 was the polish asymptote; the C5→C6 **+0.2** is the reshape breaking it. Crucially, this gain came from the *structural* dimensions (Uniqueness/Replayability/Addictiveness), which is the only place the score had room left.
2. **Prune: +55 → −36 → −76 → −95 → −15 → −2.** The magnitude keeps shrinking because the fat is gone; net-negative held for the 5th straight cycle. The metric that matters is the sign, and it's been negative for 5 cycles.
3. **Chrome: flat through 30 features and one structural reshape.** 7 cycles, 0 toolbar buttons, only-ever spend = one modal heading swap. The most durable win of the whole run.
4. **Bugs: 14 → 4 → 0 → 1 → 1 → 0.** A reshape cycle with zero Harden bugs is the maturity signal.

The game grew from 10,089 LOC (Day 29) to **12,890 LOC (Day 119)** — **+2,801 LOC for 30 features + 6 prune weeks**, ~93 LOC/shipped-feature and still falling. Prune discipline is outpacing feature complexity even through a structural reshape.

### If there is a Cycle 7 — the recommendation

The reshape thesis is proven: structure moves the score where polish can't. Concrete C7 candidates, in priority order:

1. **A second structural axis.** The Adventure Journey opened the campaign door; the next reshape-tier moves are a **level editor** with shareable custom stops (leverages the existing v3 share codec) or a lightweight **"play a friend's track" ghost-race** — either could move Uniqueness/Addictiveness again.
2. **Journey ergonomics for first-timers** — a region-collapse/resume affordance so the 12-stop map isn't daunting on stop 1 (carried Build debt from the Day 115 audit).
3. **Tutorial expansion / returning-player tour** for the now-14-feature surface — still 4 steps.
4. **Keep the prune stretch seams-based, not magnitude-based.** Two cycles at the lean floor confirm chasing prior magnitudes would violate LESSON-DAY71.

---

## 🏁 Verdict

Cycle 6 closes with the factory's **first score gain in three cycles (8.7 → 8.9)** — and, for the first time, the gain came from a **structural reshape** rather than another delightful ambient behavior. The flat puzzle-card list is now the 🗺️ **Adventure Journey**: 12 star-gated stops across 5 themed regions, a riding train, a frontier beckon, two auto-solvable warm-up stops, a drawn-in gold route, a completion certificate, and a Trailblazer sticker — all for +174 build LOC, 0 net chrome, 0 Harden bugs, and 0 new modals. The extension exits with a game that:

- Ships **30 features across 6 build weeks**, 20 bugs fixed total, 0 customer-facing regressions
- Has **0 open bugs**, **0 console errors** on live deploy
- Weighs **467,691 bytes / 12,890 LOC** (net-negative prune in 5 of 6 cycles)
- Holds a **7-cycle chrome-stability streak** (0 toolbar buttons across 30 features + one structural reshape)
- Auto-opens a 4-step tutorial that now points first-timers at the journey; 40/52 palette pieces gated by progression
- Turns the campaign into a **town-to-town adventure** on top of everything Cycle 5 did — companion pets, balloons, stationmasters, shooting stars, cargo jingles — and everything before that
- Scores **8.9/10** — Juice/Polish at a perfect 10, and now Replayability at 10 too, with Uniqueness and Addictiveness up to 9

**Cycle 5's review made a prediction and a prescription: polish had asymptoted, and only a structural move would move the score. Cycle 6 built the move, shipped it clean, and the score went up. The reshape thesis is validated — and the factory now knows that the next gain, again, will come from structure, not from another layer of delight.**

**Cycle 6: complete. Game: ship-ready. Reshape: proven. Cycle 7, if it runs, should open a second structural axis. 🚂🗺️🎫🏁**

---

*Review by Mochi, factory orchestrator. Live-tested at https://mikedyan.github.io/train-tracks/?v=119&fresh=1&cb=cycle6closeout2 with `localStorage.clear()` + reload. Compared against `reviews/prune-cycle-1..5-review.md` and `PRUNE_REPORT.md` (Day 115). All scores are honest assessments — the +0.2 is earned by the reshape moving three structural dimensions that five polish cycles left pinned at their ceilings; the polish dimensions held at their already-maxed values. Hard rule met on both LOC and bytes. The stretch was missed and correctly not chased — forcing cuts on a lean codebase violates LESSON-DAY71.*
