#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Verify a PR that changes the installed Claude config under src/claude/ has a "Claude: Plan" section
#              with its menus, or the reason it has no saved plan, and that one changing an always-on or enforcing file
#              also has an "Evaluation Criteria" section
# Usage: src/sh/git/git_validate_pr_description.sh "<pr description>" ["<changed files, one per line>"] (run from the repo root)

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/../shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/../shell_utils.sh"

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

PR_DESCRIPTION="${1-}"
# the PR's changed files, one per line, used to spot changes to the installed Claude config
CHANGED_FILES="${2-}"
# the description as a reader sees it, without HTML comments, set in the main logic
VISIBLE_DESCRIPTION=""
# the collapsible menus a "Claude: Plan" section holds
PLAN_MENUS=("intent.md" "spec.md" "plan.md" "measures" "governance")
# why the description fails, set in the main logic (empty means it's valid)
PROBLEMS=""

#=======================================================================
# Functions
#=======================================================================

# Print the description with Unix line endings and without HTML comments, so template instructions don't count
visible_description() {
    printf '%s\n' "${PR_DESCRIPTION}" | tr -d '\r' | awk '
        {
            rest = $0; visible = ""
            while (rest != "") {
                marker = in_comment ? "-->" : "<!--"
                at = index(rest, marker)
                if (!in_comment) visible = visible (at ? substr(rest, 1, at - 1) : rest)
                if (!at) break
                rest = substr(rest, at + length(marker))
                in_comment = !in_comment
            }
            print visible
        }'
}

# Succeed if a visible line matches the pattern $1, in any case (a here-string, since grep -q can break a long pipe)
has_line() {
    grep -qiE -- "${1}" <<< "${VISIBLE_DESCRIPTION}"
}

# Succeed if the description has a "## " heading containing $1
has_section() {
    has_line "^## .*${1}"
}

# Explain which plan menus are missing, or print nothing if they're all there or a reason says there's no saved plan
plan_menu_problems() {
    local menu
    has_line '^No saved plan:[[:space:]]*[^[:space:]]' && return 0
    for menu in "${PLAN_MENUS[@]}"; do
        # the menu's name with its dot escaped, as the pattern matches the whole line
        has_line "^[[:space:]]*(<details>)?[[:space:]]*<summary>Show ${menu//./\\.}</summary>[[:space:]]*$" \
            || echo "Add the 'Show ${menu}' menu to the Claude: Plan section, or a line 'No saved plan: <reason>'."
    done
}

# Explain why the section named $1 is missing, given the reason $2 it's needed, or print nothing if it's there
section_problem() {
    has_section "${1}" || echo "Add the '${1}' section that the PR template's comment names, since ${2}."
}

# Explain each reason the description fails, or print nothing if it's fine
description_problems() {
    # src/claude/ is the config that `make install` copies
    printf '%s\n' "${CHANGED_FILES}" | grep -qE '^src/claude/' || return 0
    section_problem "Claude: Plan" "this PR changes src/claude/"
    plan_menu_problems
    # CLAUDE.md, a rule in rules/always_on/ and hooks load in every session or enforce behaviour
    printf '%s\n' "${CHANGED_FILES}" | grep -qE '^src/claude/(CLAUDE\.md|rules/always_on/|hooks/)' || return 0
    section_problem "Evaluation Criteria" "this PR changes an always-on or enforcing file"
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

VISIBLE_DESCRIPTION="$(visible_description)"
PROBLEMS="$(description_problems)"
if [[ -n "${PROBLEMS}" ]]; then
    print_section_header "${ERROR}" "ERROR: The PR description needs changes."
    printf '%s\n' "${PROBLEMS}"
    exit 1
fi
print_section_header "${INFO}" "SUCCESS: Valid PR description"

print_section_header "${DEBUG}" "Script execution completed." && echo
