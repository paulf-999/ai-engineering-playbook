# 🔄 Workflow

**Purpose:** the AI-native development practices the design adopts, and the sign each one is working. It's part of the [target architecture](README.md).

The design adopts these practices from Anthropic's course on AI-native software development, as its [relevance section](reference_material/core/anthropic_ai_native_sdlc.md#-relevance-to-this-playbook) sets out. Each regular review looks for a sign that each one is working in session records and git history, keeping no numbers:

| Practice | In this design | Sign it's working | Source |
|---|---|---|---|
| 🗺️ **Plan first** | Plan mode, with each approved plan saved to its own folder in `_plans/active/` in the Claude config directory, outside any repo | Few PRs need a follow-up fix PR | [Plan mode as the default](reference_material/core/anthropic_ai_native_sdlc.md#-plays-by-stage) |
| 📝 **Intent and spec** | Each plan opens with Intent and Spec sections, which become the change's `intent.md` and `spec.md` once the plan is approved, and the spec is pasted into the PR so the reviewer can check the diff against it | Plans rarely change scope after approval | [Capture as intent.md, and Requirements and design](reference_material/core/anthropic_ai_native_sdlc.md#-plays-by-stage) |
| 🔁 **Feedback loop** | `make test` and `pre-commit run --all-files`, which define done in [`CLAUDE.md`](../../CLAUDE.md), and a [Stop hook](../../src/claude/hooks/hook_enforcement_done_checks.sh) that sends Claude back once to run them after files change | Most PRs pass CI on the first push | [Give Claude a feedback loop](reference_material/core/anthropic_ai_native_sdlc.md#-plays-by-stage) |
| 👀 **PR review loop** | A separate Claude reviewer, which sees only the change, fills the evaluation criteria for each PR that changes what loads every session or enforces behaviour, in place of a `REVIEW.md`, and a CI check confirms they and the PR's Plan Spec are answered | Red flags are caught before merge | [AI in the PR review loop](reference_material/core/anthropic_ai_native_sdlc.md#-plays-by-stage) |
| 🧪 **Evals** | Deferred until their API cost and upkeep are weighed | None while deferred | [Continuous evals in CI](reference_material/core/anthropic_ai_native_sdlc.md#-plays-by-stage) |
| 🚀 **CI/CD metrics** | Out of scope, since the repo has no deployed service | None while out of scope | [CI/CD integration, and Closing the loop on metrics](reference_material/core/anthropic_ai_native_sdlc.md#-plays-by-stage) |

- 🧭 **Adoption order:** a practice is taken up only once its prerequisites in the [course's graph](reference_material/core/anthropic_ai_native_sdlc.md#-overview) are in place. Evals come next, since their prerequisites, `CLAUDE.md` and the feedback loop, are in place. The PR review loop runs ahead of evals, its own prerequisite, since it checks a PR against the evaluation criteria rather than reviewing the code.
- ✍️ **Agent commits:** Claude commits as [`git.md`](../../src/claude/rules/on_demand/workflows/git.md) sets out: once a task is done and its checks pass, one commit per task, as [DORA advises deciding](reference_material/core/dora_ai_capabilities.md#-findings-worth-carrying-forward), and a pre-commit hook blocks commits to `main`. Its sign of working is that each commit in git history holds one finished task.
