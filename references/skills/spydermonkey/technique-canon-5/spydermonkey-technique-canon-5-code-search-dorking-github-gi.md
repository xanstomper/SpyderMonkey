# Code-search dorking (github/gitlab/gist)

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **WSTG-CONF-04** · **CWE-538** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Org-attribution via user-id chains (the SPY-067 class family), deleted-file recovery, committed secrets in value="" attributes, committed CSVs as QA telemetry. Decisive test: the recovered artifact itself (file/blob path) — the artifact is the evidence.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
