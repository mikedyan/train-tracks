
## Keyboard Shortcuts Patterns (Day 14)
- LESSON-086: When patch scripts run multiple times (from parallel subagents), CSS injection before `</style>` creates duplicates. Use idempotent markers or check-before-insert in patch scripts.
- LESSON-087: In cron sessions, exec approval can bottleneck the factory cycle. Request `allow-always` for the project directory early.
- LESSON-088: Keyboard handler must guard against input fields (`INPUT`, `TEXTAREA`, `contentEditable`) and open modals to prevent shortcut interference.
- LESSON-089: Quick-select tool state (`selectedTool`) must be cleared when starting a palette drag to prevent conflicting placement modes.
- LESSON-090: Redo stack must clear on any new action (not just place — also remove, rotate, etc.) since all go through `saveUndo()`.
- LESSON-091: Shortcut overlay should support night mode theming via CSS custom properties for consistency.
