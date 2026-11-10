<!-- version: 2.4.5 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-10 -->
<!-- applies_to: src/claude/**, **/.claude/**, **/CLAUDE.md -->
<!-- miss_cost: medium — a config change lands without its cost being weighed -->
<!-- loading: on demand — read when CLAUDE.md's pointer for changing Claude's config sends Claude here -->
# 🧭 Guiding principles for Claude config

**Purpose:** decide whether a proposed rule, skill, hook, import, setting or memory note is worth its cost, and how to build it.

## ✅ Before proposing a config change

- 🎯 **Real problem:** name the recurring problem it solves, and check an engineer would have built it anyway, since "might be useful someday" isn't a reason.
- 💰 **Cost:** estimate the tokens it adds to every session, or each time a hook fires, plus the upkeep of any new dependency or pipeline.
- 💤 **Load on demand:** prefer a path-scoped rule, a skill or a read-on-demand file over anything always-on.
- 🧰 **Right mechanism:** use a hook, test or CI check for what must always hold, since prose only advises.
- 🔁 **No duplicates:** leave out anything a CI or pre-commit check already enforces.

## 🌱 How to build it

- 🪜 **Start small:** ship the minimal version first, and add guardrails only once it proves useful.
- ↩️ **Easy to remove:** keep each piece small and single-purpose, so one small PR can take it out.
- 💸 **Automation pays back:** automate only work done about 5 or more times a month.
- 🔗 **Live sources:** link to the source of truth rather than keeping lists that go stale.
- 📐 **Size:** keep a rule to about 110 lines and one concept, and split anything longer into a parent and child files.

## 📚 Read on demand

- **Read on demand:** `_rules_on_demand/claude_config/authoring_guidelines.md`, in your Claude config directory, once a new rule, skill or agent is worth adding.
- **Read on demand:** `_rules_on_demand/claude_config/portable_paths.md`, before writing a hook, script or test for the config.
- **Read on demand:** `_rules_on_demand/claude_config/turn_budgets.md`, before testing a config change with `claude -p` or another unattended run.
