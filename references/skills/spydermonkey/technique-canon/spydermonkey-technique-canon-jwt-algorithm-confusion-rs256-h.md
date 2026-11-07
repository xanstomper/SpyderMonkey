# JWT algorithm confusion (rs256 → hs256)

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

If the verification library accepts `alg` from the token, an rs256-signed scheme falls to hs256 with the public key as HMAC secret. Decisive test: sign a token with alg=hs256 using the fetched public key PEM as the secret, send it, and require a measurable behavioral delta (accepted vs 401) — token acceptance without privilege movement is a hypothesis, not a finding. Validation-only: a forged token is PROVEN but never used for access.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
