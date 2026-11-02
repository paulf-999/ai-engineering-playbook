<!-- version: 1.2.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🧭 Design principles

For anyone adding to or reviewing this repo's Claude configuration: the principles each component follows, and the checks it must pass to be added.

## 📋 Executive Summary

- 🌱 **Stance:** a small mandatory foundation, with skills and agents used only when a task needs them.
- ⚖️ **Bar:** the configuration must beat a near-bare setup of `CLAUDE.md`, tests and CI on outcomes, effort or consistency.
- ➕ **Adding:** a component (rule, skill, hook or agent) needs a logged gap that it closes.
- 🗑️ **Keeping:** a component stays only while the task log shows it helping.
- ⚠️ **Watch for:** mandatory agent orchestration, excessive context loading, and rules that repeat CI checks.

## 🧱 Principles

- **Read:** [Principles](design_principles/01_principles.md), the principles and how each is checked.

## ✅ Evaluation criteria

- **Read:** [Evaluation criteria](design_principles/02_evaluation_criteria.md), the checks a new or ported component must pass.

## 📌 Status and terms

- 🚧 **Status:** adopted on 2026-11-02, while the always-on budget check and the task log are planned but not yet built.
- 📚 **Source:** the stance follows section 4 of the maintainer's handover document, which isn't in the repo.

### 📖 Terms

- 📥 **Always-on:** context that loads into every session, whatever the task.
- 📝 **Task log:** a planned table with one row per real task, recording its outcome and any feedback on components.
- 🔄 **CI:** continuous integration, the checks GitHub runs on every PR.
- 🪝 **Hook:** a script Claude Code runs automatically when an event happens, such as a tool call.
- 🧪 **Pre-commit:** the checks that run on your machine before each commit.
