#!/usr/bin/env python3
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOARD = ROOT / "board.md"
GIACO = ROOT / "giaco-tasks.md"
HISTORY = ROOT / "history-log.md"

parser = argparse.ArgumentParser()
parser.add_argument("title")
parser.add_argument("--owner", default="GIACO")
parser.add_argument("--priority", default="P2")
parser.add_argument("--status", default="NEXT", choices=["INBOX","NEXT","DOING","WAITING","DONE"])
args = parser.parse_args()

line = f"- [ ] ({args.priority}) [{args.owner}] {args.title}\n"

board = BOARD.read_text()
section = f"### {args.status}\n"
if section in board:
    board = board.replace(section, section + line, 1)
BOARD.write_text(board)

if args.owner.upper() == "GIACO":
    g = GIACO.read_text()
    target = "## Active\n" if args.status == "DOING" else "## Queued\n"
    g = g.replace(target, target + f"- [ ] ({args.priority}) {args.title}\n", 1)
    GIACO.write_text(g)

h = HISTORY.read_text()
entry = (
    f"\n- Time: AUTO\n"
    f"  - Change: task added\n"
    f"  - Task: {args.title}\n"
    f"  - Owner: {args.owner}\n"
    f"  - Status before -> after: n/a -> {args.status}\n"
    f"  - Notes: captured via add_task.py\n"
)
HISTORY.write_text(h + entry)
print("Task added")
