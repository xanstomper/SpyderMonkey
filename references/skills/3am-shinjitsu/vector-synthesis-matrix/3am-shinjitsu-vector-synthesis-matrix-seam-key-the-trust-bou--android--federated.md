# Seam key (the trust boundaries that define input position) — android / federated

- source canon: `3am-shinjitsu/vector-synthesis-matrix.md`
- base technique: `3am-shinjitsu-vector-synthesis-matrix-seam-key-the-trust-bou.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **android** · auth **federated** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

| Seam | Boundary | Test signature |
|---|---|---|
| A | CDN↔origin | direct-origin reach, WAF vs app behavior split |
| B | Client↔server validation | UI gate vs API enforcement divergence |
| C | Auth↔backend binding | mint vs consumer trust roots (session vs key) |
| D | Limiter↔coercion | counting vs parsing divergence |
| E | WS handshake↔frame auth | 101 passthrough vs gated frames |
| F | OAuth provider↔app | redirect_uri/state binding, callback taxonomy |
| G | Edge-function↔DB | function trust vs RLS scope split |
| H | Multi-host family | sister brands, staging, dead-DNS-live-cert |
| I | i18n/asset plane | chunk subset, env-object, template-literal paths |
| J | LLM layer | shared buffers vs per-request state |
| K | Cloud-policy | object-store / IAM policy vs enforcement gap |
| L | Device-firmware | console/OTA/update path vs signed trust |
| M | Protocol-handshake | network services' pre-auth handshake |
| N | Collab-app | webhook/grant registration trust |
| O | Monitoring-plane | orchestration/monitoring reachable anonymously |

## Probe adjustment (android × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
