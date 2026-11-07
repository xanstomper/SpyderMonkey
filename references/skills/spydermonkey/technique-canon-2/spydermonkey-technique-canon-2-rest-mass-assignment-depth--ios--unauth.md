# REST mass assignment depth — ios / unauth

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-rest-mass-assignment-depth.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- context: **ios** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Role/entitlement fields beyond the obvious (`role`, `tenantId`, `isStaff`, `quota`) re-bound on PUT/PATCH. Decisive test: unknown-field probe (send one invented field + one plausible) — echoed/persisted = the class; persisted-and-effectful = the crown (your own principal only).

## Probe adjustment (ios × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
