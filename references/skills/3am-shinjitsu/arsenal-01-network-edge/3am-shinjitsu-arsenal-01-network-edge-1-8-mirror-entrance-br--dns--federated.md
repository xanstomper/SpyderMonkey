# 1.8 Mirror/entrance brands (score 70) — dns / federated

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-8-mirror-entrance-br.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- context: **dns** · auth **federated** · chain role **pivot**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- PATTERN: `tr.<brand>`, `giris.<brand>` (TR entrance pattern), `<lang>.<brand>`,
  `<brand>-<market>` — separate hosting from CT logs + passive DNS.
- CONFIRMED WHEN: mirror on different ASN/IP-family than main = un-CDN'd, un-WAF'd surface.

## Probe adjustment (dns × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
