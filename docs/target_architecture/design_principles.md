<!-- version: 1.7.6 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-13 -->
# 🧭 Design principles

**Purpose:** the principles every part of this repo's Claude Code instructions follows, and the checks a new part must pass.

## 📋 Executive Summary

- 🌱 **Stance:** a small required core, with skills, which are step-by-step procedures, and agents, which are helpers that work separately, used only when a task needs them, as the [handover review](reference_material/core/handover_review.md) recommends.
- ⚖️ **Bar:** the instructions must do better than a minimal setup of just `CLAUDE.md`, tests and automatic checks, on results, effort or consistency.
- ➕ **Adding:** a component (a rule, skill, hook or agent) from the [old setup](legacy_architecture.md) is reviewed one file at a time for the bloat that made the old setup costly, then brought over, slimmed or left out.
- 🗑️ **Keeping:** a component is removed once a [regular review](design_principles/01_principles.md#-numbers-and-tests) finds it getting in the way, or going unused.
- ⚠️ **Watch for:** processes that make agents run every time, too much text loaded into every session, and rules that repeat automatic checks.

## 📖 The pages

Read them in this order:

1. [The principles, and how each is checked](design_principles/01_principles.md).
2. [The checks a new or ported component must pass](design_principles/02_evaluation_criteria.md).

## 📌 Status and terms

- 🚧 **Status:** adopted, with what is built tracked in the [implementation status](implementation_status.md).

This page defines the terms its child pages use:

- 💬 **Session:** one conversation with Claude Code.
- 📥 **Always-on:** text that loads into every session, whatever the task.
- 📜 **Session transcripts:** the record Claude Code keeps of each session, in the `projects/` folder of the Claude config directory, which each regular review reads for evidence of use.
