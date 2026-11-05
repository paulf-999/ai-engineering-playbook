#!/bin/bash
# version: 1.2.2
# created: 2026-11-02
# updated: 2026-11-05
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Verify a PR description stays scannable: at most 5 top-level bullets under "Additional Details", and only full links, since relative links break in a PR
# A PR that changes the installed Claude config under src/claude/ must also answer the evaluation criteria in an "Evaluation criteria" section
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
# most top-level bullets allowed under "Additional Details", matching the PR template
MAX_DETAIL_BULLETS=5
# why the description fails, set in the main logic (empty means it's valid)
PROBLEMS=""

#=======================================================================
# Functions
#=======================================================================

# Print the description without fenced code blocks, so examples shown in them aren't checked
rendered_text() {
    printf '%s\n' "${PR_DESCRIPTION}" | awk '/^ *```/ { fenced = !fenced; next } !fenced'
}

# Print the lines under the first "## " heading that contains the given text, up to the next "## " heading
section() {
    rendered_text | awk -v heading="${1}" '
        /^## / { in_section = (index($0, heading) > 0); next }
        in_section { print }
    '
}

# Print the lines under the "Additional Details" heading
details_section() {
    section "Additional Details"
}

# Count the top-level bullets in the "Additional Details" section, ignoring indented child bullets
count_detail_bullets() {
    details_section | grep -cE '^[-*] ' || true
}

# Print each link target that isn't a full URL or an in-page anchor, one per line
relative_links() {
    # inline code is removed too, so a link written as an example in backticks isn't flagged
    # shellcheck disable=SC2016  # the backticks are a literal sed pattern, not a command
    rendered_text | sed -E 's/`[^`]*`//g' | grep -oE '\]\([^)]+\)' | sed -E 's/^\]\((.*)\)$/\1/' \
        | grep -vE '^(https?://|#|mailto:)' || true
}

# Succeed if the PR changes any file under src/claude/, the config that `make install` copies
changes_claude_config() {
    printf '%s\n' "${CHANGED_FILES}" | grep -qE '^src/claude/'
}

# Succeed if the "Evaluation criteria" section has at least one top-level bullet or table body row
has_evaluation_criteria() {
    # a table's separator row, such as |---|---|, holds no answer, so it doesn't count
    section "Evaluation criteria" | grep -E '^([-*] |\|)' | grep -qvE '^\|[-: |]+\|$'
}

# Print each square-bracket placeholder left in the "Evaluation criteria" section, one per line
# inline code, links, checkboxes and alert markers such as [!TIP] are removed first, since they're real content
criteria_placeholders() {
    # shellcheck disable=SC2016  # the backticks are a literal sed pattern, not a command
    section "Evaluation criteria" | sed -E 's/`[^`]*`//g; s/\[[^]]*\]\([^)]*\)//g; s/\[![A-Z]+\]//g; s/\[[ xX]\]//g' \
        | grep -oE '\[[^]]+\]' || true
}

# Explain each reason the description fails, or print nothing if it's fine
description_problems() {
    local bullets links placeholders
    bullets="$(count_detail_bullets)"
    if (( bullets > MAX_DETAIL_BULLETS )); then
        echo "Cut 'Additional Details' to ${MAX_DETAIL_BULLETS} top-level bullets or fewer (it has ${bullets}), keeping only what a reviewer must or should know."
    fi
    if changes_claude_config && ! has_evaluation_criteria; then
        echo "Answer the 'Evaluation criteria' section with a Red flags, Shape and Working table, per docs/target_architecture/design_principles/02_evaluation_criteria.md, since this PR changes src/claude/."
    fi
    placeholders="$(criteria_placeholders)"
    if changes_claude_config && [[ -n "${placeholders}" ]]; then
        echo "Replace the template placeholders left in 'Evaluation criteria' with real answers: ${placeholders//$'\n'/, }"
    fi
    links="$(relative_links)"
    if [[ -n "${links}" ]]; then
        echo "Use full GitHub URLs, because relative links don't work in a PR description: ${links//$'\n'/, }"
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
