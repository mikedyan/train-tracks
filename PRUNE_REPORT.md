# PRUNE Report — Cycle 6 (July 13, 2026)

**Auditor:** Mochi (fresh-eyes audit, Day 115 of factory / Day 1 of Prune Week 6)
**Site under review:** https://mikedyan.github.io/train-tracks/?v=115&fresh=1&cb=prune6d1
**Code size entering Prune Week 6:** **12,892 lines / 467,828 bytes / 357 functions** (single `index.html`)
**Hard rule (end of Prune Week 6):** ≤ **12,892 lines** (net negative code = pass)
**Stretch goal:** ≤ **12,862 lines** (−30, realistic given fresh reshape material)
**Aspirational goal:** ≤ **12,847 lines** (−45, if Target D lands clean)
**Byte rule:** ≤ **467,828 bytes** (both axes must shrink — held C3/C4/C5)
**Previous prune outcomes:** C1 +55 · **C2 −36** · **C3 −76** · **C4 −95 (8.7)** · **C5 −15 (8.7, leanest ever)**

---

## TL;DR

Cycle 6 was the **reshape cycle** the Cycle-5 review demanded: the flat 🧩 puzzle-card list became a winding, star-gated **🗺️ Adventure Journey** (12 stops across 5 regions, riding 🚂 marker, 🎫 next-stop beckon, 🏁 Trailblazer sticker, drawn-in gold route, finish-line certificate, 2 warm-up on-ramp stops). Build week spent **+174 LOC** over 5 days (12,718 → 12,892) — under the +310–540 roadmap estimate, because it was a **spine over stable bones** (new `ADVENTURE_STOPS`/`renderAdventureMap` referencing the *unchanged* puzzle engine + `loadPuzzle`). Harden week added **+0 net LOC** — five consecutive clean sheets (Days 110–114), file **flat** at the build-close anchor all week. Entering Prune Week 6 at **12,892 / 467,828 / 357**.

The discipline held for a **6th straight cycle**: the reshape stayed *inside* `#puzzle-overlay` — **0 new toolbar buttons, 0 new settings tiles, 0 new modals**. Live fresh-load this morning confirms the chrome is byte-for-byte the same shape as Cycle 1 exit: toolbar 15 + HONK, settings 8 tiles / 3 sections, palette 26 logical pieces (20 locked on fresh), 13 overlays.

The honest prune news: the classic veins remain **mined out** — **0 blank runs ≥2** in the whole file, **0 dead functions** (357 named, all referenced), section fences are real delimiters. BUT Cycle 6 handed prune week something Cycle 5 didn't have: **+174 LOC of fresh reshape code** (Days 105–109) whose scribe left a normal scattering of restate-the-*what* comments, a couple of new closing-fence twins, and intra-function blanks in the big `renderAdventureMap`. That's a real, surgical vein — slightly more headroom than last cycle's −15.

**Realistic prune budget: −25 to −45 LOC** across (A) Adventure-Journey inline redundant-comment trim, (B) redundant closing fences on the 2–3 new `ADVENTURE`/`REGION` sections, (C) intra-function blank trims in `renderAdventureMap` + the new `PUZZLES[11/12]` warm-up data, and (D — OPTIONAL/risk-flagged) light DRY of the region-band / node-render loops if it stays lossless. Clears the hard rule (≤12,892) and beats the stretch (≤12,862). Aspirational (≤12,847, −45) only if D lands clean — and per LESSON-DAY71 we do **not** force DRY on cheap render loops.

**Two non-prune notes carried into a hypothetical Build week** (out of prune scope): (1) the **12-stop Adventure Journey may be long for a true first-timer** — it's a scrolly map — mitigated by the 2 gentle warm-ups and star-gating, but worth a "collapse regions" or "resume where you left off" Build idea; (2) the **tutorial is still 4 steps for a 13-feature surface**, and the **🧑 Passengers button** remains 4×-flagged for discoverability. All three are *additive* fixes — they belong in Build, not Prune.

---

## 1. Fresh Eyes Walk-Through (the 5-year-old test, take 6)

Cleared `localStorage` → reloaded `?v=115&fresh=1&cb=prune6d1`. Live DOM probe results:

