<!-- version: 2.1.7 -->
<!-- created: 2026-09-17 -->
<!-- updated: 2026-11-10 -->
<!-- applies_to: * -->
<!-- miss_cost: medium — multi-phase work runs past a wrong turn and needs redoing -->
# 🗂️ Claude plans

**Purpose:** when to pause multi-phase work, and plans in particular, for the user's approval.

- 🛑 **Phase gates:** for work of 3 or more phases, each a stage that ends in something the user can check, such as a PR, stop after each phase, say what it delivered, and wait for a go-ahead, since early feedback stops wasted phases.
  - **Skip when:** the user waives gates, or the work has a single phase.
- 🗂️ **Plan approval:** the "Implement the following plan:" message Claude Code sends after you accept a plan isn't a go-ahead, so wait for an explicit one.

- **Read on demand:** `_rules_on_demand/03_workflows/saving_plans.md`, in your Claude config directory, once a plan is approved.
- **Read on demand:** `_rules_on_demand/03_workflows/sdlc_workflow.md`, in your Claude config directory, before drafting a plan in plan mode.
