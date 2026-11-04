# Architecture change since 2026-10-03 baseline

- source canon: `holyshit-mode/case-logfare-reengagement2.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

Main host is now server-rendered (no SPA bundle); auth moved to cookie sessions; signup gained a
**Discord-membership gate** ("Verify that you are in the Logfare Discord server") — the old
no-email signup is gone. `/migrate` flow for existing accounts.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
