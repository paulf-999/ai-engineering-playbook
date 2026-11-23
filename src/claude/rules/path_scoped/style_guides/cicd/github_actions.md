---
paths:
  - ".github/workflows/**/*.yml"
  - ".github/workflows/**/*.yaml"
---
# 🚀 GitHub Actions Style Guide & Standards

**Purpose:** the principles every GitHub Actions workflow follows, so CI stays secure, fast and easy to debug. This team's triggers, names, values and scripts are in [`github_actions_team_conventions.md`](github_actions_team_conventions.md), which loads with this guide.

## 🔐 Security

- **Pinned actions:** pin every `uses:` to a full 40-character commit SHA, with its release tag in a trailing comment, never a branch or a bare tag such as `@v4`.
- **Least privilege:** set a top-level `permissions:` block of `contents: read`, and grant any wider scope only on the job that needs it.
- **No injection:** never put `${{ }}` expressions of untrusted input, such as a PR title, branch name or body, inside `run:`, and pass them through `env:` as quoted `"${VAR}"`.
- **Secrets:** read secrets only from `secrets.*` or `${{ github.token }}`, never echo them, and mask any value derived from one with `::add-mask::`.
- **Untrusted code:** never check out or run a PR's code in a `pull_request_target` or `workflow_run` workflow that has secrets or write access.

## ⏱️ Reliability

- **Timeouts:** set `timeout-minutes` on every job, since the default is 6 hours.
- **Concurrency:** give PR workflows a `concurrency:` group keyed on the PR number with `cancel-in-progress: true`, and never cancel a deploy in progress.
- **Narrow triggers:** limit `on:` with `branches:`, `paths:` or `types:` filters, so a workflow runs only when its inputs change.
- **Pinned tools:** pin the language and tool versions a job installs, and key any cache on the hash of the lockfile or config it depends on.

## 🧾 Readability

- **Names:** give every workflow, job and `run:` step a `name:` that says what it checks or does.
- **Scripts:** move a `run:` block longer than about 5 lines into a script file in the repo, so it can be linted and tested.
- **Comments:** explain each non-obvious trigger, skip or permission in a comment above it.

## 📚 Read on demand

[`on_demand/style_guides/cicd/github_actions/_security_hardening.md`](../../../on_demand/style_guides/cicd/github_actions/_security_hardening.md), in your Claude config directory, before adding a secret, a deploy job, a `pull_request_target` trigger or a third-party action.
