# Hypothesis-vs-CONFIRMED grading

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

No baseline/attack/diff = HYPOTHESIS conf 0.4, never suppressed, never CONFIRMED. Decisive test: the row's status field matches the evidence it carries — the grading integrity check.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
