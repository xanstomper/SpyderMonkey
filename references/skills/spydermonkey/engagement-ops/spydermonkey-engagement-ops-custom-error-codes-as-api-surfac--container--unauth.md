# Custom error codes as API surface signals — container / unauth

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-custom-error-codes-as-api-surfac.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

A custom error code (e.g. HTTP 200 or 404 with JSON body: `code:1901, msg:"Oops, coco is gone!", data:{}`) is NOT a standard 404 — it means the route EXISTS on the server but is returning a specific application-level error instead of a generic HTTP code. This pattern reveals:

1. **Hidden API surface**: Every endpoint that returns a custom error code is a route that SHOULD exist, revealing the API design without requiring authentication.
2. **Error taxonomy**: The error code itself (1901 vs 4001 vs 6002) can be used for API fingerprinting and distinguishing between "route exists but needs auth" vs "route doesn't exist" vs "route exists but method wrong" (405).
3. **Intelligence value**: Capture the full error response in ledger findings. The error code is itself a finding — it reveals the API gateway's auth-swallow behavior.

Always differentiate: standard 404 (route doesn't exist) vs custom error code (route exists, gateway swallowing auth). The latter is a ledger-worthy finding.

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
