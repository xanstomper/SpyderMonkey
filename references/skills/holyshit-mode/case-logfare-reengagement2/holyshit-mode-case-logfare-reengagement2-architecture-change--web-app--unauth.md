# Architecture change since 2026-10-03 baseline — web-app / unauth

- source canon: `holyshit-mode/case-logfare-reengagement2.md`
- base technique: `holyshit-mode-case-logfare-reengagement2-architecture-change.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Main host is now server-rendered (no SPA bundle); auth moved to cookie sessions; signup gained a
**Discord-membership gate** ("Verify that you are in the Logfare Discord server") — the old
no-email signup is gone. `/migrate` flow for existing accounts.

## Probe adjustment (web-app × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
