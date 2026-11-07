# GCS anonymous and allUsers grants

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-CONF-04** · **CWE-732** · **ATT&CK T1530**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Public bucket/prefix listing; uniform-vs-legacy ACL gaps. Decisive test: anonymous listing request — one read-only probe.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
