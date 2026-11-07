# Walls (validation-only, no exceptions) — windows / unauth

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-walls-validation-only-no-ex.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **windows** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Persistence is NEVER installed. Proof = the path exists (auth success, capability
  check, one read). A "takeover" that requires installing an implant to prove is not
  a takeover — it's an observation plus a plan; ship the plan.
- No destructive end-states, no data movement, no lateral damage. LOTL one-command
  reads only.
- External dangling-domain registration and third-party tenant app-install are
  third-party actions — operator-owned records/tenants only; everything else ships
  as documented feasibility.

## Probe adjustment (windows × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
