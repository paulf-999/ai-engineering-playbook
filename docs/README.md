<!-- version: 1.1.5 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-13 -->
# 📚 Docs folder guide

**Purpose:** what each folder under `docs/` holds, and where a new doc goes.

The folders, starting with the one most readers want:

- 🏗️ **Design:** [`target_architecture/`](target_architecture/) explains how the Claude Code instructions are set up and why, with the research behind them. Start here.
- 👥 **Guides:** [`guides/`](guides/) holds how-to guides for contributors, such as the [Git branching strategy](guides/git_branching_strategy.md).
- 🛠️ **How the repo maintains itself:** [`maintenance/`](maintenance/) covers upkeep, such as file headers, tests, and the scores given to tests, rules and the repo.

## 🆕 Adding a doc

`make test` fails on a new doc that misses step 2:

1. Put it in the folder for its reader, from the list above.
2. Open it with the [version header](maintenance/file_headers.md).
3. Start it with a **Purpose:** line.
