<!-- version: 1.0.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🧱 Design principles: Principles

For anyone adding to or reviewing a component: the principles it must follow, and how each one is checked.

- **Part of:** [Design principles](../design_principles.md).
- 📚 **Lessons:** each principle answers a lesson from [Where complexity outran evidence](../current_architecture/03_complexity_without_evidence.md), unless the table links another source.

| Principle | What it means | How it's checked | Lesson |
|---|---|---|---|
| 🌱 **Minimal by default** | • 🧱 **Mandatory:** only `CLAUDE.md`, tests, CI and two size checks.<br>• 🔌 **Everything else:** optional or task-specific. | • 📏 **Budget:** a planned CI check caps always-on context at 3,000 tokens.<br>• 📦 **PR size:** CI fails a PR over 20 files, bar `release/` branches. | Always-on weight |
| 💰 **Every component earns its cost** | • 📊 **Evidence:** a recurring gap in logged tasks.<br>• 🎯 **Curated context:** irrelevant context degrades answers ([DORA](../reference_material/dora_ai_capabilities/03_findings.md), pp. 32–33). | • ✅ **Criteria:** its PR answers the [evaluation criteria](02_evaluation_criteria.md). | Per-turn overhead, and rules about rules |
| 🔒 **Enforce what must hold** | • 🛡️ **Must hold:** enforced by a hook, test or CI check, not by prose. | • 👀 **Review:** the PR names the check that enforces it. | Advisory controls |
| 🔁 **No duplicate controls** | • 🚫 **One control:** a rule never restates a CI or pre-commit check. | • ✅ **Criteria:** the "No duplicate" check. | Repeated checks ([#7](https://github.com/paulf-999/ai-engineering-playbook/issues/7)) |
| 🔌 **Opt-in, never mandatory** | • 🙅 **No orchestration:** no workflow requires a skill or agent. | • ✅ **Criteria:** the "No orchestration" check. | Universal loading ([#7](https://github.com/paulf-999/ai-engineering-playbook/issues/7)) |
| 📏 **Measure outcomes and overhead** | • 📈 **Outcomes:** time to acceptance, rework and human interventions.<br>• ⚖️ **Overhead:** always-on tokens and upkeep time. | • 📝 **Task log:** one row per real task, once built.<br>• 🗓️ **Milestone:** a review every 20 tasks or 4 weeks. | No outcome data |
| 🗑️ **Retire what doesn't pay** | • 🚩 **Retire:** a component flagged unhelpful twice, or unused for a milestone. | • 🗓️ **Milestone review:** removes flagged components and runs the halving test. | No outcome data |
| 🧑 **Humans own judgement calls** | • ✋ **Accountable:** a person merges every PR and decides scope and design. | • 🔀 **Ruleset:** changes reach `main` only by PR, with checks passing.<br>• ⚠️ **Gap:** with no approval required, human merging is a convention. | Advisory controls |

## 🔢 Why these numbers

- 📏 **3,000 tokens:** about a tenth of the current [snapshot](../current_architecture/01_snapshot.md)'s load, and roughly in line with Anthropic's advice to keep `CLAUDE.md` under 200 lines.
- 🗓️ **20 tasks or 4 weeks:** enough evidence to judge a component, without letting an unused one linger.
- 🚩 **Flagged twice:** one flag may be a one-off, while two show a pattern.
- 🔪 **Halving test:** asks whether removing half the components would make outcomes materially worse.

## ♻️ Carried over

- ♻️ **Still apply:** reversible changes, growing in stages, essentials first, and live sources over stale lists, as [proposed changes](../current_architecture/05_proposed_changes.md) lists.
