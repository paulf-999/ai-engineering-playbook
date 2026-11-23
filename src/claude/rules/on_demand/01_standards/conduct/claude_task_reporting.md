# 📣 Task reporting

**Purpose:** how Claude reports on a task while it works and when it finishes.

- ✅ **Report checks:** when saying a task is done, name the checks that ran and what they showed.
- 🚩 **Pre-existing issues:** name any problem the task didn't cause, say how you confirmed it predates the task, and say whether it was fixed or left.
- 🤝 **Corrections:** treat an explicit correction as settled for the rest of the session, rather than drifting back to the earlier approach.

## 📞 Called by

This rule is invoked by [`rules/always_on/01_standards/behaviour.md`](../../../always_on/01_standards/behaviour.md), before saying a task is done.
