# 📅 Date & Time Standards

**Purpose:** Set one date and time format for technical contexts, so code, metadata and logs sort and compare consistently.

ISO format applies to technical contexts (code, metadata, logs). Human-facing content uses
English sentence-style dates instead. Do not retroactively update existing files — apply
opportunistically when a file is being actively modified for another reason.

## 📋 Contents

- [📅 Standard formats](#-standard-formats)
- [🕐 Timezone](#-timezone)
- [📋 Applies to — technical contexts](#-applies-to--technical-contexts)
- [📝 Human-facing content](#-human-facing-content)

---

## 📅 Standard formats

| Type | Format | Example |
|---|---|---|
| Date | `YYYY-MM-DD` | `2026-04-10` |
| Datetime | `YYYY-MM-DDTHH:MM:SSZ` | `2026-04-10T14:30:00Z` |

---

## 🕐 Timezone

UTC is the required timezone for all datetimes. The `Z` suffix must always be included —
it makes the timezone explicit and avoids ambiguity.

---

## 📋 Applies to — technical contexts

Use ISO format where dates are machine-readable, sortable, or stored:

- Changelog and release note dates
- Log entries and audit outputs
- Code files and technical documentation
- Memory files and plan files

---

## 📝 Human-facing content

Use English sentence-style dates in content written for a human audience, in the team's style.

## 📚 Read on demand

- [`on_demand/style_guides/utilities/datetime_team_conventions.md`](datetime_team_conventions.md), in your Claude config directory, before writing a date into a filename or a human-facing document.

## 📞 Called by

This rule is invoked by [`rules/always_on/01_standards/naming_standards.md`](../../../always_on/01_standards/naming_standards.md), when writing a date or time into a name, code or log.
