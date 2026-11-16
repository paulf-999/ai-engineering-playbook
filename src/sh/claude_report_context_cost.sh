#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Write maintenance/context_cost.md: every always-on file's estimated tokens, and a rounded total for
#              the files that load only when needed, then print every file's tokens to the terminal
#              With --stage, the pre-commit hook's mode, rewrite a stale report and stage it, so the commit includes it,
#              but in CI write nothing and exit 1, since there a stale report means one was pushed without it
# Usage: src/sh/claude_report_context_cost.sh [--stage] [repo directory, default .] (run from the repo root)

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/shell_utils.sh"

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

CHECK_ONLY=false
STAGE=false
if [[ "${1:-}" == "--stage" ]]; then
    STAGE=true
    shift
fi
# CI sets CI=true, and there a stale report can't be fixed by staging it, so it must fail the run
if [[ "${STAGE}" == true && "${CI:-}" == true ]]; then
    CHECK_ONLY=true
    STAGE=false
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
    globs="$(rule_path_globs "${REPO_DIR}/${file}" | awk '{ printf "%s`%s`", sep, $0; sep = ", " }')"
    if [[ -n "${globs}" ]]; then
        echo "With matching files: ${globs}"
    elif [[ "${file}" == */preferences/* ]]; then
        # preferences install only with PREFERENCES=1
        echo "Every session, if opted in"
    else
        echo "Every session"
    fi
}

# Round a token count to the nearest 100, so small edits to rules that load only when needed don't change the report
rounded() {
    echo $(( ($1 + 50) / 100 * 100 ))
}

# Print one table per load type, each with a subtotal, so a total never mixes files that load differently
# With "summary", print the every-session table in full, and one rounded row for each other load type
table_body() {
    local mode="${1:-full}"
    local file chars condition name
    local every="" scoped="" lazy="" every_chars=0 scoped_chars=0 lazy_chars=0 every_n=0 scoped_n=0 lazy_n=0
    local opted="" opted_chars=0 opted_n=0
    while IFS= read -r file; do
        chars=$(count_loaded_chars "${REPO_DIR}/${file}")
        condition="$(load_condition "${file}")"
        name="\`${file#"${CONFIG_DIR}"/}\`"
        case "${condition}" in
            "Every session")
                every_n=$((every_n + 1))
                every+="| ${every_n} | ${name} | ~$((chars / 4)) |"$'\n'
                every_chars=$((every_chars + chars)) ;;
            "Every session, if opted in")
                opted_n=$((opted_n + 1))
                opted+="| ${opted_n} | ${name} | ~$((chars / 4)) |"$'\n'
                opted_chars=$((opted_chars + chars)) ;;
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
    printf '\n## 👤 Every session, if opted in\n\n| # | File | Tokens |\n|---|---|---|\n%s| | **Subtotal** | **~%s** |\n' \
        "${opted}" "$((opted_chars / 4))"
    if [[ "${mode}" == summary ]]; then
        printf '\n## 💤 Only when needed\n\n| Load type | Files | Tokens |\n|---|---|---|\n'
        printf '| 📂 Path-scoped rules, with matching files | %s | ~%s |\n' "${scoped_n}" "$(rounded $((scoped_chars / 4)))"
        printf '| 💤 On demand, via a pointer | %s | ~%s |\n' "${lazy_n}" "$(rounded $((lazy_chars / 4)))"
        return
    fi
    printf '\n## 📂 Path-scoped rules\n\n| # | File | Globs | Tokens |\n|---|---|---|---|\n%s| | **Subtotal** | | **~%s** |\n' "${scoped}" "$((scoped_chars / 4))"
    printf '\n## 💤 On demand\n\n| # | File | Tokens |\n|---|---|---|\n%s| | **Subtotal** | **~%s** |\n' "${lazy}" "$((lazy_chars / 4))"
}

# Print the whole report after its header: the purpose, how it's kept current, and the table
report_body() {
    cat <<'EOF'
# 💰 Context cost

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** how many tokens the global Claude config adds to every session, and to the tasks that need more, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/` and prints every file's tokens in the terminal, a pre-commit hook rewrites and stages it when a commit changes `src/claude/`, and CI fails if it's out of date, so don't edit the tables by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../docs/target_architecture/architecture/_budget_and_guards.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 👤 **Every session, if opted in:** preferences, which load in every session only after `make install PREFERENCES=1`. They count towards the budget only for those users, but the budget check always counts them, the worst case.
- 📂 **Path-scoped rules:** loads only once Claude opens a file that matches one of its globs.
- 💤 **On demand:** loads only when Claude follows a pointer to it.

EOF
    table_body summary
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
elif [[ "${STAGE}" == true ]]; then
    if [[ ! -f "${REPORT_PATH}" ]] || [[ "$(cat "${REPORT_PATH}")" != "${EXPECTED}" ]]; then
        printf '%s\n' "${EXPECTED}" > "${REPORT_PATH}"
        git -C "${REPO_DIR}" add -- "${REPORT}"
        print_section_header "${INFO}" "Rewrote ${REPORT} for this commit's changes, and staged it."
    else
        print_section_header "${INFO}" "SUCCESS: ${REPORT} matches src/claude/."
    fi
else
    printf '%s\n' "${EXPECTED}" > "${REPORT_PATH}"
    print_section_header "${INFO}" "Wrote ${REPORT}. Every file's tokens:"
    table_body
fi

print_section_header "${DEBUG}" "Script execution completed." && echo
