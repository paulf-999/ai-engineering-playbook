# 🔍 Phase 1: gather

**Purpose:** the read-only checks, and how the branch, files, commit message, PR title, body and labels are derived.

Run these silently to understand the current state:

1. `git status` — identify changed/untracked files and current branch
2. `git diff` — review unstaged changes
3. Read `.github/pull_request_template.md` from repo root. **This file is mandatory** — stop if not found and ask the user to create one.

If the working tree is clean, check `git log main..HEAD`:

- **No commits ahead:** stop, since there is nothing to ship.
- **Commits ahead on a `feature/` or `hotfix/` branch:** ship them, so the plan drops the checkout, add and commit steps and the commit message comes from those commits.

If `git status` shows unmerged paths (conflict markers from a merge or rebase), stop and tell the user to resolve them by hand, since merge conflicts are out of scope.

## Derivations

**Branch:** If already on `feature/` or `hotfix/` branch, use it. Otherwise, derive from `$ARGUMENTS` (text after `/git-create-pr`). Pattern: `^(feature|hotfix)/[a-z0-9_]+$`

**Files to stage:** All changed/untracked files unless context suggests otherwise.

- **Likely secrets:** leave out any file that looks like a secret (`.env`, `.env.*`, `*.pem`, `*.key`, `id_rsa*`, `credentials*`, `*.p12`), and list it under "Not staged" in the Phase 2 prompt.
- **Override:** stage such a file only if the user names it explicitly after seeing the warning.

**Commit message:** Conventional Commits format `type(scope): description`

- `type`: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`
- `scope`:
  - Single file → filename in backticks (`` `git.md` ``)
  - Multiple files in one skill → skill name in backticks (`` `git-create-pr` ``)
  - Area descriptor or omit entirely for cross-area changes
- Description: lowercase, imperative, no period

**PR title:** Derived separately from commit message

- Format: `type(scope): plain English description`
- Plain English for mixed audience (what changed, why it matters)
- No filenames, code refs, path separators, or backticks
- Lowercase after colon
- Max 70 characters
- Examples:
  - ✅ `chore(settings): remove personal configuration from version control`
  - ❌ `chore(settings.local.json): untrack .claude/settings.local.json` (contains filename)

**PR body:** Use Agent tool (`subagent_type: technical-writer`) to draft following template structure exactly:

- **Wait before the gate:** start the writer as the last Phase 1 step and wait for its result before showing the Phase 2 prompt, so the prompt shows the finished body and nothing waits between prompts.
- **Summary:** 1 punchy sentence max. 2 sentences only if critical context would be lost. No jargon, no code refs. State what + why.
- **Additional Details:** Omit if not needed, and otherwise give only what a reviewer must or should know, in the template's 5 bullets or fewer, never mixing prose and bullets.
- **Links:** give every file, issue or PR the body names a full GitHub URL, with file links on the branch until the push pins them to the head commit, because CI rejects relative links in some repos and they never work in a PR.
- **Brief the writer:** pass these limits to `technical-writer` with only the must-know facts, because it keeps whatever detail the brief gives it.
- **Checkboxes:** Tick only applicable one
- **Tickets:** link a known Jira ticket or team by its full URL, and leave it out when you don't know the URL.

**Labels:** Map using file paths, branch name, commit message:

- `src/claude/skills/` → `claude-skill`
- `src/claude/agents/` → `claude-agent`
- `src/claude/rules/` → `claude-rule`
- `src/claude/hooks/` → `claude-hook`
- `tests/` → `tests`
- `src/sh/`, `.github/workflows/`, `.pre-commit-config.yaml` → `CI/CD`
- `.github/ISSUE_TEMPLATE/`, `.github/pull_request_template.md`, `.github/CONTRIBUTING.md` → `governance`
- `requirements.txt`, `pyproject.toml`, `package.json` → `dependencies`
- `settings.json`, `.github/linters/` → `config`
- Branch `hotfix/` → `hotfix`
- Type `refactor` → `refactor`
- Scope/message contains `security` → `security`
- Breaking change (`!` or `BREAKING CHANGE:`) → `breaking-change`
- All `docs/` only → `documentation`

**Check labels exist:** run `gh label list --limit 200 --json name -q '.[].name'` and split the mapped labels in two:

- **Apply:** labels the repo already has go on the `gh pr create` command.
- **Missing:** labels the repo lacks are left off the command and listed in the plan instead.
- **Why:** `gh pr create --label` aborts the whole PR when any label is missing, so one absent label must never block the PR.
