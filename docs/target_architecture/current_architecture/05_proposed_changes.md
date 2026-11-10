<!-- version: 1.2.2 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-10 -->
# 🛠️ Current architecture: Proposed changes

**Purpose:** changes proposed for two core rule files in the old Claude configuration, which aren't yet adopted.

This page is part of the [current architecture](../current_architecture.md) review. Both files load in every session: one sets Claude's guiding principles, and the other indexes its naming and writing standards. Each keeps its current layout, and only its content changes.

## 🧭 Changes to `guiding_principles.md`

The [guiding principles file](https://github.com/paulf-999/claude_ai_playbook/blob/915685f/src/claude/rules/01_essentials/guiding_principles.md) would change like this:

- 🔗 **Merge overlaps:** combine the three rows on real need, token cost and automation payback into "Every component earns its cost".
- 🎯 **Curated context:** add [DORA's finding](../reference_material/core/dora_ai_capabilities/03_findings.md) that irrelevant context degrades answers.
- 🛡️ **Enforce what must hold:** add [Anthropic's SDLC course](../reference_material/core/anthropic_ai_native_sdlc.md)'s point that written guidance can be ignored, while hooks and CI checks can't.
- 📏 **Measure outcomes:** give each component an early signal and a later result to watch, as every play, or recommended practice, in the SDLC course does.
- 🧑 **Human accountability:** state that people own every judgement call, as the SDLC course insists.

## 📐 Changes to `claude_usage_standards.md`

The [usage standards index](https://github.com/paulf-999/claude_ai_playbook/blob/915685f/src/claude/rules/01_essentials/claude_usage_standards.md) would change like this:

- 📁 **Change files:** for multi-file tasks, write a `spec.md` of intent and acceptance criteria, and a `plan.md`, so the goal is settled before building, as the SDLC course recommends.
- 🌐 **Where they live:** the rule asking for them goes in the user-level config folder, `~/.claude/`, which applies to every repo, while each task's files go in its PR.
- 🧹 **Current state only:** remove the file's history note, which breaks its own writing rules.
