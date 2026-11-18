# 📝 Authoring rules

**Purpose:** how to place, write, wire up and check a new rule, as part of the [authoring guide](../authoring_guide.md).

- 🚪 **Pick the tier:** `always_on/` only for a rule every task needs while the always-on budget holds, `path_scoped/` with a `paths:` setting for a rule tied to one kind of file, and `on_demand/` for everything else, and whenever you're unsure.
- 🧭 **Pick the kind:** put the rule in the `01_standards/` or `03_preferences/` folder its kind needs, a team convention in a `_team_conventions` file beside the standard it extends, or a style guide in `style_guides/`, sorted as [rule kinds](_rule_classification.md) sets out, and point to a preference only from another preference.
- 👉 **Pointers:** reach an on-demand file with a bullet in a `## 📚 Read on demand` section at the end of the file, naming its path, in your Claude config directory, and when to read it, or name it in a hook's block message.
- 🆕 **New-file gap:** a path-scoped rule loads only once a matching file is open, so point to it on demand too, for the first file of its kind.
- 🧩 **Children:** name each child in its parent, and keep links to other files in those pointer lines rather than a Related section.
- 🧪 **Test the pointer:** run a lean session on a matching task, and check Claude reads the file before acting.
- 🛡️ **Before merging:** a rule backed by a hook, test or CI check gets a test in `tests/`, and an always-on rule needs the PR's [evaluation criteria](../../target_architecture/design_principles/02_evaluation_criteria.md) filled.
- 🔁 **Trial:** remove it at the next regular review if the session transcripts show it hasn't paid its way.
