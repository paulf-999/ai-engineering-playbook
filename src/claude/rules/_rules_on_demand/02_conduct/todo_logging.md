<!-- version: 2.0.0 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-04 -->
# 📝 TODO logging

**Purpose:** what to do when the user says "add to TODOs" or similar.

- 📂 **Where:** add a row to the items table in `TODO.md` in your Claude config directory, unless the user names another place, and ask before creating the file if it doesn't exist.
- 🔢 **Number:** give it the next number after the highest in the table.
- 🧱 **Columns:** match the existing table's columns and their emoji values, such as `📋 Pending` for the status.
- 📝 **Description:** bullet the context and what "done" means, joining bullets with `<br>` inside the cell.
