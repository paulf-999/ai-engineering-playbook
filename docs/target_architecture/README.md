# 🏗️ Target architecture

**Purpose:** what the new set of Claude Code instructions contains, which parts Claude reads in every session and which only when needed, and how their cost and benefit are measured.

This page describes the design, and the [implementation status](implementation_status.md) says which parts are built so far.

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
| 🔒 **Required** | [`CLAUDE.md`](../../CLAUDE.md), the [global `CLAUDE.md` template](../../src/claude/CLAUDE.md) and the rules it loads in every session, the [plan-sections hook](../../src/claude/hooks/hook_enforcement_plan_sections.sh) that `make install` registers, `make test` and the CI checks, including the guards below | Every session, or every PR |
| 🧰 **Optional** | Skills, which are step-by-step procedures, agents, which work in a separate context, and on-demand rules | When the engineer or Claude asks for one |
| 📂 **Task-specific** | Path-scoped rules, whose `paths:` setting names the files they apply to | When a matching file is open |

- 🧭 **Choosing a tier:** the [evaluation criteria](design_principles/02_evaluation_criteria.md#-what-shape) match each need to a mechanism, which sets its tier.
- 🛑 **Hooks and every-session rules:** a hook, a script Claude Code runs automatically, that fires on every prompt, or a rule made to load in every session, raises a [red flag](design_principles/02_evaluation_criteria.md#-review-each-file), and the always-on budget still caps always-on rules.
- 🔐 **Tool access:** the config ships no MCP servers, which connect Claude to outside tools, and no list of pre-approved actions, so each engineer connects their own tools. `make install` adds deny rules that keep Claude's file tools out of `.env` files, though a shell command such as `cat` can still read one. Pushes aren't gated, since a prompt would stall unattended loops and the `protect_main` ruleset already requires a PR to change `main`. A PR that ships one gives it the least access it needs, per [`permission_recommendations.md`](../../src/claude/rules/on_demand/claude_config/permission_recommendations.md), as [DORA advises](reference_material/core/dora_ai_capabilities/03_findings.md).

## 🔄 Workflow

The design adopts these practices from Anthropic's course on AI-native software development, as its [relevance page](reference_material/core/anthropic_ai_native_sdlc/05_relevance.md) sets out. Each regular review looks for a sign that each one is working in session records and git history, keeping no numbers:

| Practice | In this design | Sign it's working | Source |
|---|---|---|---|
| 🗺️ **Plan first** | Plan mode, with each approved plan saved to its own folder in `_plans/active/` in the Claude config directory, outside any repo | Few PRs need a follow-up fix PR | [Plan mode as the default](reference_material/core/anthropic_ai_native_sdlc/02_plays_by_stage.md) |
| 📝 **Intent and spec** | Each plan opens with Intent and Spec sections, which become the change's `intent.md` and `spec.md` once the plan is approved, and the spec is pasted into the PR so the reviewer can check the diff against it | Plans rarely change scope after approval | [Capture as intent.md, and Requirements and design](reference_material/core/anthropic_ai_native_sdlc/02_plays_by_stage.md) |
| 🔁 **Feedback loop** | `make test` and `pre-commit run --all-files`, which define done in [`CLAUDE.md`](../../CLAUDE.md), and a [Stop hook](../../src/claude/hooks/hook_enforcement_done_checks.sh) that sends Claude back once to run them after files change | Most PRs pass CI on the first push | [Give Claude a feedback loop](reference_material/core/anthropic_ai_native_sdlc/02_plays_by_stage.md) |
| 👀 **PR review loop** | A separate Claude reviewer, which sees only the change, fills the evaluation criteria for each PR that changes what loads every session or enforces behaviour, in place of a `REVIEW.md`, and a CI check confirms they and the PR's Plan Spec are answered | Red flags are caught before merge | [AI in the PR review loop](reference_material/core/anthropic_ai_native_sdlc/02_plays_by_stage.md) |
| 🧪 **Evals** | Deferred until their API cost and upkeep are weighed | None while deferred | [Continuous evals in CI](reference_material/core/anthropic_ai_native_sdlc/02_plays_by_stage.md) |
| 🚀 **CI/CD metrics** | Out of scope, since the repo has no deployed service | None while out of scope | [CI/CD integration, and Closing the loop on metrics](reference_material/core/anthropic_ai_native_sdlc/02_plays_by_stage.md) |

- 🧭 **Adoption order:** a practice is taken up only once its prerequisites in the [course's graph](reference_material/core/anthropic_ai_native_sdlc/01_overview.md) are in place. Evals come next, since their prerequisites, `CLAUDE.md` and the feedback loop, are in place. The PR review loop runs ahead of evals, its own prerequisite, since it checks a PR against the evaluation criteria rather than reviewing the code.
- ✍️ **Agent commits:** Claude commits as [`git.md`](../../src/claude/rules/on_demand/workflows/git.md) sets out: once a task is done and its checks pass, one commit per task, as [DORA advises deciding](reference_material/core/dora_ai_capabilities/03_findings.md), and a pre-commit hook blocks commits to `main`. Its sign of working is that each commit in git history holds one finished task.

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

- 📄 **Context size:** the Rule size guard caps every rule at 110 lines, including on-demand and path-scoped rules, so a single read stays at about 2 pages, far below the 20-page standards document [DORA warns](reference_material/core/dora_ai_capabilities/03_findings.md) is too much for a model. On-demand files need no limit of their own.

## 📏 Measures

Each [regular review](design_principles/01_principles.md#-numbers-and-tests) takes these from the session transcripts, git history and budget check since the last review:

| Measure | Definition | Unit |
|---|---|---|
| 💬 **Component feedback** | Parts that helped, got in the way or went unused | One line each |
| 💰 **Every-session tokens** | The estimate the budget check reports | Tokens |

- 🗑️ **Acting on feedback:** each review removes [components that don't pay](design_principles/01_principles.md) and runs the [halving test](design_principles/01_principles.md#-numbers-and-tests).

## 📖 Other pages in this folder

After this page, read these in order. The implementation status and reference material are linked at the top.

1. [Design principles](design_principles.md): the principles every part follows, and the checks a new part must pass.
2. [Review of the old setup](legacy_architecture.md): what the earlier, larger set of instructions contained, what worked, and where it grew heavier than the evidence justified.

To add a rule, skill, hook or agent, go straight to the [evaluation criteria](design_principles/02_evaluation_criteria.md).
