"""Tests for the plan manager: listing saved plans by status, and filing plans without overwriting any."""

import importlib
import os
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import pytest
from _paths import REPO_ROOT

sys.path.insert(0, str(REPO_ROOT / "src" / "py"))
manage_plans = importlib.import_module("claude_manage_plans")

TODAY = date(2026, 11, 24)
STATUS_FOLDERS = [("🟢 Active", "active"), ("⏸️ Parked", "parked"), ("✅ Done", "done"), ("🗑️ Dropped", "dropped")]


@pytest.fixture(autouse=True)
def home(tmp_path, monkeypatch):
    """Point the home and Claude config folders at tmp_path, so no test touches the real ones."""
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("CLAUDE_CONFIG_DIR", str(tmp_path / "config"))
    return tmp_path


def make_plan(home, folder, name, status_line):
    """Save a plan folder, with a spec beside its plan, and return the folder's path."""
    plan = home / "config/_plans" / folder / name
    plan.mkdir(parents=True)
    (plan / "plan.md").write_text(f"# Plan\n\n{status_line}\n", encoding="utf-8")
    (plan / "spec.md").write_text(name)
    return plan


def status_line(status, updated=TODAY):
    """Return a plan's status line."""
    return f"**Plan status:** {status} · updated {updated}"


def make_scratch(config, name, age_days):
    """Write a scratch plan last changed age_days ago and return its path."""
    path = config / "plans" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(name)
    changed = datetime(TODAY.year, TODAY.month, TODAY.day, 12) - timedelta(days=age_days)
    os.utime(path, (changed.timestamp(), changed.timestamp()))
    return path


def run(*args):
    """Run the script's main with a fixed date."""
    manage_plans.main(list(args), today=TODAY)


@pytest.mark.parametrize(("status", "folder"), STATUS_FOLDERS)
def test_clean_files_the_whole_folder_by_status(home, status, folder):
    """A plan in another folder moves, with all its files, to the one its status names."""
    start = "parked" if folder == "active" else "active"
    old = make_plan(home, start, "x", status_line(status))
    run("clean", "--yes")
    new = home / "config/_plans" / folder / "x"
    assert not old.exists()
    assert (new / "plan.md").exists() and (new / "spec.md").read_text() == "x"


def test_clean_files_a_plan_outside_every_status_folder(home):
    """A plan saved straight into _plans/ is filed too."""
    make_plan(home, ".", "x", status_line("✅ Done"))
    run("clean", "--yes")
    assert (home / "config/_plans/done/x/plan.md").exists()


@pytest.mark.parametrize("line", ["", "**Plan status:** 🟣 Waiting · updated 2026-11-24"])
def test_unknown_status_is_reported_and_left(home, capsys, line):
    """Both commands name a plan with a missing or unrecognised status, and clean leaves it."""
    plan = make_plan(home, "active", "x", line)
    run("list")
    assert "active/x" in capsys.readouterr().out
    run("clean", "--yes")
    assert "active/x" in capsys.readouterr().out
    assert plan.exists()


def test_plan_name_clash_is_reported_and_left(home, capsys):
    """A plan whose name is taken in the target folder stays, and neither copy changes."""
    plan = make_plan(home, "active", "x", status_line("✅ Done"))
    taken = make_plan(home, "done", "x", status_line("✅ Done"))
    (taken / "spec.md").write_text("original")
    run("clean", "--yes")
    assert "active/x" in capsys.readouterr().out
    assert plan.exists() and (taken / "spec.md").read_text() == "original"


def test_two_plans_bound_for_one_name_do_not_merge(home):
    """When two folders would land on one name, only the first moves."""
    make_plan(home, "active", "x", status_line("✅ Done"))
    second = make_plan(home, "parked", "x", status_line("✅ Done"))
    run("clean", "--yes")
    assert second.exists()
    assert sorted(p.name for p in (home / "config/_plans/done/x").iterdir()) == ["plan.md", "spec.md"]


def test_scratch_name_clash_is_reported_and_left(home, capsys):
    """A scratch plan whose name is archived already stays, and the archived copy is unchanged."""
    path = make_scratch(home / "config", "x.md", 20)
    archived = home / "config/plans/archive/x.md"
    archived.parent.mkdir()
    archived.write_text("original")
    run("clean", "--yes")
    assert "x.md" in capsys.readouterr().out
    assert path.exists() and archived.read_text() == "original"


@pytest.mark.parametrize(("age", "archived"), [(13, False), (14, True)])
def test_scratch_plans_are_archived_at_14_days(home, age, archived):
    """A scratch plan is archived once unchanged for 14 days."""
    path = make_scratch(home / "config", "x.md", age)
    run("clean", "--yes")
    assert path.exists() is not archived
    assert (home / "config/plans/archive/x.md").exists() is archived


