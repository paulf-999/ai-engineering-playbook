# 🛡️ Security hardening

**Purpose:** the GitHub Actions practices that keep secrets, tokens and third-party code from being abused, following GitHub's security hardening guide. This team's triggers and pins are in [`github_actions_team_conventions.md`](../../../path_scoped/style_guides/github_actions_team_conventions.md).

## 📦 Third-party actions

- **Vet first:** prefer actions from GitHub or a verified creator, and read the source of any other before adding it.
- **SHA pins:** a tag can be moved to new code, so pin the commit SHA and let Dependabot's `github-actions` ecosystem raise updates.
- **Fewer actions:** use a one-line `run:` step instead of an action that only wraps a CLI already on the runner.

## 🔑 Tokens and credentials

- **`GITHUB_TOKEN` scopes:** grant each `write` scope, such as `contents: write` or `pull-requests: write`, only on the job that writes.
- **Checkout credentials:** set `persist-credentials: false` on `actions/checkout` when no later step pushes, so the token isn't left in `.git/config`.
- **OIDC over keys:** authenticate to a cloud with `id-token: write` and the provider's OIDC login action, not a long-lived access key in a secret.
- **Environments:** put deploy secrets in a GitHub environment with required reviewers, and reference it with `environment:` on the deploy job.

## 🚪 Untrusted triggers

- **`pull_request` for forks:** it runs a fork's code without secrets and with a read-only token, so use it for every check of PR code.
- **`pull_request_target` and `workflow_run`:** they run with secrets on the base branch, so use them only for labelling or commenting, and never check out `github.event.pull_request.head.sha`.
- **Untrusted contexts:** treat `github.head_ref` and any `github.event.*` field a user writes, such as titles, bodies, comments and commit messages, as untrusted input.

## 📝 Logs and artifacts

- **No secret output:** never `echo`, `set -x` or `env` dump a step that holds a secret, since masking misses transformed values.
- **Artifacts:** never upload a folder holding credentials, such as `.git/` or `~/.config/`, as an artifact.

## 📞 Called by

- [`rules/path_scoped/style_guides/github_actions.md`](../../../path_scoped/style_guides/github_actions.md), before adding a secret, a deploy job, a `pull_request_target` trigger or a third-party action.
