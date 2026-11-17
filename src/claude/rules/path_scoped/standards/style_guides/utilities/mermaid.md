---
paths:
  - "**/*.mmd"
---
# 🔀 Mermaid Diagram Standards

**Purpose:** when to add a Mermaid diagram and at what level, so diagrams stay readable. This team's direction, placement and styling are in [`team_conventions/utilities/mermaid.md`](../../../team_conventions/utilities/mermaid.md), which loads with this guide.

[Mermaid](https://mermaid.js.org) is a Markdown-native diagramming language for flowcharts, sequence diagrams, and more.

These standards apply to every Mermaid diagram: `.mmd` files load this guide automatically, and for a diagram embedded in a Markdown doc, read this guide and `rules/path_scoped/team_conventions/utilities/mermaid.md`, in your Claude config directory, before adding one.

## ⚡ Key rules

- ✅ **When:** add one only for a flow with at least two decision nodes or a conditional stop path, and never for a simple linear workflow.
- 📐 **Level:** keep it at phase or step level, such as `2: Validate inputs`, leaving implementation detail to the prose.
- 💬 **Comments:** put each `%%` comment on its own line, since Mermaid doesn't allow one after a statement.
- 🧩 **Subgraphs:** group a phase's steps in a subgraph only when it has 3 or more.

## 📐 Diagram level

Keep diagrams at **phase/step level**:

- A reader should grasp the shape of the flow from the diagram
- Implementation detail belongs in the corresponding prose — not in the diagram

| ❌ Too detailed | ✅ Right level |
|---|---|
| `Check if file exists with os.path.exists()` | `2: Validate inputs` |
| `POST /repos/{owner}/{repo}/pulls/{number}/reviews` | `4: Post review` |
