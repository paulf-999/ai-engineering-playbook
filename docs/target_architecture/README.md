<!-- version: 1.3.3 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-13 -->
# 🏗️ Target architecture docs

**Purpose:** what the docs in this folder cover, and the order to read them in.

Together they describe a small, focused set of instructions for Claude Code, and why it's built that way.

## 📖 Reading order

1. [Target architecture](target_architecture.md): what the instructions contain, which are read on every task and which only when needed, and how their cost and benefit are measured.
2. [Design principles](design_principles.md): the principles every part follows, and the checks a new part must pass.
3. [Review of the old setup](legacy_architecture.md): what the earlier, larger set of instructions contained, what worked, and where it grew heavier than the evidence justified.
4. [Reference material](reference_material/README.md): the sources the other pages cite, such as Anthropic's course on AI-native software development and research from DORA, Google's DevOps research programme.

## 🛠️ How the repo maintains itself

The [implementation status](implementation_status.md) shows which parts are built and which are outstanding. To add a rule, skill, hook or agent, go straight to the [evaluation criteria](design_principles/02_evaluation_criteria.md).
