# 📤 Saved plans

**Purpose:** where to keep a plan, with its `intent.md` and `spec.md`, once the user approves it, so approved plans aren't lost in plan mode's scratch folder, and how to track it until it ends.

- 🔗 **Spec link:** open the plan's Spec section with a **spec.md** bullet linking the absolute path it will be saved to, marked "(saved on approval)".
- 📂 **Change folder:** before starting work, make `_plans/active/YYYY_MM_DD_<topic>/` in your Claude config directory (`$CLAUDE_CONFIG_DIR`, or `~/.claude` when unset), rather than in the repo you're working in.
- ✂️ **Split it:** write the plan's Intent section to `intent.md` in the [layout below](#-intent-layout), its Spec section to `spec.md` under the [line below](#-spec-layout), and the rest to `plan.md`, which links to both, waiting until approval since plan mode lets Claude write only its own plan file.
- 🏷️ **Status line:** put `**Plan status:** 🟢 Active · updated <date>` under the H1 of `plan.md`, and update the date whenever a phase moves on.
- 📍 **Absolute paths:** write the full path, such as `/Users/<you>/.claude/_plans/...`, since the Write tool would turn a `~` into a folder literally named `~`.
- 🗑️ **Scratch copy:** treat plan mode's own file as disposable once split, and don't refer to it again.

## 🎯 Intent layout

Write `intent.md` in this layout, with one to three lines per section and "none" for an empty one:

```markdown
# Intent: <topic>

**Started:** <UTC datetime> · **Saved:** <UTC datetime> · **Decision:** accepted · **Edits after spec:** 0

## Problem
## Proposed outcome
## Success
## Affected users and systems
## Constraints
## Open questions
```

- ✍️ **Recording:** fill in all four fields on saving, with **Started** as the time of the first conversation, or "unknown".
- ✅ **Accepted:** approving a plan accepts its intent.
- 🗑️ **Closed:** when the user abandons a plan before approving it, save its intent in `_plans/dropped/YYYY_MM_DD_<topic>/` with `**Decision:** closed`, once plan mode allows writes, beside a short `plan.md` with status `🗑️ Dropped`.
- 🔢 **Edits:** add 1 to **Edits after spec** for each change to `intent.md` after `spec.md` is first saved.
- ❓ **Open questions:** list only minor or deferred points, since material choices are settled first.

## 📐 Spec layout

Put this line under the H1 of `spec.md`, filling in all three fields on saving:

```markdown
**Saved:** <UTC datetime> · **Approved by:** <role> · **Edits after plan:** 0
```

- 👤 **Approved by:** give a role, such as maintainer, never a name.
- 🔢 **Edits:** add 1 to **Edits after plan** for each change to `spec.md` after `plan.md` is first saved.

## 📏 Measures

These measures show whether capturing intent and the spec helps, and come from the fields above:

| Measure | Type | How to work it out |
|---|---|---|
| ⏱️ Time to a saved intent | Leading, an early sign | **Saved** minus **Started**, expected to be hours rather than weeks |
| 🌱 Survival rate | Lagging, seen later | Accepted intents divided by accepted plus closed intents |
| ✏️ Edits after spec | Lagging, seen later | The **Edits after spec** count |
| 📐 Spec edits after the plan | Lagging, seen later | The **Edits after plan** count |

## 🏷️ Statuses

Each status has its own folder in `_plans/`:

| Status | Folder | Set it when |
|---|---|---|
| 🟢 Active | `active/` | The user approves the plan |
| ⏸️ Parked | `parked/` | The user says to pause it |
| ✅ Done | `done/` | The last step passes its check |
| 🗑️ Dropped | `dropped/` | The user says to abandon it |

- 📦 **Moving:** move the plan's whole folder to match in the same turn as the status change, without overwriting one of the same name.
- 🔗 **Links:** link a plan's saved files to each other relatively, such as `[spec.md](spec.md)`, so a move keeps the links working.

## 📞 Called by

This rule is invoked by [`rules/always_on/01_standards/ai_sdlc_workflow.md`](../../always_on/01_standards/ai_sdlc_workflow.md), when writing a plan, if installed.
