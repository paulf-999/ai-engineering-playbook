<!-- version: 1.3.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# 🧭 Design principles

**Purpose:** the principles every part of this repo's Claude configuration follows, and the checks a new part must pass.

## 📋 Executive Summary

- 🌱 **Stance:** a small required core, with skills and agents used only when a task needs them.
- ⚖️ **Bar:** the configuration must beat a near-bare setup of `CLAUDE.md`, tests and CI on results, effort or consistency.
- ➕ **Adding:** a component, meaning a rule, skill, hook or agent, needs a gap seen in real tasks that it closes.
- 🗑️ **Keeping:** a component stays only while the task log shows it helping.
- ⚠️ **Watch for:** workflows that force agents to run, too much context in every session, and rules that repeat CI checks.

## 📖 The pages

Read them in this order:

1. [The principles, and how each is checked](design_principles/01_principles.md).
2. [The checks a new or ported component must pass](design_principles/02_evaluation_criteria.md).

## 📌 Status and terms

- 🚧 **Status:** adopted on 2026-11-02, while the always-on budget check and the task log are planned but not yet built.

These pages define their own terms:

- 📥 **Always-on:** context that loads into every session, whatever the task.
- 📝 **Task log:** a planned table with one row per real task, recording its outcome and any feedback on components.
