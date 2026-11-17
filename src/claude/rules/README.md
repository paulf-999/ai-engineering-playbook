# 📏 rules

**Purpose:** what each folder of rules holds, and when its rules load.

| Folder | Purpose |
|---|---|
| 🔁 [`always_on/`](always_on/) | Rules Claude loads in every session |
| 📂 [`path_scoped/`](path_scoped/) | Rules that load when Claude works on a file matching the rule's `paths:` list |
| 💤 [`on_demand/`](on_demand/) | Detail Claude reads only when a rule's "Read on demand" pointer or a hook sends it there |
