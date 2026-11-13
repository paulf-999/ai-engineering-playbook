<!-- version: 1.1.1 -->
<!-- created: 2026-09-17 -->
<!-- updated: 2026-11-11 -->
<!-- applies_to: * -->
<!-- miss_cost: medium — an approved plan is lost in the scratch folder -->
# 📤 Saving plans

**Purpose:** where to keep a plan, with its `intent.md` and `spec.md`, once the user approves it, so approved plans aren't lost in plan mode's scratch folder.

- 📂 **Change folder:** before starting work, make `_plans/active/YYYY_MM_DD_<topic>/` in your Claude config directory.
- ✂️ **Split it:** write the plan's Intent section to `intent.md`, its Spec section to `spec.md`, and the rest to `plan.md`, which links to both, waiting until approval since plan mode lets Claude write only its own plan file.
- 🏷️ **Status line:** put `**Plan status:** 🟢 Active · updated <date>` under the H1 of `plan.md`, and update the date whenever a phase moves on.
- 📍 **Absolute paths:** write the full path, such as `/Users/<you>/.claude/_plans/...`, since the Write tool would turn a `~` into a folder literally named `~`.
- 🗑️ **Scratch copy:** treat plan mode's own file as disposable once split, and don't refer to it again.
