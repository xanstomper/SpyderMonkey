# Signature-verification gaps (server-trust asymmetry)

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

The SPY-101 family: mint endpoints open, verify endpoints gated — asymmetric hardening. Decisive test: mint without credentials vs verify's bean-validation — the asymmetry IS the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
