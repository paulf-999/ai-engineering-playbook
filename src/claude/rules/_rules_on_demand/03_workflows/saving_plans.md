<!-- version: 1.0.2 -->
<!-- created: 2026-09-17 -->
<!-- updated: 2026-11-10 -->
<!-- applies_to: * -->
<!-- miss_cost: medium — an approved plan is lost in the scratch folder -->
<!-- loading: on demand — read once a plan is approved, as claude_plans.md's pointer says -->
# 📤 Saving plans

**Purpose:** where to keep a plan once the user approves it, so approved plans aren't lost in plan mode's scratch folder.

- 📂 **Copy it:** before starting work, copy the approved plan to `_plans/active/YYYY_MM_DD_<topic>.md` in your Claude config directory.
- 🏷️ **Status line:** put `**Plan status:** 🟢 Active · updated <date>` under its H1, and update the date whenever a phase moves on.
- 📍 **Absolute paths:** write the full path, such as `/Users/<you>/.claude/_plans/...`, since the Write tool would turn a `~` into a folder literally named `~`.
- 🗑️ **Scratch copy:** treat plan mode's own file as disposable once copied, and don't refer to it again.
