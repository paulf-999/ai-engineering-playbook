# 🌿 Git Branching Strategy

**Purpose:** which branches to use in this repo, and how to name them.

Every branch starts from `main` and merges back into it through a PR, and a [pre-commit hook](../../src/sh/git/git_validate_branch_name.sh) checks each branch name.

## 🌱 Branch Types

| Branch | Use it for |
|---|---|
| 🏠 `main` | The long-lived branch that every other branch merges into |
| ✨ `feature/` | New features |
| 🚑 `hotfix/` | Urgent fixes |
| 📦 `release/` | One bulk change over the PR file limit, as [below](#-exceptions-for-large-changes--use-the-release-prefix) |

## 📦 Exceptions for Large Changes — Use the `release/` Prefix

CI fails a PR that changes more files than the limit below, because small PRs are quicker and safer to review. A `release/` branch is exempt, for changes that must land together:

- 🔖 **Prefix:** start the branch name with `release/`.
- 🔁 **Same change:** apply one kind of change in bulk, such as formatting or a consistent rename.
- 🔧 **Limit:** the 20-file default is set in [`git_validate_num_file_changes.sh`](../../src/sh/git/git_validate_num_file_changes.sh), and the `MAX_FILES_ALLOWED` environment variable overrides it.

```bash
git checkout -b release/reformat_all_sql_models
```

## 📝 Naming Rules

The part after the prefix follows these rules:

- 🔡 **Characters:** only lowercase letters, numbers and underscores.
- ❓ **Why:** such names are safe in shell commands, URLs and CI without quoting.
- 🧩 **Exact pattern:** the `VALID_GIT_BRANCH_NAME` variable in the hook script.
- 🤖 **Dependabot:** CI skips the check for Dependabot's PRs, because their `dependabot/...` names can't be changed.

## ✅ Examples

Each row shows a valid name and an invalid one that breaks a single rule:

| Valid | Invalid | Rule broken |
|---|---|---|
| 🔗 `feature/add_pr_template` | `feature/add-pr-template` | Hyphen |
| 🔠 `feature/add_pr_123` | `feature/Add_PR` | Uppercase |
| 🔲 `hotfix/fix_commitlint` | `hotfix/fix commitlint` | Space |
| 💲 `hotfix/fix_symbol` | `hotfix/fix$symbol` | Special character |
| 🏷️ `release/reformat_all_sql_models` | `bugfix/fix_typo` | Unknown prefix |
