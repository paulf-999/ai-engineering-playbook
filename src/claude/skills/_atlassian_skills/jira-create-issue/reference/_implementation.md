# 🛠️ jira-create-issue implementation

**Purpose:** maps the skill's phases to what Claude reads and does in each, so no ticket is created before the user approves it.

## 🔄 Phases

| Phase | What happens | Detail |
|---|---|---|
| **0 — Pre-check** | Call `getAccessibleAtlassianResources` for the cloud ID | `_error_handling.md` → No MCP server |
| **1 — Project** | Take the project key from the user or the values file, and confirm it | `_local/jira_values.md` |
| **2 — Draft** | Write the summary, description and acceptance criteria, and fill the fields from the conventions, as a Story with a parent epic by default | `on_demand/style_guides/jira/jira_team_conventions.md` |
| **3 — Confirm** | Show every field, with unknowns as `< TODO >`, and wait for an explicit yes | SKILL.md → Instructions |
| **4 — Create** | Call `createJiraIssue`, then report the issue key and browse link | `_error_handling.md` |

## 📋 Drafting rules

- **No values file:** offer to save the template from the conventions to `_local/jira_values.md`, and carry on with its values as `< TODO >`.
- **Parent epic:** every type except an Epic gets one, so confirm the key the user names with `getJiraIssue`, and ask for one rather than guessing.
- **Sprint:** take the sprint ID from the values file and confirm it with `searchJiraIssuesUsingJql`, as the conventions describe.
- **Story points:** above 0, following the conventions table, so admin work is at least `0.5` and features use `1`, `2`, `3`, `5`, `8` or `13`.
- **Unknown values:** ask for each value the user can give before Phase 3, and mark the rest `< TODO >` in the draft.
- **Creating with `< TODO >` left:** a yes creates the ticket with those fields empty, and the report lists them so the user can fill them in Jira.
- **Changes at the confirm step:** apply them and show the full ticket again before asking once more.
