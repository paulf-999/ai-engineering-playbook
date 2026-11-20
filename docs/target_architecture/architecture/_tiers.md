# 🎚️ Tiers

**Purpose:** the three groups every component sits in, by when it loads, and how a new one is placed. It's part of the [target architecture](../README.md).

Every component, meaning one file of instructions or one automatic check, sits in one of three tiers, or groups, by when it loads:

| Tier | Contains | Loads |
|---|---|---|
| 🔒 **Required** | [`CLAUDE.md`](../../../CLAUDE.md), the [global `CLAUDE.md` template](../../../src/claude/CLAUDE.md) and the rules it loads in every session, the [plan-sections](../../../src/claude/hooks/hook_enforcement_plan_sections.sh), [done-checks](../../../src/claude/hooks/hook_enforcement_done_checks.sh), [worktree-edits](../../../src/claude/hooks/hook_enforcement_worktree_edits.sh) and [kaizen reminder](../../../src/claude/hooks/hook_reminder_kaizen_due.sh) hooks that a global `make install` registers, `make test` and the CI checks, including the [design guards](_budget_and_guards.md#️-design-guards) | Every session, or every PR |
| 🧰 **Optional** | Skills, which are step-by-step procedures, agents, which work in a separate context, and on-demand rules | When the engineer or Claude asks for one |
| 📂 **Task-specific** | Path-scoped rules, whose `paths:` setting names the files they apply to | When a matching file is open |

- 🧭 **Choosing a tier:** the [evaluation criteria](../design_principles/02_evaluation_criteria.md#-what-shape) match each need to a mechanism, which sets its tier.
- 🛑 **Hooks and every-session rules:** a rule made to load in every session raises the always-on weight [red flag](../design_principles/02_evaluation_criteria.md#-review-each-file), and the always-on budget still caps always-on rules.
- 🔐 **Tool access:** the config ships no MCP servers, which connect Claude to outside tools, and no list of pre-approved actions, so each engineer connects their own tools. `make install` adds deny rules that keep Claude's file tools out of `.env` files, though a shell command such as `cat` can still read one. Pushes aren't gated, since a prompt would stall unattended loops and the `protect_main` ruleset already requires a PR to change `main`. A PR that ships one gives it the least access it needs, per [`permission_recommendations.md`](../../../src/claude/rules/on_demand/01_standards/claude_config/permission_recommendations.md), as [DORA advises](../reference_material/core/dora_ai_capabilities.md#-findings-worth-carrying-forward).
