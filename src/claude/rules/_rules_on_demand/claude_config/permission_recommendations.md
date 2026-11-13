<!-- version: 1.1.0 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-13 -->
<!-- applies_to: **/settings.json, **/settings.local.json -->
<!-- miss_cost: high — a broad allowlist lets destructive commands run unasked -->
# 🔐 Permission recommendations

**Purpose:** how to recommend Claude Code permissions, such as a `settings.json` allowlist, with the least access needed.

- ✅ **Auto-allow read-only commands:** commands that only read, such as `git status`, `git diff` and `grep`, are safe to allow.
- 🚫 **Gate writes:** keep commands that change state, such as `rm` or `git reset --hard`, behind a prompt, but not `git push` to a branch that server-side rules already protect, since a prompt there stalls unattended loops.
- 🎯 **No wildcards for destructive tools:** list specific safe subcommands, such as `Bash(git log:*)`, rather than `Bash(git:*)`.
- 📝 **Say why:** explain what each recommended permission unblocks and why it's safe.
