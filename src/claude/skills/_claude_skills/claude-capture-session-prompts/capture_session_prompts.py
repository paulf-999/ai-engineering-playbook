#!/usr/bin/env python3
"""Write one day's Claude Code prompts from history.jsonl to a markdown table, with secrets masked.

Reads ``history.jsonl`` from the Claude config directory (``CLAUDE_CONFIG_DIR``, or ``~/.claude`` when unset), keeps
the entries for one local-time date, and writes ``<output-dir>/YYYY_MM_DD_claude_prompts.md``.

Usage::

    python3 capture_session_prompts.py [--date YYYY-MM-DD] [--output-dir DIR] [--force]
"""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import date, datetime
from pathlib import Path

# Credential formats masked before any prompt text reaches the report
SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    # a whole pasted key, header to footer, or to the end of the prompt when the footer is missing
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?(?:-----END [A-Z ]*PRIVATE KEY-----|$)", re.S),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{36}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{22,}"),
    re.compile(r"xox[abprs]-[A-Za-z0-9-]+"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
]
# Keeps the key name, including env-style ones such as DB_PASSWORD, and masks only a value of 8 or more characters
KEY_VALUE_SECRET = re.compile(r"(?i)\b(\w*(?:password|secret|token|api[_-]?key)\w*)(\s*[:=]\s*)\S{8,}")
REDACTED = "[REDACTED]"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse the command-line arguments, defaulting to today and the current folder."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--date", type=date.fromisoformat, default=date.today(), help="YYYY-MM-DD, default today")
    parser.add_argument(
        "--output-dir", type=Path, default=Path.cwd(), help="folder to write to, default the current one"
    )
    parser.add_argument("--force", action="store_true", help="overwrite an existing report for the same date")
    return parser.parse_args(argv)


def read_prompts(history_file: Path, target_date: date) -> list[dict]:
    """Return the entries stamped on the target local date, skipping malformed lines."""
    if not history_file.exists():
        return []
    entries = []
    for line in history_file.read_text(encoding="utf-8").splitlines():
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "timestamp" in entry and datetime.fromtimestamp(entry["timestamp"] / 1000).date() == target_date:
            entries.append(entry)
    return entries


def mask_secrets(text: str) -> str:
    """Replace each known credential format, and each password-like value, with a redaction marker."""
    for pattern in SECRET_PATTERNS:
        text = pattern.sub(REDACTED, text)
    return KEY_VALUE_SECRET.sub(rf"\1\2{REDACTED}", text)


def table_cell(text: str) -> str:
    """Make text safe for one markdown table cell, escaping pipes and collapsing whitespace."""
    return " ".join(text.replace("|", "\\|").split())


def render_report(entries: list[dict], target_date: date) -> str:
    """Render the entries as a markdown table of time, project folder and masked prompt."""
    lines = [
        f"# 📊 Claude prompts for {target_date}",
        "",
        f"**Purpose:** every prompt sent to Claude Code on {target_date}, in local time, with secrets masked.",
        "",
        "| # | Time | Project | Prompt |",
        "|---|---|---|---|",
    ]
    for number, entry in enumerate(entries, 1):
        moment = datetime.fromtimestamp(entry["timestamp"] / 1000)
        project = Path(entry.get("project") or "-").name
        prompt = table_cell(mask_secrets(entry.get("display", "")))
        lines.append(f"| {number} | {moment:%H:%M} | {table_cell(project)} | {prompt} |")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    """Write the report, returning 1 without writing when one exists for the date and --force wasn't given."""
    args = parse_args(argv)
    config_dir = Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude")
    entries = read_prompts(config_dir / "history.jsonl", args.date)
    if not entries:
        print(f"No prompts found for {args.date}")
        return 0
    output_path = args.output_dir / f"{args.date:%Y_%m_%d}_claude_prompts.md"
    # a report may hold the user's own edits, so never replace one without --force
    if output_path.exists() and not args.force:
        print(f"{output_path} already exists and may hold your edits; re-run with --force to overwrite it")
        return 1
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_report(entries, args.date), encoding="utf-8")
    print(f"Wrote {len(entries)} prompts to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
