<!-- version: 1.1.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🧭 Anthropic: The AI-native SDLC Playbook

For anyone shaping the target architecture: what Anthropic's AI-native SDLC (software development lifecycle) course recommends, where its limits are, and which parts may fit a personal playbook.

- **Source:** [The AI-native SDLC playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook), Claude Academy (Anthropic), 14 lessons, about 1 hour of reading.
- **Version:** no date or version is published, so cite the lesson and the access date, 2026-11-02, when every lesson was read in full.
- **Labels:** "The course says" and "Caveats" report the source, while "Our reading" and "Relevance" are this playbook's interpretation.

## 📋 The course says: overview

- **Shape:** twelve "plays" across six stages (Plan, Design, Build, Test, Deploy, Maintain), each with prerequisites, steps, governance and a leading and a lagging indicator.
- **Thread:** each stage leaves a versioned artefact for the next, from `intent.md` to `spec.md` to `plan.md` to code, evals and review findings.
- **Accountability:** "Humans remain accountable for every decision that requires judgment" ([Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction)).
- **Where to start:** the plays with no prerequisites are capture intent, plan mode, `CLAUDE.md`, skills, a feedback loop and hooks as approval gates ([Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction)).
- **Non-linear:** plays are modular, so organisations can take the stages in a different order.

## 🔄 The course says: plays by stage

| Stage | Play | Core practice | Suggested indicators |
|---|---|---|---|
| Plan | [Capture as intent.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/capture-intent) | Claude interviews the requester and writes `intent.md` from a template, and the product owner corrects it before it's committed | Time to a committed `intent.md`; share accepted into Design |
| Design | [Requirements and design](https://academy.claude.com/courses/ai-native-sdlc-playbook/requirements-and-design) | Claude writes `spec.md` from the approved intent, constrained by policy skills, and a human decides whether to proceed | Intent-to-spec time; spec edits after the first `plan.md` |
| Build | [Plan mode as the default](https://academy.claude.com/courses/ai-native-sdlc-playbook/plan-mode) | Iterate in plan mode until someone who never saw the conversation could implement it, then commit it as `plan.md` and update it when work diverges | First-pass merges; rework cycles; merged diff matching `plan.md` |
| Build | [The CLAUDE.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/claude-md) | Keep it under one page of commands, conventions and repeated mistakes, and add a correction "when Claude makes a mistake twice" | Repeated mistakes; time to a new joiner's first merged PR |
| Build | [Skills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge) | Write one inconsistently enforced policy as an owned skill, and pair must-hold policies with a hook or PR check, because "a skill is a control, though an advisory one" | Policy-to-skill time; PR findings citing the policy |
| Build | [Parallel sessions and subagents](https://academy.claude.com/courses/ai-native-sdlc-playbook/parallel-sessions-and-subagents) | Run independent tasks in separate worktrees, start with two or three sessions, and "add sessions only while review is keeping up" | Sessions per engineer while review quality holds; rework rate |
| Test | [Give Claude a feedback loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/give-claude-a-feedback-loop) | One check command that fails loudly, listed in `CLAUDE.md` as part of done, with a failing test first for bugs: "fix the code, not the test" | First-pass CI success; review time; change failure rate |
| Test | [Continuous evals in CI](https://academy.claude.com/courses/ai-native-sdlc-playbook/continuous-evals-in-ci) | 20 to 50 real tasks as evals, rerun when the model, `CLAUDE.md`, skills or hooks change, plus one eval per production incident | Eval pass rate; incident-to-eval time |
| Deploy | [AI in the PR review loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/ai-in-the-pr-review-loop) | Automated review guided by a `REVIEW.md`, whose findings never approve or block, so the authoring agent "has no way to approve" its own code | Time to first review; defects caught before merge |
| Deploy | [Hooks as approval gates](https://academy.claude.com/courses/ai-native-sdlc-playbook/hooks-as-approval-gates) | Each required human approval becomes a hook that allows, asks or blocks, with non-negotiable ones in managed settings | Gate wait time; gate violations reaching production |
| Deploy | [CI/CD integration and deployment](https://academy.claude.com/courses/ai-native-sdlc-playbook/ci-cd-integration-and-deployment) | Non-interactive Claude for judgement steps in CI, read-only first, sandboxed, with autonomy tiered by environment and a rehearsed rollback | Failures triaged without paging; DORA delivery measures |
| Maintain | [Closing the loop on metrics](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-the-loop-on-metrics) | Deterministic, tested detection that flags readings two or three standard deviations (σ) from a rolling average, where Claude diagnoses at 2σ and may open a PR at 3σ, writing findings back as `intent.md` | Breach-to-triage time; repeat incidents |

## ⚠️ Caveats

- **Audience:** engineering, platform and security leads whose organisations already use Claude Code, with the closing lesson aimed at large, regulated enterprises.
- **Evidence:** no lesson cites measured outcomes, so the indicators are proposals and the one numeric claim, that capturing intent drops "from a multi-week elicitation and refinement cycle to hours" ([Capture as intent.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/capture-intent)), is an expectation.
- **Vendor source:** Anthropic publishes both the course and the tools it recommends, and calls it a consolidation of its Applied AI team's practice without saying how that was gathered.
- **Organisation features:** several plays assume features an organisation's admins run, such as managed settings (admin-set rules users can't override), the managed Code Review service, usage telemetry exported through OpenTelemetry, and Claude Tag (Claude in Slack, in beta).
- **Examples:** the worked example, an insurer's claims portal, is illustrative rather than prescriptive.

## 🔍 Our reading

- **Spine:** specify, plan, then verify against versioned artefacts, a sequence a personal playbook can follow without any organisation features.
- **Advisory versus enforced:** the course itself separates advisory controls (skills, `CLAUDE.md`) from enforced ones (hooks, required CI checks), the same split needed when reviewing this playbook's previous Claude configuration, the `claude_ai_playbook` repository.
- **Measurement:** every play names a leading and a lagging indicator, giving ready candidates for checking whether a change actually helped.

## 🎯 Relevance to this playbook (proposed, not yet adopted)

| Play | Proposed | Why |
|---|---|---|
| Capture intent, requirements and design | Adapt | A single intent-and-spec file per change suits one maintainer, who also plays the product owner |
| Plan mode and `plan.md` | Adopt | Plan mode is already used, so committing the plan is the gap |
| `CLAUDE.md` | Adopt | The one-page limit and "mistake twice" rule are both checkable |
| Skills | Adapt | Only for knowledge that must be applied consistently, paired with a hook or CI check |
| Parallel sessions and subagents | Adapt | Worktrees fit, but one reviewer caps how many sessions are useful |
| Feedback loop | Adopt | `make test` and pre-commit already give one command each |
| Continuous evals | Adapt | A small eval set is feasible, but API cost and upkeep need weighing first |
| PR review loop | Adapt | A `REVIEW.md` fits, though a solo maintainer can't separate author and approver |
| Hooks as approval gates | Adapt | Project hooks only, as a personal setup has no managed settings |
| CI/CD integration, closing the loop on metrics | Out of scope for now | Both need a deployed service, which this repo doesn't have |
