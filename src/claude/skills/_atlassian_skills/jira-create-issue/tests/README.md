# 🧪 jira-create-issue tests

**Purpose:** what each scenario in `evals.yaml` checks, so an author can test a change to the skill against them.

Each scenario records a user request, its setup and the expected result. They aren't code, and nothing runs them yet, so treat them as worked examples to check the skill against by hand.

## 📋 Scenarios

| # | Scenario | Phase | What it checks |
|---|---|---|---|
| 1 | `happy_path_story_ticket` | Full flow | Reads the conventions, drafts a Story under a confirmed epic, and creates it only after a yes |
| 2 | `named_type_kept` | Draft | A requested Bug stays a Bug rather than the Story default |
| 3 | `mcp_unavailable_stops` | Pre-check | Stops and asks for the Atlassian MCP server instead of drafting or inventing a ticket |
| 4 | `unknown_values_left_as_todo` | Draft | Asks for the project and marks unknown values `< TODO >` rather than guessing |
| 5 | `zero_story_points_queried` | Draft | Story points of 0 are queried against the conventions table, not rounded up |
| 6 | `missing_title_requested` | Draft | A request with no clear work is asked about, never invented |
| 7 | `declined_confirmation_creates_nothing` | Confirm | A "no" at the confirm step creates nothing |
| 8 | `created_ticket_reports_key_and_link` | Create | On success, reports the new issue's key and link |
| 9 | `update_request_out_of_scope` | Not for | A request to update an existing ticket is turned down |
| 10 | `confluence_request_goes_elsewhere` | Not for | A Confluence request doesn't fire this skill |

- **No handler tests:** this skill has no Python code, so `evals.yaml` is its only test.
