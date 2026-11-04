<!-- version: 1.1.0 -->
<!-- created: 2025-09-18 -->
<!-- updated: 2026-11-03 -->
# 🐍 Virtual Environment Setup

**Purpose:** how to create the Python virtual environment this repo needs, so its packages stay separate from your system Python.

The commands are for Linux, macOS or [WSL](https://learn.microsoft.com/windows/wsl/) on Windows, since the repo's `make` targets and hook scripts need a bash shell.

## 1️⃣ Create it

Check the `python-version` in [`ci.yml`](../../.github/workflows/ci.yml), so local results match CI. Then create the environment from the project root, naming that version, such as `python3.13`:

```bash
python3.13 -m venv .venv
```

## 2️⃣ Activate it

```bash
source .venv/bin/activate
```

Your shell prompt usually shows `(.venv)` once it's active.

## 3️⃣ Install

Install the requirements and the pre-commit git hooks:

```bash
make deps
```

## 4️⃣ Deactivate or remove it

Run `deactivate` when you're finished, or `rm -rf .venv` to remove the environment completely.
