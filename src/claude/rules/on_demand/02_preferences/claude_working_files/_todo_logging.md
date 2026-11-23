# 📝 TODO logging

**Purpose:** what to do when the user says "add to TODOs" or similar.

- 📂 **Where:** add a row to the pending items table in `TODO.md` in your Claude config directory, unless the user names another place, and ask before creating the file if it doesn't exist.
- 🔢 **Number:** give it the next number after the highest in the table.
- 🧱 **Columns:** match the existing table's columns and their emoji values, such as `🔴 High` for the priority.
- 📝 **Description:** bullet the context and what "done" means, joining bullets with `<br>` inside the cell.

## 📚 Read on demand

- [`_templates/preferences/TODO.md.template`](../../../../_templates/preferences/TODO.md.template), in your Claude config directory, when creating a missing `TODO.md`, for its table layout.

## 📞 Called by

This rule is invoked by [`rules/always_on/02_preferences/claude_working_files.md`](../../../always_on/02_preferences/claude_working_files.md), when the user asks to add something to their TODOs.
