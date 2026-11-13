<!-- created: 2026-06-07 -->
# 💼 Business Value Tab

**Purpose:** Set the standards for populating the Business Value tab on Jira tickets — covering format, audience, scoring framework, and a worked example.

The field ID, framework name, matrix link and weights live in the Jira values in `_local/jira_values.md` in your Claude config directory.

## 📋 Contents

- [🧱 Format](#-format)
- [👥 Audience guidance](#-audience-guidance)
- [📊 Impact Rating block](#-impact-rating-block)
- [🧮 Scoring frameworks](#-scoring-frameworks)
- [📝 Worked example](#-worked-example)

---

## 🧱 Format

Every Business Value statement must follow this structure:

1. **Intro** — 1–2 sentences written for a non-technical business audience
2. **Bullet points** — up to 3 bullets covering risk, context, and scope
3. **Impact Rating block** — always present; see format below

---

## 👥 Audience guidance

The Business Value tab is read by external stakeholders and non-technical audiences.

- **Acceptable:** Named company-wide systems — e.g. "GitHub Enterprise migration", "Salesforce"
- **Not acceptable:** internal tooling names, such as Airflow, dbt, Docker, PAT or GHCR.
  - **Instead:** describe the tool by what it does, such as "automated data pipelines" or "the software that runs data transformations".

---

## 📊 Impact Rating block

Always append the following block after the intro and bullets:

```text
Impact Rating (per <your prioritisation framework>):
* a. Prioritization Matrix: <link to your team's prioritisation matrix>
* b. Priority Value Driver: <driver> – Score: <N>
* c. Secondary Value Driver: <driver> – Score: <N>
* d. Calculated Score: <value>
```

Fill in scores when the driver and rating are clear at creation time. Use `< TODO >` only when genuinely uncertain.

**Score calculation:** Only the top two drivers are scored.
`Calculated Score = (primary score × primary weight) + (secondary score × secondary weight)`

---

## 🧮 Scoring frameworks

Use your organisation's framework, with the categories and weights listed in `jira_values.md`.

- **Second framework:** if your team weights some work differently (for example platform reliability or operational continuity), list that framework in `jira_values.md` too, and say when it applies.
- **No framework yet:** leave the Impact Rating scores as `< TODO >` rather than inventing categories or weights.

**Scoring rubric:**

- 🔴 **5, Critical or immediate:** imminent regulatory, financial or customer impact, or a production outage if not addressed.
- 🟠 **3, Strategic or important:** removes significant recurring manual work, or unlocks a new insight or capability.
- 🟢 **1, Maintenance or low impact:** minor tweaks, nice-to-have metadata, or R&D with no clear return.
- ↕️ **4 or 2:** a driver that sits between the levels either side.

---

## 📝 Worked example

With example weights of 15% and 20%, a 5 and a 4 score `5 × 0.15 + 4 × 0.20 = 1.55`:

```text
A mandatory company-wide system change (GitHub Enterprise migration) will prevent the
data platform from running its automated processes unless addressed before the deadline.

- All data reports and dashboards will stop receiving updates
- Non-negotiable timeline — driven by a migration outside the team's control
- Scope: identify the solution now; implementation follows as a separate piece of work

Impact Rating (per <your prioritisation framework>):
* a. Prioritization Matrix: <link to your team's prioritisation matrix>
* b. Priority Value Driver: Platform Reliability & Technical Risk – Score: 5
* c. Secondary Value Driver: Ops Efficiency – Score: 4
* d. Calculated Score: 1.55
```
