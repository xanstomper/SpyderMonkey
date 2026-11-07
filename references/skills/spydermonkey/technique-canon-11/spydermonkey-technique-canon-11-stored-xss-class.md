# Stored-XSS class

- source canon: `spydermonkey/technique-canon-11.md`
- bindings: **WSTG-INPV-02** · **CWE-79** · **ATT&CK T1189**
- generated: 2026-11-07

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Persistent payloads in your own objects rendering for OTHER principals — needs two principals (the two-role context rule). Decisive test: your own second account renders it = confirmed; single-principal = hypothesis.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
