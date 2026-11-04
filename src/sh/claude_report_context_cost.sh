#!/bin/bash
# version: 1.0.0
# created: 2026-11-04
# updated: 2026-11-04
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Write docs/maintenance/context_cost.md, a table of each src/claude/ file's estimated tokens and when it loads
#              With --check, write nothing and exit 1 if the committed table is out of date
# Usage: src/sh/claude_report_context_cost.sh [--check] [repo directory, default .] (run from the repo root)

# Load reusable shell script vars & functions
source src/sh/shell_utils.sh

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

CHECK_ONLY=false
if [[ "${1:-}" == "--check" ]]; then
    CHECK_ONLY=true
    shift
fi
REPO_DIR="${1:-.}"
CONFIG_DIR="src/claude"
REPORT="docs/maintenance/context_cost.md"
# the report's version header, kept as it is so the header bump doesn't make the table look stale
HEADER_LINES=3
ALWAYS_ON_CHARS=0

#=======================================================================
# Functions
#=======================================================================

# Print when a file loads: on demand, with matching files, or in every session
load_condition() {
    local file="${1}" globs
    if [[ "${file}" == "${CONFIG_DIR}/rules/_rules_lazy_load/"* ]]; then
        echo "On demand, via a pointer"
        return
    fi
    # the globs listed under paths: in the file's opening --- block
    globs="$(awk 'NR == 1 && $0 != "---" { exit } NR > 1 && $0 == "---" { exit } /^paths:/ { on = 1; next } on && /^[[:space:]]*-/ { gsub(/^[[:space:]]*-[[:space:]]*|"|\047/, ""); printf "%s`%s`", sep, $0; sep = ", " } on && !/^[[:space:]]*-/ { on = 0 }' "${REPO_DIR}/${file}")"
    if [[ -n "${globs}" ]]; then
        echo "With matching files: ${globs}"
    else
        echo "Every session"
    fi
}

# Print the report's table body: one row per tracked markdown file, then the always-on total
table_body() {
    local file chars condition
    echo "| File | Loads | Tokens |"
    echo "|---|---|---|"
    while IFS= read -r file; do
        chars=$(count_loaded_chars "${REPO_DIR}/${file}")
        condition="$(load_condition "${file}")"
        if [[ "${condition}" == "Every session" ]]; then
            ALWAYS_ON_CHARS=$((ALWAYS_ON_CHARS + chars))
        fi
        echo "| \`${file#"${CONFIG_DIR}"/}\` | ${condition} | ~$((chars / 4)) |"
    done < <(git -C "${REPO_DIR}" ls-files -- "${CONFIG_DIR}/*.md" | sort)
    echo "| **Every-session total** | | **~$((ALWAYS_ON_CHARS / 4))** |"
}

# Print the whole report after its header: the purpose, how it's kept current, and the table
report_body() {
    cat <<'EOF'
# 💰 Context cost

**Purpose:** how many tokens each file in the global Claude config adds, and when it loads, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/`, and a pre-commit check fails if it's out of date, so don't edit the table by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../target_architecture/target_architecture.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 📂 **With matching files:** loads only once Claude opens a file that matches one of its globs.
- 💤 **On demand:** loads only when Claude follows a pointer to it.

EOF
    table_body
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

use_utf8_locale
EXPECTED="$(report_body)"
REPORT_PATH="${REPO_DIR}/${REPORT}"

if [[ "${CHECK_ONLY}" == true ]]; then
    if [[ ! -f "${REPORT_PATH}" ]] || [[ "$(tail -n +$((HEADER_LINES + 1)) "${REPORT_PATH}")" != "${EXPECTED}" ]]; then
        print_section_header "${ERROR}" "ERROR: ${REPORT} is out of date. Run make context_cost and commit the result."
        exit 1
    fi
    print_section_header "${INFO}" "SUCCESS: ${REPORT} matches src/claude/."
else
    TODAY="$(date +%F)"
    HEADER="<!-- version: 1.0.0 -->"$'\n'"<!-- created: ${TODAY} -->"$'\n'"<!-- updated: ${TODAY} -->"
    if [[ -f "${REPORT_PATH}" ]]; then
        HEADER="$(head -n "${HEADER_LINES}" "${REPORT_PATH}")"
    fi
    printf '%s\n%s\n' "${HEADER}" "${EXPECTED}" > "${REPORT_PATH}"
    print_section_header "${INFO}" "Wrote ${REPORT}."
fi

print_section_header "${DEBUG}" "Script execution completed." && echo
