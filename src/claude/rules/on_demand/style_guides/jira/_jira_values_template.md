<!-- created: 2026-11-05 -->
# 🧩 Jira values template

**Purpose:** the organisation-specific Jira values the Jira style guide needs, as placeholders to copy and fill in.

- 📋 **Copy it:** save a copy as `_local/jira_values.md` in your Claude config directory, then replace each `<placeholder>`.
- 🔒 **Keep it local:** `make install` never touches `_local/`, and the filled-in copy never belongs in a repo.
- 🚫 **No copy yet:** leave affected fields as `< TODO >` and ask the user, rather than guessing a value.

## 🗂️ Project and board

| Setting | Value |
|---|---|
| Project key | `<PROJ>` |
| Board ID | `<board-id>` |
| Claude-created label | `<team>-claude-created` |
| Summary area | `<Area>`, e.g. your team name |

## 🔧 Custom field IDs

| Field | Jira ID | Type |
|---|---|---|
| Story points | `customfield_<n>` | Number |
| Sprint | `customfield_<n>` | Integer sprint ID |
| Business value | `customfield_<n>` | ADF document |

## 🔢 Sprint IDs

| Sprint | ID |
|---|---|
| `<sprint number>` | `<sprint ID>` |

## 📦 Components

| Component | ID | When to use |
|---|---|---|
| `<year-level component>` | `<id>` | Every ticket, if your project uses one |
| `<quarter component>` | `<id>` | The quarter of the ticket's sprint |

## 💼 Business value scoring

- **Framework name:** `<your prioritisation framework>`
- **Prioritisation matrix:** `<link to your team's prioritisation matrix>`

| Category | Weight |
|---|---|
| `<category>` | `<weight %>` |
