<!-- created: 2026-09-18 -->
<!-- applies_to: **/*.sh, **/*.py -->
<!-- miss_cost: medium — a hook, script or test breaks on another machine, often silently -->
# 🌍 Portable paths

**Purpose:** how hooks, scripts and tests for Claude's config find files, so they work on any machine.

- 🚫 **No hard-coded paths:** never hard-code a home folder, username or `~/.claude` path, since the config directory varies between machines.
- 🐍 **Python:** read the config directory from `CLAUDE_CONFIG_DIR`, using `~/.claude` only as the fallback when it's unset.
- 🐚 **Shell:** resolve paths from the script's own location, using `"$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"`.
- 🛡️ **Guard clauses too:** compare against the resolved directory, never a substring such as `*".claude/"*`.
- 📅 **Why:** hard-coded paths pass on the machine that wrote them and fail silently elsewhere, as the old config's hooks and tests did.
