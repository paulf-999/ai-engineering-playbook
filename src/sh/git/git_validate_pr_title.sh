#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Verify a PR title follows Conventional Commits, using the commitlint version the commit-msg hook pins
# Usage: src/sh/git/git_validate_pr_title.sh <PR title>
#        (run from the repo root, so .pre-commit-config.yaml is found)

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/../shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/../shell_utils.sh"

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

# the PR title to check
PR_TITLE="${1:?Usage: git_validate_pr_title.sh <PR title>}"
# the hook config that pins the commitlint version
PRE_COMMIT_CONFIG=".pre-commit-config.yaml"

#=======================================================================
# Functions
#=======================================================================

# Print the commitlint config version the commit-msg hook pins
pinned_commitlint_version() {
    grep -oE '@commitlint/config-conventional@[0-9.]+' "${PRE_COMMIT_CONFIG}" | head -1 | cut -d@ -f3
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

VERSION="$(pinned_commitlint_version || true)"
if [[ -z "${VERSION}" ]]; then
    print_section_header "${ERROR}" "ERROR: no @commitlint/config-conventional version found in ${PRE_COMMIT_CONFIG}"
    exit 1
fi

# Squash merges use the PR title as the commit message on main, so check it as one
printf '%s\n' "${PR_TITLE}" | npx --yes -p "@commitlint/cli@${VERSION}" \
    -p "@commitlint/config-conventional@${VERSION}" commitlint --extends @commitlint/config-conventional
print_section_header "${INFO}" "SUCCESS: PR title follows Conventional Commits"

print_section_header "${DEBUG}" "Script execution completed." && echo