def test_only_top_level_markdown_scratch_plans_are_archived(home):
    """Other file types, and files in subfolders, stay put."""
    kept = [make_scratch(home / "config", name, 20) for name in ["notes.txt", "draft/x.md"]]
    run("clean", "--yes")
    assert all(path.exists() for path in kept)


def test_config_folder_defaults_to_dot_claude(home, monkeypatch):
    """With CLAUDE_CONFIG_DIR unset, saved and scratch plans are read from ~/.claude."""
    monkeypatch.delenv("CLAUDE_CONFIG_DIR")
    make_scratch(home / ".claude", "x.md", 14)
    plan = home / ".claude/_plans/active/x/plan.md"
    plan.parent.mkdir(parents=True)
    plan.write_text(status_line("✅ Done"), encoding="utf-8")
    run("clean", "--yes")
    assert (home / ".claude/plans/archive/x.md").exists()
    assert (home / ".claude/_plans/done/x/plan.md").exists()


@pytest.mark.parametrize(("answer", "moved"), [("y", True), ("n", False), ("", False)])
def test_clean_previews_then_asks(home, monkeypatch, capsys, answer, moved):
    """Without --yes, clean shows the moves first and makes them only on a y."""
    plan = make_plan(home, "active", "x", status_line("✅ Done"))
    seen = []
    monkeypatch.setattr("builtins.input", lambda _prompt: seen.append(capsys.readouterr().out) or answer)
    run("clean")
    assert "active/x" in seen[0] and "done" in seen[0]
    assert plan.exists() is not moved


def test_clean_without_input_moves_nothing(home, monkeypatch):
    """A closed stdin counts as a no."""
    plan = make_plan(home, "active", "x", status_line("✅ Done"))

    def closed(_prompt):
        raise EOFError

    monkeypatch.setattr("builtins.input", closed)
    run("clean")
    assert plan.exists()


def test_second_clean_finds_nothing_and_asks_nothing(home, monkeypatch, capsys):
    """Once filed, a plan isn't moved again."""
    make_plan(home, "active", "x", status_line("✅ Done"))
    run("clean", "--yes")
    capsys.readouterr()
    monkeypatch.setattr("builtins.input", lambda _prompt: pytest.fail("asked with nothing to move"))
    run("clean")
    assert "Nothing to move" in capsys.readouterr().out


def test_list_groups_by_status_and_moves_nothing(home, capsys):
    """Each plan is listed under its status with the group's count, and a misfiled one is flagged."""
    for status, folder in STATUS_FOLDERS:
        make_plan(home, folder, f"{folder}_plan", status_line(status))
    misfiled = make_plan(home, "active", "finished", status_line("✅ Done"))
    run("list")
    out = capsys.readouterr().out
    headings = ["Active (1)", "Parked (1)", "Done (2)", "Dropped (1)"]
    positions = [out.index(heading) for heading in headings]
    assert positions == sorted(positions)
    assert out.index("Done (2)") < out.index("finished") < out.index("Dropped (1)")
    assert "misfiled in active/" in out
    assert out.count("misfiled") == 1
    assert misfiled.exists()


@pytest.mark.parametrize(
    ("status", "age", "flagged"), [("🟢 Active", 13, False), ("🟢 Active", 14, True), ("⏸️ Parked", 30, False)]
)
def test_list_flags_active_plans_not_updated_for_14_days(home, capsys, status, age, flagged):
    """Only an Active plan whose status line is 14 or more days old is flagged."""
    folder = dict(STATUS_FOLDERS)[status]
    make_plan(home, folder, "x", status_line(status, TODAY - timedelta(days=age)))
    run("list")
    assert (f"not updated for {age} days" in capsys.readouterr().out) is flagged


def test_list_dates_a_plan_without_a_date_by_its_file(home, capsys):
    """An Active plan with no updated date falls back to when its plan.md last changed."""
    plan = make_plan(home, "active", "x", "**Plan status:** 🟢 Active")
    changed = datetime(TODAY.year, TODAY.month, TODAY.day, 12) - timedelta(days=14)
    os.utime(plan / "plan.md", (changed.timestamp(), changed.timestamp()))
    run("list")
    assert "not updated for 14 days" in capsys.readouterr().out


@pytest.mark.parametrize("args", [["list"], ["clean", "--yes"]])
def test_no_plan_folders_is_not_an_error(home, args):
    """A machine with no plans yet gets no error and no new folders."""
    run(*args)
    assert list(Path(home).iterdir()) == []


def test_clean_with_yes_prints_only_the_count(home, capsys):
    """With --yes there's nothing to approve, so clean gives one line however many plans it moves."""
    make_plan(home, "active", "finished", status_line("✅ Done"))
    for name in ("a.md", "b.md"):
        make_scratch(home / "config", name, 14)
    run("clean", "--yes")
    assert capsys.readouterr().out == "Moved 3 plan(s) into their status or archive folder.\n"
