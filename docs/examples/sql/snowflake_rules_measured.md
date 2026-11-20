# 📏 Measured: do the SQL and Snowflake rules change Claude's output?

**Purpose:** what 24 scripted runs showed about whether the SQL and Snowflake rules make Claude follow them, on 4 standalone SQL tasks outside dbt.

> [!NOTE]
> Run on 2026-11-20 with Claude Opus 5.5. It measures whether Claude follows the written rules, using checks the rules' author wrote, not whether the SQL is correct or cheaper to run, which needs a warehouse and people to judge. It's 3 runs per task, on one model and one sparse sample project, so treat the figures as a signal, not a precise rate. The SQLFluff settings and the query-profile check aren't measured, since no run lints or executes SQL. The [dbt](../dbt/dbt_rules_measured.md) and [Airflow](../airflow/airflow_rules_measured.md) rules are measured separately.

## 📊 Results

Each task ran 3 times without the rules and 3 times with them, in a fresh copy of a sparse sample project: a README and one existing report query in lowercase, with trailing commas, single-letter aliases, a bare `JOIN` and a subquery. A script checked each output against the rules:

| Task | Without the rules | With the rules |
|---|---|---|
| 🏭 **Warehouse:** create one for the standard dbt runs in prod | 80% | 100% |
| 📥 **Table:** land payment events in `RAW.SHOP` | 28% | 100% |
| 🧮 **Transform:** rebuild a customer revenue table in `ANALYTICS.FINANCE` | 46% | 100% |
| ✏️ **Refactor:** make the existing report query easier to read | 52% | 100% |
| **All checks**, the mean of the 4 task figures | **51%** | **100%** |

Split by [kind of rule](../../guides/authoring_guide/_rule_classification.md):

| Checks | Without | With |
|---|---|---|
| 🧰 **Standards:** `AUTO_SUSPEND` set, a small warehouse, `NUMBER`, `VARCHAR` and `TIMESTAMP_NTZ` types, no bare `id` column, CTEs not subqueries, a last CTE named `final`, no `SELECT *` from a table, named join types, no single-letter aliases | 67% | 100% |
| 🏢 **Team conventions:** `AUTO_SUSPEND = 60`, an S warehouse for prod dbt runs, uppercase keywords, leading commas, singular table names | 27% | 100% |

## 🔍 What changed

- 🔠 **Casing and commas came only with the rules:** every run without them wrote lowercase keywords, and every table, transform and refactor used trailing commas.
- 🏭 **Warehouse settings matched anyway:** all 3 runs without the rules already set `AUTO_SUSPEND = 60` and a `SMALL` size, so only the casing differed.
- 🕒 **Types followed the guide only with the rules:** without them, all 3 tables stored the event time as `TIMESTAMP_TZ`, and one used `TIMESTAMP_LTZ` for a load time.
- 🧱 **CTEs either way, but no `final`:** every run without the rules avoided subqueries, but none named its last CTE `final`, and all 3 transforms used single-letter aliases.
- 🏷️ **Singular names with the rules:** all 3 tables without them were named `payment_events`, and all 3 with them `payment_event`.

## 🧪 How it was run

- 🤖 **Each run:** a separate `claude -p --safe-mode` session, so nothing else loaded, with read and write tools only and the same prompt in both conditions, ending "Go ahead without asking me questions."
- 📦 **With the rules:** the session's system prompt held what a default install loads when Claude works on a `.sql` file outside a dbt `models/` folder: `CLAUDE.md`, the always-on rules, and the SQL, SQL team conventions and code security rules. The on-demand files, including the Snowflake guides, sat in a config folder for Claude to read when a rule pointed there. That matches an install closely, but isn't one, since the installer won't run inside Claude Code.
- ✅ **Scoring:** a script read each run's new or changed `.sql` files and checked them, after a self-test on hand-made good and bad outputs. It can tell whether a rule was followed, but not whether the SQL runs or the refactor kept its results.
- 💰 **Cost:** $3.95 for the 24 runs, with runs that had the rules costing more.
