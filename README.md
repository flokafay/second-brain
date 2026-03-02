# Second Brain

This is your lightweight command center for:
- Your personal tasks
- Tasks delegated to Giaco
- Priorities and next actions
- Daily planning and review

## Files
- `board.md` → master visual board (kanban + metrics)
- `history-log.md` → append-only timeline of all changes
- `snapshots/` → point-in-time state captures
- `OPERATING-SYSTEM.md` → rules for keeping this consistent
- `inbox.md` → quick capture (raw thoughts/tasks)
- `personal-tasks.md` → tasks you do yourself
- `giaco-tasks.md` → tasks for Giaco to execute
- `today.md` → daily plan (Top 3 + schedule)
- `weekly-review.md` → weekly reset/checkpoint
- `projects.md` → project list and status
- `waiting-on.md` → items blocked by others

## Basic Workflow
1. Capture anything fast in `inbox.md`
2. Process inbox into personal/delegated lists
3. Reflect status in `board.md` (single source of truth)
4. Log every status change in `history-log.md`
5. Take snapshots in `snapshots/` for point-in-time visibility
6. Mark completion with `- [x]`

## Automation helpers
- `tools/add_task.py` → add a task directly into board + history
- `tools/update_task_status.py` → move task status + log timeline
