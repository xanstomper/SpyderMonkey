# Technique: rate-limit brute test (reusable) — mobile-api / federated

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-technique-rate-limit-brute-t.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **mobile-api** · auth **federated** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

For any code-exchange/token endpoint: 15–20 rapid POSTs with garbage codes in a shell loop, collect `-w "%{http_code}"`. All 401/400 with zero 429 = brute surface open. Confirm uniform error strings (no oracle), note entropy/TTL as the unknown.

## Probe adjustment (mobile-api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
