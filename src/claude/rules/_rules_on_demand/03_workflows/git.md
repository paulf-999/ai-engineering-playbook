<!-- version: 2.0.4 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-11 -->
<!-- applies_to: * -->
<!-- miss_cost: medium — a commit picks up another session's files or runs in the wrong repo -->
# 🌿 Git

**Purpose:** how Claude uses git safely, in any repo, alongside each repo's own conventions.

## 📝 Commits

- 🎯 **Logical boundary:** when asked to commit, commit once a task is done and its checks pass, not after every edit, since follow-ups mean the work is still in flight, and push only when asked.
- 📜 **Repo conventions:** follow each repo's `CONTRIBUTING.md` and CI for branch names, commit messages and PRs, rather than a global copy.
- 🧩 **Flag complex operations:** say so before a stash, reset or cross-branch reconcile, and offer the simplest option, such as redoing a small edit.

## 🔀 Shared working trees

- 🔍 **Unfamiliar changes:** if `git status` shows files you didn't touch, stop and ask whose they are, since another session may be working in the same tree.
- 🧹 **Clean index:** run a plain `git reset`, which only unstages, before staging each separate commit, so another commit's files can't slip in.
- 🌳 **Worktrees:** suggest `git worktree` when another session or sub-agent will work on the same repo.

## 🔒 Safe patterns

- 📍 **Use `git -C`:** write `git -C <repo> <command>` rather than `cd`, so later commands run in the right folder.
- ⚠️ **Untrusted repos:** a repo's own config can run code even on `git status`, and its hooks run on commits, so ask before running git in one you didn't create or clone.
