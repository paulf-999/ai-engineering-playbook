#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Write maintenance/context_cost.md, a table of each src/claude/ file's estimated tokens and when it loads
#              With --check, write nothing and exit 1 if the committed table is out of date
# Usage: src/sh/claude_report_context_cost.sh [--check] [repo directory, default .] (run from the repo root)

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/shell_utils.sh"

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
REPORT="maintenance/context_cost.md"

#=======================================================================
# Functions
#=======================================================================

# Print when a file loads: on demand, with matching files, or in every session
# the config's README is for people browsing the repo, so like the templates it's read only when opened
load_condition() {
    local file="${1}" globs
    if [[ "${file}" == "${CONFIG_DIR}/rules/on_demand/"* || "${file}" == "${CONFIG_DIR}/_templates/"* \
        || "${file}" == "${CONFIG_DIR}/README.md" ]]; then
        echo "On demand, via a pointer"
        return
    fi
    # the globs listed under paths: in the file's opening --- block
    globs="$(awk 'NR == 1 && $0 != "---" { exit } NR > 1 && $0 == "---" { exit } /^paths:/ { on = 1; next } on && /^[[:space:]]*-/ { gsub(/^[[:space:]]*-[[:space:]]*|"|\047/, ""); printf "%s`%s`", sep, $0; sep = ", "; next } on && !/^[[:space:]]*-/ { on = 0 }' "${REPO_DIR}/${file}")"
    if [[ -n "${globs}" ]]; then
        echo "With matching files: ${globs}"
    else
        echo "Every session"
    fi
}

# Print one table per load type, each with a subtotal, so a total never mixes files that load differently
table_body() {
    local file chars condition name
    local every="" scoped="" lazy="" every_chars=0 scoped_chars=0 lazy_chars=0 every_n=0 scoped_n=0 lazy_n=0
    while IFS= read -r file; do
        chars=$(count_loaded_chars "${REPO_DIR}/${file}")
        condition="$(load_condition "${file}")"
        name="\`${file#"${CONFIG_DIR}"/}\`"
        case "${condition}" in
            "Every session")
                every_n=$((every_n + 1))
                every+="| ${every_n} | ${name} | ~$((chars / 4)) |"$'\n'
                every_chars=$((every_chars + chars)) ;;
            "On demand"*)
                lazy_n=$((lazy_n + 1))
                lazy+="| ${lazy_n} | ${name} | ~$((chars / 4)) |"$'\n'
                lazy_chars=$((lazy_chars + chars)) ;;
            *)
                scoped_n=$((scoped_n + 1))
                scoped+="| ${scoped_n} | ${name} | ${condition#With matching files: } | ~$((chars / 4)) |"$'\n'
                scoped_chars=$((scoped_chars + chars)) ;;
        esac
    # sort by byte value, so the order is the same on every machine whatever its locale
    done < <(git -C "${REPO_DIR}" ls-files -- "${CONFIG_DIR}/*.md" | LC_ALL=C sort)
    printf '## 🔒 Every session\n\n| # | File | Tokens |\n|---|---|---|\n%s| | **Subtotal** | **~%s** |\n' "${every}" "$((every_chars / 4))"
    printf '\n## 📂 Path-scoped rules\n\n| # | File | Globs | Tokens |\n|---|---|---|---|\n%s| | **Subtotal** | | **~%s** |\n' "${scoped}" "$((scoped_chars / 4))"
    printf '\n## 💤 On demand\n\n| # | File | Tokens |\n|---|---|---|\n%s| | **Subtotal** | **~%s** |\n' "${lazy}" "$((lazy_chars / 4))"
}

# Print the whole report after its header: the purpose, how it's kept current, and the table
report_body() {
    cat <<'EOF'
# 💰 Context cost

**Purpose:** how many tokens each file in the global Claude config adds, and when it loads, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/`, and a pre-commit check fails if it's out of date, so don't edit the tables by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../target_architecture/target_architecture.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 📂 **Path-scoped rules:** loads only once Claude opens a file that matches one of its globs.
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
    if [[ ! -f "${REPORT_PATH}" ]] || [[ "$(cat "${REPORT_PATH}")" != "${EXPECTED}" ]]; then
        print_section_header "${ERROR}" "ERROR: ${REPORT} is out of date. Run make context_cost and commit the result."
        if [[ -f "${REPORT_PATH}" ]]; then
            diff "${REPORT_PATH}" <(echo "${EXPECTED}") || true
        fi
        exit 1
    fi
    print_section_header "${INFO}" "SUCCESS: ${REPORT} matches src/claude/."
else
    printf '%s\n' "${EXPECTED}" > "${REPORT_PATH}"
    print_section_header "${INFO}" "Wrote ${REPORT}."
fi

print_section_header "${DEBUG}" "Script execution completed." && echo
