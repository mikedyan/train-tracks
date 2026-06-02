# 🚂 Train Tracks — Cycle 4 Build Roadmap

**Cycle:** 4 (Build → Harden → Prune, Days 74–88)
**Start date:** 2026-06-02 (Day 74)
**Theme:** **"Living World"** — make the world feel reactive and alive, without growing the toolbar.
**Entering state:** 11,790 LOC / 419,531 bytes / 325 functions / 0 open bugs / 15 toolbar buttons + HONK
**LOC budget for build week (advisory):** ≤ +900 LOC across the 5 days (Cycle 3 spent 814)
**Hard rule:** **Zero new toolbar buttons.** Settings tile additions allowed only if a feature truly needs an off-switch (e.g. reduced-motion users want a "no critters" tile? we'll see).

---

## 🎯 Why this theme

Cycle 3's score moved because features were *additive to the world* (Sky changes atmosphere, Animals add behavior, Stickers add a collection hook) rather than parallel mechanics. Cycle 4 leans harder into that — every feature should make a kid say *"wait, what was that?"* the first time they see it. The world watches them, decorates itself, and celebrates with them. Nothing new to click; everything to notice.

The Cycle 3 review also flagged:
- 🧑 Passengers toolbar button reads ambiguously (deferred to a future cycle, NOT this one — would need UX surface change)
- Tutorial only covers 3 of 8 surface features (also deferred — better suited for a Harden/Prune-week polish day)

Cycle 4 holds chrome flat and pours all the build-week budget into world-life.

---

## 📅 The 5 features

### **Day 74 (Mon, Jun 2) — 🦋 Ambient Critters**

Small butterflies + bees flit around scenery during play. Anchored to flowers/trees/animals/houses. Pure CSS-driven wander animation; auto-on; cleans up on stop. Builds on Day 12 (Animated Scenery) and Day 30 (Animal Reactions). **Auto-on, no toggle** (LESSON-DAY46-F). Pure-CSS animation pattern (LESSON-DAY59-A) — JS only toggles a class.

*Expected size:* +60–100 LOC. *Verification:* Spawn after `▶️ Play`, hover above scenery, drift smoothly, vanish on `⏹️ Stop`.

### **Day 75 (Tue, Jun 3) — 🚦 Station Arrival Signal**

Each station gets a tiny stoplight in the upper-right corner. Green when no train is incoming. Yellow ~2 cells out. Red as a train passes through. Auto-on. Tiny visual hook that turns every station into a "train arriving!" moment for kids. No sound (the existing whistle song already announces it).

*Expected size:* +80–120 LOC.

### **Day 76 (Wed, Jun 4) — 🎉 Confetti Cannon**

Every 5th cargo delivery (or passenger arrival) → station fires a confetti cannon. Colored particles arc up and float down, all trains do a 1-tap shared honk, on-screen "🎉 ×5 DELIVERIES!" toast. Connects existing cargo (Day 46) + passenger (Day 25) + sticker (Day 63) systems into one celebration loop.

*Expected size:* +90–140 LOC.

### **Day 77 (Thu, Jun 5) — 🌧️ Puddle Splashes**

In rain weather (Day 31), small puddles randomly appear on horizontal track tiles. When a train passes through, it kicks up a quick splash + a "kssh" SFX. Pure rain-day reward; vanishes 5s after rain stops. Builds on existing weather system.

*Expected size:* +100–160 LOC.

### **Day 78 (Fri, Jun 6) — 🛤️ Train Trail**

Each train leaves a faint, color-matched trail behind it as it moves — a soft glow of its body color that fades over ~1.5s. Kids can *see* where the blue train just went vs the red train. Pure visual; auto-on; no new UI. Closes the "I want to see my train's path" instinct most kids have.

*Expected size:* +90–130 LOC.

---

## 🚧 Discipline carry-overs

1. **Numbers > vibes** (3-cycle-proven). Build week LOC budget is advisory, NOT a hard rule — that's for prune week.
2. **Zero new toolbar buttons.** Every feature is auto-on or already accessible from existing chrome.
3. **Pure CSS where possible** (LESSON-DAY59-A). JS just toggles classes; the GPU draws.
4. **Live verification rhythm** (LESSON-DAY59-E): JS parse → push → fresh-load → `evaluate` for computed style → multi-second sample → screenshot.
5. **Test the trigger, not just the declaration** (LESSON-DAY59-E): a CSS animation that loads but isn't activated by the right class-toggle is the most common visual-feature bug.

— Mochi 🐯
