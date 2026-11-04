<!-- version: 1.7.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-04 -->
# 🧭 Design principles

**Purpose:** the principles every part of this repo's Claude configuration follows, and the checks a new part must pass.

## 📋 Executive Summary

- 🌱 **Stance:** a small required core, with skills and agents used only when a task needs them, as the [handover review](reference_material/handover_review.md) recommends.
- ⚖️ **Bar:** the configuration must beat a near-bare setup of `CLAUDE.md`, tests and CI on results, effort or consistency.
- ➕ **Adding:** a component (a rule, skill, hook or agent) from the [old configuration](current_architecture.md) is reviewed one file at a time for the bloat that made the old setup costly, then ported, slimmed or left out.
- 🗑️ **Keeping:** a component is removed once the [task log](../maintenance/task_log.md) shows it getting in the way, or going unused.
- ⚠️ **Watch for:** workflows that force agents to run, too much context in every session, and rules that repeat CI checks.

## 📖 The pages

Read them in this order:

1. [The principles, and how each is checked](design_principles/01_principles.md).
2. [The checks a new or ported component must pass](design_principles/02_evaluation_criteria.md).

## 📌 Status and terms

- 🚧 **Status:** adopted, with the always-on budget check and the [task log](../maintenance/task_log.md) in place.

This page defines the terms its child pages use:

- 📥 **Always-on:** context that loads into every session, whatever the task.
- 📝 **Task log:** a [table](../maintenance/task_log.md) with one row per real task, recording its outcome and any feedback on components.
