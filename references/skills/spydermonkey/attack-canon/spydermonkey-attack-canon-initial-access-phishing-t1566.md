# Initial Access Phishing (T1566)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: spearphish attachment/link into a user
- probe: LAB ONLY — the dojo replays the pattern; kage rules detect the trace
- wall: REFUSED live against real users, no exceptions

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
