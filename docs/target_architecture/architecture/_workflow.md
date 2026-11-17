# 🔄 Workflow

**Purpose:** the AI-native development practices the design adopts. It's part of the [target architecture](../README.md).

The design adopts these practices from Anthropic's course on AI-native software development, as its [relevance section](../reference_material/core/anthropic_ai_native_sdlc.md#-relevance-to-this-playbook) sets out.

| Practice | In this design | Source |
|---|---|---|
| 🗺️ **Plan first** | Plan mode, with each approved plan saved to its own folder in `~/.claude_work/_plans/active/`, outside any repo, for users who opt into preferences | [Plan mode as the default](../reference_material/core/anthropic_ai_native_sdlc.md#-plays-by-stage) |
| 📝 **Intent and spec** | Each plan past the size [`ai_sdlc_workflow.md`](../../../src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) sets opens with Intent and Spec sections, which become the change's `intent.md` and `spec.md` once the plan is approved, saved only with the [saved-plans preference](../../../src/claude/README.md#-preferences). Any PR that changes `src/claude/` pastes its spec, or says why it has none, so the reviewer can check the diff against it | [Capture as intent.md, and Requirements and design](../reference_material/core/anthropic_ai_native_sdlc.md#-plays-by-stage) |
| 🔁 **Feedback loop** | `make test` and `pre-commit run --all-files`, which define done in [`CLAUDE.md`](../../../CLAUDE.md), and a [Stop hook](../../../src/claude/hooks/hook_enforcement_done_checks.sh) that sends Claude back once to run them after files change | [Give Claude a feedback loop](../reference_material/core/anthropic_ai_native_sdlc.md#-plays-by-stage) |
| 👀 **PR review loop** | A PR answers the [evaluation criteria](../design_principles/02_evaluation_criteria.md) when they say it must, in place of a `REVIEW.md`, and a CI check confirms that line and the PR's Plan Spec are present | [AI in the PR review loop](../reference_material/core/anthropic_ai_native_sdlc.md#-plays-by-stage) |

- 🧭 **Adoption order:** a practice is taken up only once its prerequisites in the [course's graph](../reference_material/core/anthropic_ai_native_sdlc.md#-overview) are in place. Evals come next, since their prerequisites, `CLAUDE.md` and the feedback loop, are in place, and [#234](https://github.com/paulf-999/ai-engineering-playbook/issues/234) tracks them. CI/CD metrics are out of scope, since the repo has no deployed service. The PR review loop runs ahead of evals, its own prerequisite, since it checks a PR against the evaluation criteria rather than reviewing the code.
- ✍️ **Agent commits:** Claude commits as [`git.md`](../../../src/claude/rules/on_demand/01_standards/workflows/git.md) sets out: once a task is done and its checks pass, one commit per task, as [DORA advises deciding](../reference_material/core/dora_ai_capabilities.md#-findings-worth-carrying-forward), and a pre-commit hook blocks commits to `main`.
