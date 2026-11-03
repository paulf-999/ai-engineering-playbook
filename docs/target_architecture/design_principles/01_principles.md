<!-- version: 1.2.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# 🧱 Design principles: Principles

For anyone adding to or reviewing a component: the principles it must follow, and how each one is checked.

- **Part of:** [Design principles](../design_principles.md).
- 📚 **Lessons:** each principle answers a lesson from [Where complexity outran evidence](../current_architecture/03_complexity_without_evidence.md), unless the table links another source.

| Principle | What it means | Checked by | Lesson |
|---|---|---|---|
| 🌱 **Minimal by default** | Everything beyond the [mandatory tier](../target_architecture.md#-tiers) is optional. | A planned budget check on always-on context | Always-on weight |
| 💰 **Every component earns its cost** | It closes a gap seen in logged tasks. | Its PR's [evaluation criteria](02_evaluation_criteria.md) answers | Per-turn overhead, and [irrelevant context](../reference_material/dora_ai_capabilities/03_findings.md) (DORA, pp. 32–33) |
| 🔒 **Enforce what must hold** | Use a hook, test or CI check, not prose. | The PR naming that check | Advisory controls |
| 🔁 **No duplicate controls** | A rule never restates a CI or pre-commit check. | The "No duplicate" criterion | Repeated checks ([#7](https://github.com/paulf-999/ai-engineering-playbook/issues/7)) |
| 🔌 **Opt-in, never mandatory** | No workflow requires a skill or agent. | The "No orchestration" criterion | Universal loading ([#7](https://github.com/paulf-999/ai-engineering-playbook/issues/7)) |
| 📏 **Measure outcomes and overhead** | Log each task's [outcome and overhead](../target_architecture.md#-measures). | The planned task log | No outcome data |
| 🗑️ **Retire what doesn't pay** | Retire a component flagged unhelpful twice, or unused for a milestone. | The milestone review | No outcome data |
| 🧑 **Humans own judgement calls** | A person merges every PR and decides scope and design. | PR-only `main`, though approval isn't enforced | Advisory controls |

## 🔢 Numbers and tests

- 📏 **3,000 tokens:** a tenth of the [snapshot](../current_architecture/01_snapshot.md)'s load, and the top of our estimate for Anthropic's 200-line `CLAUDE.md` advice (2,000–3,000 tokens).
- 🗓️ **Milestone, every 20 tasks or 4 weeks:** enough evidence to judge a component, without letting an unused one linger.
- 🚩 **Flagged twice:** one flag may be chance, two show a pattern.
- 🔪 **Halving test:** would losing half the components materially hurt outcomes?

## ♻️ Carried over

- ♻️ **Still apply:** reversible changes, growing in stages, essentials first, and live sources over stale lists, from the [proposed changes](../current_architecture/05_proposed_changes.md).
