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
- 🛠️ **Writing one:** follow the playbook repo's [authoring guide](https://github.com/paulf-999/ai-engineering-playbook/blob/main/docs/guides/authoring_guide.md), which also covers portable paths for hooks, scripts and tests.

## 📚 Read on demand

- [`on_demand/01_standards/claude_config/turn_budgets.md`](turn_budgets.md), in your Claude config directory, before testing a config change with `claude -p` or another unattended run.

## 📞 Called by

This rule is invoked by [`CLAUDE.md`](../../../../CLAUDE.md), before proposing or adding a rule, skill, hook, import, setting or memory note to Claude's config.
