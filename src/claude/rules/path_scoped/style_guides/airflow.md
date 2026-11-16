---
paths:
  - "**/dags/**/*.py"
---
# 🌬️ Airflow Style Guide & Standards

**Purpose:** the principles every DAG follows, so pipelines stay reliable and easy to debug. This team's layout, helpers, names and values are in [`team_conventions/airflow.md`](../team_conventions/airflow.md), which loads with this guide.

## 🏗️ Core principles

- **Idempotency:** re-running a logical date gives identical results, so dedupe inputs and use `MERGE` or `CREATE OR REPLACE`, not `INSERT`.
- **Atomicity:** one task does one logical operation, so a failure can be retried alone; group related tasks in a TaskGroup.
- **Config-driven:** environment values such as warehouse size and Slack channels go in the DAG's config, never in DAG code.
- **Fail fast:** inherit non-zero `retries` and a `retry_delay` from `default_args`, never set retries to `0` in production, and set `on_failure_callback`.
- **Names and schedules:** use descriptive `snake_case` names without unclear abbreviations or acronyms, and set `schedule` explicitly, never the deprecated `schedule_interval`.

## 📚 Read on demand

- `on_demand/style_guides/airflow/_tasks_and_operators.md`, in your Claude config directory, when writing `dag.py`, choosing an operator or wiring tasks.
- `on_demand/style_guides/airflow/_best_practices.md`, before changing retries, callbacks, tests or Variables.
