<!-- version: 1.1.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# ✅ Design principles: Evaluation criteria

For anyone adding a component or porting one from the [current configuration](../current_architecture.md): the checks it must pass, answered in its PR description under one top-level **Evaluation criteria** bullet, with a child bullet per check.

- **Part of:** [Design principles](../design_principles.md).
- 🧭 **Before the task log and budget check exist:** cite the tasks in the PR description, and estimate always-on tokens as characters ÷ 4, compared with the [budget](01_principles.md#-numbers-and-tests).
- 📚 **Terms:** always-on, task log and the other terms are defined in the parent's [Status and terms](../design_principles.md#-status-and-terms).

## 🚪 Should it exist?

- [ ] 📊 **Evidence:** the gap appears in at least two logged tasks, since one may be a one-off.
- [ ] 🤖 **Model gap:** rerunning the task with a near-bare setup (only `CLAUDE.md`, tests and CI) still shows the gap.
- [ ] 🔁 **No duplicate:** CI, pre-commit and existing components don't already handle it.

## 🧰 What shape?

- [ ] 🧭 **Right mechanism:** its form fits the need, per the table below.
- [ ] 🎚️ **Tier:** it's optional or loaded only for the tasks that need it, unless every engineer needs it on every task.
- [ ] 💰 **Cost:** always-on context stays within the [always-on budget](01_principles.md#-numbers-and-tests).
- [ ] 🔌 **No orchestration:** no workflow requires it, so it stays [opt-in](01_principles.md).

| Need | Mechanism |
|---|---|
| 📌 **A fact for every session** | `CLAUDE.md` |
| 📂 **Guidance for certain files** | A path-scoped rule, which loads only when those files are open |
| 🔄 **A multi-step procedure** | A skill |
| 🛡️ **Something that must always hold** | A hook, test or CI check |
| 👥 **A separate context or independent view** | An agent |

## 🧪 Is it working?

- [ ] 🔬 **Before and after:** rerunning the logged task with the component no longer shows the gap.
- [ ] 📈 **Indicators:** the PR names an early signal and a later outcome to watch, such as fewer corrections and less rework.
- [ ] ↩️ **Clean exit:** one small PR could remove it without breaking anything else.
