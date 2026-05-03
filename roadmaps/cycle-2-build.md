# Cycle 2 — Build Week Roadmap (Days 44–48)

**Cycle window:** May 3 – May 7, 2026 (Build days 1–5)
**Cycle 1 close-out score:** 8.3/10 (vs Day 14 baseline 5.3 actual / 7.2 potential)
**Theme:** Make the game *personal* and *deeper* without bloating chrome. Cycle 1 made it polished; Cycle 2 makes kids feel like it's *theirs*.

---

## Why these 5 features

The Day 14 expert panel listed 10 wishlist items kids would love. Cycle 1 shipped 7. Three remain:
- Doppler train sounds (low value, high effort — defer)
- **Bigger grid options** ✅ scheduled Day 2
- "Story or purpose" — partially shipped via Passenger Delivery (Day 25). We deepen that with **Cargo Missions** Day 3.

Plus 3 fresh ideas that came out of the prune-week review:
- **Train name labels** (Day 1) — emotional ownership. Kids name their stuff. "MARK'S TRAIN" floating above the loco is a magic moment.
- **Track replay / ghost train** (Day 4) — record-and-play a route. Coding-lite for 5-year-olds.
- **Sound packs** (Day 5) — alternate whistle/chug palettes. Cheap variety, fun A/B.

Constraint: every feature must work in both day/night, both desktop/mobile, and respect the toolbar simplicity won in Prune Week 1. We are NOT adding new top-bar buttons. New entries go inside Settings or Customization.

---

## Day 1 (Tue May 3) — 🏷️ Train Name Labels

**Pitch:** Tap a train, type its name, see it float above the loco when it rolls. "MARK'S TRAIN", "RAINBOW EXPRESS", "CHOO-CHOO ALEX". Kids LOVE labeling their stuff. Free emotional ownership.

**Surface:**
- New ⚙️ Settings entry: "🏷️ Name your trains"
- Modal lists currently placed trains (one row per train) with a text input per train (max 14 chars, ALL-CAPS auto-format).
- During play, render a small pill-shaped label above each loco when its name is non-empty.
- Names persist with save state, share links, and auto-save (the existing `{...t}` spread copies the new field for free).

**Acceptance:**
- Place red train, name it "MARK", press Play → "MARK" floats above the red loco.
- Empty names render no label (zero visual cost).
- Reload the page → name persists via auto-save.
- Share link round-trips the name.
- Mobile: modal works on 375px viewport.
- Reduced motion: label has no bob, just follows the loco directly.

**Out of scope:** No emoji picker, no font/color customization, no per-car names.

---

## Day 2 (Wed May 4) — 🟦 Bigger Grid Option (16×10)

**Pitch:** The Day 14 wishlist's last open item. 12×8 is fine for a beginner; 16×10 lets ambitious kids build a real loop network. Toggle in Settings → "Big Grid Mode".

**Plan:**
- Settings switch: `state.bigGrid = true/false`
- ROWS/COLS become reactive: 12×8 default, 16×10 when toggled
- Re-render grid + sidebar palette repositioning + auto-save preserves choice
- Random generator scales output to fit
- Existing tracks survive the switch (clipped if shrinking, padded with empty cells if growing — no data loss)
- Mobile: keep cellSize sensible (use existing pinch-zoom)

**Acceptance:** Toggle on, grid grows; toggle off, grid clips back; placed pieces survive both directions; persists across reload.

**Watch-outs:**
- Puzzle layouts assume 12×8 — bigger grid mode disables puzzle launching (toast: "Puzzles use small grid").
- Share links must encode grid size in the hash.

---

## Day 3 (Thu May 5) — 📦 Cargo Delivery Missions

**Pitch:** Passenger Delivery (Day 25) gave the game *purpose*. Cargo deepens it. A station marked "📦 LOGS" and another marked "🏗️ FACTORY" — pick up logs at one, deliver to the other. Reward = unlock progress + confetti.

**Plan:**
- Reuse station infrastructure. Add `cargoType: 'logs'|'milk'|'mail'|'coal'` to a fraction of stations on random gen.
- Visual: small icon badge over the station roof.
- When loco passes pickup station with empty cargo, auto-pick-up (badge moves to loco).
- When loco passes matching delivery station, auto-drop-off, +confetti, +1 to "deliveries" stat.
- Deliveries unlock pieces faster (existing progression hook).

**Acceptance:** Random gen produces ≥1 cargo pair; loco picks up, delivers, confetti fires; deliveries persist in stats.

---

## Day 4 (Fri May 6) — 👻 Track Replay / Ghost Train

**Pitch:** Press 🔴 REC, build a track piece-by-piece. Press ⏯️ PLAY, watch a ghost rebuild it for you, one piece a second. Coding-lite. Mark replays his masterpiece for dad.

**Plan:**
- New 🔴 button (in Settings or as a small icon) toggles record mode.
- Record mode logs each placement/removal/rotation with timestamp and piece info into `state.replay`.
- Stop recording → "▶️ Replay" button.
- On replay, clear the grid and play back actions at 1.5× original speed (or fixed 600ms each).
- Save replay to a slot, share via URL hash.

**Acceptance:** Build a 6-piece loop with REC on; press Play → ghost rebuilds it; train auto-runs at end.

**Out of scope:** Multi-track replays, undo during replay, editing recorded replays.

---

## Day 5 (Sat May 7) — 🔊 Sound Packs

**Pitch:** Right now we have ONE whistle. Three feels like more. "Classic", "Toy Steamer", "Modern Diesel" packs change the whistle, chug, and horn timbre. Settings → Sound Pack.

**Plan:**
- Refactor SFX synthesis into a `SOUND_PACKS = { classic, toy, diesel }` config object — frequencies, durations, waveforms.
- Settings dropdown picks active pack.
- Persist via localStorage.

**Acceptance:** Switch packs, hear a clearly different whistle and chug. Pack persists across reload. No size-bloat of audio assets (still all synthesized, no files).

---

## Hard rules for Cycle 2 build week

1. Every feature ships with: pass `node --check`, no console errors on the deployed site, smoke test in browser before commit.
2. No new top-bar buttons. New surfaces live inside the Settings/Customization/Share menus from Prune Week 1.
3. Settings entries get short kid-friendly labels with one emoji.
4. Update LESSONS_LEARNED.md after every day.
5. Commit & push every day. State JSON updated every day.
6. Mobile + reduced-motion + night mode parity for every feature.

---

*Roadmap by Mochi, factory orchestrator, Cycle 2 Day 1 (May 3, 2026). All 5 picks defensible against the Day 14 wishlist + Cycle 1 review's deferred items.*