| Element | First impression | Verdict |
|---|---|---|
| 🚂 Train Tracks header | Friendly, on-brand | ✅ Keep |
| Tutorial auto-pops (`display:flex`) | 4-step overlay on cold boot | ✅ Keep (expand in Build) |
| Left palette: Tracks · Trains · Cars · Scenery | 26 logical pieces, 6 unlocked at fresh | ✅ Keep |
| Locked pieces dim (`.palette-locked`) | **40/52 DOM nodes locked** (20/26 logical) | ✅ Keep — progression healthy |
| Grid (8×12 green felt, 96 cells) | "I can put things there" | ✅ Keep |
| Toolbar (15 + 📯 HONK play-only) | Same shape as Cycle 1 exit | ✅ Keep |
| Settings drawer | **8 tiles / 3 sections (🔊 Audio · 🖼️ Display · 🎮 Game)** | ✅ Keep |
| 🧩 → 🗺️ Adventure Journey | 12 stops, 5 regions, 🎫 beckon on First Track, dashed rail | ✅ Keep (watch length) |

**Verdict:** The UX prune work from Cycles 1–5 survived a 6th build week *and* a structural reshape. The reshape is *invisible in the chrome* on fresh load — the only chrome change ever spent was the modal heading (🧩 Challenge Puzzles → 🗺️ Adventure Journey, Day 105). **Nothing new to cut from the chrome.** Screenshot captured: warm-up region (First Track + Round the Bend) → Meadow region, "🎫 All aboard!" beckon on the frontier, gold/green/grey stop states, dashed rail. **0 console errors** on the whole fresh boot.

**The one 5-year-old wince:** the Adventure Journey is a *long scroll* — 12 stops stacked vertically across 5 region bands. A first-timer sees stop 1 (great) but has to scroll to sense the whole line. Not a defect (gating + warm-ups make the on-ramp gentle, and length = replay value kids love), but a **Build-week** candidate for region-collapse / "you are here" auto-scroll. **Out of prune scope** (fixing it is additive).

---

## 2. Inventory & Counts (vs Cycle 5 baseline)

### Toolbar — **15 + HONK while playing** (unchanged 6 cycles)
▶️ Play · 🎲 Random · 🗑️ Clear · ↩️ Undo · ↪️ Redo · 🔊 vol · ☀️ day/night · 💾 Save · 🧩 Journey · 🌤️ Weather · 🌸 Biome · 🧑 Passengers · 📤 Share · ❓ Help · ⚙️ Settings — plus play-only 📯 HONK.
→ **No change from Cycle 5.** 6-cycle streak, verified live (`#controls` = 16 buttons incl. HONK).

### Settings Drawer — **8 tiles in 3 sections** (unchanged)
- 🔊 AUDIO: 🎵 Music · 🔊 Sound pack (Classic/Toy/Diesel)
- 🖼️ DISPLAY: ♿ High Contrast · ⬛ Big Grid
- 🎮 GAME: 🏷️ Name Trains · 🎬 Track Replay · 📊 Stats · ⭐ Sticker Book
→ Identical to Cycle 5. Reshape shipped with **zero settings growth**.

### Palette — **26 logical pieces, 4 sections** (unchanged)
Tracks (9) · Trains (5) · Cars (3) · Scenery (9). **20/26 locked at fresh** (40/52 DOM nodes counting the mobile-drawer mirror). Verified live: `#sidebar .palette-piece` = 26, 6 unlocked.

### Adventure Journey — **12 stops · 5 regions · 12 puzzles** (Cycle 6 reshape)
Regions: `start` (🌱 Warm-Up: First Track, Round the Bend) → `meadow` → `hills` → `desert` → `night`. `ADVENTURE_STOPS.length` = 12, `PUZZLES.length` = 12, `ADVENTURE_REGIONS` = 5 keys. Fresh boot: 1 frontier beckon, "0/12 stops". **All inside the reused `#puzzle-overlay`.**

### Modals — **13 overlays** (unchanged)
`weather`, `sky`, `save`, `settings`, `track-replay`, `train-names`, `share`, `shortcuts`, `puzzle`, `screenshot`, `stats`, `sticker`, `tutorial`. No new modal in Cycle 6 (the reshape reused `puzzle-overlay`).

### Code health (entering Prune Week 6)

