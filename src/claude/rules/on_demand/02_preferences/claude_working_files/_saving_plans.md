# 📤 Saving plans

**Purpose:** where to keep a plan, with its `intent.md` and `spec.md`, once the user approves it, so approved plans aren't lost in plan mode's scratch folder.

- 🔗 **Spec link:** open the plan's Spec section with a **spec.md** bullet linking the absolute path it will be saved to, marked "(saved on approval)".
- 📂 **Change folder:** before starting work, make `.claude_work/_plans/active/YYYY_MM_DD_<topic>/` in your home folder, outside every repo, so a plan is never committed.
- ✂️ **Split it:** write the plan's Intent section to `intent.md`, its Spec section to `spec.md`, and the rest to `plan.md`, which links to both, waiting until approval since plan mode lets Claude write only its own plan file.
- 🏷️ **Status line:** put `**Plan status:** 🟢 Active · updated <date>` under the H1 of `plan.md`, and update the date whenever a phase moves on.
- 📍 **Absolute paths:** write the full path, such as `/Users/<you>/.claude_work/_plans/...`, since the Write tool would turn a `~` into a folder literally named `~`.
- 🗑️ **Scratch copy:** treat plan mode's own file as disposable once split, and don't refer to it again.

## 📞 Called by

This rule is invoked by [`rules/always_on/02_preferences/claude_working_files.md`](../../../always_on/02_preferences/claude_working_files.md), when writing a plan.
