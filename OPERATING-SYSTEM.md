# Second Brain Operating System

## Capture Rule
- Any new task goes to `inbox.md` immediately.

## Processing Rule
- Move tasks from inbox to:
  - `personal-tasks.md` if owner is ME
  - `giaco-tasks.md` if delegated to GIACO
- Reflect live status in `board.md`.

## Status Rule
Every task should include:
- Priority: P1/P2/P3
- Owner: ME/GIACO
- Status: INBOX/NEXT/DOING/WAITING/DONE
- Optional due date

## Change Logging Rule
On any status change, append one line in `history-log.md`.

## Snapshot Rule
Take a snapshot file in `snapshots/` whenever:
- day starts
- day ends
- before major planning
- before/after big execution sprint

## Visibility Rule
For instant visibility, always check in this order:
1. `board.md` (live view)
2. `giaco-tasks.md` (delegated queue)
3. `history-log.md` (timeline)
