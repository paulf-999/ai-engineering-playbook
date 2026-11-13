<!-- created: 2026-05-20 -->
# 🎫 Ticket Conventions

**Purpose:** Set the standards for summary naming, description structure, acceptance criteria format, and issue type usage for Jira tickets.

## 📋 Contents

- [🔖 Summary (title) naming](#-summary-title-naming)
- [📋 Description structure](#-description-structure)
- [🧩 Issue types](#-issue-types)

---

## 🔖 Summary (title) naming

- 📐 **Format:** `<Area> — <action or topic>`, with an em-dash (—) separator.
- 🏷️ **Area:** the team or domain the ticket belongs to, such as `Data Platform`.
- ✏️ **Action or topic:** an imperative or noun phrase, short enough to read at a glance in a backlog view.

Examples:

- `Data Platform — Sprint 63 planning prep`
- `Data Platform — Claude AI playbook Jira style guide`

---

## 📋 Description structure

Every ticket body follows a **two-section structure**:

```text
<1-sentence context line>

* <bullet>
* <bullet>
* <bullet>

### Acceptance criteria

* <outcome bullet>
* <outcome bullet>
```

**Rules:**

- 💬 **Context first:** open with one sentence saying what the ticket is for and why.
- 🔹 **Then bullets:** follow straight away with bullets for scope, tasks or actions, with no prose paragraphs.
- 🧱 **Separator:** put a `### Acceptance criteria` H3 heading between the two sections.
- 🎯 **Acceptance criteria:** write observable outcomes, specific and testable, so it's clear when the work is done.
- ⏱️ **Scannable:** keep every description readable in under 10 seconds.

**Canonical example:**

*Description:*

```text
Sprint planning prep for Sprint 63.

* Review roadmap priorities
* Assess what's complete, in-flight, and outstanding from Sprint 62
* Confirm availability/capacity for myself and a teammate
* Identify and size Sprint 63 candidates for us both
```

*Acceptance criteria:*

```text
* Availability/capacity confirmed for myself and a teammate for Sprint 63
* Sprint 63 backlog finalised and tickets moved into sprint in Jira
```

---

## 🧩 Issue types

| Type | When to use |
|---|---|
| **Story** | Any deliverable unit of work — a feature, task, or piece of analysis |
| **Epic** | A theme, programme, or multi-sprint initiative grouping related stories |

Use Stories for all day-to-day tickets. Reserve Epics for grouping related work across sprints. Every Story must have a parent Epic set.
