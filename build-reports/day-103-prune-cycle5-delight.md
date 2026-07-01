# Day 103 — Cycle 5 Prune Week: Delight Polish (Hero Balloon)

**Date:** 2026-07-01 (Wed) · Factory Day 103 · Cycle 5 Prune Week (Delight Polish day)
**Site:** https://mikedyan.github.io/train-tracks/
**Mandate:** Tiny kid-facing magic inside an existing play-time behavior, no new chrome, inside the week's banked LOC margin (PRUNE_REPORT Day-103 budget: +0..+8 LOC).

## What shipped
🎈 **Hero Balloon** — the **first** floating balloon of each play session now spawns **1.6× larger** and as the classic red 🎈, so kids notice the balloon feature within the first second of play and are tempted to steer the train into it. Every subsequent balloon in that session is normal-sized/random as before. Mirrors the Day 87 "hero critter" pattern (first ambient critter 1.5×): a pure enhancement inside an existing play-time behavior — **no new toolbar button, no settings tile, no modal** (6-cycle chrome-stability streak intact).

### Implementation (3 surgical lines)
- Module scope: `let balloonHeroPending = true;` (Day 90 balloon block).
- `startBalloonSystem()`: resets `balloonHeroPending = true` on every play start so each session gets one hero.
- `spawnBalloon()`: converted `const size` → `let size`; one guard line `if (balloonHeroPending) { balloonHeroPending = false; size *= 1.6; heroEmoji = '🎈'; }`. Restructured the `textContent`/`size` ordering so the hero override applies before the CSS var is written (also absorbed one stray blank line).

Respects the existing `prefersReducedMotion()` early-return in `spawnBalloon` (hero inherits it — no motion, no hero, no exceptions). Night-mode / high-contrast balloon CSS unchanged.

## Size / rules
| Metric | Entry (Day 102) | Exit (Day 103) | Δ |
|---|---|---|---|
| LOC | 12,715 | **12,718** | **+3** |
| Bytes | 455,284 | **455,567** | **+283** |

- **LOC budget +0..+8:** +3 ✅ (within budget).
- **Week hard rule ≤12,733 LOC (net-negative):** cleared by **15**. Cumulative C5 Prune (Days 100→103): **−15 LOC**.
- **Week byte rule ≤455,636 (both axes shrink):** at **455,567 = −69** under the ceiling ✅. Both axes net-negative for the week. (First draft came in at 455,660, +24 over ceiling; trimmed my own comment verbosity ~93 B to land −69 under — honest, not padded.)

## Verification (live, deployed)
`?v=103d&fresh=1&cb=d103hero4` after Pages rebuild (served HTML = 455,567 B, 3 `balloonHeroPending` matches):
- `spawnBalloon.toString()` includes `balloonHeroPending` → **hasHero: true** (deployed source confirmed).
- `startBalloonSystem()` → 4× `spawnBalloon()`: sizes **[34.9, 24.3, 26.5, 22.3]px** → **first = 34.9px hero** (>28.8 = min-base×1.6), rest max 26.5px. **heroFirst: true**, first emoji **🎈**.
- **0 console errors** across the sequence.
- JS parse clean (`node --check` on extracted inline script). HTML balanced: div 188/188, button 55/55, script 1/1, style 1/1.

## Notes
- Zero functional change to any other system; the hero only rescales the session's first balloon.
- Deploy propagation was slow (~4 min) + a stale browser HTML cache masked the update; confirmed via direct `curl` of the served bytes before the final green live probe.
- **NEXT:** Day 104 = Cycle 5 Prune Week Day 5 — Expert Panel + Validation (full fresh-load user flow, score 10 dimensions vs Cycle 4's 8.7, write `reviews/prune-cycle-5-review.md`, close Cycle 5). Prune Week 5 currently −15 LOC / −69 B, both axes negative.
