# 🆘 jira-create-issue error handling

**Purpose:** what Claude does when a pre-check or Jira call fails, so it never reports a ticket that doesn't exist.

- **No MCP server:** if `getAccessibleAtlassianResources` fails or isn't available, tell the user to enable the Atlassian MCP server and restart Claude Code, then stop.
- **Permission denied (403):** say the user lacks create-issue access to the project, and stop.
- **Unknown issue type or field (400 or 404):** look the project's fields up with `getJiraIssueTypeMetaWithFields`, and ask the user rather than retrying with a guess.
- **Assignee not found:** ask for the person's email or account ID, or leave the assignee as `< TODO >`.
- **Epic not found:** ask for the right epic key, or leave the parent as `< TODO >`, and never attach an unconfirmed epic.
- **Any failure:** never report a key or link the MCP call didn't return.
