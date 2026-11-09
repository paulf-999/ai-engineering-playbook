<!-- version: 1.1.4 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-09 -->
# 📦 src

**Purpose:** what belongs in the `src/` folder, and where new code goes.

The folder holds the repo's code, organised by language or tool:

- 📂 **One folder each:** such as `sh/` for shell scripts and `make/` for files the root `Makefile` includes.
- 🆕 **New language:** give it its own folder, such as `py/` for Python.
- 🧠 **Claude config:** `claude/` mirrors your Claude config directory, and `make install` copies each file to the same path there.
  - **Except:** files in `claude/rules/_rules_on_demand/` install beside `rules/`, since Claude Code loads everything under `rules/` in every session.
- 🧪 **Tests:** the [tests README](../tests/README.md) says where each script's tests go.
