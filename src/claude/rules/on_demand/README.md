# 💤 on_demand

**Purpose:** rules Claude reads only when another rule's "Read on demand" pointer or a hook sends it there, sorted into folders by [kind of rule](../../README.md#-three-kinds-of-rule).

| Folder | Kind of rule |
|---|---|
| 🧰 [`01_standards/`](01_standards/) | Good practice for anyone using the tool, whatever their team, such as quoting bash variables or using dbt's `ref()` |
| 🏢 [`02_team_conventions/`](02_team_conventions/) | This team's own choices for its shared work, such as its dbt layer prefixes, folder layouts or CI tools |
| 👤 [`03_preferences/`](03_preferences/) | One person's taste in how Claude replies, lays out docs and keeps their own files, installed only with `PREFERENCES=1` |
