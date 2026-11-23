# 🎫 Jira team conventions

**Purpose:** this team's Jira ticket structure, required fields, sprint assignment and business-value scoring. Another team can replace them with its own, while the standards stay in `../jira.md`.

Your project's field IDs, components, sprint IDs and scoring weights live in `_local/jira_values.md` in your Claude config directory.

- 📋 **No values file:** save the [template below](#-values-file-template) there, and ask the user to fill it in. `make install` never touches `_local/`, and the filled-in copy never belongs in a repo.
- 🚫 **Unknown value:** leave the field as `< TODO >` and ask, rather than guessing, or look a field ID up with `getJiraIssueTypeMetaWithFields`.

## 🎫 Ticket structure

- 📐 **Summary:** `<Area> — <action or topic>`, with an em-dash, such as `Data Platform — Sprint 63 planning prep`.
- 💬 **Description:** one context sentence, then bullets for scope or tasks, with no prose paragraphs.
- 🎯 **Acceptance criteria:** under a `### Acceptance criteria` heading, as specific, testable outcomes.
- 🧩 **Issue type:** a Story for any unit of work, with a parent Epic, and an Epic only to group work across sprints.
- 🏷️ **Label:** add the Claude-created label from your values file to every ticket Claude writes.

## ✅ Ready for a sprint

Every ticket needs all of these before it enters a sprint:

| Field | Rule |
|---|---|
| Summary and description | Follow the structure above, with acceptance criteria, not a placeholder |
| Story points | Above 0: at least `0.5` for admin, planning or ceremonies, and `1`, `2`, `3`, `5`, `8` or `13` for features |
| Assignee and parent epic | Both set, with the epic confirmed via `getJiraIssue` |
| Components | Those your values file lists as required, plus the quarter of the ticket's sprint where used |
| Priority | **Medium**, unless there's a stated reason |
| Status | **Backlog**, never left in Triage |
| Business value | Filled in as below |

## 📅 Sprint and epic

- 🔢 **Sprint ID:** the Sprint field takes Jira's internal ID from your values file, not the board's sprint number. Extrapolate past the table by 1 a sprint, and confirm with `searchJiraIssuesUsingJql`.
- 🗓️ **Which sprint:** the one the work happens in, except planning prep, which goes in the current sprint.
- 🏆 **Parent epic:** the initiative's epic for delivery work, and the assignee's planning epic for admin, asking the user rather than assuming.

## 💼 Business value

Written for non-technical readers, so name company-wide systems such as Salesforce, but describe internal tools such as dbt or Airflow by what they do:

```text
<1–2 sentence intro>
- <up to 3 bullets: risk, context and scope>

Impact Rating (per <your prioritisation framework>):
* a. Prioritisation Matrix: <link from your values file>
* b. Priority Value Driver: <driver> – Score: <N>
* c. Secondary Value Driver: <driver> – Score: <N>
* d. Calculated Score: <primary score × weight + secondary score × weight>
```

- 🔴 **5:** imminent regulatory, financial or customer impact, or an outage.
- 🟠 **3:** removes significant recurring manual work, or unlocks a new capability.
- 🟢 **1:** minor tweaks, or work with no clear return, with 4 and 2 for drivers in between.
- ❓ **No framework:** leave the scores as `< TODO >` rather than inventing categories or weights.

## 🧩 Values file template

```markdown
# Jira values

| Setting | Value |
|---|---|
| Project key | `<PROJ>` |
| Board ID | `<board-id>` |
| Claude-created label | `<team>-claude-created` |
| Summary area | `<Area>` |
| Story points field | `customfield_<n>` |
| Sprint field | `customfield_<n>` |
| Business value field | `customfield_<n>` |
| Prioritisation framework | `<name>`, matrix at `<link>` |

| Sprint | ID |
|---|---|
| `<sprint number>` | `<sprint ID>` |

| Component | ID | When to use |
|---|---|---|
| `<component>` | `<id>` | `<every ticket, or the quarter of the ticket's sprint>` |

| Business value category | Weight |
|---|---|
| `<category>` | `<weight %>` |
```

## 📞 Called by

This rule is invoked by:

- [`rules/on_demand/style_guides/jira.md`](../jira.md), before writing or changing a ticket, for this team's ticket format, fields, sprints and scoring.
- [`skills/_atlassian_skills/jira-create-issue/SKILL.md`](../../../../skills/_atlassian_skills/jira-create-issue/SKILL.md), before drafting a ticket.
- [`skills/_atlassian_skills/jira-create-issue/reference/_implementation.md`](../../../../skills/_atlassian_skills/jira-create-issue/reference/_implementation.md), at step 2, when drafting the ticket.
