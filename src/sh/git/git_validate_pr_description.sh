#!/bin/bash
# version: 1.0.0
# created: 2026-11-02
# updated: 2026-11-02
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Verify a PR description stays scannable: at most 5 top-level bullets under "Additional Details", and only full links, since relative links break in a PR
# Usage: src/sh/git/git_validate_pr_description.sh "<pr description>" (run from the repo root)

# Load reusable shell script vars & functions
source src/sh/shell_utils.sh

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

PR_DESCRIPTION="${1-}"
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

# Print the lines under the "Additional Details" heading, up to the next "## " heading
details_section() {
    rendered_text | awk '
        /^## / { in_details = ($0 ~ /Additional Details/); next }
        in_details { print }
    '
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

# Explain each reason the description fails, or print nothing if it's fine
description_problems() {
    local bullets links
    bullets="$(count_detail_bullets)"
    if (( bullets > MAX_DETAIL_BULLETS )); then
        echo "Cut 'Additional Details' to ${MAX_DETAIL_BULLETS} top-level bullets or fewer (it has ${bullets}), keeping only what a reviewer must or should know."
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
