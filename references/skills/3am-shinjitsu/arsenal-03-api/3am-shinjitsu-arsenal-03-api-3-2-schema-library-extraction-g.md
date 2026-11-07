# 3.2 Schema-library extraction → gate-order proof (score 90, no session needed)

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- The bundle ships the server's zod/io-ts validation chunk: every param name, enum, refinement.
- Build COMPLETE valid shapes → fire the authz matrix → uniform "Invalid parameters" becomes
  explicit ("Not logged in") = validation runs BEFORE auth (gate-order proof).
- Trust vocabulary: `*_requested` naming + optional client fields (`userExpectedFeeCoins`) =
  server treats client figures as advisory. NO cross-user identifier in a shape = IDOR
  structurally impossible there — negative, ledger it.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
