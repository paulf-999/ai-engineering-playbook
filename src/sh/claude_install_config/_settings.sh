#!/bin/bash

# Description: Keep the config's hooks and deny rules in settings.json in step, keeping every other setting
# Usage: source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_settings.sh",
#        from claude_install_config.sh, which sets the paths and inputs these functions read

#=======================================================================
# Variables
#=======================================================================

# each hook the config ships, as event|matcher|path, with an empty matcher for events that take none,
# and a matcher may hold "|" itself, since only the first and last fields are split off
SHIPPED_HOOKS=(
    "PreToolUse|ExitPlanMode|hooks/ai_sdlc_workflow/hook_enforcement_plan_sections.sh"
    "PreToolUse|ExitPlanMode|hooks/ai_sdlc_workflow/hook_enforcement_plan_review.sh"
    "PreToolUse|Edit|Write|NotebookEdit|hooks/git/hook_enforcement_worktree_edits.sh"
    "Stop||hooks/ai_sdlc_workflow/hook_enforcement_done_checks.sh"
    "SessionStart||hooks/claude_kaizen/hook_reminder_kaizen_due.sh"
)
# deny rules that keep Claude's file tools out of .env files, kept last in this order so the carve-out follows its rule
# a bare filename matches at any depth, and a "!" rule carves out of earlier rules in the same settings file, per
# https://code.claude.com/docs/en/permissions.md
DENY_RULES=("Read(.env)" "Read(.env.*)" "Read(!.env.example)")
# settings.json's content, set by read_settings and changed by the merges
SETTINGS_JSON=""

#=======================================================================
# Functions
#=======================================================================

# Keep one entry per hook in settings.json at the current path, or none if it isn't shipped, then the deny rules
register_settings() {
    local current
    # bash ignores set -e inside these three, so each returns 1 itself once it has said why it can't go on
    read_settings || return 0
    current="${SETTINGS_JSON}"
    merge_hooks || return 0
    merge_deny_rules || return 0
    jq -cn '$ARGS.positional' --args ${DENY_RULES[@]+"${DENY_RULES[@]}"} > "${DENY_MANIFEST}"
    [[ "${SETTINGS_JSON}" == "${current}" ]] && return 0
    if file_exists "${SETTINGS}"; then back_up_file "${BACKUP_DIR}" settings.json; fi
    write_settings
    log_message "${INFO}" "Updated the config's hooks and deny rules in ${SETTINGS}."
}

# Set SETTINGS_JSON to what settings.json holds, failing if jq is missing or can't read it, so it's left alone
read_settings() {
    SETTINGS_JSON="{}"
    if ! command -v jq > /dev/null; then
        log_message "${WARNING}" "jq isn't installed, so the config's hooks weren't added to ${SETTINGS}."
        return 1
    fi
    if file_exists "${SETTINGS}" && ! SETTINGS_JSON="$(jq '.' "${SETTINGS}" 2> /dev/null)"; then
        log_message "${WARNING}" "${SETTINGS} isn't valid JSON, so the config's hooks weren't added."
        return 1
    fi
}

# Merge each hook the config ships into SETTINGS_JSON
merge_hooks() {
    local entry event matcher hook ship command status
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
        # the plan review takes seconds, so Claude Code shows this while it runs
        status=""
        [[ "${hook##*/}" == hook_enforcement_plan_review.sh ]] && status="Reviewing plan against quality gates"
        if ! merge_hook "${event}" "${matcher}" "${command}" "/${hook##*/}\"" "${ship}" "${status}"; then
            log_message "${WARNING}" "${SETTINGS} has a hooks.${event} that isn't a list, so the hooks weren't added."
            return 1
        fi
    done
}

# Merge one hook into SETTINGS_JSON: strip it wherever it's registered, matched by file name so an old path counts, then
# re-add it if shipped, failing if the event's value isn't a list, so can't take the hook
# the command is an absolute path, since hook commands in user settings can't refer to CLAUDE_CONFIG_DIR
merge_hook() {
    SETTINGS_JSON="$(jq --arg event "${1}" --arg matcher "${2}" --arg command "${3}" --arg suffix "${4}" \
        --argjson ship "${5}" --arg status "${6}" '
        def ours: (.command? // "") as $c | ($c | type) == "string" and ($c | endswith($suffix));
        (.hooks[$event] // []) as $old
        | if ($old | type) != "array" then error("hooks.\($event) is not a list") else . end
        | ($old
            | map(if (.hooks? | type) == "array" and any(.hooks[]; ours)
                then .hooks |= map(select(ours | not)) | select(.hooks != [])
                else . end)
            | . + (if $ship
                then [(if $matcher == "" then {} else {matcher: $matcher} end)
                    + {hooks: [{type: "command", command: $command}
                        + (if $status == "" then {} else {statusMessage: $status} end)]}]
                else [] end)
          ) as $new
        | if $new == $old then . else .hooks[$event] = $new end' <<< "${SETTINGS_JSON}" 2> /dev/null)"
}

# Drop the deny rules the last install added from SETTINGS_JSON, then put the config's at the end, in order, keeping
# every other rule
merge_deny_rules() {
    local previous
    # an unreadable deny manifest counts as empty, so install still adds the current rules
    previous="$(jq -c 'if type == "array" then . else [] end' "${DENY_MANIFEST}" 2> /dev/null || echo "[]")"
    if ! SETTINGS_JSON="$(jq --argjson previous "${previous}" --args '
        (.permissions.deny // []) as $old
        | if ($old | type) != "array" then error("permissions.deny is not a list") else . end
        | ($previous + $ARGS.positional) as $ours
        | ($old | map(select(. as $rule | $ours | index($rule) | not)) + $ARGS.positional) as $new
        | if $new == $old then . else .permissions.deny = $new end' \
        ${DENY_RULES[@]+"${DENY_RULES[@]}"} <<< "${SETTINGS_JSON}" 2> /dev/null)"; then
        log_message "${WARNING}" "${SETTINGS} has a permissions.deny that isn't a list, so the settings weren't added."
        return 1
    fi
}

# Write SETTINGS_JSON to settings.json, keeping its mode and any symlink, through a temporary file that's then moved, so
# a failed write can't leave it half written
write_settings() {
    local path="${SETTINGS}" mode
    if [[ -L "${path}" ]]; then path="$(readlink -f "${path}")"; fi
    if file_exists "${path}"; then
        # GNU stat, then macOS's
        mode="$(stat -c %a "${path}" 2> /dev/null || stat -f %Lp "${path}")"
        # settings can hold secrets, so the temporary file starts out private
        (umask 077 && printf '%s\n' "${SETTINGS_JSON}" > "${path}.tmp")
        chmod "${mode}" "${path}.tmp"
    else
        printf '%s\n' "${SETTINGS_JSON}" > "${path}.tmp"
    fi
    mv "${path}.tmp" "${path}"
}
