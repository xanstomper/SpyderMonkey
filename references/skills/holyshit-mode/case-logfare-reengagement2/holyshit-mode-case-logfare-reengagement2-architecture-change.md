# Architecture change since 2026-10-03 baseline

- source canon: `holyshit-mode/case-logfare-reengagement2.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Main host is now server-rendered (no SPA bundle); auth moved to cookie sessions; signup gained a
**Discord-membership gate** ("Verify that you are in the Logfare Discord server") — the old
no-email signup is gone. `/migrate` flow for existing accounts.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
