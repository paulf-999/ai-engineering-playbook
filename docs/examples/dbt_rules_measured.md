# 📏 Measured: do the dbt rules change Claude's output?

**Purpose:** what 24 scripted runs showed about whether the dbt and SQL rules make Claude follow them, on 4 common dbt tasks.

> [!NOTE]
> Run on 2026-11-17 with Claude Opus 5.5. It measures whether Claude follows the written rules, not whether the result is better dbt, which needs people to judge. The infra guides aren't measured yet.

## 📊 Results

Each task ran 3 times without the rules and 3 times with them, in a fresh copy of the same small sample project. A script checked each output against the rules:

| Task | Without the rules | With the rules |
|---|---|---|
| 🧮 **Mart model:** "count each customer's orders" | 67% | 100% |
| 📥 **Staging model** for a raw `payments` source | 62% | 87% |
| 📸 **Snapshot** tracking changes to customers | 55% | 100% |
| 📝 **YAML** for an existing staging model | 100% | 100% |
| **All checks** | **71%** | **97%** |

Split by [kind of rule](../guides/authoring_guide/_rule_kinds.md):

| Checks | Without | With |
|---|---|---|
| 🧰 **Standards:** `ref()` or `source()`, CTEs ending in `final`, a YAML file, every column described, `unique` and `not_null` on the grain | 77% | 98% |
| 🏢 **Team conventions:** layer folder and prefix, singular names, uppercase keywords, leading commas, the snapshot strategy and schema | 56% | 94% |

## 🔍 What changed

- 📥 **Staging models came with YAML:** without the rules, none of the 3 staging runs wrote a properties file, and with them all 3 did.
- 🏷️ **Names and folders followed the team's layers:** with the rules, every mart, staging and snapshot file landed in its layer folder with its prefix.
- 📸 **Snapshots used the team's settings:** the `check` strategy and `WAREHOUSE` schema appeared in every run with the rules, and in none without.
- ❌ **Still missed:** the staging model was named in the plural, `staging_shop_payments`, in all 3 runs with the rules, though the SQL guide asks for singular names. One of those runs also skipped the `final` CTE.
- 🤔 **Asking first:** with the rules, Claude stopped to ask about the missing base layer before building, as the rules tell it to. The scripted runs told it to go ahead and note its assumptions, in both conditions.

## 🧪 How it was run

- 🗂️ **Sample project:** a `dbt_project.yml`, a sources file for `shop.orders`, `customers` and `payments`, and staging models for orders and customers.
- 🤖 **Each run:** a separate `claude -p --safe-mode` session, so nothing else loaded, with read and write tools only and the same prompt in both conditions.
- 📦 **With the rules:** the session's system prompt held what a default install loads when Claude works on a dbt model: `CLAUDE.md`, the always-on rules, and the dbt, SQL and testing guides with their team conventions. The on-demand files sat in a config folder for Claude to read when a rule pointed there. That matches an install closely, but isn't one, since the installer won't run inside Claude Code.
- ✅ **Scoring:** a script read each run's new files and checked them. It can tell whether a rule was followed, but not whether the model is correct.
- 💰 **Cost:** $4.64 for the 24 runs.
