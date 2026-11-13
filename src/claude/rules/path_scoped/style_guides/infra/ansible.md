---
paths:
  - "**/playbooks/**/*.yml"
  - "**/roles/**/*.yml"
---
<!-- created: 2026-04-08 -->
<!-- applies_to: Ansible playbooks and roles -->
<!-- miss_cost: medium — playbooks drift from the team's structure and need reworking -->
# 📦 Ansible Style Guide & Standards

**Purpose:** Define the team's standards for writing and structuring Ansible projects.

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

- All playbooks and roles must pass `ansible-lint` (production profile) before committing.
- It's enforced via a pre-commit hook — fix the underlying issue rather than suppressing warnings.
- Ansible-lint skips: `role-name[path]`, which nested capability directories need, and no others.

## 📚 Read on demand

- `on_demand/style_guides/infra/ansible/_repo_structure.md`, in your Claude config directory, before adding a file or folder to the repo.
- `on_demand/style_guides/infra/ansible/_playbooks.md`, when adding a playbook or its folder, tags or play settings.
- `on_demand/style_guides/infra/ansible/_roles_and_tasks.md`, when creating a role or writing its tasks.
- `on_demand/style_guides/infra/ansible/_variables.md`, when adding variables to `group_vars`, `host_vars` or role defaults.
