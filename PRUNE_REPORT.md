# PRUNE Report — Cycle 1 (Apr 28, 2026)

**Auditor:** Mochi (fresh-eyes audit, Day 39 of factory cycle)
**Site under review:** https://mikedyan.github.io/train-tracks/
**Code size entering Prune week:** 10,089 lines / 348 KB (single index.html)

---

## TL;DR

The game's **core gameplay loop is excellent** — drag pieces, build a loop, hit play, watch the train chug. A 5-year-old will get that in 10 seconds. But the **toolbar has metastasized**: 21 visible buttons + a speed slider + 2 toggle states, many of them cryptic single-emoji icons that mean nothing to a kid. The palette is tight (26 items, well-grouped), but the bottom toolbar reads like a developer's debug console.

This week's mission: **shrink the chrome, not the game.** Cut button count by ~35%, hide power-user features behind a settings menu, keep the joyful surface (HONK, Random, Puzzles, Play) front-and-center.

---

## 1. Fresh Eyes Walk-Through (the 5-year-old test)

I loaded the page cold (no localStorage, no saved track). Auto-restored a small ducky-cow-house track from prior session. Here's what a 5-year-old sees:

| Element | First impression | Verdict |
|---|---|---|
| Big "🚂 Train Tracks" header | Friendly, on-brand | ✅ Keep |
| Left palette with chunky pieces & labels | Beautiful, instantly clear | ✅ Keep |
| Grid with auto-restored track + animals | "Ooh trains!" | ✅ Keep |
| ▶️ Play button (big green, top-left of toolbar) | Obviously the start button | ✅ Keep |
| 🎲 Random / 🗑️ Clear / ↩️ Undo / ↪️ Redo | Recognizable from any app | ✅ Keep |
| Speed slider (with bunny + tortoise emojis!) | Cute, intuitive | ✅ Keep |
| 🔊 / 🎵 / ☀️ / ⌨️ / ☀️ / 🌸 / 🔗 / 📸 / ❓ / 🧑 / 📊 / ♿ / ⛶ | "What are all these?" | ⚠️ **Trim** |
| 💾 Save / 🧩 Puzzles | Big colored buttons, recognizable | ✅ Keep |
| Hidden 📯 HONK (only when playing) | Kids will SCREAM with joy | ✅ Keep |

**The verdict from a 5-year-old:** the top of the toolbar is great. The second row (10 cryptic icons) is intimidating noise.

---

## 2. Inventory & Counts

### Toolbar buttons (visible right now: 21)

**Row 1 (10 buttons + slider):**
1. ▶️ Play
2. 🎲 Random
3. 🗑️ Clear
4. ↩️ Undo
5. ↪️ Redo
6. _Speed slider (bunny↔tortoise)_
7. 🔊 Mute
8. 🎵 Music toggle
9. ☀️ Day/Night
10. 💾 Save
11. ⌨️ Keyboard shortcuts

**Row 2 (10 buttons):**
12. 🧩 Puzzles
13. ☀️ Weather (same emoji as Day/Night — confusing!)
14. 🌸 Biome
15. 🔗 Share link
16. 📸 Screenshot
17. ❓ Help / Tutorial
18. 🧑 Passengers toggle
19. 📊 Stats & Milestones
20. ♿ High-contrast mode
21. ⛶ Fullscreen

**Hidden until playing:** 📯 HONK!

### Palette items (26)
- 9 track types: Straight, Curve, T-Split, Cross, Bridge, Tunnel, Station, Crossing, Rainbow
- 5 trains: Red, Blue, Green, Yellow, Purple
- 3 cars: Freight, Passenger, Caboose
- 9 scenery: Tree, House, Cow, Water, Flower, Sheep, Horse, Duck, People

### Modes / Settings
- Day mode / Night mode
- Sound on/off / Music on/off
- 4 weather states (sunny, rain, snow, ?)
- 4 biomes (grass + 3 others)
- High-contrast mode
- Reduced motion (auto via system pref)
- Passengers ON/OFF
- 10 puzzles + sandbox

### JavaScript surface
- 270 functions in one file
- 39 `<button>` elements in HTML (some are mobile-drawer dupes)
- 75 `palette-piece` references (3× per item: desktop palette, mobile drawer, possibly other)

---

## 3. Findings — What feels overwhelming / unnecessary

### 🚨 P0 — Confusing for kids
1. **☀️ used for TWO different buttons** (Day/Night AND Weather). Two adjacent buttons with the same icon is genuinely confusing. **Action:** unify or change one icon.
2. **Second toolbar row is icon soup.** Ten unlabeled emoji buttons in a row, no spacing, no grouping. A kid (and many adults) won't know what 🎵 vs 🔊, ☀️ vs ☀️, 🌸 vs 🧑 vs ♿ mean.
3. **⌨️ Keyboard shortcuts button is a kid antipattern.** A 5-year-old doesn't use a keyboard for shortcuts. This belongs in a settings menu (or removable entirely — the help screen can list shortcuts).

### 🟡 P1 — Power-user clutter
4. **♿ High-contrast** — accessibility is important but it's a settings toggle, not a frontline button. Hide in settings.
5. **📊 Stats & Milestones** — fun-but-not-essential. Auto-shows on milestone unlocks anyway. Hide in settings or move next to Puzzles.
6. **🎵 Music vs 🔊 Mute** — two adjacent sound toggles. Most kid apps use one 🔊/🔇 button that toggles ALL audio. Keep one, fold music opt-in into settings (or auto-on with global mute respecting it).
7. **⛶ Fullscreen** — most parents will F11 the browser if they want it. Low-value frontline button.
8. **🔗 Share / 📸 Screenshot** — both are "show off your track" features. A single 📤 Share menu (with options for "copy link" / "save image") would feel cleaner than two adjacent icon buttons.

