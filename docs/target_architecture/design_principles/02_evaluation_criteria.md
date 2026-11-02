<!-- version: 1.0.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# ✅ Design principles: Evaluation criteria

For anyone adding a component or porting one from the current configuration: the checks it must pass, answered in a few lines in its PR description.

- **Part of:** [Design principles](../design_principles.md).
- 🚧 **Status:** the task log and the always-on budget check are planned, not yet built.

## 🚪 Should it exist?

- [ ] 📊 **Evidence:** the gap appears in at least two logged tasks.
- [ ] 🤖 **Model gap:** rerunning the task with a near-bare setup (only `CLAUDE.md`, tests and CI) still shows the gap.
- [ ] 🔁 **No duplicate:** CI, pre-commit and existing components don't already handle it.

## 🧰 What shape?

- [ ] 🧭 **Right mechanism:** its form fits the need, per the table below.
- [ ] 🎚️ **Tier:** it's optional or task-specific, unless every engineer needs it on every task.
- [ ] 💰 **Cost:** the always-on budget check still passes.
- [ ] 🔌 **No orchestration:** no workflow requires it.

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
