<!-- created: 2026-04-11 -->
<!-- applies_to: * -->
<!-- miss_cost: low — dates drift between formats -->
# 📅 Date & Time Standards

**Purpose:** Set one date and time format for technical contexts, so code, metadata and logs sort and compare consistently.

ISO format applies to technical contexts (code, metadata, logs). Human-facing content uses
English sentence-style dates instead. Do not retroactively update existing files — apply
opportunistically when a file is being actively modified for another reason.

## 📋 Contents

- [📅 Standard formats](#-standard-formats)
- [🕐 Timezone](#-timezone)
- [📋 Applies to — technical contexts](#-applies-to--technical-contexts)
- [🚧 Known exceptions](#-known-exceptions)
- [📝 Does not apply — human-facing content](#-does-not-apply--human-facing-content)

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

- Metadata headers (e.g. the `created` comment line)
- Changelog and release note dates
- Log entries and audit outputs
- Code files and technical documentation
- Memory files and plan files

---

## 🚧 Known exceptions

- **Filenames:** a date in a filename uses underscores, as in `2026_04_10_<topic>.md`, since filenames are snake_case.

---

## 📝 Does not apply — human-facing content

Use English sentence-style dates (e.g. `1st May 2026`, `23rd April 2026`) in content written for a human audience:

- Confluence pages
- Pull request descriptions
- Teams messages and emails
- Jira ticket descriptions and comments
- Meeting notes, agendas, catch-up prep and other narrative documents
