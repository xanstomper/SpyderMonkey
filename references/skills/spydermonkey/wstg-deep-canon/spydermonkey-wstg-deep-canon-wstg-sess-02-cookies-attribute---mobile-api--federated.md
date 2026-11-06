# WSTG-SESS-02 Cookies Attribute Flags — mobile-api / federated

- source canon: `spydermonkey/wstg-deep-canon.md`
- base technique: `spydermonkey-wstg-deep-canon-wstg-sess-02-cookies-attribute-.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **mobile-api** · auth **federated** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: missing Secure/HttpOnly/SameSite on session cookies
- probe: Set-Cookie header inventory across the lab replica's flows
- wall: read-only

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
