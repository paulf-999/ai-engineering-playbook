<!-- version: 1.3.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-11 -->
# 🏗️ Target architecture docs

**Purpose:** what the docs in this folder cover, and the order to read them in.

Together they plan a new, leaner Claude Code configuration for this repo.

## 📖 Reading order

1. [Review of the old Claude configuration](current_architecture.md): what it contains, what works well, and where it grew heavier than the evidence justified.
2. [Design principles](design_principles.md): the principles every part of the new configuration follows, and the checks a new part must pass.
3. [Target architecture](target_architecture.md): what the new configuration contains, what loads when, and how its cost and benefit are measured.
4. [Implementation status](implementation_status.md): which parts of the target architecture are built, which are outstanding, and the effort each needs.
5. [Reference material](reference_material/README.md): the sources the other pages cite, such as Anthropic's course on AI-native software development and research from DORA (DevOps Research and Assessment).

## ➕ Adding a component

To add a rule, skill, hook or agent, go straight to the [evaluation criteria](design_principles/02_evaluation_criteria.md), which its PR must answer.
