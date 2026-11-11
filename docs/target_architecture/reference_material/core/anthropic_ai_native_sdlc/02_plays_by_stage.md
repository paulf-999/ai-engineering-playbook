<!-- version: 1.1.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-11 -->
# 🔄 AI-native SDLC course: Plays by stage

**Purpose:** each of the course's plays, grouped by stage, with its core practice and how to tell it's working.

This page is part of the [summary of Anthropic's SDLC course](../anthropic_ai_native_sdlc.md). Each play pairs an early signal that it's working with a later result to measure:

| Stage | Play | Core practice | Early signal | Later result |
|---|---|---|---|---|
| 📝 Plan | [Capture as intent.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/capture-intent) | Claude interviews the requester and drafts `intent.md`, which the product owner corrects | Time to a committed `intent.md` | Share of intent files accepted into design |
| 📐 Design | [Requirements and design](https://academy.claude.com/courses/ai-native-sdlc-playbook/requirements-and-design) | Claude drafts `spec.md` from the approved intent, and a person decides whether to proceed | Time from intent to spec | Spec edits after the first `plan.md` |
| 🗺️ Build | [Plan mode as the default](https://academy.claude.com/courses/ai-native-sdlc-playbook/plan-mode) | Refine the plan until a stranger could build from it, then commit it as `plan.md` | Changes merged from the first pass | Rework per change, and how often the merged diff still matches `plan.md` |
| 📘 Build | [The CLAUDE.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/claude-md) | Keep it under a page, and add a correction "when Claude makes a mistake twice" | How often a mistake repeats | Time to a new joiner's first merged PR |
| 🧠 Build | [Skills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge) | Write a skill for knowledge that must be applied consistently, and back must-hold policies with a hook or PR check | Time from a policy's approval to its skill update | PR findings that cite the policy |
| 🔀 Build | [Parallel sessions and subagents](https://academy.claude.com/courses/ai-native-sdlc-playbook/parallel-sessions-and-subagents) | One separate checkout per task, adding sessions "only while review is keeping up" | Sessions per engineer while review quality holds | Changes merged per engineer per week, read with the rework rate |
| 🔁 Test | [Give Claude a feedback loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/give-claude-a-feedback-loop) | One command that fails loudly, and a failing test before each bug fix | First-pass CI success for agent-written changes | Review time and change failure rate |
| 🧪 Test | [Continuous evals in CI](https://academy.claude.com/courses/ai-native-sdlc-playbook/continuous-evals-in-ci) | Rerun 20 to 50 real tasks, called evals, on a schedule and whenever `CLAUDE.md`, skills or hooks change | Eval pass rate, and time for an incident to become an eval | Regressions caught in CI rather than in production |
| 👀 Deploy | [AI in the PR review loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/ai-in-the-pr-review-loop) | Automated review applies a `REVIEW.md` checklist, but can't approve its own code | Time to first review | Defects caught before merge |
| 🚧 Deploy | [Hooks as approval gates](https://academy.claude.com/courses/ai-native-sdlc-playbook/hooks-as-approval-gates) | Each required approval becomes a hook that allows, asks or blocks an action | Time spent waiting at gates | Gate breaches reaching production |
| 🚀 Deploy | [CI/CD integration and deployment](https://academy.claude.com/courses/ai-native-sdlc-playbook/ci-cd-integration-and-deployment) | Run Claude unattended and sandboxed, starting with read-only steps and adding write steps behind the existing gates, while a person authorises each release | Pipeline failures triaged without paging a person | DORA measures |
| 📉 Maintain | [Closing the loop on metrics](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-the-loop-on-metrics) | Tested code flags unusual readings, then Claude diagnoses them and, for the largest, may open a PR | Time from a flagged reading to an `intent.md` in the triage queue | Repeat incidents, and findings that become merged fixes |
