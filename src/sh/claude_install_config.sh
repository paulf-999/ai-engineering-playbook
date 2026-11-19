#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Copy the repo's Claude config (src/claude/) into your Claude config directory, backing up each file it overwrites
#              On-demand files in rules/on_demand/ go beside rules/, since Claude Code loads everything under rules/
#              A manifest records what was installed, so files the repo has since removed are backed up and removed,
#              along with any folder that leaves empty
#              It also keeps the config's hooks and deny rules in settings.json in step, keeping every other setting
#              With PROJECT set, it installs into that repo's .claude/ folder instead, leaving the done checks and worktree edits hooks out unless HOOKS=1
#              With UNINSTALL=1, it removes what the manifest lists, restores each file's pre-install backup and strips
#              the config's hooks and deny rules from settings.json
#              With YES=1, install skips the typed confirmation for provisioning scripts, but never from Claude Code
#              It adds the rules in 02_preferences/ folders unless PREFERENCES=0, but never into a PROJECT install
#              It never installs the skill, agent and rule templates, which are for authoring in this repo
# Usage: [PROJECT=<repo> [HOOKS=1]] [PREFERENCES=0|1] [UNINSTALL=1 | YES=1] src/sh/claude_install_config.sh (run from the repo root, at
#        your own terminal or in a provisioning script; make install and make uninstall call it)

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/shell_utils.sh"

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

# mirrors the config directory's layout, so each file is copied to the same relative path, except on-demand files
SOURCE_DIR="src/claude"
LAZY_RULES_DIR="rules/on_demand"
CONFIG_DIR="${CLAUDE_CONFIG_DIR:-${HOME}/.claude}"
# a repo to install into instead of your Claude config directory, and whether its install includes the done checks hook
PROJECT="${PROJECT:-}"
WITH_HOOKS="${HOOKS:-}"
UNINSTALL="${UNINSTALL:-}"
# skips install's typed confirmation, for devcontainers and onboarding scripts that have no terminal
ASSUME_YES="${YES:-}"
# 0 leaves out the rules in 02_preferences/ folders, one person's taste, which otherwise install everywhere but a project
PREFERENCES="${PREFERENCES:-}"
# authoring templates that never install
AUTHORING_TEMPLATES=" _templates/AGENT.md.template _templates/rule.md.template "
if [[ -n "${PROJECT}" ]]; then
    if [[ ! -d "${PROJECT}" ]]; then
        echo "PROJECT=${PROJECT} isn't a folder - nothing changed." >&2
        exit 1
    fi
    PROJECT="$(cd "${PROJECT}" && pwd)"
    TARGET_DIR="${PROJECT}/.claude"
    # backups go in your own config directory, so they're never committed with the repo
    BACKUP_PREFIX="${CONFIG_DIR}/backups/project_$(basename "${PROJECT}")_"
else
    TARGET_DIR="${CONFIG_DIR}"
    BACKUP_PREFIX="${TARGET_DIR}/backups/install_"
fi
# what a project install says about preferences, which only go into your own config
PROJECT_PREFERENCES_NOTE="Preferences don't install into a project; add them to your own config with make install"
# each install's backups start with BACKUP_PREFIX then the date, so uninstall can find the oldest copy of each file
BACKUP_DIR="${BACKUP_PREFIX}$(date +%Y_%m_%d_%H%M%S)"
[[ "${UNINSTALL}" == 1 ]] && BACKUP_DIR="${BACKUP_PREFIX}uninstall_$(date +%Y_%m_%d_%H%M%S)"
# where an install backs up a copy an earlier install wrote, which uninstall never restores, since it isn't the user's
UPGRADE_BACKUP_DIR="${BACKUP_PREFIX}upgrade_$(date +%Y_%m_%d_%H%M%S)"
# the paths the last install wrote, one per line, so the next install can remove any the repo no longer has
MANIFEST="${TARGET_DIR}/.playbook_install_manifest"
# the tracked files under SOURCE_DIR, set by list_source_files
SOURCE_FILES=()
# where each source file installs, one per line, set by list_source_files
TARGET_PATHS=""
# files the last install wrote that the repo no longer has, set by list_removed_files
REMOVED_FILES=()
# settings.json holds personal settings, so install merges the hooks into it rather than copying a file over it
SETTINGS="${TARGET_DIR}/settings.json"
# each hook the config ships, as event|matcher|path, with an empty matcher for events that take none,
# and a matcher may hold "|" itself, since only the first and last fields are split off
SHIPPED_HOOKS=(
    "PreToolUse|ExitPlanMode|hooks/hook_enforcement_plan_sections.sh"
    "PreToolUse|Edit|Write|NotebookEdit|hooks/hook_enforcement_worktree_edits.sh"
    "Stop||hooks/hook_enforcement_done_checks.sh"
)
# deny rules that keep Claude's file tools out of .env files, kept last in this order so the carve-out follows its rule
# a bare filename matches at any depth, and a "!" rule carves out of earlier rules in the same settings file, per
# https://code.claude.com/docs/en/permissions.md
DENY_RULES=("Read(.env)" "Read(.env.*)" "Read(!.env.example)")
# the deny rules the last install added, as a JSON list, so the next install can remove any the config has since dropped
DENY_MANIFEST="${TARGET_DIR}/.playbook_install_deny_rules"

