#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Fail a PR that changes a skill's files without bumping the version in its skill.contract.yaml
# Usage: src/sh/git/git_validate_skill_versions.sh <base ref> [head ref]
#        (head ref defaults to HEAD; run from the repo root)

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/../shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/../shell_utils.sh"

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

BASE_REF="${1:?Required: base ref to compare against (arg 1)}"
HEAD_REF="${2:-HEAD}"

#=======================================================================
# Functions
#=======================================================================

# Print the version line of the contract at path $2 in ref $1, or nothing when it doesn't exist there
contract_version() {
    git show "${1}:${2}" 2> /dev/null | grep -m 1 '^version:' || true
}

# List each skill folder, as src/claude/skills/<group>/<skill>, that has a file changed since the branch left the base
changed_skills() {
    git diff --name-only "${BASE_REF}...${HEAD_REF}" -- src/claude/skills \
        | awk -F/ 'NF > 5 { print $1 "/" $2 "/" $3 "/" $4 "/" $5 }' | sort -u
}

# Exit 1, naming each existing skill that changed while its contract version stayed the same
check_versions() {
    local skill contract base_version stale=()
    while read -r skill; do
        [[ -n "${skill}" ]] || continue
        contract="${skill}/skill.contract.yaml"
        base_version="$(contract_version "$(git merge-base "${BASE_REF}" "${HEAD_REF}")" "${contract}")"
        # a skill new in this PR, or one it deletes, has no earlier version to compare
        [[ -n "${base_version}" ]] || continue
        [[ "$(contract_version "${HEAD_REF}" "${contract}")" == "${base_version}" ]] && stale+=("${skill##*/}")
    done <<< "$(changed_skills)"
    if [[ "${#stale[@]}" -gt 0 ]]; then
        print_section_header "${ERROR}" "ERROR: these skills changed without a version bump in skill.contract.yaml: ${stale[*]}."
        echo -e "Bump each one's version, such as 1.1.0 to 1.2.0 for a behaviour change, or 1.1.1 for a fix."
        exit 1
    fi
    print_section_header "${INFO}" "SUCCESS: every changed skill has a new contract version."
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

check_versions

print_section_header "${DEBUG}" "Script execution completed." && echo
