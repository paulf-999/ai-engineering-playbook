#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Install the repo's Claude config (src/claude/) into your Claude config directory, or uninstall it,
#              backing up each file it overwrites or removes and keeping your other settings
# Usage: [OPTION=value ...] src/sh/claude_install_config.sh, from the repo root (make install and make uninstall call it)
#        PROJECT=<repo>   use that repo's .claude/ folder instead, without preferences
#        HOOKS=1          with PROJECT, include the done checks and worktree edits hooks
#        PREFERENCES=0    leave out the rules in 02_preferences/ folders
#        UNINSTALL=1      remove what the last install added, restoring the files it replaced
#        YES=1            skip install's typed confirmation, but never from Claude Code
#        RENDER_PYTHON=   a Python that has Jinja, if not the repo's .venv

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/shell_utils.sh"
# shellcheck source=SCRIPTDIR/claude_install_config/_paths.sh
source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_paths.sh"
# shellcheck source=SCRIPTDIR/claude_install_config/_file_selection.sh
source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_file_selection.sh"
# shellcheck source=SCRIPTDIR/claude_install_config/_file_changes.sh
source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_file_changes.sh"
# shellcheck source=SCRIPTDIR/claude_install_config/_confirmation.sh
source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_confirmation.sh"
# shellcheck source=SCRIPTDIR/claude_install_config/_settings.sh
source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_settings.sh"

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

# no variables of its own, since _paths.sh sets them

#=======================================================================
# Functions
#=======================================================================

# Copy the config into the target, after a typed confirmation
run_install() {
    # Source: _settings.sh
    render_settings
    # Source: _file_selection.sh
    select_files
    # Source: _confirmation.sh
    confirm_install
    # Source: _file_changes.sh
    update_files
    # Source: _settings.sh
    register_settings
    # Source: this script
    file_plans
}

# Remove what the last install added, after a typed confirmation
run_uninstall() {
    # with no files to install or settings rendered, every file the manifest lists counts as removed, and no hook or deny
    # rule ships
    # Source: _file_selection.sh
    list_removed_files
    # Source: _confirmation.sh
    confirm_uninstall
    # Source: _file_changes.sh
    uninstall_files
    # Source: _settings.sh
    register_settings
    rm -f "${DENY_MANIFEST}"
}

# File saved plans by status and archive old drafts, which is a preference, so it's skipped with PREFERENCES=0 and in a project
file_plans() {
    [[ "${PREFERENCES}" == 1 ]] || return 0
    if ! python3 "$(dirname "${BASH_SOURCE[0]}")/../py/claude_manage_plans.py" clean --yes; then
        log_message "${WARNING}" "Saved plans weren't filed or drafts archived - run make clean_plans to see why."
    fi
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

if [[ "${UNINSTALL}" == 1 ]]; then run_uninstall; else run_install; fi

print_section_header "${DEBUG}" "Script execution completed." && echo
