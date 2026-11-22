# 🌿 Git

**Purpose:** how Claude uses git safely, in any repo, alongside each repo's own conventions.

## 📝 Commits

- 🎯 **Logical boundary:** commit once a task is done and its checks pass, not after every edit, since follow-ups mean the work is still in flight.
- 📜 **Repo conventions:** read each repo's `CONTRIBUTING.md` before creating a branch, and follow it and CI for branch names, commit messages and PRs, rather than a global copy.
- 🧩 **Flag complex operations:** say so before a stash, reset or cross-branch reconcile, and offer the simplest option, such as redoing a small edit.
- 🪜 **No stacked PRs:** branch each PR from `main`, never from another open PR's branch, since squash-merging the first leaves the second merging into a dead branch.

## 🔀 Shared working trees

- 🔍 **Unfamiliar changes:** if `git status` shows files you didn't touch, stop and ask whose they are, since another session may be working in the same tree.
- 🧹 **Clean index:** run a plain `git reset`, which only unstages, before staging each separate commit, so another commit's files can't slip in.
- 🌳 **Worktrees:** before your first edit or branch switch, move into your own `git worktree` if another session or sub-agent works in the same repo, so neither sees the other's changes.
  - **Signs:** the user mentions one, `ListAgents` shows another session in this repo, or commits or staged files appear that you didn't make.

## 🔒 Safe patterns

- 📍 **Use `git -C`:** write `git -C <repo> <command>` rather than `cd`, so later commands run in the right folder.
- ⚠️ **Untrusted repos:** a repo's own config can run code even on `git status`, and its hooks run on commits, so ask before running git in one you didn't create or clone.

## 📞 Called by

- [`hooks/hook_enforcement_worktree_edits.sh`](../../../hooks/hook_enforcement_worktree_edits.sh), when it blocks a session's first edit in a repo's main folder.
- [`rules/always_on/01_standards/behaviour.md`](../../always_on/01_standards/behaviour.md), before any git command.
