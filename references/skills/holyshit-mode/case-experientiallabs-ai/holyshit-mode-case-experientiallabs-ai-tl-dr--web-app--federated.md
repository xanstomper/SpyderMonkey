# TL;DR — web-app / federated

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-tl-dr.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **federated** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

The operator's public gateway (`api.experientiallabs.ai`) is well-hardened — every `/v1/*`
inference route 401s without a valid `xpl_` key, the management API is session/org-gated, and
the Next.js admin console is auth-routed. However, the **internal serving fleet** under
`*.xplabs.ai` leaks heavily and exposes an **unauthenticated elastic-scaling control-plane
write** on the DeepSeek lane — a real compromise.

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
