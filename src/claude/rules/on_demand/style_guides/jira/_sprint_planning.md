<!-- created: 2026-05-20 -->
# 📅 Sprint Planning

**Purpose:** Set sprint IDs, quarter-to-component mapping, parent epic references, and capacity conventions.

Your project's board, sprint IDs and component IDs live in the Jira values in `_local/jira_values.md` in your Claude config directory.

## 📋 Contents

- [🔢 Sprint IDs](#-sprint-ids)
- [📦 Quarter components](#-quarter-components)
- [🏆 Parent epics](#-parent-epics)
- [📏 Capacity conventions](#-capacity-conventions)
- [🔄 Sprint assignment rule](#-sprint-assignment-rule)

---

## 🔢 Sprint IDs

The Sprint field takes Jira's internal sprint ID, not the sprint number shown on the board.

- 🔎 **Look it up:** take the ID from the sprint table in `jira_values.md`.
- 📈 **Beyond the table:** sprint IDs usually go up by 1 per sprint, so extrapolate from the last known value.
- ✅ **Confirm it:** check an extrapolated ID with `searchJiraIssuesUsingJql` before using it.

---

## 📦 Quarter components

If your project tags tickets by quarter, derive the quarter component from the sprint the ticket is assigned to.

- 🏷️ **Names and IDs:** take them from the components table in `jira_values.md`.
- ➕ **Year component:** add any year-level component that table lists as required on every ticket.

---

## 🏆 Parent epics

Parent epics are **initiative-specific** — there is no single shared planning epic to default to. Select the parent epic based on the work being done:

- 🚀 **Feature or delivery work:** use the relevant initiative or project epic.
- 🗓️ **Planning prep or admin work:** use the assignee's own planning epic, and ask the user for it rather than assuming.

Confirm the epic ID via `getJiraIssue` before setting the parent. Do not hardcode or default to a personal planning epic.

---

## 📏 Capacity conventions

- 🧾 **Admin and overhead tasks:** give planning prep, ceremonies and BAU at least **0.5 story points**.
- 📐 **Feature stories:** size them on the team's agreed scale of `1`, `2`, `3`, `5`, `8` and `13`.
- 🚫 **Before the sprint:** set story points before a ticket enters the sprint, since `0` is a hygiene failure.

---

## 🔄 Sprint assignment rule

Assign a ticket to the sprint in which the **work will be done**.

Exception: planning prep tickets are assigned to the **current sprint** (the sprint running at the time of creation), since the prep occurs before the next sprint begins.