| Metric | C5 exit (D104) | C6 build-close (D109) | C6 entry (D115) | Δ vs C5 exit |
|---|---|---|---|---|
| Lines | 12,718 | 12,892 | **12,892** | **+174** |
| Bytes | 455,567 | 467,828 | **467,828** | **+12,261** |
| Functions | 354 | 357 | **357** | **+3** |
| Modals | 13 | 13 | **13** | 0 |
| Toolbar buttons | 15+HONK | 15+HONK | **15+HONK** | 0 |
| Settings tiles | 8 | 8 | **8** | 0 |
| Palette pieces | 26 | 26 | **26** | 0 |
| Blank runs ≥2 | 1 | 0 | **0** | −1 |
| Dead functions | 0 | 0 | **0** | 0 |
| Open bugs | 0 | 0 | **0** | 0 |
| Console errors live | 0 | 0 | **0** | 0 |

**The chrome held through a structural reshape.** Cycle 6 grew the engine by +174 LOC / +3 functions (`isAdventureStopUnlocked`, `startAdventureStop`, `renderAdventureMap`) and 2 new puzzle-data entries, without spending a byte of toolbar/settings/modal/palette real estate.

---

## 3. Audit Targets — Code-Side Cuts

The C3 veins stay spent: **0** blank runs ≥2, **0** dead functions, legitimate section fences are real delimiters. But Cycle 6's **+174 LOC of Adventure-Journey code (Days 105–109)** is a fresh, surgical vein.

### Target A — Adventure-Journey inline redundant comments (~10–16 LOC)
The reshape scribe left a normal scattering of restate-the-*what* comments over self-documenting code. Confirmed live in the source:
- **~L11055 / L11069** warm-up puzzle preambles — keep the *why* ("gentlest first stop", "auto-connect orients them") but the twin restatements can compress.
- **~L11155 `// Group consecutive stops into region segments...`** over an obvious `reduce`/loop → trim to a phrase.
- **~L11178 `// Region bands (behind the rail)...`** partially restates the code → keep the *why* (z-order), drop the *what*.
- **~L11212 `// Journey train rides at the furthest-reached stop...`** → keep 1 line, it explains intent.
- Sweep `renderAdventureMap` + `ADVENTURE_STOPS`/`ADVENTURE_REGIONS` blocks for the same pattern.

**Est. −10 to −16 LOC.** Zero functional change. **Keep** comments explaining *why* (z-order, `pathLength=100` normalization, star-gate math, region boundary midpoints) — cut only comments restating *what*.

### Target B — redundant closing fences on Cycle-6 sections (~4–8 LOC)
Days 105–109 introduced new `=====` section headers (ADVENTURE JOURNEY / REGION PALETTE). Per the C3 Day-70 rule, a section needs **one** top delimiter, not a closing twin. Evaluate the bottom `=====` fences on the Cycle-6-added sections only; collapse the redundant *closing* fence, preserve the top header. (55 total fences in file — only Cycle-6 twins are fair game.)

**Est. −4 to −8 LOC.** Identical to the C3 Day-70 pattern that cleared cleanly.

### Target C — intra-function blank trims in the reshape (~6–10 LOC)
`renderAdventureMap` is the biggest new function and carries generous single-blank separators; the `PUZZLES[11/12]` warm-up data + `ADVENTURE_STOPS` literal have a few noise blanks. Trim the ones that don't separate logical phases (LESSON-DAY71: cut noise, not structure — the phase-separating blanks that make the map render readable stay).

**Est. −6 to −10 LOC.**

