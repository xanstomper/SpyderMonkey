# Report contract

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Every finding states: affected domain, asset, preconditions, exact minimal proof,
attacker gain, confidence, remediation, verification, and scope/decay notes. "Unknown"
is never silently converted into "safe".

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
