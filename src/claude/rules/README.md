# 📏 Rules

**Purpose:** what each folder of rules holds, and when its rules load.

## ⚙️ How a rule loads

[Claude Code](https://code.claude.com/docs/en/memory) loads a rule's `.md` file in one of three ways:

- 🔁 **[Always on](always_on/):** every `.md` file under `~/.claude/rules/` loads at the start of each session, so it costs context every time.
- 📂 **[Path scoped](path_scoped/):** a rule in `rules/` whose frontmatter has a `paths:` list loads only when Claude reads or edits a matching file.
- 💤 **[On demand](on_demand/):** a file outside `rules/` never loads by itself; Claude reads it when a rule's "Read on demand" pointer or a hook sends it there, which is why `on_demand/` installs beside `rules/`, not inside it.

## 📁 Folders

| Folder | Purpose |
|---|---|
| 🔁 [`always_on/`](always_on/) | Rules Claude loads in every session |
| 📂 [`path_scoped/`](path_scoped/) | Rules that load when Claude works on a file matching the rule's `paths:` list |
| 💤 [`on_demand/`](on_demand/) | Detail Claude reads only when a rule's "Read on demand" pointer or a hook sends it there |

## 🧪 Evals

[`evals.yaml`](evals.yaml) holds A/B cases that check each rule earns its place: `make evals RULES=1` runs every prompt with and without its rule, and reports whether the rule helps.
