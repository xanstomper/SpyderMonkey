# Service-account token exposure

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

SA tokens in mounts/configmaps/logs readable from the confirmed foothold. Decisive test: token file readable in YOUR test pod/replica — the lab replica proves the class shape; live proof needs the foothold (kaisha-priced).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
