# 🧪 confluence-create-page tests

**Purpose:** what each scenario in `evals.yaml` checks, so an author can test a change to the skill against them.

Each scenario records a user request, its setup and the expected result. They aren't code, and nothing runs them yet, so treat them as worked examples to check the skill against by hand.

## 📋 Scenarios

| # | Scenario | Phase | What it checks |
|---|---|---|---|
| 1 | `happy_path_general_page` | Full flow | Confirms the place, saves a draft, and creates the page as a Confluence draft only after approval |
| 2 | `happy_path_platform_risk_assessment` | Full flow | Pre-fills themes from cited evidence, rates them in full words, and creates only after approval |
| 3 | `mcp_unavailable_stops` | Pre-check | Stops and asks for the Atlassian MCP server before choosing a pattern |
| 4 | `space_not_named_is_confirmed` | Pattern and place | Asks for the space and parent page instead of inferring them |
| 5 | `parent_page_required` | Pattern and place | Never creates a page at the space root |
| 6 | `unsupported_pattern_offers_valid_ones` | Not for | Turns down an unsupported page type and offers the two patterns |
| 7 | `personal_names_replaced_with_roles` | Gather | Replaces a named person with a role, and says so |
| 8 | `draft_review_iteration` | Draft review | Revises the same draft and asks again, never creating the page mid-review |
| 9 | `publish_permission_denied` | Create | A permission error names the space, gives the fix and keeps the draft |
| 10 | `page_update_request_out_of_scope` | Not for | Turns down a request to edit an existing page |
| 11 | `jira_request_goes_elsewhere` | Not for | A Jira request doesn't fire this skill |

- **No handler tests:** this skill has no Python code, so `evals.yaml` is its only test.
