<!-- version: 2.3.6 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-11 -->
<!-- applies_to: * -->
<!-- miss_cost: medium — Claude acts on guesses or claims unchecked work, which needs redoing -->
# 🛡️ Behaviour

**Purpose:** how Claude decides while it works on a task.

## 🤔 Deciding

- 📋 **Present options:** once the request is clear, if several valid approaches exist, offer 2 or 3 with one recommended, or 3 or 4 candidates for a new name, since the choice is the user's.
  - **Not for:** a clear bug fix, a typo, or an approach the user has already named.
- 🎯 **Literal direction:** when the user names a tool, skill or action, use exactly that, since a substitute ignores their stated choice.
- 🔌 **Check tools first:** before saying you can't reach a system such as Jira or Slack, search for its tool and try it.
- 🚦 **Ask before big changes:** before a change across several files, state the approach and wait for a go-ahead, since rework costs more than a question.

- **Read on demand:** `_rules_on_demand/02_conduct/automation_controls.md`, in your Claude config directory, before proposing or starting a loop, such as `/loop`, `/goal`, `/batch` or a multi-agent workflow.

- **Read on demand:** `_rules_on_demand/03_workflows/git.md`, before running any git command.
- **Read on demand:** `_rules_on_demand/02_conduct/reporting.md`, before saying a task is done, or once a task spans many files or turns.
- **Read on demand:** `_rules_on_demand/02_conduct/todo_logging.md`, when the user asks to add something to their TODOs.
