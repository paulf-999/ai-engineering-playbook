<!-- version: 1.2.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# ✅ Design principles: Evaluation criteria

**Purpose:** the checks a new component, or one ported from the [old configuration](../current_architecture.md), must pass before it's added.

This page is part of the [design principles](../design_principles.md), which also define always-on and task log. Answer each check in the PR's Additional Details section, under one **Evaluation criteria** bullet with a child per check, since that section allows only five top-level bullets.

Until the task log and budget check exist:

- 🧾 **Evidence:** cite the tasks in the PR description.
- 🧮 **Tokens:** estimate always-on tokens as characters ÷ 4, against the [3,000-token budget](01_principles.md#-numbers-and-tests).

## 🚪 Should it exist?

It should exist only if all three hold:

- [ ] 📊 **Evidence:** the gap appears in at least two logged tasks, since one may be a one-off.
- [ ] 🤖 **Claude still gets it wrong:** rerunning the task with only `CLAUDE.md`, tests and CI still shows the gap.
- [ ] 🔁 **No duplicate:** CI, pre-commit and existing components don't already handle it.

## 🧰 What shape?

Its shape passes when:

- [ ] 🧭 **Right mechanism:** its form fits the need, per the table below.
- [ ] 🎚️ **Tier:** it loads only for the tasks that need it, unless every engineer needs it on every task.
- [ ] 💰 **Cost:** always-on context stays within the budget.
- [ ] 🔌 **No orchestration:** no workflow requires it, so it stays [opt-in](01_principles.md).

| Need | Mechanism |
|---|---|
| 📌 **A fact for every session** | `CLAUDE.md` |
| 📂 **Guidance for certain files** | A path-scoped rule, which loads only when those files are open |
| 🔄 **A multi-step procedure** | A skill |
| 🛡️ **Something that must always hold** | A hook, test or CI check |
| 👥 **A separate context or independent view** | An agent |

## 🧪 Is it working?

After it's added, it passes when:

- [ ] 🔬 **Before and after:** rerunning the logged task with the component no longer shows the gap.
- [ ] 📈 **Signals:** the PR names an early signal and a later result to watch, such as fewer corrections and less rework.
- [ ] ↩️ **Clean exit:** one small PR could remove it without breaking anything else.
