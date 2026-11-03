<!-- version: 1.2.2 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# 🧱 Design principles: Principles

**Purpose:** the principles every new or changed component must follow, and how each one is checked.

They're part of this repo's [design principles](../design_principles.md).

| Principle | What it means | Checked by | [Lesson](../current_architecture/03_complexity_without_evidence.md) |
|---|---|---|---|
| 🌱 **Minimal by default** | Beyond the [mandatory core](../target_architecture.md#-tiers) of `CLAUDE.md`, tests and CI, everything is optional. | A planned budget check on context loaded every session | Always-on weight |
| 💰 **Every component earns its cost** | It closes a gap seen in logged tasks. | Its PR's answers to the [evaluation criteria](02_evaluation_criteria.md) | Per-turn overhead, and [irrelevant context](../reference_material/dora_ai_capabilities/03_findings.md) (DevOps Research and Assessment, pp. 32–33) |
| 🔒 **Enforce what must hold** | Use a hook, test or CI check, not prose. | The PR naming that check | Advisory controls |
| 🔁 **No duplicate controls** | A rule never restates a CI or pre-commit check. | The "No duplicate" criterion | Repeated checks ([#7](https://github.com/paulf-999/ai-engineering-playbook/issues/7)) |
| 🔌 **Opt-in, never mandatory** | No workflow requires a skill or agent. | The "No orchestration" criterion | Universal loading ([#7](https://github.com/paulf-999/ai-engineering-playbook/issues/7)) |
| 📏 **Measure outcomes and overhead** | Log each task's [outcome and overhead](../target_architecture.md#-measures). | The planned task log, one row per task | No outcome data |
| 🗑️ **Retire what doesn't pay** | Retire a component flagged unhelpful twice, or unused for a milestone. | The milestone review | No outcome data |
| 🧑 **Humans own judgement calls** | A person merges every PR and decides scope and design. | Changes reach `main` only by PR, though approval isn't enforced | Advisory controls |

## 🔢 Numbers and tests

- 📏 **3,000-token ceiling on every-session context:** a tenth of what the [current configuration](../current_architecture/01_snapshot.md) loads, and the top of our 2,000–3,000-token estimate for Anthropic's 200-line `CLAUDE.md` advice.
- 🗓️ **Milestone, every 20 tasks or 4 weeks:** enough evidence to judge a component, without letting an unused one linger.
- 🚩 **Flagged twice:** in the task log, one flag may be chance, while two show a pattern.
- 🔪 **Halving test, at each milestone:** would losing half the components materially hurt outcomes?

## ♻️ Carried over

These principles from the current setup still apply:

- Make every change easy to reverse.
- Grow in small stages.
- Load essentials first, and detail only on demand.
- Link to live sources rather than keeping lists that go stale.
