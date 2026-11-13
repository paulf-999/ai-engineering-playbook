<!-- created: 2026-11-10 -->
# 🗂️ Ansible: Repo structure

**Purpose:** where each kind of file goes in the team's Ansible repo.

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
