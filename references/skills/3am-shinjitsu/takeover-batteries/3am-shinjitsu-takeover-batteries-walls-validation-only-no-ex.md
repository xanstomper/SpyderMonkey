# Walls (validation-only, no exceptions)

- source canon: `3am-shinjitsu/takeover-batteries.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Persistence is NEVER installed. Proof = the path exists (auth success, capability
  check, one read). A "takeover" that requires installing an implant to prove is not
  a takeover — it's an observation plus a plan; ship the plan.
- No destructive end-states, no data movement, no lateral damage. LOTL one-command
  reads only.
- External dangling-domain registration and third-party tenant app-install are
  third-party actions — operator-owned records/tenants only; everything else ships
  as documented feasibility.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
