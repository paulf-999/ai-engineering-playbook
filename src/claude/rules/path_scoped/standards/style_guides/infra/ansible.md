---
paths:
  - "**/playbooks/**/*.yml"
  - "**/roles/**/*.yml"
---
# 📦 Ansible Style Guide & Standards

**Purpose:** how to write and structure Ansible projects. This team's names, folders, lint profile and hierarchy are in [`team_conventions/infra/ansible.md`](../../../team_conventions/infra/ansible.md), which loads with this guide.

## 🏷️ Naming conventions

| Construct | Convention | Example |
|-----------|------------|---------|
| Variables in roles | `[role]_[variable_name]` | `webserver_port` |
| Tags | `snake_case` | `install`, `configure`, `restart` |

Use FQCN for all modules: `ansible.builtin.apt`, not `apt`.

---

## 🔩 Linting

- All playbooks and roles must pass `ansible-lint` before committing, at the team's profile.
- Fix the underlying issue rather than suppressing warnings.

## 📚 Read on demand

- `on_demand/standards/style_guides/infra/ansible/_roles_and_tasks.md`, in your Claude config directory, when creating a role or writing its tasks.
- `on_demand/standards/style_guides/infra/ansible/_plays_and_variables.md`, when writing a play, or adding role defaults or `host_vars`.
