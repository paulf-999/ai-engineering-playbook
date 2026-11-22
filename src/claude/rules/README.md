# 📏 Rules

**Purpose:** what each folder of rules holds, and when its rules load.

## ⚙️ How a rule loads

[Claude Code](https://code.claude.com/docs/en/memory) loads a rule's `.md` file in one of three ways, one per folder:

| Folder | When it loads |
|---|---|
| 🔁 [`always_on/`](always_on/) | At each session start, since it has no `paths:` list, so it always costs context |
| 📂 [`path_scoped/`](path_scoped/) | Only when Claude reads or edits a file matching its frontmatter's `paths:` list |
| 💤 [`on_demand/`](on_demand/) | Never by itself: Claude reads it when a rule's "Read on demand" pointer or a hook sends it there, so it installs beside `rules/`, not inside it |

## 🧪 Evals

[`evals.yaml`](evals.yaml) holds A/B cases that check each rule earns its place: `make evals RULES=1` runs every prompt with and without its rule, and reports whether the rule helps.
