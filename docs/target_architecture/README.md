# 🏗️ Target architecture

**Purpose:** what the new set of Claude Code instructions contains, which parts Claude reads in every session and which only when needed, and how their cost and benefit are measured.

This page describes the design, and the [build progress issue](https://github.com/paulf-999/ai-engineering-playbook/issues/235) lists the parts not built yet.

The design rests on the [reference material](reference_material/README.md), and each choice follows the Source column of the [principles](design_principles/01_principles.md).

## 📋 Executive Summary

A session is one conversation with Claude Code. A small core is read in every session, everything else only when a task needs it, and a regular review removes any part that isn't helping.

- 🌱 **Small core:** only the [required group](#️-tiers) loads in every session or runs on every PR.
- 📥 **On demand:** everything else loads only when a task calls for it.
- 💰 **Budget:** an automatic check caps how much text loads into every session.
- 📏 **Measures:** each regular review notes which parts helped, got in the way or went unused, from session records and git history, and the budget check reports how much loads every session.

## 🎚️ Tiers

Every component, meaning one file of instructions or one automatic check, sits in one of three tiers, or groups, by when it loads:

| Tier | Contains | Loads |
|---|---|---|
| 🔒 **Required** | [`CLAUDE.md`](../../CLAUDE.md), the [global `CLAUDE.md` template](../../src/claude/CLAUDE.md) and the rules it loads in every session, the [plan-sections hook](../../src/claude/hooks/hook_enforcement_plan_sections.sh) that `make install` registers, `make test` and the CI checks, including the [design guards](#️-design-guards) | Every session, or every PR |
| 🧰 **Optional** | Skills, which are step-by-step procedures, agents, which work in a separate context, and on-demand rules | When the engineer or Claude asks for one |
| 📂 **Task-specific** | Path-scoped rules, whose `paths:` setting names the files they apply to | When a matching file is open |

- 🧭 **Choosing a tier:** the [evaluation criteria](design_principles/02_evaluation_criteria.md#-what-shape) match each need to a mechanism, which sets its tier.
- 🛑 **Hooks and every-session rules:** a hook, a script Claude Code runs automatically, that fires on every prompt, or a rule made to load in every session, raises a [red flag](design_principles/02_evaluation_criteria.md#-review-each-file), and the always-on budget still caps always-on rules.
- 🔐 **Tool access:** the config ships no MCP servers, which connect Claude to outside tools, and no list of pre-approved actions, so each engineer connects their own tools. `make install` adds deny rules that keep Claude's file tools out of `.env` files, though a shell command such as `cat` can still read one. Pushes aren't gated, since a prompt would stall unattended loops and the `protect_main` ruleset already requires a PR to change `main`. A PR that ships one gives it the least access it needs, per [`permission_recommendations.md`](../../src/claude/rules/on_demand/claude_config/permission_recommendations.md), as [DORA advises](reference_material/core/dora_ai_capabilities.md#-findings-worth-carrying-forward).

## 🔄 Workflow

- 🔄 **[Workflow](architecture/_workflow.md):** the AI-native development practices the design adopts, the order they're adopted in, and agent commits.

## 💰 Always-on budget

- 📏 **Measure:** the tokens, the units Claude reads text in, that load into every session, estimated as total characters ÷ 4, leaving out HTML comments, which Claude Code strips.
- 📂 **Counted:** the `CLAUDE.md` files and their `@` imports, rules with no `paths:` setting, and skill and agent descriptions, in both the project's `.claude/` and the global config in `src/claude/`.
- 🚫 **Not counted:** auto memory's `MEMORY.md`, which Claude Code also loads every session but keeps on each machine, outside the repo, and caps at 200 lines or 25KB.
- 🚧 **Ceiling:** set in the [principles' numbers](design_principles/01_principles.md#-numbers-and-tests), and raised only by a PR that links logged evidence.

## 🛡️ Design guards

These checks protect the design itself, alongside the repo's other [CI checks](../../.github/workflows/ci.yml):

| Guard | Fails when | How it runs |
|---|---|---|
| 💰 **Always-on budget** | The estimate exceeds the ceiling | [`claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh), as a pre-commit hook that CI also runs |
| 📏 **Rule size** | A rule runs over 110 lines, not counting comments or frontmatter | [`test_rules_structure.py`](../../tests/src/claude/test_rules_structure.py), in the pytest run that CI also runs |
| 📦 **PR size** | A PR changes more files than its limit allows, except on a `release/` branch | Runs [`git_validate_num_file_changes.sh`](../../src/sh/git/git_validate_num_file_changes.sh) |

- 📄 **Context size:** the Rule size guard caps every rule at 110 lines, including on-demand and path-scoped rules, so a single read stays at about 2 pages, far below the 20-page standards document [DORA warns](reference_material/core/dora_ai_capabilities.md#-findings-worth-carrying-forward) is too much for a model. On-demand files need no limit of their own.

## 📏 Measures

Each [regular review](design_principles/01_principles.md#-numbers-and-tests) takes these from the session transcripts, git history and budget check since the last review:

| Measure | Definition | Unit |
|---|---|---|
| 💬 **Component feedback** | Parts that helped, got in the way or went unused | One line each |
| 💰 **Every-session tokens** | The estimate the budget check reports | Tokens |

- 🗑️ **Acting on feedback:** each review removes [components that don't pay](design_principles/01_principles.md) and runs the [halving test](design_principles/01_principles.md#-numbers-and-tests).

## 📖 Further reading

After this page, read these in order. The build progress and reference material are linked at the top.

1. [Design principles](design_principles.md): the principles every part follows, and the checks a new part must pass.
2. [Review of the old setup](../../maintenance/old_setup_review.md): what the earlier, larger set of instructions contained, what worked, and where it grew heavier than the evidence justified.

To add a rule, skill, hook or agent, go straight to the [evaluation criteria](design_principles/02_evaluation_criteria.md).
