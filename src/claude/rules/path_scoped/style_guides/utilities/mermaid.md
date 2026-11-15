---
paths:
  - "**/*.mmd"
---
# 🔀 Mermaid Diagram Standards

**Purpose:** Keep Mermaid diagrams consistent and readable across skills and READMEs.

[Mermaid](https://mermaid.js.org) is a Markdown-native diagramming language for flowcharts, sequence diagrams, and more.

These standards apply to every Mermaid diagram: `.mmd` files load this guide automatically, and for a diagram embedded in a Markdown doc, read this guide before adding one.

## ⚡ Key rules

- ✅ **When:** add one only for a flow with at least two decision nodes or a conditional stop path, and never for a simple linear workflow.
- 📐 **Level:** keep it at phase or step level, such as `2: Validate inputs`, leaving implementation detail to the prose.
- 🧭 **Direction:** always top-down, with `flowchart TD`.
- 📍 **Placement:** for a skill, a `flow.md` page beside `SKILL.md`, never inside it.

## 📚 Read on demand

- `on_demand/style_guides/utilities/mermaid/_fundamentals.md`, in your Claude config directory, when deciding whether, where and at what level to add a diagram.
- `on_demand/style_guides/utilities/mermaid/_advanced.md`, when choosing node shapes, styling or subgraphs.
