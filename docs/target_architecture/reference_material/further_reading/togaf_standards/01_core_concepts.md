<!-- version: 1.0.0 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-04 -->
# 🧩 TOGAF: Core concepts

**Purpose:** the terms the TOGAF Standard builds on, from what an enterprise is to how an architecture is described to the people who care about it.

This page is part of the [summary of the TOGAF Standard](../togaf_standards.md).

## 🏢 Enterprise and architecture

The standard starts from these definitions:

- 🏢 **Enterprise:** any group of organisations that share a set of goals, from a single department to a whole company and its partners.
- 🏗️ **Architecture:** how a system's parts are structured and relate, plus the principles that guide its design and change over time.
- 🎯 **Enterprise architecture:** that view applied across the whole enterprise, so change in one area supports the shared goals.
- 💡 **Why it matters:** it lets an organisation make change faster and cheaper, with less duplication and lower risk.

## 🗂️ The four architecture domains

| Domain | What it describes |
|---|---|
| 💼 **Business** | Strategy, governance, organisation and the key business processes. |
| 🗄️ **Data** | The structure of the organisation's data assets and how they are managed. |
| 🖥️ **Application** | Each application, how they interact, and which business processes they serve. |
| ⚙️ **Technology** | The hardware, software and network infrastructure the applications run on. |

- 🔗 **Grouping:** the Data and Application domains together form the Information Systems Architectures.

## 🧱 Building blocks

A building block is a reusable package of capability that meets a business need, and it comes in two kinds:

- 📐 **Architecture Building Block (ABB):** says what capability is needed, without naming a product.
- 🔧 **Solution Building Block (SBB):** the real product or component that delivers an ABB.

## 👥 Stakeholders, concerns, viewpoints and views

These four terms describe how an architecture is shown to the people it affects:

- 👤 **Stakeholder:** a person or group with an interest in the architecture, such as a sponsor, user or operator.
- ❓ **Concern:** something a stakeholder cares about, such as cost, security or performance.
- 🔭 **Viewpoint:** a reusable template saying how to build a view for a given set of concerns.
- 🖼️ **View:** what a stakeholder actually sees, built from a viewpoint to answer their concerns.
  - **Example:** a security viewpoint defines what a security view of the payments system must show.

## 📏 Architecture principles

- 📜 **What they are:** lasting rules that guide architecture decisions, agreed early and reused across efforts.
- 🧾 **Format:** each has a name, a statement, a rationale and its implications.
