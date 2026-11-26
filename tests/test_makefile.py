"""Tests for the Makefile's deps target, which must only install into an active virtualenv, and evals' own setup."""

import os
import subprocess

from _paths import REPO_ROOT


def fake_python(tmp_path):
    """Put a stand-in python first on PATH that records its arguments, and return (env, log of its calls)."""
    # so the tests install nothing and leave the real git hooks alone, even if the virtualenv guard breaks
    log = tmp_path / "calls.log"
    python = tmp_path / "bin" / "python"
    python.parent.mkdir()
    python.write_text(f'#!/bin/sh\necho "$*" >> "{log}"\n')
    python.chmod(0o755)
    return {**os.environ, "PATH": f"{python.parent}{os.pathsep}{os.environ['PATH']}"}, log


def run_deps(env):
    """Run `make deps` from the repo root with the given environment and return the full result."""
    return subprocess.run(["make", "deps"], cwd=REPO_ROOT, env=env, capture_output=True, text=True, check=False)


def test_deps_stops_without_a_virtualenv(tmp_path):
    """Without VIRTUAL_ENV set, deps exits non-zero, points to the virtualenv setup doc and installs nothing."""
    env, log = fake_python(tmp_path)
    env.pop("VIRTUAL_ENV", None)
    result = run_deps(env)
    assert result.returncode != 0, "make deps should stop without a virtualenv"
    assert "docs/guides/virtualenv_setup.md" in result.stdout, (
        f"expected a pointer to the virtualenv setup doc: {result.stdout}"
    )
    assert not log.exists(), f"make deps ran python without a virtualenv: {log.read_text() if log.exists() else ''}"


def test_deps_installs_with_the_virtualenv_python(tmp_path):
    """With a virtualenv active, deps runs pip and pre-commit through that virtualenv's python."""
    env, log = fake_python(tmp_path)
    env["VIRTUAL_ENV"] = str(tmp_path)

    result = run_deps(env)

    assert result.returncode == 0, f"make deps should succeed in a virtualenv: {result.stdout}{result.stderr}"
    assert log.read_text().splitlines() == ["-m pip install -r requirements.txt", "-m pre_commit install"], (
        "deps should install requirements, then the git hooks, through the virtualenv's python"
    )


def dry_run_evals(venv):
    """Return the commands `make -n evals` would run with its virtualenv at venv."""
    result = subprocess.run(
        ["make", "-n", "evals", f"EVALS_VENV={venv}"], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    )
    return result.stdout


def test_evals_creates_its_own_virtualenv_on_first_use(tmp_path):
    """Without a ready virtualenv, evals creates one, installs only the pinned pyyaml, then runs with its python."""
    venv = tmp_path / "venv"
    commands = dry_run_evals(venv)
    assert f"test -x {venv}/bin/python || python3 -m venv {venv}" in commands, (
        "never rebuild over an existing virtualenv"
    )
    assert "grep -i '^pyyaml==' requirements.txt" in commands
    assert f"{venv}/bin/python src/py/claude_run_trigger_evals.py" in commands


def test_evals_reuses_a_ready_virtualenv(tmp_path):
    """Once the virtualenv is ready, evals runs straight away without creating or installing anything."""
    venv = tmp_path / "venv"
    venv.mkdir()
    (venv / ".evals_ready").touch()
    commands = dry_run_evals(venv)
    assert "-m venv" not in commands and "pip install" not in commands
    assert f"{venv}/bin/python src/py/claude_run_trigger_evals.py" in commands


def test_test_runs_pytest_through_the_active_python():
    """make test runs pytest as `python -m pytest`, so it uses the interpreter make deps installed into."""
    # a bare `pytest` script can point at a different Python than `python` in a virtualenv rebuilt over an old one
    result = subprocess.run(["make", "-n", "test"], cwd=REPO_ROOT, capture_output=True, text=True, check=True)
    commands = result.stdout.splitlines()
    assert any(line.startswith("python -m pytest --help") for line in commands), result.stdout
    assert "python -m pytest" in commands, result.stdout
