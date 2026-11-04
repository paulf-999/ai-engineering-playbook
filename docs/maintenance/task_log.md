<!-- version: 1.1.2 -->
<!-- created: 2026-11-03 -->
<!-- updated: 2026-11-04 -->
# 📝 Task log

**Purpose:** a record of real tasks done with this repo's Claude configuration, and of each regular review, so each component's trial and removal rest on evidence.

The [target architecture's measures](../target_architecture/target_architecture.md#-measures) define each column. This repo is public, so describe each task in general terms, with no client or employer details.

## 🧾 Tasks

Add one row when a task's change is accepted, and add rework to that row when a later fix is needed. Take time to acceptance from the session's transcript, from the first prompt to acceptance. Leave out any gap of over 15 minutes with no messages, which counts as a break.

| Date | Task | Time to acceptance (minutes) | Rework (fix commits) | Interventions | Component feedback |
|---|---|---|---|---|---|
| 📚 2026-11-03 | Summarised a published industry survey report into a reference page, updated the source register, and raised a PR | 17 | 0 | 0 | PR links point to the branch, not a commit, so break after merge; PR template's unticked options were removed; no title or plan confirmed before raising the PR |

## 🔁 Reviews

Add one row at each [regular review](../target_architecture/design_principles/01_principles.md#-numbers-and-tests):

| Date | Always-on tokens | Upkeep (hours) | Notes |
|---|---|---|---|
| 🏁 2026-11-03 | 887 | — | Starting point, measured by the [always-on budget check](../target_architecture/target_architecture.md#-always-on-budget) before any component is added |
| 🔧 2026-11-04 | 2,077 | 2.3 | Porting session, not a regular review: five files ported, plus about 15 independent review agents at about 90,000 tokens each |
