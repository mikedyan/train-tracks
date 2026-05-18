# Cycle 3 Build — Mini-Roadmap (Days 59–63)

**Cycle:** 3 of 3 (final rotation in the 90-day plan)
**Week:** Build (May 18–22, 2026)
**Author:** Mochi (factory orchestrator)
**Baseline:** 11,156 LOC / 391,508 bytes / 0 open bugs / 8.4/10 score (Day 58 close-out)

---

## Lens for Cycle 3

This is the **final build week** before the 90-day plan ends. Cycle-2 close-out review (Day 58) explicitly recommended doubling down on the **cargo + replay + sound** foundation. But Cycle 3 also gets to be a victory lap — pick features that make a 5-year-old's eyes light up, not features that "round out the toolkit." Less plumbing, more wonder.

Filter every Day's pick through one question: **"Would a 5-year-old say WOW out loud?"**

---

## The 5 Picks

### Day 1 (Mon, May 18) — 🌅 Time-of-Day Sky During Play
A sun (☀️) or moon (🌙) arcs across the top of the grid viewport during play. The sky tint gently shifts through sunrise → noon → afternoon → sunset over ~60 seconds. Auto-respects night mode (moon arc + indigo tint). Stops cleanly on Stop. Pure CSS animation — zero new JS loop, minimal runtime cost.

**Why kids:** Magic. The world feels *alive* while the train chuffs. Long play sessions become storybook scenes.
**Risk:** Low. Pure CSS additive. No state, no save/load surface area, no share-link impact.
**Target LOC:** ~75–100 net (CSS + 2 JS hooks).

### Day 2 (Tue, May 19) — 🐮🐑 Animal Passengers
Cows, sheep, and ducks adjacent to stations can be "picked up" and ride in the train (small emoji badge over the locomotive). They moo/baa happily during transit, and hop off at the next station. Reuses Day 25's passenger pipeline + Day 30's animal SFX.

**Why kids:** "The cow is in the train!" — instant story material. Bridges existing scenery + passenger systems.
**Risk:** Medium. Animation logic, position tracking, but uses existing systems.
**Target LOC:** ~150–200 net.

### Day 3 (Wed, May 20) — 🎵 Whistle Songs
Each train color gets a tiny 4-note melody (pentatonic, ~1.5s) that plays at stations instead of the plain whistle. Red = bold, Blue = mellow, Yellow = chirpy, Green = pastoral, Purple = mysterious. Reuses Day 27's music infrastructure (pentatonic scheduling).

**Why kids:** Their favorite train sounds *different*. Pure audio joy.
**Risk:** Low–Medium. Audio only, no DOM. Sound-pack interaction needs thought.
**Target LOC:** ~80–120 net.

### Day 4 (Thu, May 21) — 🎬 Replay Sharing
Encode a track-replay (Day 47) into the share-link byte format. Friends paste the link → game plays the build animation, then runs the trains. Extends Day 23's encoder/decoder with a v3 byte layout (compact action log).

**Why kids:** "Watch how I built it!" — pride + show-and-tell. Bridges build + replay + share into one feature.
**Risk:** Medium–High. Byte-level encoding, backward compat with v1/v2 hashes, replay state machine integration.
**Target LOC:** ~120–180 net.

### Day 5 (Fri, May 22) — ⭐ Sticker Book
Earn collectible stickers for milestones (Build 10 tracks, Solve 3 puzzles, 5 cargo deliveries, Sound-pack switcher, Night driver, etc.). Modal shows a 4×3 grid: earned stickers in color, unearned grayed out. ~12 stickers total. Persists in localStorage.

**Why kids:** Tactile collectible feel. Drives return visits. "Mom, I got a new sticker!"
**Risk:** Low. New modal + counter checks against existing gameStats. No new game mechanics.
**Target LOC:** ~150–200 net.

---

## Aggregate Budget

| Metric | Day 58 close | Day 63 target | Δ |
|---|---:|---:|---:|
| LOC | 11,156 | ≤11,650 | +~500 max |
| Bytes | 391,508 | ≤420 KB | +~30 KB max |
| Open bugs | 0 | 0 | 0 |
| Console errors live | 0 | 0 | 0 |

Build week is allowed to grow — that's its job. But aim for **clean adds**, not feature creep. Each day's feature should integrate with at least one existing system (Day 1 → night mode; Day 2 → passengers + animals; Day 3 → music + sound packs; Day 4 → share + replay; Day 5 → stats + milestones). No orphans.

---

## Anti-Goals (things NOT to do this week)

1. **No new track piece types.** We already have 9 (straight, curve, T-split, cross, bridge, tunnel, station, crossing, rainbow). Enough.
2. **No PvP / leaderboards / accounts.** Single-player, local-only.
3. **No new modals beyond Sticker Book.** We have 10 already (Day 49 audit). Adding a 11th is the limit.
4. **No grid-size changes.** Day 45 settled 12×8 ↔ 16×10. Don't touch.
5. **No new sound-effect surfaces beyond whistle songs.** Day 3 is the only audio expansion.

---

## Harden + Prune Preview

Cycle 3 Harden Week (Days 64–68) gets to revisit the **0/26 locked-pieces flag** Day 54 raised and decide: keep progression as a launch hook, or formally remove it. Plus stress-test the new replay-sharing path (Day 4) under big-grid + 5 trains + weather.

Cycle 3 Prune Week (Days 69–73) closes the 90-day plan. Hard rule: **end-of-prune LOC ≤ start-of-prune LOC**, AND end-of-prune bytes ≤ start-of-prune bytes × 1.05 (catch the byte-bloat trend from cycle 2).

---

**Let's ship. 🚂✨**
