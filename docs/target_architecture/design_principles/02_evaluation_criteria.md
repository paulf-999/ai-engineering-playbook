<!-- version: 1.6.2 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-04 -->
# ✅ Design principles: Evaluation criteria

**Purpose:** the checks a new component, or one ported from the [old configuration](../current_architecture.md), faces when it's added and while it's on trial.

This page is part of the [design principles](../design_principles.md), which also define always-on.

Answer each check in the PR's Additional Details section, under one **Evaluation criteria** bullet with a child per check, since the [PR template](../../../.github/pull_request_template.md) limits that section's bullets.

## 🚪 Review each file

Each file from the old configuration is reviewed on its own for bloat, and you decide whether to port it as is, port a slimmed version or leave it out. Reviewed files can then share a PR.

- [ ] 🚩 **Red flags:** for each file, the PR lists every hit below and every failed [What shape?](#-what-shape) check, with the decision and why.
  - **Ports vs new:** for a port these inform the decision but never block it, while a new component must pass every check.

The flags come from the [review of the old setup](../current_architecture/03_complexity_without_evidence.md) and the [handover review](../reference_material/handover_review.md), and cover how a component loads and enforces, not its topic.

| Red flag | Spotted by | Suggested fix |
|---|---|---|
| 🏋️ **Always-on weight** | No `paths:` setting, or imported into `CLAUDE.md` | Make it path-scoped or on demand |
| ⏱️ **Per-turn overhead** | A hook that fires on every prompt, such as `UserPromptSubmit` | Fire on a narrower event |
| 🗣️ **Advisory-only control** | Prose for something that must always hold, such as "never commit to main" | Keep the prose, and consider adding a hook or CI check |

## 🧰 What shape?

Its shape passes when:

- [ ] 🔁 **No duplicate:** CI, pre-commit and existing components don't already handle it.
- [ ] 🧭 **Right mechanism:** its form fits the need, per the table below.
- [ ] 🎚️ **Tier:** it sits in a [tier](../target_architecture.md#-tiers) that loads only for the tasks that need it, unless every engineer needs it on every task.
- [ ] 💰 **Cost:** always-on context stays within the [always-on budget](../target_architecture.md#-always-on-budget).
- [ ] 🔌 **No orchestration:** no workflow requires it, so it stays [opt-in](01_principles.md).

| Need | Mechanism |
|---|---|
| 📌 **A fact for every session** | `CLAUDE.md` |
| 📂 **Guidance for certain files** | A path-scoped rule, which loads only when those files are open |
| 🔄 **A multi-step procedure** | A skill |
| 🛡️ **Something that must always hold** | A hook, test or CI check |
| 👥 **A separate context or independent view** | An agent |

## 🧪 Is it working?

Once it's in use, it passes when:

- [ ] 🧪 **Trial:** at the next [review](01_principles.md#-numbers-and-tests), it has been used and hasn't got in the way.
- [ ] 📈 **Signals:** the PR names an early signal and a later result to watch, such as fewer corrections and less rework.
- [ ] ↩️ **Clean exit:** one small PR could remove it without breaking anything else.
