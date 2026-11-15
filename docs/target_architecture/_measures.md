# 📏 Measures

**Purpose:** what each regular review records, and how it acts on it. It's part of the [target architecture](README.md).

Each [regular review](design_principles/01_principles.md#-numbers-and-tests) takes these from the session transcripts, git history and budget check since the last review:

| Measure | Definition | Unit |
|---|---|---|
| 💬 **Component feedback** | Parts that helped, got in the way or went unused | One line each |
| 💰 **Every-session tokens** | The estimate the budget check reports | Tokens |

- 🗑️ **Acting on feedback:** each review removes [components that don't pay](design_principles/01_principles.md) and runs the [halving test](design_principles/01_principles.md#-numbers-and-tests).