### Target D — DRY the render loops (OPTIONAL / RISK-FLAGGED, ~0–10 LOC)
`renderAdventureMap` builds region bands, node dots, and the two rail polylines with some structurally-similar DOM-assembly scaffolding. A small helper *might* fold the node-creation or band-creation loop. **BUT** the reshape is the score-moving feature this cycle — per LESSON-DAY71 and LESSON-DAY105 (spine-over-bones, don't destabilize the reshape in its first prune) we ship D **only if** the diff stays clearly lossless and the map smoke-tests green (12 nodes render, beckon advances, progress rail draws in, certificate on complete). If it feels lossy, **skip** and bank the honest smaller win.

**Est. −0 to −10 LOC net.**

### What I'm NOT cutting
- **Any Adventure Journey stop.** 12 stops = replay value; length is a Build-week UX question (region collapse / resume), not a code cut.
- **Legit section fences / the reused `#puzzle-overlay` structure.**
- **Function count.** 357, all referenced (0 orphans). Cutting for a count hurts readability (LESSON-DAY71).
- **Reshape *why* comments.** `pathLength=100` normalization, region-boundary midpoints, star-gate `stops[i-1]` logic, beckon frontier scan — all real *why*.
- **CSS.** Cycle-6 CSS (`.adv-node`, `.adv-beckon`, `.adv-path-done`, `.adv-certificate`, region bands) all have live JS paths (verified: nodes/beckon/rail render live).

---

## 4. Day-by-Day Plan

| Day | Theme | Target LOC Δ | Notes |
|---|---|---|---|
| **115 Mon** | Fresh Eyes Audit | 0 | This report. Hard ≤12,892, stretch ≤12,862, aspirational ≤12,847. |
| **116 Tue** | Simplify (Target A) | **−10 to −16** | Trim Adventure-Journey inline redundant comments. |
| **117 Wed** | Code Cleanup (Target B + C) | **−10 to −18** | Collapse Cycle-6 closing fences + intra-`renderAdventureMap` blank trims. |
| **118 Thu** | Delight Polish (+ optional Target D) | **+0 to +8** (D: −0..−10) | Tiny kid magic inside existing play-time behavior; evaluate render-loop DRY only if lossless. |
| **119 Fri** | Expert Panel + Validation | 0 | Live `?v=119&fresh=1` full user flow, JS parse, 0 console errors, `reviews/prune-cycle-6-review.md`, commit/push/Telegram. |

**Cumulative target: −25 to −45 LOC.** Clears the hard rule (≤12,892) with margin and beats the stretch (≤12,862). Aspirational (≤12,847) requires Target D to land clean — not forced.

---

## 5. Risks & Watch-Items
1. **Don't destabilize the reshape in its first prune.** The Adventure Journey is Cycle 6's score-moving feature — treat Target D with extra caution; a held line beats a fragile DRY (LESSON-DAY71/105).
2. **Byte rule.** C3/C4/C5 all shrank bytes. Comment trims are byte-cheap but real — track in build-reports and land honestly under 467,828.
3. **Don't over-trim reshape blanks.** `renderAdventureMap` reads cleanly *because* of phase-separating blanks. Cut noise, not structure.
4. **Delight polish stays off the toolbar.** 6-cycle chrome-stability streak is a feature — additions live inside existing modals or play-time behavior.
5. **Smaller cut is OK.** This is still one of the leanest codebases the factory prunes. A clean −25 honest LOC beats a forced −45. The hard rule is net-negative; everything past that is bonus.

---

## 6. Live Smoke Test (this morning, Day 115)

Verified live on `?v=115&fresh=1&cb=prune6d1` after `localStorage.clear()` + reload:

- ✅ Tutorial overlay auto-opens on cold boot (`display:flex`), 4 steps
- ✅ Palette: 52 DOM nodes / 40 locked (26 logical / 20 locked — progression healthy), 6 unlocked
- ✅ Settings: 3 section headers (🔊 Audio / 🖼️ Display / 🎮 Game), 8 tiles
- ✅ 13 overlays present; no new feature-modal vs Cycle 5
- ✅ `localStorage` after fresh load: only `trainTracks_stickers`
- ✅ Grid: 96 cells (8×12)
- ✅ 🗺️ Adventure Journey opens: heading correct, 12 stops, 5 region bands, 1 "🎫 All aboard!" frontier beckon on First Track, dashed rail, "0/12 stops" (screenshot captured)
- ✅ **0 console errors** across clear → gen → open-journey sequence
- ✅ 0 dead functions (357 named, all referenced), 0 blank runs ≥2

**Anchor confirmed: 12,892 LOC / 467,828 bytes / 357 functions. Prune Week 6 is live.**

---

*Audit by Mochi. The hard rule is numbers, not vibes. C2–C5 all cleared their numeric rules; 4 of 5 went net-negative. Cycle 6 hands prune week +174 LOC of fresh reshape material — the win this week is an honest net-negative on that vein, not a record chase, and above all: don't scratch the reshape.*
