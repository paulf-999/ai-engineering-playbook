---
<!-- version: 1.4.0 -->
<!-- created: 2026-04-08 -->
<!-- updated: 2026-11-05 -->
paths:
  - "**/playbooks/**/*.yml"
  - "**/roles/**/*.yml"
---

# 📦 Ansible Style Guide & Standards

**Purpose:** Define the team's standards for writing and structuring Ansible projects.

## 🗂️ Repo structure

```text
group_vars/                         # variable files shared across all playbooks
  all.yml                           # global defaults and Vault lookups
  l1_<env>.yml                      # environment-wide variables
  l2_<env>_<site>.yml               # site-level within an environment
  ...                               # l3–l6 files as needed (see the variables page)
host_vars/                          # host-specific variable files
  <inventory_hostname>.yml
inventory/
  <scope>/                          # one subdirectory per inventory scope
    ansible.cfg                     # scope-specific configuration
    vars.yaml                       # scope metadata/variables
    <provider>_<account>_<plugin>.yml  # dynamic inventory plugin config
playbooks/
  <dept_or_app>/                    # one subdirectory per owner or application
    [<team>/]                       # optional team-level nesting
      <app>_<asset_role>_<descriptor>.yml
      group_vars -> ../../group_vars  # symlink, one more ../ under a team folder
      roles -> ../../roles            # symlink, one more ../ under a team folder
roles/
  <technical_capability>/           # functional grouping (e.g. application, systems)
    <role_name>/
      defaults/
        main.yml
      tasks/
        main.yml
      handlers/
      templates/
      files/
      meta/
filter_plugins/                     # custom Jinja2 filters
pipelines/                          # CI/CD pipeline definitions
```

- No `inputs/` directory — this repo does not use a config-driven YAML inputs pattern.
- No single root-level `ansible.cfg` — each inventory scope has its own.
- No static `.ini` inventory files — all inventories use dynamic plugins.

---

## 🏷️ Naming conventions

| Construct | Convention | Example |
|-----------|------------|---------|
| Playbook files | `[app]_[asset_role]_[descriptor].yml` | `acme_ilb_setup.yml` |
| Role directories | `roles/[capability]/[role_name]` | `roles/systems/azure_devops_agent` |
| Inventory scope dirs | `[org]-[env]-[qualifier]` | `acme-prd-cde`, `acme-stg-dct` |
| Dynamic plugin files | `[provider]_[account/site]_[plugin].yml` | `aws_28122221233_aws_ec2.yml` |
| Variables in roles | `[role]_[variable_name]` | `webserver_port` |
| Variables in vars files | `[app/dept]__[role]_[variable_name]_[descriptor]` | `acme__nginx_port_http` |
| Task names | Sentence case, descriptive | `Install nginx package` |
| Tags | `snake_case` | `install`, `configure`, `restart` |

Use FQCN for all modules: `ansible.builtin.apt`, not `apt`.

---

## 🔩 Linting

- All YAML files must pass `yamllint --strict` before committing.
- All playbooks and roles must pass `ansible-lint` (production profile) before committing.
- Both are enforced via pre-commit hooks — fix the underlying issue rather than suppressing warnings.
- Ansible-lint skips: `role-name[path]`, which nested capability directories need, and no others.

## 📚 Read on demand

- **Read on demand:** `_rules_on_demand/style_guides/infra/ansible/_playbooks.md`, in your Claude config directory, when adding a playbook or its folder, tags or play settings.
- **Read on demand:** `_rules_on_demand/style_guides/infra/ansible/_roles_and_tasks.md`, when creating a role or writing its tasks.
- **Read on demand:** `_rules_on_demand/style_guides/infra/ansible/_variables.md`, when adding variables to `group_vars`, `host_vars` or role defaults.
