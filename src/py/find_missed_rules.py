"""Count how often each path-based Claude Code rule applied to a session, but never loaded.

Usage: python3 find_missed_rules.py <your Claude folder> <start date>, such as ~/.claude 2026-11-19

It covers user-level rules whose `paths:` is a quoted list, reads transcripts locally and prints only counts. The
transcript format is undocumented, so a Claude Code update could break it.
"""

import json
import re
import sys
from collections import Counter
from fnmatch import fnmatch
from pathlib import Path


def load_rules(home):
    """Return each path-based rule's globs, keyed by the rule's path."""
    rules = {}
    for rule in (home / "rules").rglob("*.md"):
        if frontmatter := re.match(r"---\n(.*?)\n---", rule.read_text(), re.S):
            rules[str(rule)] = re.findall(r'- "([^"]+)"', frontmatter[1])
    return rules


def read_session(log):
    """Return a transcript's start time, loaded rules, touched files, and whether any instructions loaded."""
    started, loaded, touched, instructed = "", set(), set(), False
    for line in log.read_text(errors="ignore").splitlines():
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue  # a session that is still running can end mid-line
        started = started or entry.get("timestamp", "")
        attachment = entry.get("attachment") or {}
        instructed = instructed or attachment.get("type") == "instructions"
        if attachment.get("type") == "nested_memory":
            loaded.add(attachment["path"])
        content = (entry.get("message") or {}).get("content")
        for part in content if isinstance(content, list) else []:
            if isinstance(part, dict) and part.get("name") in ("Read", "Edit", "Write"):
                touched.add(part["input"].get("file_path", ""))
    return started, loaded, touched, instructed


def count_misses(home, since):
    """Return how many sessions each rule applied to, and how many of those never loaded it."""
    rules, applied, missed = load_rules(home), Counter(), Counter()
    for log in (home / "projects").glob("*/*.jsonl"):
        started, loaded, touched, instructed = read_session(log)
        if started < since or not instructed:  # older sessions, and any that ran without your rules
            continue
        for rule, globs in rules.items():
            if any(fnmatch(file, "*" + glob.replace("**/", "")) for file in touched for glob in globs):
                applied[rule] += 1
                missed[rule] += rule not in loaded
    return applied, missed


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 find_missed_rules.py <your Claude folder> <start date>")
    applied, missed = count_misses(Path(sys.argv[1]).expanduser().resolve(), sys.argv[2])
    for rule, count in applied.most_common():
        print(f"{Path(rule).name:40} missed {missed[rule]} of {count}")
