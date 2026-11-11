---
paths:
  - "**/dags/**/*.py"
---
<!-- version: 1.6.2 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-11 -->
<!-- applies_to: Airflow DAG files -->
<!-- miss_cost: medium — DAGs fail or retry badly and need reworking -->
# 🌬️ Airflow Style Guide & Standards

**Purpose:** the four principles every DAG in `dmt_airflow_dags/` follows, so pipelines stay reliable and easy to debug.

## 🏗️ Core principles

- **Idempotency:** re-running a logical date gives identical results, so dedupe inputs and use `MERGE` or `CREATE OR REPLACE`, not `INSERT`.
- **Atomicity:** one task does one logical operation, so a failure can be retried alone; group related tasks in a TaskGroup.
- **Config-driven:** environment values such as warehouse size and Slack channels go in the DAG's `config.yaml`, never in DAG code.
- **Fail fast:** inherit `retries=3` and `retry_delay=timedelta(minutes=5)` from `default_args`, never set retries to `0` in production, and set `on_failure_callback`.

## 📚 Read on demand

- `_rules_on_demand/style_guides/airflow/_dag_design.md`, in your Claude config directory, when creating a DAG folder or naming a DAG.
- `_rules_on_demand/style_guides/airflow/_dag_configuration.md`, when editing a DAG's `config.yaml`, schedule or tags.
- `_rules_on_demand/style_guides/airflow/_tasks_and_operators.md`, when writing `dag.py`, choosing an operator or wiring tasks.
- `_rules_on_demand/style_guides/airflow/_best_practices.md`, before changing retries, callbacks, tests or Variables.
