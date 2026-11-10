<!-- version: 1.0.2 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-10 -->
<!-- applies_to: **/settings.json, **/settings.local.json -->
<!-- miss_cost: high — a broad allowlist lets destructive commands run unasked -->
# 🔐 Permission recommendations

**Purpose:** how to recommend Claude Code permissions, such as a `settings.json` allowlist, with the least access needed.

- ✅ **Auto-allow read-only commands:** commands that only read, such as `git status`, `git diff` and `grep`, are safe to allow.
- 🚫 **Gate writes:** keep commands that change state, such as `git push`, `git commit` and `rm`, behind a prompt.
- 🎯 **No wildcards for destructive tools:** list specific safe subcommands, such as `Bash(git log:*)`, rather than `Bash(git:*)`.
- 📝 **Say why:** explain what each recommended permission unblocks and why it's safe.
