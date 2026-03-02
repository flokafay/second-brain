#!/usr/bin/env python3
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOARD = ROOT / "board.md"
HISTORY = ROOT / "history-log.md"

parser = argparse.ArgumentParser()
parser.add_argument("title")
parser.add_argument("--from_status", required=True, choices=["INBOX","NEXT","DOING","WAITING","DONE"])
parser.add_argument("--to_status", required=True, choices=["INBOX","NEXT","DOING","WAITING","DONE"])
parser.add_argument("--done", action="store_true")
args = parser.parse_args()

board = BOARD.read_text()
from_marker = f"### {args.from_status}\n"
to_marker = f"### {args.to_status}\n"

start = board.find(from_marker)
if start == -1:
    raise SystemExit("from_status section not found")
end = board.find("\n### ", start + 1)
if end == -1:
    end = len(board)
section = board[start:end]

needle = None
for ln in section.splitlines(True):
    if args.title in ln:
        needle = ln
        break
if not needle:
    raise SystemExit("task not found in from_status")

new_line = needle
if args.done:
    new_line = new_line.replace("- [ ]", "- [x]")

board = board.replace(needle, "", 1)
board = board.replace(to_marker, to_marker + new_line, 1)
BOARD.write_text(board)

h = HISTORY.read_text()
h += (
    f"\n- Time: AUTO\n"
    f"  - Change: status updated\n"
    f"  - Task: {args.title}\n"
    f"  - Owner: GIACO\n"
    f"  - Status before -> after: {args.from_status} -> {args.to_status}\n"
    f"  - Notes: updated via update_task_status.py\n"
)
HISTORY.write_text(h)
print("Status updated")