### 🟢 P2 — Code-side prune candidates (defer to Day 41)
9. Mobile drawer duplicates the entire palette HTML — 26 pieces × 2. Could be generated from one source array (DRY, removes ~50 lines).
10. 21+ inline `style=` attributes on toolbar buttons. Move colors to per-button CSS classes (`.btn-weather`, `.btn-biome`, etc.) — already partially done. Reduces inline noise, eases theming.
11. 270 functions in one file — likely some leftovers from earlier days (e.g., older scenery handlers, dead random-track generators). Hunt with grep on Wednesday.

### ❌ NOT cuts — keep these despite count
- 9 scenery items: kids LOVE scenery variety. No cut.
- 5 train colors: kids pick a favorite. No cut.
- 9 track types: every one serves a real building purpose. No cut.
- 10 puzzles: more puzzles = more replay. No cut.
- HONK button: chef's kiss. No cut. Ever.
- Random + Clear + Undo: foundational. No cut.

---

## 4. Tutorial / First-30-seconds check

- ❓ Help button opens a multi-step tutorial overlay (`tutorial-step-emoji/title/desc` exist in DOM). Good.
- Tutorial is **opt-in** via the ❓ button. A first-time visitor with no localStorage gets dropped onto the grid with no guidance. **Recommendation (defer to Thursday's "Delight Polish"):** auto-show tutorial on first visit (already implemented? — verify Wednesday).
- Auto-restored track on page load is a strong "wow, something's already happening" signal. Keep.

---

## 5. Proposed Cuts for Tuesday (Day 40 — Simplify)

Goal: **toolbar goes from 21 visible buttons → ~12 visible buttons.** Net code change should be slightly negative or neutral (HTML shrinks, small new "settings menu" component added). Kid-facing surface gets calmer; nothing is *removed*, just *moved*.

### Cut #1 — Consolidate sound: 🔊 + 🎵 → single 🔊 button
- One button toggles all audio (SFX + music together).
- Music auto-starts at low volume when audio is on; mute kills both.
- Saves 1 toolbar slot.

### Cut #2 — Fix the ☀️ collision
- 🌗 for day/night toggle (shows current state: ☀️ when day, 🌙 when night)
- 🌦️ for weather cycle (shows current weather as the icon)
- No collision, both stay self-explanatory.

### Cut #3 — Move power-user controls into a ⚙️ Settings menu
- ⌨️ Keyboard shortcuts → into Settings
- 📊 Stats & Milestones → into Settings (still auto-pops on unlock)
- ♿ High-contrast → into Settings
- ⛶ Fullscreen → into Settings (or remove; F11 works)
- One ⚙️ button replaces four. Net: -3 toolbar buttons.

### Cut #4 — Combine Share into a single 📤 menu
- 📤 button opens a tiny menu: "Copy link" / "Save image"
- Replaces 🔗 + 📸. Net: -1 toolbar button.

### Cut #5 — Verify ❓ Help is actually useful, otherwise keep visible
- Help is the one "ask for help" button kids and parents need. Stays prominent.

### After cuts (proposed Tuesday end-state — ~12 visible):
**Row 1:** ▶️ Play · 🎲 Random · 🗑️ Clear · ↩️ Undo · ↪️ Redo · [speed slider] · 🔊 Sound · 🌗 Day/Night · 💾 Save
**Row 2:** 🧩 Puzzles · 🌦️ Weather · 🌸 Biome · 🧑 Passengers · 📤 Share · ❓ Help · ⚙️ Settings

12-13 buttons + speed slider. Calmer, clearer, still complete.

### Code cleanup for Wednesday (Day 41)
- DRY the palette: generate desktop + mobile drawer from one array. Target -50 lines.
- Hunt unused functions (Day 14 dup-bug taught us this game accumulates them). Target -100 lines.
- Audit inline `style=` on buttons; move to classes. Target -20 lines.
- **Total file-size goal:** end Prune week ≤9,900 lines (down from 10,089). Net negative code = pass.

### Delight polish for Thursday (Day 42)
- Verify tutorial auto-shows on first visit (no localStorage state).
- Confirm Random generator's first output is consistently delightful (closed loop, no dead-ends, ≥1 train).
- Double-check first 30 seconds of brand-new-user gameplay — does it sing?

---

## 6. Risks & non-goals

- **Don't remove features.** Power-user flows (high-contrast, stats, shortcuts) must remain reachable, just one click deeper.
- **Don't break saved tracks / puzzle progress.** Settings-menu refactor is pure UI; no state schema changes.
- **Mobile drawer must keep working.** Anything we cut from the desktop toolbar must also be reflected (or unified) in the mobile drawer.
- **HONK is sacred.** Don't touch the horn.

---

## 7. Friday score commitment (Day 43)

I'll re-run the 10-dimension expert-panel scoring (per `reviews/expert-panel-day14.md` template) and compare:
- Visual appeal
- First-30s magic
- Kid-friendliness (chrome simplicity)
- Discoverability
- Performance
- Code health (line count + duplication)
- Accessibility
- Mobile experience
- Bug count
- "Squeal factor"

Target: **+1 to +2 points on chrome simplicity, kid-friendliness, and code health**, no regression elsewhere.

---

*Audit complete. On to Tuesday: simplify.*
