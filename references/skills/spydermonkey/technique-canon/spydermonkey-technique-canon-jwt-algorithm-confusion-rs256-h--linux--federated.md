# JWT algorithm confusion (rs256 → hs256) — linux / federated

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-jwt-algorithm-confusion-rs256-h.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **linux** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

If the verification library accepts `alg` from the token, an rs256-signed scheme falls to hs256 with the public key as HMAC secret. Decisive test: sign a token with alg=hs256 using the fetched public key PEM as the secret, send it, and require a measurable behavioral delta (accepted vs 401) — token acceptance without privilege movement is a hypothesis, not a finding. Validation-only: a forged token is PROVEN but never used for access.

## Probe adjustment (linux × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
