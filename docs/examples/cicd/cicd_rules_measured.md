# 📏 Measured: do the GitHub Actions rules change Claude's output?

**Purpose:** what 24 scripted runs showed about whether the GitHub Actions rules make Claude follow them, on 4 common workflow tasks in a sparse sample project.

> [!NOTE]
> Run on 2026-11-20 with Claude Opus 5.5. It measures whether Claude follows the written rules, using checks the rules' author wrote, not whether the result is a better workflow, which needs people to judge. It's 3 runs per task, on one model, so treat the figures as a signal, not a precise rate.

## 📊 Results

Each task ran 3 times without the rules and 3 times with them, in a fresh copy of a sparse sample: a small Python package with a `requirements.txt`, a `.pre-commit-config.yaml` and one plain `tests.yml` workflow, so the conventions come only from the rules. A script checked each output against the rules.

| Task | Without | With |
|---|---|---|
| 🪝 **Lint:** run the pre-commit hooks on every PR to `main` | 32% | 100% |
| 🔍 **Audit:** check `requirements.txt` with `pip-audit` | 27% | 100% |
| 🏷️ **PR title:** check it follows Conventional Commits | 20% | 100% |
| ✏️ **Edit:** post the pytest summary as a PR comment from `tests.yml` | 40% | 80% |
| **All checks**, the mean of the 4 task figures | **30%** | **95%** |

Split by [kind of rule](../../guides/authoring_guide/_rule_classification.md):

| Checks | Without | With |
|---|---|---|
| 🧰 **Standards:** SHA-pinned actions, read-only top-level `permissions:`, no untrusted input in `run:`, job timeouts, PR concurrency, narrow triggers, pinned installs, named jobs and steps, short `run:` blocks | 51% | 97% |
| 🏢 **Team conventions:** `snake_case.yml` names, the `---` and header comment, the `main` trigger and concurrency group, `ubuntu-latest` with a 10-minute timeout, `'Area: what'` job names, `# vX.Y.Z` pin comments, 4-space indents, commented scopes, Python 3.13 with a pip cache, versions read from `requirements.txt` | 6% | 100% |

## 🔍 What changed

- 🔐 **Security basics came without the rules:** every new workflow set read-only `permissions:`, and every PR title run passed the title through `env:`, not `${{ }}` in the script.
- 📌 **Pins, timeouts and concurrency came only with the rules:** without them, every new workflow that used an action pinned a tag such as `@v4`, and none set `timeout-minutes` or a `concurrency:` group.
- 🐚 **Scripts moved out of YAML:** with the rules, every run put its check in a `src/sh/` script, while without them the PR title and edit runs wrote 10 to 23-line `run:` blocks.
- ❌ **Still missed:** in the edit, 2 of 3 runs with the rules granted `pull-requests: write` on the job but added no top-level `permissions:`, and none pinned the existing `@v4` actions.
- ⚠️ **A pin that doesn't exist:** 1 of 18 SHAs written with the rules was off by one digit, for `actions/cache` `v4.2.3`, so that workflow would fail to start. Every pin also named an older release than this repo's own.

## 🧪 How it was run

- 🗂️ **Sample project:** the sparse sample above, with one existing `tests.yml` that uses tag pins, no `permissions:` and no timeout.
- 🤖 **Each run:** a separate `claude -p --safe-mode` session, so nothing else loaded, with read and write tools only and the same prompt in both conditions, ending "Go ahead without asking me questions."
- 📦 **With the rules:** the session's system prompt held what a default install loads when Claude works on a file under `.github/workflows/`: `CLAUDE.md`, the always-on rules, and the GitHub Actions guide with its team conventions. The on-demand files sat in a config folder for Claude to read when a rule pointed there. That matches an install closely, but isn't one, since the installer won't run inside Claude Code.
- ✅ **Scoring:** a script parsed each run's new or changed workflow and checked it, scoring only the added lines in the edit. It can tell whether a rule was followed, but not whether the workflow runs, so the bad pin was found by checking each SHA against its tag by hand.
- 🔧 **Scorer fixes after the runs:** after reading the outputs, a comment above a `permissions:` block was made to count as commenting the scope, and the edit task gained a check that new `run:` blocks stay at 6 lines or fewer. The figures above use the fixed scorer.
- 💰 **Cost:** $4.22 for the 24 runs, $2.70 with the rules and $1.52 without, since runs with the rules also wrote a script.
