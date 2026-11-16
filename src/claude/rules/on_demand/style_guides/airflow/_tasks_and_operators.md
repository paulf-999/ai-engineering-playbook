# ⚙️ Tasks, Operators & Dependencies

**Purpose:** how to design tasks, choose operators and wire dependencies, so DAGs stay consistent and maintainable.

## 📋 dag.py

Keep `dag.py` to the DAG definition and task wiring, with configuration read from outside the file. This team's boilerplate and helpers are in [`team_conventions/airflow.md`](../../../path_scoped/team_conventions/airflow.md).

## 📋 Contents

- [🧩 Task design principles](#-task-design-principles)
- [🔧 Operator selection](#-operator-selection)
- [📂 DAG-specific helpers](#-dag-specific-helpers)
- [🔗 Task dependencies](#-task-dependencies)
- [📦 TaskGroups](#-taskgroups)
- [📤 XComs](#-xcoms)

---

## 🧩 Task design principles

- **One operation per task:** do not bundle unrelated steps into a single task
- **Independently re-runnable:** tasks must be safe to rerun without side effects from previous runs
- **Simplicity:** keep task functions small and single-purpose — extract complex logic into the team's shared modules
- **Descriptive IDs:** task IDs must be unique and describe the action performed, with the team's prefixes

---

## 🔧 Operator selection

Prefer purpose-built operators over generic ones. Common patterns:

| Use case | Preferred operator | Example |
|----------|-------------------|---------|
| Python logic | `PythonOperator` with a callable from the DAG's helpers | `task_transform()` |
| Snowflake SQL | `SQLExecuteQueryOperator`, which replaces the deprecated `SnowflakeOperator` | `task_load()` |
| dbt runs and Airbyte syncs | The team's shared helpers | `task_dbt_run()` |
| Trigger child DAG | `TriggerDagRunOperator` | `task_trigger_child()` |
| Wait for condition | A sensor, such as `ExternalTaskSensor`, with `mode="reschedule"` | avoid holding worker slots |
| Branching | `BranchPythonOperator` | conditional task routing |

---

## 📂 DAG-specific helpers

Keep Python callables and SQL queries out of `dag.py`, in the DAG's own helper files, as the team's conventions name them.

---

## 🔗 Task dependencies

- **Use `>>`:** always use the `>>` operator to define dependencies
- **Never use:** `set_upstream()` or `set_downstream()`
- **Group at bottom:** define all dependencies together at the bottom of the DAG block, kept separate from task definitions

---

## 📦 TaskGroups

Use `TaskGroup` to visually group related tasks in the Airflow UI, and reuse the team's TaskGroup generators for common patterns.

---

## 📤 XComs

- **Use sparingly:** XComs are not designed for large data transfers — pass only small values (IDs, counts, status flags)
- **Avoid large data:** do not pass DataFrames or large result sets between tasks
- **Use storage:** write intermediate data to storage (S3, Snowflake stage) and pass only the reference
