# JA3/JA4 client fingerprints (infra intel)

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Fingerprint the EGRESS the service expects vs accepts — anomalies map bot-walls and API tiers. Decisive test: same request two fingerprints — differential handling = the intel (register as recon, not vuln).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
