# 🎨 style_guides

**Purpose:** style guide detail Claude reads only when a guide's "Read on demand" pointer sends it there, with each topic's standards and team conventions side by side.

- 🧰 **Standards:** a plain name, such as `jira.md` or the `dbt/` children of `path_scoped/style_guides/dbt.md`.
- 🏢 **Team conventions:** a `_team_conventions` file in the same topic folder, such as `jira/jira_team_conventions.md` or `dbt/_layout_team_conventions.md`.

| File or folder | What it covers |
|---|---|
| 🌬️ [`airflow/`](airflow/) | Airflow tasks, operators and practices; this team's DAG design and configuration |
| 🔷 [`azure_devops/`](azure_devops/) | Azure Pipelines security hardening; this team's Python jobs |
| 🔵 [`dbt/`](dbt/) | dbt model organisation, names, YAML and snapshots; this team's layout, macros and keys |
| 🚀 [`github_actions/`](github_actions/) | GitHub Actions security hardening; this team's Python jobs |
| 🏗️ [`infra/`](infra/) | Ansible, Docker and Terraform detail, with this team's Ansible and Terraform choices |
| 🎫 [`jira.md`](jira.md), [`jira/`](jira/) | Jira ticket writing; this team's ticket structure, fields, sprints and scoring |
| 🐍 [`python/`](python/) | Python testing, logging, complexity and modules; this team's environment and test setup |
| 🗄️ [`sql/`](sql/) | SQL formatting, CTEs and Snowflake standards; this team's warehouse and SQLFluff settings, in `snowflake.md` |
| 🧰 [`utilities/`](utilities/) | Datetime standards, with this team's date style and Mermaid styling |
