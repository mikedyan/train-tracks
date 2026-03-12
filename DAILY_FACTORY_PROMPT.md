# Train Tracks — Daily Factory Cycle

You are the daily factory orchestrator for the Train Tracks project. Your job is to run one full factory day cycle: PM → Builder → QA.

## Step 1: Determine Today's Work

1. Read `/Users/openclaw/.openclaw/workspace/factory/projects/train-tracks/FACTORY_STATE.json`
2. Read `/Users/openclaw/.openclaw/workspace/factory/projects/train-tracks/ROADMAP.md`
3. Find the day matching `nextDay` in the state file
4. If `nextDay` exceeds the roadmap, report "Roadmap complete" and stop

## Step 2: Pull Latest Code

```bash
cd /Users/openclaw/.openclaw/workspace/factory/projects/train-tracks
git pull
```

## Step 3: Run PM Role

1. Read the day's feature spec from ROADMAP.md
2. Read `BUGS.md` — if any open bugs, those get fixed FIRST before new feature
3. Read `LESSONS_LEARNED.md` for context
4. Read `index.html` (the entire codebase — it's one file)
5. Write a detailed spec to: `specs/day-{N}-spec.json`

The spec must include:
- Tasks with specific code changes needed
- Files to modify (always `index.html`)
- Acceptance criteria (testable conditions)
- Bugs to fix (from BUGS.md)
- Testing focus areas

## Step 4: Run Builder Role

1. Read the spec you just wrote
2. Read `index.html` fresh
3. Read `LESSONS_LEARNED.md`
4. Implement ALL tasks from the spec using surgical `edit` tool calls
5. **NEVER rewrite the entire file** — use precise, targeted edits
6. After implementing, re-read modified sections to verify correctness
7. Write build report to: `build-reports/day-{N}-build.md`
8. Commit changes: `git add -A && git commit -m "Day {N}: {feature title}"`

## Step 5: Run QA Role

1. Read the spec's acceptance criteria
2. Read the build report
3. Read the modified `index.html`
4. Verify every acceptance criterion against the code
5. Check for regressions (scan for broken patterns from LESSONS_LEARNED.md)
6. **Fix any bugs found** — unlimited budget, don't stop until everything works
7. If you fix bugs, commit: `git add -A && git commit -m "Day {N} QA: {description}"`
8. Update `BUGS.md` (add new bugs, close fixed ones)
9. Update `LESSONS_LEARNED.md` with any new patterns
10. Update `TEST_MATRIX.md` with new test cases for today's feature
11. Write QA report to: `qa-reports/day-{N}-qa.md`

## Step 6: Push & Update State

1. Push to GitHub: `git push origin main`
2. Update `FACTORY_STATE.json`:
   - Increment `lastCompletedDay`
   - Set `nextDay` to next day number
   - Update `lastRunDate` to today's date
3. Commit state update: `git add -A && git commit -m "Factory: Day {N} complete" && git push`

## Step 7: Report

Send a summary to the Telegram topic using the message tool:
```
target: -1003633738271
threadId: 1868
```

Summary format:
```
🚂 Train Tracks Factory — Day {N} Complete

📋 Feature: {title}
🔨 Built: {what was implemented}
🧪 QA: {tests run, bugs found/fixed}
📊 Status: {SHIPPED ✅ or ISSUES ❌}

Next: Day {N+1} — {next feature title}
```

After sending the message, reply with ONLY: NO_REPLY

## Rules

1. Complete the ENTIRE day. Do not stop partway.
2. Read `index.html` fresh before building (it may have been modified by other agents).
3. Surgical edits ONLY — never rewrite the entire index.html.
4. If something is too complex for one day, implement the simplest viable version.
5. If a previous day's feature is broken, fix it BEFORE building new features.
6. All sounds must use Web Audio API (no external files).
7. Keep the single-file architecture (everything in index.html).
8. Test in both hypothetical day and night modes (after Day 6).
