---
paths:
  - ".github/workflows/**/*.yml"
  - ".github/workflows/**/*.yaml"
---
# 🚀 GitHub Actions team conventions

**Purpose:** this team's workflow triggers, names, values and scripts. Another team can replace them with its own, while the standards stay in `github_actions.md`.

## 🧱 Basics

- 📁 **Files:** one `snake_case.yml` per trigger set, such as `ci.yml` or `pip_audit.yml`, opening with `---` and a comment saying what it checks and why.
- 🎯 **Triggers:** `pull_request` on `main`, plus `push` on `main` only where caches must be saved for new PRs.
- 🐢 **Slow checks:** a separate workflow with a `paths:` filter, a weekly `schedule:` and `workflow_dispatch`, so PR CI stays fast.
- 🔒 **Permissions:** top-level `contents: read`, with any extra scope, such as `pull-requests: read`, commented with why.
- 🔁 **Concurrency:** group `<workflow>-${{ github.event.pull_request.number || github.ref }}`, with `cancel-in-progress: true`.
- 🖥️ **Runners:** `runs-on: ubuntu-latest` and `timeout-minutes: 10` on every job.
- 🏷️ **Job names:** a `snake_case` job ID and a quoted `'<Area>: <what it checks>'` name, such as `'Lint: run the pre-commit hooks'`.
- 📌 **Action pins:** a SHA then a `# vX.Y.Z` comment, two spaces after it, which Dependabot's weekly `github-actions` updates keep current.

## 📋 Standard workflow boilerplate

Every workflow starts the same way, with 4-space indents that `yamlfmt` keeps:

```yaml
---
# What this workflow checks, and why it runs when it does
name: CI

on:
    pull_request:
        branches: [main]

permissions:
    contents: read

# Cancel an older run on the same PR when new commits are pushed
concurrency:
    group: ci-${{ github.event.pull_request.number || github.ref }}
    cancel-in-progress: true

jobs:
    lint:
        name: 'Lint: run the pre-commit hooks'
        runs-on: ubuntu-latest
        timeout-minutes: 10
        steps:
            - uses: actions/checkout@<sha>  # vX.Y.Z
```

## 🔧 Steps

- 🐚 **Checks as scripts:** each check is a script under `src/sh/`, called from `run:` with its inputs as quoted arguments.
- 📏 **One command per `run:`:** a `run:` step holds one command on one line, such as `pytest`, and any shell logic, meaning variables, pipes or several commands, goes in a script.
- 🛡️ **Env comment:** every `env:` that carries untrusted input has the comment "Passed through env, not ${{ }} in the script, so a crafted <input> can't inject shell".
- 🪝 **Local parity:** CI re-runs `pre-commit run --all-files --show-diff-on-failure`, so `--no-verify` can't skip a hook.
- 🤖 **Dependabot:** skip only the checks its fixed `dependabot/...` branch names can't pass, with an `if:` on `github.event.pull_request.user.login`.

## 📚 Read on demand

- [`on_demand/style_guides/github_actions/_python_jobs_team_conventions.md`](../../on_demand/style_guides/github_actions/_python_jobs_team_conventions.md), in your Claude config directory, when a job sets up Python, installs a tool or caches dependencies.
