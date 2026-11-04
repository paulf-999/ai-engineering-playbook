#!/bin/bash
# version: 1.2.0
# created: 2026-11-03
# updated: 2026-11-04
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Fail when the Claude context loaded into every session is estimated at over the token budget
# Usage: src/sh/claude_validate_always_on_budget.sh [directory to check, default .] (run from the repo root)

# Load reusable shell script vars & functions
source src/sh/shell_utils.sh

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

CHECK_DIR="${1:-.}"
# the token ceiling, set in docs/target_architecture/design_principles/01_principles.md; override via the ALWAYS_ON_TOKEN_BUDGET env var
TOKEN_BUDGET="${ALWAYS_ON_TOKEN_BUDGET:-3000}"
# the files Claude loads in every session, before any @-imports they pull in
CONTEXT_FILES=("CLAUDE.md" "src/claude/CLAUDE.md")
# the project config (.claude/) and the global config make install copies (src/claude/), which both load here
CONFIG_ROOTS=(".claude" "src/claude")
TOTAL_CHARS=0

#=======================================================================
# Functions
#=======================================================================

# Count characters rather than bytes, so an emoji counts once
use_utf8_locale() {
    local utf8_locale
    utf8_locale="$(locale -a 2>/dev/null | grep -iE '^(c|en_us)\.utf-?8$' | head -n 1 || true)"
    if [[ -n "${utf8_locale}" ]]; then
        export LC_ALL="${utf8_locale}"
    fi
}

# Normalise the budget to a whole number, or exit 1
validate_token_budget() {
    if ! TOKEN_BUDGET="$(to_whole_number "${TOKEN_BUDGET}")"; then
        print_section_header "${ERROR}" "ERROR: ALWAYS_ON_TOKEN_BUDGET must be a whole number of up to 9 digits, got '${ALWAYS_ON_TOKEN_BUDGET}'."
        exit 1
    fi
}

# Add a file's characters to the total and print its estimate
count_file() {
    local path="${1}" chars
    chars=$(wc -m < "${CHECK_DIR}/${path}" | tr -d ' ')
    TOTAL_CHARS=$((TOTAL_CHARS + chars))
    echo "  ~$((chars / 4)) tokens  ${path}"
}

# Count a context file and every repo file it imports with a line starting '@'
count_with_imports() {
    local path="${1}" import
    [[ -f "${CHECK_DIR}/${path}" ]] || return 0
    count_file "${path}"
    # imports from the home folder, such as @~/notes.md, aren't in the repo, so they can't be counted here
    while IFS= read -r import; do
        if [[ "${import}" == "~"* ]]; then
            log_message "${WARNING}" "Not counted: @${import}, which is outside the repo."
        elif [[ -f "${CHECK_DIR}/$(dirname "${path}")/${import}" ]]; then
            count_file "$(dirname "${path}")/${import}"
        fi
    done < <(sed -n 's/^@\([^[:space:]]*\).*/\1/p' "${CHECK_DIR}/${path}")
}

# Count every rule in each config root's rules/ that has no paths: setting, so loads in every session
count_always_on_rules() {
    local root
    for root in "${CONFIG_ROOTS[@]}"; do
        count_always_on_rules_in "${root}"
    done
}

# Count the always-on rules under one config root's rules/ folder
count_always_on_rules_in() {
    local rule root="${1}"
    [[ -d "${CHECK_DIR}/${root}/rules" ]] || return 0
    while IFS= read -r rule; do
        # a paths: line inside the opening --- block scopes the rule to matching files
        if ! awk 'NR == 1 && $0 != "---" { exit 1 } NR > 1 && $0 == "---" { exit 1 } /^paths:/ { found = 1 } END { exit !found }' "${CHECK_DIR}/${rule}"; then
            count_file "${rule}"
        fi
    # on-demand files kept in rules/_rules_lazy_load/ install beside rules/, so they don't load every session
    done < <(cd "${CHECK_DIR}" && find "${root}/rules" -path "${root}/rules/_rules_lazy_load" -prune -o -name '*.md' -print | sort)
}

# Print a file's description from its opening --- block, including one folded over several lines with > or |
description_text() {
    awk '
        NR == 1 && $0 != "---" { exit }
        NR > 1 && $0 == "---" { exit }
        # the indented lines under "description: >" or "description: |" are the text itself
        in_block && /^[[:space:]]/ { print; next }
        { in_block = 0 }
        /^description:/ {
            value = $0
            sub(/^description:[[:space:]]*/, "", value)
            if (value ~ /^[>|][-+]?[[:space:]]*$/) { in_block = 1 } else { print value }
        }
    ' "${1}"
}

# Count each skill's and agent's description, which Claude sees in every session so it can pick one
count_descriptions() {
    local file chars root
    for root in "${CONFIG_ROOTS[@]}"; do
        while IFS= read -r file; do
            chars=$(description_text "${CHECK_DIR}/${file}" | wc -m | tr -d ' ')
            TOTAL_CHARS=$((TOTAL_CHARS + chars))
            echo "  ~$((chars / 4)) tokens  ${file} (description)"
        # either folder may be missing, which mustn't stop the other being searched
        done < <(cd "${CHECK_DIR}" && { find "${root}/skills" -name 'SKILL.md' 2>/dev/null || true; find "${root}/agents" -name '*.md' 2>/dev/null || true; } | sort)
    done
}

# Compare the estimate with the budget, exiting 1 when it's over
check_budget() {
    local tokens=$((TOTAL_CHARS / 4))
    if [[ "${tokens}" -gt "${TOKEN_BUDGET}" ]]; then
        print_section_header "${ERROR}" "ERROR: always-on context is ~${tokens} tokens, over the ${TOKEN_BUDGET}-token budget."
        echo -e "Trim it, move detail to a file loaded on demand, or raise the budget in a PR that links logged evidence (see docs/target_architecture/target_architecture.md)."
        exit 1
    fi
    print_section_header "${INFO}" "SUCCESS: always-on context is ~${tokens} tokens, within the ${TOKEN_BUDGET}-token budget."
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

use_utf8_locale
validate_token_budget
log_message "${DEBUG_DETAILS}" "Estimated tokens, as characters ÷ 4:"
for context_file in "${CONTEXT_FILES[@]}"; do
    count_with_imports "${context_file}"
done
count_always_on_rules
count_descriptions
check_budget

print_section_header "${DEBUG}" "Script execution completed." && echo
