<!-- version: 2.1.1 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-07 -->
<!-- applies_to: * -->
<!-- miss_cost: low — TODO rows drift from the table layout -->
<!-- loading: on demand — read when behaviour.md's TODO pointer sends Claude here -->
# 📝 TODO logging

**Purpose:** what to do when the user says "add to TODOs" or similar.

- 📂 **Where:** add a row to the pending items table in `TODO.md` in your Claude config directory, unless the user names another place, and ask before creating the file if it doesn't exist.
- **Read on demand:** `_templates/TODO.md.template`, in your Claude config directory, when creating a missing `TODO.md`, for its table layout.
- 🔢 **Number:** give it the next number after the highest in the table.
- 🧱 **Columns:** match the existing table's columns and their emoji values, such as `🔴 High` for the priority.
- 📝 **Description:** bullet the context and what "done" means, joining bullets with `<br>` inside the cell.
