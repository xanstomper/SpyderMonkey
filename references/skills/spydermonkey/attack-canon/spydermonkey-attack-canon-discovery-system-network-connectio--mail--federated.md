# Discovery System Network Connections (T1049) — mail / federated

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-discovery-system-network-connectio.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- context: **mail** · auth **federated** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: connection/route enumeration
- probe: passive — headers/proxies reveal topology without touching hosts
- wall: NO-GAIN

## Probe adjustment (mail × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
