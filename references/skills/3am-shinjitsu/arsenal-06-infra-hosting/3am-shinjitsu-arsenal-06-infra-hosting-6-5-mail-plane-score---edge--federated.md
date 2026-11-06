# 6.5 Mail plane (score 70) — edge / federated

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- base technique: `3am-shinjitsu-arsenal-06-infra-hosting-6-5-mail-plane-score-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **edge** · auth **federated** · chain role **pivot**

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- SPF/DKIM/DMARC gaps (`dig TXT` all three) → spoofing exposure (document, don't send).
- Subdomain takeover: orphaned MX/CNAME to NXDOMAIN'd services = registration takeover
  executable same-day (verify the provider's "domain not found" page fingerprint).

## Probe adjustment (edge × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
