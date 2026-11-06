# CONTINUATION flood / rapid reset (documented DoS classes) — mobile-api / federated

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-continuation-flood-rapid-rese.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **mobile-api** · auth **federated** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Characterize as EXPOSURE (does the edge cap CONTINUATION frames/reset rate?) — register the cap absence as the finding; the flood itself is NEVER fired outside the dojo lab.

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
