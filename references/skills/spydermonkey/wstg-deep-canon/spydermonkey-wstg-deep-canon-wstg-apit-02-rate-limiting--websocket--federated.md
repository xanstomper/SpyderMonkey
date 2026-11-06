# WSTG-APIT-02 Rate Limiting — websocket / federated

- source canon: `spydermonkey/wstg-deep-canon.md`
- base technique: `spydermonkey-wstg-deep-canon-wstg-apit-02-rate-limiting.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **websocket** · auth **federated** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: missing/naive rate limits
- probe: 3-request timing differential on the lab replica — the limit SHAPE, never a flood
- wall: proof is the missing counter, not an outage

## Probe adjustment (websocket × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
