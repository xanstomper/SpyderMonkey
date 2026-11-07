# 4.9 Web3-wallet auth chain (score 75)

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Read the challenge SPEC from the bundle: flat `personal_sign` with NO timestamp/expiry/
  nonce-binding = replayable challenge (hypothesis ~65 until replay test on own wallet).
- Ephemeral keypair signup when the exchange is open = autonomous self-account (no identity
  fraud, shred the key from RAM after). State-cookie carrier (`state` cookie, never the
  `?state=` URL param — query_state mirror may be unread).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
