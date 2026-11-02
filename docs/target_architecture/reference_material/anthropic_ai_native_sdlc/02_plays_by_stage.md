<!-- version: 1.0.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🔄 AI-native SDLC course: Plays by stage

For anyone shaping the target architecture: the twelve plays by stage, with their core practice and suggested indicators.

- **Part of:** [Anthropic: The AI-native SDLC Playbook](../anthropic_ai_native_sdlc.md).
- 📈 **Leading and lagging indicators:** an early signal that a practice is working, and a later measure of its outcome.
- 🧪 **Evals:** repeatable test tasks that check an AI agent still behaves as expected after a change.
- 🔒 **Managed settings:** Claude Code settings set by an organisation's admins, which users can't override.
- 🚚 **DORA delivery measures:** DORA's software delivery metrics, such as lead time for changes and change failure rate.

| Stage | Play | Core practice | Suggested indicators |
|---|---|---|---|
| 📝 Plan | [Capture as intent.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/capture-intent) | • **Draft:** Claude interviews the requester and writes `intent.md` from a template.<br>• **Review:** the product owner corrects it before it's committed. | • **Leading:** time to a committed `intent.md`.<br>• **Lagging:** share of intent files the product owner accepts into Design. |
| 📐 Design | [Requirements and design](https://academy.claude.com/courses/ai-native-sdlc-playbook/requirements-and-design) | • **Draft:** Claude writes `spec.md` from the approved intent, constrained by policy skills.<br>• **Decide:** a human decides whether to proceed. | • **Leading:** time from the `intent.md` commit to the `spec.md` commit.<br>• **Lagging:** spec edits after the first `plan.md`. |
| 🗺️ Build | [Plan mode as the default](https://academy.claude.com/courses/ai-native-sdlc-playbook/plan-mode) | • **Iterate:** refine the plan until someone who never saw the conversation could implement it.<br>• **Commit:** save as `plan.md`, updating it as work diverges. | • **Leading:** share of changes that merge from the first implementation pass.<br>• **Lagging:** rework cycles and how often the merged diff matches `plan.md`. |
| 📘 Build | [The CLAUDE.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/claude-md) | • **Scope:** under one page of commands, conventions and repeated mistakes.<br>• **Update:** add a correction "when Claude makes a mistake twice". | • **Leading:** repeated mistakes.<br>• **Lagging:** time to a new joiner's first merged PR. |
| 🧠 Build | [Skills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge) | • **Start:** write one inconsistently enforced policy as an owned skill.<br>• **Enforce:** pair must-hold policies with a hook or PR check. | • **Leading:** time from a policy's approval to its skill update merging.<br>• **Lagging:** PR findings citing the policy. |
| 🔀 Build | [Parallel sessions and subagents](https://academy.claude.com/courses/ai-native-sdlc-playbook/parallel-sessions-and-subagents) | • **Isolate:** one worktree (repo checkout) per independent task.<br>• **Scale:** start with two or three, then "add sessions only while review is keeping up". | • **Leading:** sessions per engineer while review quality holds.<br>• **Lagging:** rework rate. |
| 🔁 Test | [Give Claude a feedback loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/give-claude-a-feedback-loop) | • **Check:** one command that fails loudly, listed in `CLAUDE.md` as done.<br>• **Bugs:** failing test first, then "fix the code, not the test". | • **Leading:** first-pass CI success.<br>• **Lagging:** review time and change failure rate. |
| 🧪 Test | [Continuous evals in CI](https://academy.claude.com/courses/ai-native-sdlc-playbook/continuous-evals-in-ci) | • **Suite:** 20 to 50 real tasks, rerun when the model, `CLAUDE.md`, skills or hooks change.<br>• **Incidents:** add one eval per production incident. | • **Leading:** eval pass rate.<br>• **Lagging:** time for a production incident to become a permanent eval. |
| 👀 Deploy | [AI in the PR review loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/ai-in-the-pr-review-loop) | • **Review:** automated review applies `REVIEW.md`.<br>• **Approval:** findings neither approve nor block, so the authoring agent "has no way to approve" its own code. | • **Leading:** time to first review.<br>• **Lagging:** defects caught before merge. |
| 🚧 Deploy | [Hooks as approval gates](https://academy.claude.com/courses/ai-native-sdlc-playbook/hooks-as-approval-gates) | • **Gate:** each required human approval becomes a hook that allows, asks or blocks.<br>• **Lock:** non-negotiable gates live in managed settings. | • **Leading:** gate wait time.<br>• **Lagging:** gate violations reaching production. |
| 🚀 Deploy | [CI/CD integration and deployment](https://academy.claude.com/courses/ai-native-sdlc-playbook/ci-cd-integration-and-deployment) | • **Start:** use non-interactive Claude for read-only judgement steps in CI, sandboxed.<br>• **Limit:** tier autonomy by environment, with a rehearsed rollback. | • **Leading:** failures triaged without paging.<br>• **Lagging:** DORA delivery measures. |
| 📉 Maintain | [Closing the loop on metrics](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-the-loop-on-metrics) | • **Detect:** deterministic, tested code flags unusual readings.<br>• **Respond:** Claude diagnoses, may open a PR, and writes findings back as `intent.md`. | • **Leading:** breach-to-triage time.<br>• **Lagging:** repeat incidents. |

## 🔍 Play details

- 🧠 **Skills:** pair must-hold policies with a hook or PR check, because "a skill is a control, though an advisory one" ([Skills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge)).
- 📉 **Metric thresholds:** the tested code flags readings two or three standard deviations (σ) from a rolling average ([Closing the loop on metrics](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-the-loop-on-metrics)).
  - **Response:** Claude diagnoses at 2σ and may open a PR at 3σ.
