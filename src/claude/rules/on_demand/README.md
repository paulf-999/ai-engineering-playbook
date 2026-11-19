# 💤 on_demand

**Purpose:** rules Claude reads only when another rule's "Read on demand" pointer or a hook sends it there, with style guide detail in one folder and other rules sorted by [kind of rule](../../README.md#-three-kinds-of-rule).

| Folder | What it holds |
|---|---|
| 🧰 [`01_standards/`](01_standards/) | Good practice for anyone using the tool, whatever their team, such as reporting on a task or using git safely |
| 👤 [`02_preferences/`](02_preferences/) | One person's taste in how Claude replies, lays out docs and keeps their own files, left out with `PREFERENCES=0` |
| 🎨 [`style_guides/`](style_guides/) | Style guide detail, with this team's conventions beside each topic's standards |
