"""List saved plans by status, and file them into the folder their status line names.

Saved plans live in ~/.claude_work/_plans/, one folder each, and plan mode's own scratch plans in
<Claude config>/plans/, where <Claude config> is $CLAUDE_CONFIG_DIR, or ~/.claude when unset. Nothing is deleted or
overwritten: anything that can't be moved safely is reported and left in place.

Usage: claude_manage_plans.py list | clean [--yes]
"""

import argparse
import os
import re
from datetime import date
from pathlib import Path

STATUSES = ["Active", "Parked", "Done", "Dropped"]
MAX_AGE_DAYS = 14
STATUS_LINE = re.compile(r"^\*\*Plan status:\*\*(.*)$", re.MULTILINE)
# The emoji before the status word is optional
STATUS_WORD = re.compile(rf"\s*(?:[^\w\s]+\s*)?({'|'.join(STATUSES)})\b")
UPDATED = re.compile(r"\bupdated (\d{4}-\d{2}-\d{2})\b")


def saved_plans_dir():
    """Return the folder that holds saved plans."""
    return Path.home() / ".claude_work" / "_plans"


def scratch_plans_dir():
    """Return the folder plan mode writes its scratch plans to."""
    return Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude") / "plans"


def days_since_changed(path, today):
    """Return how many days ago a file last changed."""
    return (today - date.fromtimestamp(path.stat().st_mtime)).days


def saved_plans():
    """Return each saved plan's folder, whether in a status folder or straight in _plans/."""
    root = saved_plans_dir()
    status_folders = [root / status.lower() for status in STATUSES]
    loose = [plan.parent for plan in root.glob("*/plan.md") if plan.parent not in status_folders]
    filed = [path for folder in status_folders for path in folder.glob("*") if path.is_dir()]
    return sorted(filed + loose)


def read_plan(folder, today):
    """Return a plan's status, or None when missing or unrecognised, and the days since it was updated."""
    plan = folder / "plan.md"
    if not plan.is_file():
        return None, 0
    line = STATUS_LINE.search(plan.read_text(encoding="utf-8", errors="replace"))
    text = line.group(1) if line else ""
    status = STATUS_WORD.match(text)
    updated = UPDATED.search(text)
    try:
        days = (today - date.fromisoformat(updated.group(1))).days if updated else days_since_changed(plan, today)
    except ValueError:
        days = days_since_changed(plan, today)
    return status and status.group(1), days


def label(path):
    """Return a plan's path relative to the folder that holds its kind of plan."""
    for root in (saved_plans_dir(), scratch_plans_dir()):
        if root in path.parents:
            return f"{root.name}/{path.relative_to(root)}"
    return str(path)


def find_moves(today):
    """Return the (source, target) moves to make, and a line for each plan to leave in place."""
    wanted, left = [], []
    for folder in saved_plans():
        status, _ = read_plan(folder, today)
        if status is None:
            left.append(f"{label(folder)}: missing or unrecognised status")
        elif folder.parent != saved_plans_dir() / status.lower():
            wanted.append((folder, saved_plans_dir() / status.lower() / folder.name))
    for path in sorted(scratch_plans_dir().glob("*.md")):
        if path.is_file() and days_since_changed(path, today) >= MAX_AGE_DAYS:
            wanted.append((path, scratch_plans_dir() / "archive" / path.name))
    moves = []
    for source, target in wanted:
        if os.path.lexists(target) or target in [taken for _, taken in moves]:
            left.append(f"{label(source)}: {label(target)} already exists")
        else:
            moves.append((source, target))
    return moves, left


def list_plans(today):
    """Print saved plans grouped by status, flagging those misfiled or stale."""
    groups = {status: [] for status in STATUSES}
    unknown = []
    for folder in saved_plans():
        status, days = read_plan(folder, today)
        if status is None:
            unknown.append(label(folder))
            continue
        flags = []
        if folder.parent != saved_plans_dir() / status.lower():
            flags.append(f"misfiled in {folder.parent.name}/")
        if status == "Active" and days >= MAX_AGE_DAYS:
            flags.append(f"not updated for {days} days")
        groups[status].append(f"{folder.name}{' — ' if flags else ''}{', '.join(flags)}")
    groups["Missing or unrecognised status"] = unknown
    printed = [f"{name} ({len(plans)})\n" + "\n".join(f"  {plan}" for plan in plans) for name, plans in groups.items()]
    print("\n".join(text for text, plans in zip(printed, groups.values()) if plans) or "No saved plans.")


def clean_plans(today, assume_yes):
    """File saved plans and archive old scratch plans, listing the moves and asking first unless assume_yes."""
    moves, left = find_moves(today)
    for line in left:
        print(f"Left in place: {line}")
    if not moves:
        print("Nothing to move.")
        return
    if not assume_yes:
        for source, target in moves:
            print(f"{label(source)} -> {label(target.parent)}/")
        try:
            answer = input(f"Move these {len(moves)}? [y/N] ")
        except EOFError:
            answer = ""
        if answer.strip().lower() != "y":
            print("Nothing moved.")
            return
    moved = 0
    for source, target in moves:
        # Checked again, since the target may have appeared while the question was open
        if os.path.lexists(target):
            print(f"Left in place: {label(source)}: {label(target)} already exists")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        source.rename(target)
        moved += 1
    print(f"Moved {moved} plan(s) into their status or archive folder.")


def main(argv=None, today=None):
    """Run the command named on the command line."""
    parser = argparse.ArgumentParser(description="List or file saved plans.")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="list saved plans by status")
    clean = commands.add_parser("clean", help="file saved plans and archive old scratch plans")
    clean.add_argument("--yes", action="store_true", help="move without asking")
    args = parser.parse_args(argv)
    today = today or date.today()
    if args.command == "list":
        list_plans(today)
    else:
        clean_plans(today, args.yes)


if __name__ == "__main__":
    main()
