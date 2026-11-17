# 🧭 Sorting a rule by kind

**Purpose:** how to decide whether a rule is a standard, a team convention or a preference, and where each kind lives, as part of the [authoring guide](../authoring_guide.md).

## 🗂️ The three kinds

Every rule sits in a load-time folder, then a kind folder: `rules/<always_on|path_scoped|on_demand>/<standards|team_conventions|preferences>/`.

| Kind | Test | Folder | Installs |
|---|---|---|---|
| 🧰 **Standard** | Good practice for anyone using the tool, whatever their team | `standards/` | Always |
| 🏢 **Team convention** | This company's own choice for its shared work: folder layouts, environment names, naming patterns, macros, helper modules, CI and vendor tools, lint skips, required fields, version pins or house writing style | `team_conventions/` | By default, since the repo starts the team from its shared conventions |
| 👤 **Preference** | Something the maintainer has ruled a preference: how Claude lays out its replies and docs, or where it keeps one user's own working files | `preferences/` | Only with `make install PREFERENCES=1` |

## ⚖️ Deciding

Ask these in order, and stop at the first yes:

1. 👤 **Is it on the preference list?** The reply format, bold-keyword bullets, the markdown layout rule, and where Claude saves plans, TODOs, drafts, error write-ups and session notes are preferences. A new preference needs the maintainer's ruling.
2. 🏢 **Does it name this company's files, tools, teams or roles?** Examples are `includes/common.py`, Azure Pipelines, the `data_management` owner or CODEOWNERS steps. If so, it's a team convention.
3. 🎨 **Is it a pick between equally valid styles?** It's a standard only when it matches the guide's reference below, and a team convention otherwise, including where the reference is silent.
4. 🔢 **Is it a number?** It's a team convention when the reference or the tool's own default sets a different one, such as 120-character lines where ruff defaults to 88. It's a standard when neither sets one, such as a 3-day lookback.
5. 🧰 **Otherwise,** it's a standard.

| Guide | Reference |
|---|---|
| dbt and SQL | dbt Labs' style guide |
| Python | PEP 8 and ruff's defaults |
| Bash | Google's shell style guide |
| Ansible | ansible-lint's defaults |
| Terraform | HashiCorp's style guide |
| Docker | Docker's best practices |
| Makefile | the GNU Make manual |
| Airflow | the Airflow docs |
| Datetime | ISO 8601 |
| Mermaid, Jira, writing style, naming and audiences | none, so every style pick is a team convention |

**Maintainer's rulings:** British spelling and `snake_case` names are team conventions, in `always_on/team_conventions/house_style.md`. Claude's skill and agent naming patterns are standards, since the Agent Skills spec sets them.

## ✂️ Splitting a guide by kind

When one guide holds both kinds, split it rather than mixing them:

- 📂 **Mirror the path:** a guide at `path_scoped/standards/style_guides/<path>.md` gets its team conventions at `path_scoped/team_conventions/<path>.md`, with the same `paths:` list, so both load on a matching file. `test_rules_structure.py` checks the globs match.
- 🔗 **Refer by role:** where a standard depends on a convention, the guide keeps the generic rule and names the convention by role, such as "the team's row-limiting macro", linking to the team file.
- 🧩 **Children:** bulky detail goes in `on_demand/team_conventions/<path>/_<aspect>.md` children. Children on either side of a split may be under the usual 40-line floor.
- 🚫 **No restating:** a convention lives in one team file only, so another team can replace the `team_conventions/` folders in a fork and keep the standards.
