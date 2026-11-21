# 📚 Docs folder guide

**Purpose:** what each folder under `docs/` holds, and where a new doc goes.

The folders, starting with the one most readers want:

- 🏗️ **Design:** [`target_architecture/`](target_architecture/) explains how the Claude Code instructions are set up and why, with the research behind them. Start here.
- 👀 **Examples:** [`examples/`](examples/) shows what Claude does differently with the playbook installed, such as [a dbt model](examples/dbt/dbt_before_and_after.md).
- 👥 **Guides:** [`guides/`](guides/) holds how-to guides for contributors, such as the [Git branching strategy](guides/git_branching_strategy.md) and the [authoring guide](guides/authoring_guide.md).
- 🛠️ **How the repo maintains itself:** the top-level [`maintenance/`](../maintenance/) folder, kept apart from these docs, covers upkeep, such as the token report and the scores given to tests, rules and the repo.

## 🆕 Adding a doc

1. Put it in the folder for its reader, from the list above.
2. Open it as [`audience_and_depth.md`](../src/claude/rules/on_demand/01_standards/conduct/audience_and_depth.md#-openings) sets out.
