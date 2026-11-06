# MASTG Deep Links and Intent Redirection (MASTG-PLATFORM-06) — firmware / federated

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-deep-links-and-intent-redire.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **firmware** · auth **federated** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: hijackable deep links, intent passthrough
- probe: static link inventory; am-probe the lab app with crafted intents
- wall: lab device

## Probe adjustment (firmware × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
