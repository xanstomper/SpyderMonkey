# Discord OAuth Flow

- source canon: `holyshit-mode/case-logfare-ai.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- State cookie: HS256 JWT with `nonce` claim
- Purpose: `discord_signup`
- Expiry: 10 minutes
- redirect_uri: Hardcoded server-side
- alg:none attack: Rejected

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
