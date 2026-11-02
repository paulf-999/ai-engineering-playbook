<!-- version: 1.1.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🧭 Design principles

For anyone adding to or reviewing this repo's Claude configuration: the principles every component must follow, how each one is checked, and the criteria a new or ported component must pass.

## 📋 Executive Summary

- **Stance:** a small mandatory foundation, with skills and agents used only when a task needs them.
- **Bar:** the configuration earns its place only if it gives comparable or better outcomes than a near-bare setup of `CLAUDE.md`, tests and CI alone, with less total effort and less variation in quality.
- **Adding:** a component (rule, skill, hook or agent), whether new or ported from the current configuration, is added only when logged tasks show a gap that it closes.
- **Keeping:** a component stays only while the task log shows it helping, and is removed in one small PR when it doesn't.
- **Lessons:** each principle answers a lesson from the [current architecture](current_architecture.md) or [issue #7](https://github.com/paulf-999/ai-engineering-playbook/issues/7), so the rebuild doesn't repeat it.

## 📌 Status and terms

- **Status:** adopted on 2026-11-02, while the always-on budget check and the task log are planned but not yet built.
- **Always-on:** context that loads into every session, whatever the task.
- **Task log:** a planned table with one row per real task, recording its outcome and any feedback on components.
- **Hook:** a script Claude Code runs automatically when an event happens, such as a tool call.
- **Pre-commit:** the checks that run on your machine before each commit.

## ⚖️ Guiding stance

- **Two approaches:** encoding standards and processes in a shared framework, or relying on initial design, the model's own capabilities and post-build testing.
- **Source:** section 4 of the maintainer's handover document, which isn't in the repo.
- **Neither wins by default:** the framework must show it beats the near-bare setup on outcomes, effort or consistency.
- **Watch for:** mandatory agent orchestration, excessive context loading and rules that repeat CI/CD (continuous integration and delivery) checks.

## 🧱 Principles

| Principle | What it means | How it's checked | Lesson it answers, from [Where complexity outran evidence](current_architecture/03_complexity_without_evidence.md) unless linked |
|---|---|---|---|
| 🌱 **Minimal by default** | • **Mandatory tier:** only `CLAUDE.md`, one test command, CI, the planned always-on budget check and the PR size check.<br>• **Everything else:** optional or task-specific, loaded only when a task needs it. | • **Budget:** a planned CI check will fail if always-on context exceeds 3,000 tokens, estimated as characters ÷ 4.<br>• **Why 3,000:** about a tenth of the current configuration's load, and within Anthropic's 200-line `CLAUDE.md` guidance.<br>• **PR size:** CI already fails a PR of more than 20 files, except on `release/` branches. | • **Always-on weight:** about 30,000 tokens loaded into every session, per the [snapshot](current_architecture/01_snapshot.md) at commit `915685f`. |
| 💰 **Every component earns its cost** | • **Evidence:** a recurring gap in logged tasks justifies each component.<br>• **Curated context:** irrelevant context degrades answers, so less is often better ([DORA findings](reference_material/dora_ai_capabilities/03_findings.md), pp. 32–33). | • **Criteria:** the component's PR answers the evaluation criteria below. | • **Per-turn overhead:** a hook injected the same reminder into every turn.<br>• **Rules about rules:** authoring and scorecard standards that don't change outcomes directly. |
| 🔒 **Enforce what must hold** | • **Advisory:** prose rules and skills guide Claude.<br>• **Enforced:** anything that must always hold is a hook, test or CI check. | • **Review:** a PR adding a must-hold rule names the check that enforces it. | • **Advisory controls:** most safeguards relied on Claude checking itself. |
| 🔁 **No duplicate controls** | • **One control per concern:** a rule doesn't restate what CI or pre-commit already enforces. | • **Criteria:** the "No duplicate" criterion below. | • **Repeated checks:** [issue #7](https://github.com/paulf-999/ai-engineering-playbook/issues/7) flags rules that repeat CI/CD checks, adding context without adding safety. |
| 🔌 **Opt-in, never mandatory** | • **No orchestration:** no workflow requires a skill or agent to be used. | • **Criteria:** the "No orchestration" criterion below. | • **Universal loading:** [issue #7](https://github.com/paulf-999/ai-engineering-playbook/issues/7) asks for capabilities loaded per task, rather than everything universally. |
| 📏 **Measure outcomes and overhead** | • **Outcomes:** time to an accepted change, rework, and how often a human steps in.<br>• **Overhead:** always-on tokens, and time spent maintaining the configuration. | • **Task log:** a planned log with one row per real task.<br>• **Milestone:** a review point every 20 logged tasks or 4 weeks, whichever comes first.<br>• **Why:** 20 tasks give enough evidence to judge a component, and 4 weeks stops an unused one lingering. | • **No outcome data:** nothing showed which components helped. |
| 🗑️ **Retire what doesn't pay** | • **Feedback:** a component that helps, hinders or goes unused gets a one-line note in the task log.<br>• **Retire:** a component flagged unhelpful twice, or unused for a milestone, is removed.<br>• **Why twice:** one flag may be a one-off, while two show a pattern. | • **Milestone review:** retires flagged components.<br>• **Halving test:** asks whether removing half the components would make outcomes materially worse. | • **No outcome data:** without evidence, nothing showed which components to remove. |
| 🧑 **Humans own judgement calls** | • **Accountable:** a person merges every PR and decides every question of scope or design. | • **Branch ruleset:** every change to `main` goes through a PR with all required CI checks passing.<br>• **Gap:** the ruleset requires no approvals, so a person merging each PR is a convention, not enforced. | • **Advisory controls:** approval rested on Claude's own restraint. |

- **Carried over:** the current configuration's other principles, which [proposed changes](current_architecture/05_proposed_changes.md) lists, still apply:
  - **Reversible:** every change is easy to undo.
  - **In stages:** a feature starts small and grows only once it proves useful.
  - **Essentials first:** each page and rule gives the core idea before the detail.
  - **Live sources:** point to the real file or setting, rather than keeping lists that go stale.

## ✅ Evaluation criteria for a new or ported component

Answer each criterion in a few lines in the component's PR description, with no separate scorecard.

| Stage | Criterion | Passes when |
|---|---|---|
| Should it exist? | • **Evidence:** a gap appears in the task log. | • **Recurring:** the gap appears in at least two logged tasks. |
| | • **Model gap:** Claude gets it wrong without the component. | • **Still wrong:** rerunning the task with the near-bare setup still shows the gap. |
| | • **No duplicate:** nothing else covers it. | • **Uncovered:** CI, pre-commit and existing components don't already handle it. |
| What shape? | • **Right mechanism:** the form fits the need. | • **Fact for every session:** `CLAUDE.md`.<br>• **Guidance for certain files:** a path-scoped rule, which loads only when those files are open.<br>• **Multi-step procedure:** a skill.<br>• **Must always hold:** a hook or CI check.<br>• **Separate context or independent view:** an agent. |
| | • **Tier:** it loads only when needed. | • **Default:** optional or task-specific, unless every engineer needs it on every task. |
| | • **Cost:** it fits the budget. | • **Always-on:** the 3,000-token budget check still passes. |
| | • **No orchestration:** nothing depends on it. | • **Optional:** no workflow requires it. |
| Is it working? | • **Before and after:** it closes the gap. | • **Fixed:** rerunning the logged task with the component no longer shows the gap. |
| | • **Indicator:** its benefit is visible. | • **Named:** the PR names a leading (early) signal and a lagging (later) outcome to watch in the task log, such as fewer corrections and less rework. |
| | • **Retire trigger:** it can leave cleanly. | • **Clean exit:** one small PR removes it without breaking anything else. |
