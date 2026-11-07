# IV reuse and nonce-counter classes

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Deterministic ciphertext prefixes across messages (ECB-class visual repetition) and IV/nonce reuse detectable from ciphertext pairs of YOUR OWN test material. Decisive test: two same-prefix plaintexts → ciphertext prefix delta (ECB) or equality (IV reuse).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
