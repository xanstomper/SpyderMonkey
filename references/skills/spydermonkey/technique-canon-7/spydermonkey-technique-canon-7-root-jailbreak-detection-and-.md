# Root/jailbreak detection and integrity checks (placement class)

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Client-only checks are the placement finding (canon-III); integrity attestation absence (no Play Integrity / DeviceCheck) is the posture row. Decisive test: manifest/API-analysis of your build — the absent attestation = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
