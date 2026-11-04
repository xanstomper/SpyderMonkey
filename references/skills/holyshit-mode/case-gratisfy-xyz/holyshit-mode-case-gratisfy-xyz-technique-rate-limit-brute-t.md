# Technique: rate-limit brute test (reusable)

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## The technique

For any code-exchange/token endpoint: 15–20 rapid POSTs with garbage codes in a shell loop, collect `-w "%{http_code}"`. All 401/400 with zero 429 = brute surface open. Confirm uniform error strings (no oracle), note entropy/TTL as the unknown.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
