<!-- version: 1.0.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🎯 AI-native SDLC course: Relevance to this playbook (proposed, not yet adopted)

For anyone shaping the target architecture: which plays fit a personal playbook, as a proposal.

- **Part of:** [Anthropic: The AI-native SDLC Playbook](../anthropic_ai_native_sdlc.md).
- **Evals:** repeatable test tasks that check an AI agent still behaves as expected after a change.
- **Managed settings:** Claude Code settings set by an organisation's admins, which users can't override.

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
