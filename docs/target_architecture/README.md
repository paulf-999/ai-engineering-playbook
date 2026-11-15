# 🏗️ Target architecture

**Purpose:** what the new set of Claude Code instructions contains, which parts Claude reads in every session and which only when needed, and how their cost and benefit are measured.

This page describes the design, and the [build progress issue](https://github.com/paulf-999/ai-engineering-playbook/issues/235) lists the parts not built yet.

The design rests on the [reference material](reference_material/README.md), and each choice follows the Source column of the [principles](design_principles/01_principles.md).

## 📋 Executive Summary

A session is one conversation with Claude Code. A small core is read in every session, everything else only when a task needs it, and a regular review removes any part that isn't helping.

- 🌱 **Small core:** only the [required group](architecture/_tiers.md) loads in every session or runs on every PR.
- 📥 **On demand:** everything else loads only when a task calls for it.
- 💰 **Budget:** an automatic check caps how much text loads into every session.
- 📏 **Measures:** each regular review notes which parts helped, got in the way or went unused, from session records and git history, and the budget check reports how much loads every session.

## 🗂️ The design in detail

- 🎚️ **[Tiers](architecture/_tiers.md):** the three groups every component sits in, by when it loads, and tool access.
- 🔄 **[Workflow](architecture/_workflow.md):** the six AI-native development practices, the order they're adopted in, and agent commits.
- 💰 **[Budget and guards](architecture/_budget_and_guards.md):** what the always-on budget counts and caps, and the three checks that protect the design.
- 📏 **[Measures](architecture/_measures.md):** what each regular review records from session transcripts and git history, and how it acts on it.

## 📖 Further reading

After this page, read these in order. The build progress and reference material are linked at the top.

1. [Design principles](design_principles.md): the principles every part follows, and the checks a new part must pass.
2. [Review of the old setup](../../maintenance/old_setup_review.md): what the earlier, larger set of instructions contained, what worked, and where it grew heavier than the evidence justified.

To add a rule, skill, hook or agent, go straight to the [evaluation criteria](design_principles/02_evaluation_criteria.md).
