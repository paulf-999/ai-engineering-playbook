---
paths:
  - "**/*.mmd"
---
# 🔀 Mermaid team conventions

**Purpose:** this team's own diagram choices. Another team can replace them with its own, while the standards stay in `style_guides/utilities/mermaid.md`.

## 🧭 Direction

Always use top-down layout:

```text
flowchart TD
```

## 📍 Placement

| Context | Location | How to reference |
|---|---|---|
| Skills | `flow.md` child page, co-located with `SKILL.md` | `See [\`flow.md\`](flow.md) for the full decision flow.` |
| Role READMEs | Inline under `## Install sequence` or equivalent heading | — |

- Do not embed diagrams directly in `SKILL.md` — a child page keeps `SKILL.md` short.

## 📚 Read on demand

- `on_demand/team_conventions/utilities/mermaid_styling.md`, in your Claude config directory, when choosing node shapes, node text or styling.
