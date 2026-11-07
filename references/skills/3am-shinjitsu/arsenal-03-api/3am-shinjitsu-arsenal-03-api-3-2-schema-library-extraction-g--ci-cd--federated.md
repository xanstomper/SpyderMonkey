# 3.2 Schema-library extraction → gate-order proof (score 90, no session needed) — ci-cd / federated

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-2-schema-library-extraction-g.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **ci-cd** · auth **federated** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- The bundle ships the server's zod/io-ts validation chunk: every param name, enum, refinement.
- Build COMPLETE valid shapes → fire the authz matrix → uniform "Invalid parameters" becomes
  explicit ("Not logged in") = validation runs BEFORE auth (gate-order proof).
- Trust vocabulary: `*_requested` naming + optional client fields (`userExpectedFeeCoins`) =
  server treats client figures as advisory. NO cross-user identifier in a shape = IDOR
  structurally impossible there — negative, ledger it.

## Probe adjustment (ci-cd × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