#=======================================================================
# Functions
#=======================================================================

# Print where a source file installs: on-demand files move from rules/on_demand/ to on_demand/,
# and a skill in a group folder such as skills/_git_skills/ installs flat under skills/, where Claude Code finds it
target_path() {
    local file="${1}"
    if [[ "${file}" == "${LAZY_RULES_DIR}/"* ]]; then
        echo "${file#rules/}"
    elif [[ "${file}" =~ ^skills/_[^/]+/(.+/.+)$ ]]; then
        echo "skills/${BASH_REMATCH[1]}"
    else
        echo "${file}"
    fi
}

# Print a source file as it installs: in a project, pointers name the project's .claude/ folder, not your config directory
render() {
    render_text < "${SOURCE_DIR}/${1}"
}

# Print text from stdin as it installs, so a past version of a file can be compared with what an install wrote
render_text() {
    if [[ -n "${PROJECT}" ]]; then
        # shellcheck disable=SC2016  # the backticks and \$CLAUDE_CONFIG_DIR are literal text in the rules, not expansions
        sed -e 's/in your Claude config directory (`$CLAUDE_CONFIG_DIR`, or `~\/.claude` when unset)/in this project'"'"'s `.claude\/` folder/' \
            -e 's/in your Claude config directory/in this project'"'"'s `.claude\/` folder/'
    else
        cat
    fi
}

# Print where to back up an installed path: the upgrade folder for a copy an earlier install wrote, else the usual one
backup_dir_for() {
    if file_exists "${MANIFEST}" && grep -Fxq -- "${1}" "${MANIFEST}"; then
        echo "${UPGRADE_BACKUP_DIR}"
    else
        echo "${BACKUP_DIR}"
    fi
}

# Collect the files git tracks under SOURCE_DIR, so untracked drafts and caches are never installed,
# leaving the done checks and worktree edits hooks out of a project install unless HOOKS=1, while the plan sections hook
# always installs
list_source_files() {
    local file
    while IFS= read -r -d '' file; do
        file="${file#"${SOURCE_DIR}"/}"
        [[ -n "${PROJECT}" && "${WITH_HOOKS}" != 1 && "${file}" =~ ^hooks/hook_enforcement_(done_checks|worktree_edits)\.sh$ ]] \
            && continue
        [[ "${PREFERENCES}" != 1 && ( "/${file}" == */preferences/* || "/${file}" == */02_preferences/* ) ]] && continue
        [[ "${AUTHORING_TEMPLATES}" == *" ${file} "* || "${file}" == _templates/skills/* ]] && continue
        # a README explains a folder to people browsing the repo, and never loads
        [[ "${file##*/}" == README.md ]] && continue
        # a skill group's own files, such as its README, describe the group, which doesn't exist once installed flat
        [[ "${file}" =~ ^skills/_[^/]+/[^/]+$ ]] && continue
        SOURCE_FILES+=("${file}")
        TARGET_PATHS+="$(target_path "${file}")"$'\n'
    done < <(git ls-files -z -- "${SOURCE_DIR}")
    if [[ "${#SOURCE_FILES[@]}" -eq 0 ]]; then
        log_message "${ERROR}" "No tracked files found under ${SOURCE_DIR} - nothing to install."
        exit 1
    fi
}

# Settle PREFERENCES: an explicit 0 or 1 wins, otherwise preferences install,
# except into a project, which never gets them, since its .claude/ folder is shared
resolve_preferences() {
    if [[ -n "${STYLE:-}" ]]; then
        log_message "${WARNING}" "STYLE is gone: the reply format is a preference, left out with PREFERENCES=0, and the writing-style rule always installs."
    fi
    case "${PREFERENCES}" in
        0 | 1) ;;
        "")
            PREFERENCES=1
            [[ -n "${PROJECT}" ]] && PREFERENCES=0
            ;;
        *)
            log_message "${ERROR}" "PREFERENCES must be 0 or 1, not '${PREFERENCES}' - nothing changed."
            exit 1
            ;;
    esac
    if [[ -n "${PROJECT}" && "${PREFERENCES}" == 1 ]]; then
        log_message "${ERROR}" "${PROJECT_PREFERENCES_NOTE} - nothing changed."
        exit 1
    fi
}

