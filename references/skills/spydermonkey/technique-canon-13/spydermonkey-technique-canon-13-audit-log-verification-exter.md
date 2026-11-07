# Audit-log verification (external signal)

- source canon: `spydermonkey/technique-canon-13.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Missing log coverage inferred from unlogged test actions visible server-side — provable only from the operator's own visibility; characterize as hypothesis-grade from client-visible traces. Decisive test: none without operator logs — the honest ceiling row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
