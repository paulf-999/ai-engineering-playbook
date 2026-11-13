#!/bin/bash
# version: 1.5.1
# created: 2026-11-02
# updated: 2026-11-13
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Verify a PR that changes the installed Claude config under src/claude/ fills its "Plan Spec" section and answers
#              the evaluation criteria in an "Evaluation Criteria" section
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
# the heading of the section that carries the change's spec
SPEC_HEADING="Plan Spec"
# why the description fails, set in the main logic (empty means it's valid)
PROBLEMS=""

#=======================================================================
# Functions
#=======================================================================

# Print the description without fenced code blocks, so examples shown in them aren't checked
rendered_text() {
    printf '%s\n' "${PR_DESCRIPTION}" | awk '/^ *```/ { fenced = !fenced; next } !fenced'
}

# Print the lines under the first "## " heading that contains the given text, in any case, up to the next "## " heading
section() {
    rendered_text | awk -v heading="${1}" '
        /^## / { in_section = (index(tolower($0), tolower(heading)) > 0); next }
        in_section { print }
    '
}

# Succeed if the PR changes any file under src/claude/, the config that `make install` copies
changes_claude_config() {
    printf '%s\n' "${CHANGED_FILES}" | grep -qE '^src/claude/'
}

# Succeed if the "Evaluation Criteria" section has at least one top-level bullet or table body row
has_evaluation_criteria() {
    # a table's separator row, such as |---|---|, holds no answer, so it doesn't count
    section "Evaluation Criteria" | grep -E '^([-*] |\|)' | grep -qvE '^\|[-: |]+\|$'
}

# Succeed if the spec section has a line that isn't blank or part of the template's show/hide wrapper and info note
has_spec() {
    # shellcheck disable=SC2016  # the backticks are a literal grep pattern, not a command
    section "${SPEC_HEADING}" | grep -vE '^ *(</?(details|summary)>|> .*What is `spec\.md`)' \
        | grep -q '[^[:space:]]'
}

# Print each square-bracket placeholder left in the section whose heading contains $1, one per line
# inline code, links, checkboxes and alert markers such as [!TIP] are removed first, since they're real content
placeholders() {
    # shellcheck disable=SC2016  # the backticks are a literal sed pattern, not a command
    section "${1}" | sed -E 's/`[^`]*`//g; s/\[[^]]*\]\([^)]*\)//g; s/\[![A-Z]+\]//g; s/\[[ xX]\]//g' \
        | grep -oE '\[[^]]+\]' || true
}

# Explain each reason the description fails, or print nothing if it's fine
description_problems() {
    local placeholders
    changes_claude_config || return 0
    if ! has_spec; then
        echo "Fill the '${SPEC_HEADING}' section with the change's spec.md, or say why it has none, since this PR changes src/claude/."
    fi
    placeholders="$(placeholders "${SPEC_HEADING}")"
    if [[ -n "${placeholders}" ]]; then
        echo "Replace the template placeholders left in '${SPEC_HEADING}' with the change's spec: ${placeholders//$'\n'/, }"
    fi
    if ! has_evaluation_criteria; then
        echo "Answer the 'Evaluation Criteria' section with a Red flags, Shape and Working table, per docs/target_architecture/design_principles/02_evaluation_criteria.md, since this PR changes src/claude/."
    fi
    placeholders="$(placeholders "Evaluation Criteria")"
    if [[ -n "${placeholders}" ]]; then
        echo "Replace the template placeholders left in 'Evaluation Criteria' with real answers: ${placeholders//$'\n'/, }"
    fi
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

PROBLEMS="$(description_problems)"
if [[ -n "${PROBLEMS}" ]]; then
    print_section_header "${ERROR}" "ERROR: The PR description needs changes."
    printf '%s\n' "${PROBLEMS}"
    exit 1
fi
print_section_header "${INFO}" "SUCCESS: Valid PR description"

print_section_header "${DEBUG}" "Script execution completed." && echo
