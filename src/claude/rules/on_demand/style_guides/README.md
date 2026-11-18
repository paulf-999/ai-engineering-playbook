# 🎨 style_guides

**Purpose:** style guide detail Claude reads only when a guide's "Read on demand" pointer sends it there, with each topic's standards and team conventions side by side.

- 🧰 **Standards:** a plain name, such as `jira.md` or the `dbt/` children of `path_scoped/style_guides/dbt.md`.
- 🏢 **Team conventions:** the same name plus `_team_conventions`, such as `jira_team_conventions.md` or the `dbt_team_conventions/` children.

| File or folder | What it covers |
|---|---|
| 🌬️ [`airflow/`](airflow/), [`airflow_team_conventions/`](airflow_team_conventions/) | Airflow tasks, operators and practices; this team's DAG design and configuration |
| 🔵 [`dbt/`](dbt/), [`dbt_team_conventions/`](dbt_team_conventions/) | dbt model organisation, names, YAML and snapshots; this team's layout, macros and keys |
| 🏗️ [`infra/`](infra/) | Ansible, Docker and Terraform detail, with this team's Ansible and Terraform choices |
| 🎫 [`jira.md`](jira.md), [`jira_team_conventions.md`](jira_team_conventions.md) | Jira ticket writing; this team's ticket structure, fields, sprints and scoring |
| 🐍 [`python/`](python/), [`python_team_conventions/`](python_team_conventions/) | Python testing, logging, complexity and modules; this team's environment and test setup |
| 🗄️ [`sql/`](sql/), [`sql_snowflake_team_conventions.md`](sql_snowflake_team_conventions.md) | SQL formatting, CTEs and Snowflake standards; this team's warehouse and SQLFluff settings |
| 🧰 [`utilities/`](utilities/) | Datetime standards, with this team's date style and Mermaid styling |
