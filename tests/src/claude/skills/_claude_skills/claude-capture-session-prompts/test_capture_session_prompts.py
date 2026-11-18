"""claude-capture-session-prompts' script keeps one date's prompts, masks secrets and never overwrites a report unasked.

Sample secrets are built by joining pieces, so this file holds no literal that secret scanners would flag.
"""

import importlib.util
import json
from datetime import datetime

import pytest
from _paths import REPO_ROOT

SCRIPT = REPO_ROOT / "src/claude/skills/_claude_skills/claude-capture-session-prompts/capture_session_prompts.py"
spec = importlib.util.spec_from_file_location("capture_session_prompts", SCRIPT)
capture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capture)


def stamp(text: str) -> int:
    """Return a local-time 'YYYY-MM-DD HH:MM' as a millisecond timestamp, as history.jsonl stores it."""
    return int(datetime.strptime(text, "%Y-%m-%d %H:%M").timestamp() * 1000)


@pytest.fixture
def config_dir(tmp_path, monkeypatch):
    """A Claude config directory whose history.jsonl holds prompts from two dates and one malformed line."""
    monkeypatch.setenv("CLAUDE_CONFIG_DIR", str(tmp_path))
    lines = [
        json.dumps({"display": "fix the | pipe", "timestamp": stamp("2026-11-18 09:05"), "project": "/r/playbook"}),
        "not json",
        json.dumps({"display": "yesterday's prompt", "timestamp": stamp("2026-11-17 23:59")}),
    ]
    (tmp_path / "history.jsonl").write_text("\n".join(lines), encoding="utf-8")
    return tmp_path


def test_writes_only_the_target_dates_prompts(config_dir, tmp_path):
    """A report holds only the target date's prompts, one row each, skipping malformed lines."""
    assert capture.main(["--date", "2026-11-18", "--output-dir", str(tmp_path / "out")]) == 0
    report = (tmp_path / "out/2026_11_18_claude_prompts.md").read_text(encoding="utf-8")
    assert "| 1 | 09:05 | playbook | fix the \\| pipe |" in report, (
        "the row should hold time, project and escaped prompt"
    )
    assert "yesterday" not in report, "a prompt from another date leaked into the report"


@pytest.mark.parametrize(
    "secret",
    [
        "AKIA" + "ABCDEFGHIJKLMNOP",
        "gh" + "p_" + "a" * 36,
        "github" + "_pat_" + "b" * 30,
        "xo" + "xb-" + "1234-abcd",
        "sk" + "-ant-" + "c" * 24,
        "-----BEGIN " + "RSA PRIVATE" + " KEY-----\nMIIEabc\n-----END " + "RSA PRIVATE" + " KEY-----",
    ],
)
def test_masks_known_secret_formats(secret):
    """Each known credential format is masked."""
    assert capture.mask_secrets(f"use {secret} here") == "use [REDACTED] here", "a secret survived masking"


@pytest.mark.parametrize("key", ["password", "DB_PASSWORD", "GITHUB_TOKEN"])
def test_masks_a_password_value_but_keeps_its_key(key):
    """A password-like value is masked, and its key name kept, including env-style names."""
    assert capture.mask_secrets(f"{key} = " + "hunter2hunter2") == f"{key} = [REDACTED]"


def test_keeps_an_existing_report_unless_forced(config_dir, tmp_path):
    """An existing report is kept unless --force is passed."""
    report = tmp_path / "2026_11_18_claude_prompts.md"
    report.write_text("my edits", encoding="utf-8")
    args = ["--date", "2026-11-18", "--output-dir", str(tmp_path)]
    assert capture.main(args) == 1, "an existing report should stop the run"
    assert report.read_text(encoding="utf-8") == "my edits", "the user's edits were overwritten"
    assert capture.main([*args, "--force"]) == 0
    assert "09:05" in report.read_text(encoding="utf-8"), "--force should replace the report"