# Succeed if an installed path is a preference
is_preference() {
    [[ "/${1}" == */preferences/* || "/${1}" == */02_preferences/* ]]
}

# Remove the folders that removing REMOVED_FILES left empty, walking up from each file, so other empty folders stay
remove_emptied_folders() {
    local file folder
    for file in "${REMOVED_FILES[@]+"${REMOVED_FILES[@]}"}"; do
        folder="$(dirname "${file}")"
        # rmdir only removes an empty folder, so the walk stops at the first one that still holds something
        while [[ "${folder}" != "." ]] && rmdir "${TARGET_DIR}/${folder}" 2> /dev/null; do
            folder="$(dirname "${folder}")"
        done
    done
    return 0
}

# Collect the manifest's paths that are no longer installed, skipping any path that could point outside the target
list_removed_files() {
    local path
    file_exists "${MANIFEST}" || return 0
    while IFS= read -r path; do
        [[ -n "${path}" && "${path}" != /* && "${path}" != *..* ]] || continue
        if ! grep -Fxq -- "${path}" <<< "${TARGET_PATHS}" && file_exists "${TARGET_DIR}/${path}"; then
            REMOVED_FILES+=("${path}")
        fi
    done < "${MANIFEST}"
}

# Say how to keep the preferences an install is removing, if it's removing any
print_opt_in_note() {
    local file
    [[ "${PREFERENCES}" == 1 ]] && return 0
    for file in "${REMOVED_FILES[@]}"; do
        if is_preference "${file}"; then
            if [[ -n "${PROJECT}" ]]; then
                log_message "${WARNING}" "${PROJECT_PREFERENCES_NOTE}."
            else
                log_message "${WARNING}" "PREFERENCES=0 removes the preferences: rerun with a plain make install to keep them."
            fi
            return 0
        fi
    done
}

# Show what will change and require 'install' typed at a real terminal, so Claude's Bash tool can't run it unattended,
# unless YES=1 opts out outside Claude Code, which sets CLAUDECODE in its Bash tool
confirm_install() {
    local answer file
    if [[ "${ASSUME_YES}" == 1 && -n "${CLAUDECODE:-}" ]]; then
        log_message "${ERROR}" "YES=1 can't be used from Claude Code - run make install from your own terminal."
        exit 1
    fi
    if [[ "${ASSUME_YES}" != 1 && ! -t 0 ]]; then
        log_message "${ERROR}" "Run make install from your own terminal - nothing changed."
        exit 1
    fi
    log_message "${INFO}" "Installing ${#SOURCE_FILES[@]} file(s) into ${TARGET_DIR}."
    if [[ "${#REMOVED_FILES[@]}" -gt 0 ]]; then
        log_message "${WARNING}" "Removing ${#REMOVED_FILES[@]} file(s) an earlier install added:"
        for file in "${REMOVED_FILES[@]}"; do
            if [[ "${PREFERENCES}" != 1 ]] && is_preference "${file}"; then
                echo "  ${file} (holds preferences, left out)"
            else
                echo "  ${file} (no longer in the repo)"
            fi
        done
        print_opt_in_note
    fi
    echo
    echo "It also updates settings.json, backing up anything it changes to $(dirname "${BACKUP_DIR}")."
    [[ "${ASSUME_YES}" == 1 ]] && return 0
    echo
    read -r -p "$(echo -e "${DEBUG}Type 'install' to continue:${COLOUR_OFF} ")" answer || true
    if [[ "${answer}" != "install" ]]; then
        log_message "${WARNING}" "Install cancelled - nothing changed."
        exit 1
    fi
}

# Show what uninstall removes and require 'uninstall' typed at a real terminal, as confirm_install does
confirm_uninstall() {
    local answer file
    if [[ ! -t 0 ]]; then
        log_message "${ERROR}" "Run make uninstall from your own terminal - nothing changed."
        exit 1
    fi
    if [[ "${#REMOVED_FILES[@]}" -eq 0 ]]; then
        log_message "${WARNING}" "No install manifest lists files in ${TARGET_DIR} - nothing to uninstall."
        exit 1
    fi
    log_message "${WARNING}" "Removing ${#REMOVED_FILES[@]} file(s) the last install added to ${TARGET_DIR}:"
    for file in "${REMOVED_FILES[@]}"; do
        echo "  ${file}"
    done
    echo "Each is backed up to ${BACKUP_DIR} first, and any file an install replaced is restored from its oldest backup."
    echo "It also removes the config's hooks and deny rules from ${SETTINGS}, keeping every other setting."
    read -r -p "Type 'uninstall' to continue: " answer || true
    if [[ "${answer}" != "uninstall" ]]; then
        log_message "${WARNING}" "Uninstall cancelled - nothing changed."
        exit 1
    fi
}

# Back up and remove each installed file, restoring its oldest backup, which holds the user's own file,
# since an upgrade backs up the playbook's own previous version to the upgrade folder instead
uninstall_files() {
    local file original restored=0
    for file in "${REMOVED_FILES[@]}"; do
        mkdir -p "$(dirname "${BACKUP_DIR}/${file}")"
        cp -p "${TARGET_DIR}/${file}" "${BACKUP_DIR}/${file}"
        rm "${TARGET_DIR}/${file}"
        # the glob expands in date order, and the leading digit skips uninstall backups
        for original in "${BACKUP_PREFIX}"[0-9]*/"${file}"; do
            if file_exists "${original}"; then
                cp -p "${original}" "${TARGET_DIR}/${file}"
                restored=$((restored + 1))
                break
            fi
        done
    done
    rm -f "${MANIFEST}"
    remove_emptied_folders
    log_message "${INFO}" "Removed ${#REMOVED_FILES[@]} file(s), restoring ${restored} from backups."
}

# Copy each file over the target, backing up any existing copy that differs, and skipping identical ones
install_files() {
    local file relative target backup_dir copied=0 backed_up=0
    for file in "${SOURCE_FILES[@]}"; do
        relative="$(target_path "${file}")"
        target="${TARGET_DIR}/${relative}"
        if file_exists "${target}" && cmp -s <(render "${file}") "${target}"; then
            continue
        fi
        if file_exists "${target}"; then
            backup_dir="$(backup_dir_for "${relative}")"
            mkdir -p "$(dirname "${backup_dir}/${relative}")"
            cp -p "${target}" "${backup_dir}/${relative}"
            backed_up=$((backed_up + 1))
        fi
        mkdir -p "$(dirname "${target}")"
        render "${file}" > "${target}"
        copied=$((copied + 1))
    done
    log_message "${INFO}" "Installed ${copied} changed file(s), backing up ${backed_up}, into ${TARGET_DIR}."
}

# Back up and remove each file the repo no longer has, then record what this install wrote
remove_old_files() {
    local file
    # each removed file is one the manifest lists, so an earlier install wrote it
    for file in "${REMOVED_FILES[@]+"${REMOVED_FILES[@]}"}"; do
        mkdir -p "$(dirname "${UPGRADE_BACKUP_DIR}/${file}")"
        cp -p "${TARGET_DIR}/${file}" "${UPGRADE_BACKUP_DIR}/${file}"
        rm "${TARGET_DIR}/${file}"
    done
    remove_emptied_folders
    log_message "${INFO}" "Removed ${#REMOVED_FILES[@]} file(s) an earlier install added." false
    printf '%s' "${TARGET_PATHS}" > "${MANIFEST}"
}

# Keep one entry per hook in settings.json at the current path, or none if it isn't shipped, then the deny rules,
# backing up the old file
register_settings() {
    local current updated entry event matcher hook ship previous command
    if ! command -v jq > /dev/null; then
        log_message "${WARNING}" "jq isn't installed, so the config's hooks weren't added to ${SETTINGS}."
        return 0
    fi
    current="{}"
    # a settings file jq can't read is left alone, rather than replaced
    if file_exists "${SETTINGS}" && ! current="$(jq '.' "${SETTINGS}" 2> /dev/null)"; then
        log_message "${WARNING}" "${SETTINGS} isn't valid JSON, so the config's hooks weren't added."
        return 0
    fi
    updated="${current}"
    for entry in "${SHIPPED_HOOKS[@]}"; do
        event="${entry%%|*}"
        hook="${entry##*|}"
        matcher="${entry#*|}"
        matcher="${matcher%|*}"
        ship=false
        grep -Fxq -- "${hook}" <<< "${TARGET_PATHS}" && ship=true
        # a project's settings are shared, so its hook command names the project through Claude Code's own variable
        command="bash \"${TARGET_DIR}/${hook}\""
        [[ -n "${PROJECT}" ]] && command="bash \"\$CLAUDE_PROJECT_DIR/.claude/${hook}\""
        # strip the hook wherever it's registered, matched by file name so an old path counts, then re-add it if shipped
        # an event value that isn't a list can't take the hook, so it's reported rather than aborting the install
        # the command is an absolute path, since hook commands in user settings can't refer to CLAUDE_CONFIG_DIR
        if ! updated="$(jq --arg event "${event}" --arg matcher "${matcher}" \
            --arg command "${command}" --arg suffix "/${hook}\"" --argjson ship "${ship}" '
            def ours: (.command? // "") as $c | ($c | type) == "string" and ($c | endswith($suffix));
            (.hooks[$event] // []) as $old
            | if ($old | type) != "array" then error("hooks.\($event) is not a list") else . end
            | ($old
                | map(if (.hooks? | type) == "array" and any(.hooks[]; ours)
                    then .hooks |= map(select(ours | not)) | select(.hooks != [])
                    else . end)
                | . + (if $ship
                    then [(if $matcher == "" then {} else {matcher: $matcher} end)
                        + {hooks: [{type: "command", command: $command}]}]
                    else [] end)
              ) as $new
            | if $new == $old then . else .hooks[$event] = $new end' <<< "${updated}" 2> /dev/null)"; then
            log_message "${WARNING}" "${SETTINGS} has a hooks.${event} that isn't a list, so the hooks weren't added."
            return 0
        fi
    done
    # an unreadable deny manifest counts as empty, so install still adds the current rules
    previous="$(jq -c 'if type == "array" then . else [] end' "${DENY_MANIFEST}" 2> /dev/null || echo "[]")"
    # drop the rules the last install added, then put the config's rules at the end, in order, keeping every other rule
    if ! updated="$(jq --argjson previous "${previous}" --args '
        (.permissions.deny // []) as $old
        | if ($old | type) != "array" then error("permissions.deny is not a list") else . end
        | ($previous + $ARGS.positional) as $ours
        | ($old | map(select(. as $rule | $ours | index($rule) | not)) + $ARGS.positional) as $new
        | if $new == $old then . else .permissions.deny = $new end' ${DENY_RULES[@]+"${DENY_RULES[@]}"} <<< "${updated}" 2> /dev/null)"; then
        log_message "${WARNING}" "${SETTINGS} has a permissions.deny that isn't a list, so the settings weren't added."
        return 0
    fi
    jq -cn '$ARGS.positional' --args ${DENY_RULES[@]+"${DENY_RULES[@]}"} > "${DENY_MANIFEST}"
    [[ "${updated}" == "${current}" ]] && return 0
    if file_exists "${SETTINGS}"; then
        mkdir -p "${BACKUP_DIR}"
        cp -p "${SETTINGS}" "${BACKUP_DIR}/settings.json"
    fi
    # write a temporary file, then move it, so a failed write can't leave settings.json half written
    printf '%s\n' "${updated}" > "${SETTINGS}.tmp"
    mv "${SETTINGS}.tmp" "${SETTINGS}"
    log_message "${INFO}" "Updated the config's hooks and deny rules in ${SETTINGS}."
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

if [[ "${UNINSTALL}" == 1 ]]; then
    # with no files to install, every file the manifest lists counts as removed, and no hook or deny rule ships
    DENY_RULES=()
    list_removed_files
    confirm_uninstall
    uninstall_files
    register_settings
    rm -f "${DENY_MANIFEST}"
else
    resolve_preferences
    list_source_files
    list_removed_files
    confirm_install
    install_files
    remove_old_files
    register_settings
fi

print_section_header "${DEBUG}" "Script execution completed." && echo
