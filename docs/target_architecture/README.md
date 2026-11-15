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
- 🔄 **[Workflow](architecture/_workflow.md):** the four AI-native development practices it adopts, the order they're adopted in, and agent commits.
- 💰 **[Budget and guards](architecture/_budget_and_guards.md):** what the always-on budget counts and caps, and the three checks that protect the design.
- 📏 **[Measures](architecture/_measures.md):** what each regular review records from session transcripts and git history, and how it acts on it.

## 🏛️ The old setup

This design replaces [`claude_ai_playbook`](https://github.com/paulf-999/claude_ai_playbook), a personal Claude Code setup reviewed at commit `915685f` (2026-10-31). Its safe installer, tests and checks made it reproducible, but about 30,000 tokens of rules loaded into every session, whatever the task.

### 🚩 Where complexity outran evidence

- 🏋️ **Always-on weight:** about 30,000 tokens loaded every session, and nothing measured how many a task used.
- 🔁 **Per-turn overhead:** a hook added the response-format rules to every prompt, including trivial ones.
- 📐 **Rules about rules:** standards for writing rules, scoring them and dating them added upkeep without changing engineering results.
- 🗣️ **Advisory controls:** most safeguards were written rules that relied on Claude checking itself.
- 📉 **No outcome data:** nothing recorded delivery time, rework or human effort, so nobody could tell which components helped.

The lessons carried forward: start minimal, review each old component for those patterns before porting it, ask whether removing half the components would make results worse, and keep the old setup's safe installer, portable paths, checks that can fail, on-demand loading and fresh-context review.

## 📖 Further reading

Read the [design principles](design_principles.md) next: the principles every part follows, and the checks a new part must pass.

Outside reading the design doesn't cite yet, but which each gives a view the others don't:

- 📈 **[State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/):** survey evidence on AI adoption and outcomes.
- ⚖️ **[METR's trial of early-2025 AI on experienced developers](https://arxiv.org/abs/2507.09089):** a randomised trial showing felt speed-ups can hide real slowdowns.
- 🧰 **[Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html):** when to guide Claude and when to enforce, from outside Anthropic.
- 🧪 **[Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents):** a method for testing whether each part of the config still helps.
- 📘 **[Best practices for Claude Code](https://code.claude.com/docs/en/best-practices):** Anthropic's split between guidance Claude may follow and rules that always hold.
- 🏛️ **[The TOGAF Standard, 10th Edition](https://www.opengroup.org/togaf):** a shared method and vocabulary for enterprise architecture.

To add a rule, skill, hook or agent, go straight to the [evaluation criteria](design_principles/02_evaluation_criteria.md).
