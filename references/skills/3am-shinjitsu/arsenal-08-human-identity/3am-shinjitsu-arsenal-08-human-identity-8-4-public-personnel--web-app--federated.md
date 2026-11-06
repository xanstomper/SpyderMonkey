# 8.4 Public personnel surface (score 50) — web-app / federated

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- base technique: `3am-shinjitsu-arsenal-08-human-identity-8-4-public-personnel.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- context: **web-app** · auth **federated** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- Email-format deduction from public sources (press releases, public docs), leadership pages,
  generic-role addresses (support@, billing@) — used ONLY to rate phishing exposure and to
  write the remediation section.

## Probe adjustment (web-app × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
