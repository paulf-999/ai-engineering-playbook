---
name: jira-create-issue
description: Create a Jira ticket in the team's conventions — use when asked to create a Jira ticket, create a bug in Jira or log this as a Jira ticket
---

## 🤖 Instructions for Claude

- **Pre-check:** call `getAccessibleAtlassianResources` to get the cloud ID, and if it fails tell the user to enable the Atlassian MCP server and restart Claude Code, then stop.
- **Read first:** read `reference/_implementation.md`, then `on_demand/style_guides/jira.md`, `on_demand/style_guides/jira/jira_team_conventions.md` and `_local/jira_values.md` in your Claude config directory before drafting.
- **Always:** draft a Story with a parent epic unless the user names another type, ask for the values the user can give, and mark the rest `< TODO >`.
- **Always:** show the full ticket and wait for an explicit yes before calling `createJiraIssue`.
- **Never:** infer the Jira project, so take it from the user or the values file and confirm it.
- **Never:** invent a title, story points, an assignee or a parent epic the user hasn't given.

## 🎯 Purpose

Turns a request into one Jira ticket that is ready for a sprint, with one confirmation before anything is created:

- **Draft** — writes the summary, description and acceptance criteria in the team's format.
- **Fields** — fills story points, epic, sprint, components, priority and business value from the conventions and your values file.
- **Confirm** — shows the whole ticket, with every unknown value marked `< TODO >`, before creating it.
- **Report** — gives back the new issue's key and link.

## 💡 Example Usage

```text
$ /jira-create-issue the dbt nightly run times out on the orders model, 2 points
[Phase 1] Project DATA (from your values file), is that right? y
[Phase 2] Story · "Data Platform — fix the orders model timeout" · 2 points
          Parent epic: < TODO >, which epic should this sit under? DATA-310
[Phase 3] Here is the ticket I will create: …
          Create it? y
[Phase 4] DATA-1234 created: https://yourteam.atlassian.net/browse/DATA-1234
```

## ✨ Best For

Raising one well-formed ticket quickly, without looking up field IDs, sprint IDs or the scoring rules by hand.

**Caveats:** it creates one new ticket at a time.

- **Existing tickets:** it doesn't update, move or link tickets, so do that in Jira.
- **Values file:** without `_local/jira_values.md`, the field and sprint IDs stay `< TODO >` until you fill it in.
- **Evals:** `make evals` checks the scenarios in `tests/evals.yaml` tagged `trigger:`.

## 📚 References

- `reference/_implementation.md` — the phase map and what each phase reads
- `reference/_error_handling.md` — what to do when the MCP server or Jira rejects a call
- `tests/evals.yaml` — 2 scenarios, each run by `make evals`
