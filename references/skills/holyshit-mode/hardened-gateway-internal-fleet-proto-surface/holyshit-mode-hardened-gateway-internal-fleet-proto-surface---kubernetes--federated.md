# Honest ceiling — kubernetes / federated

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- base technique: `holyshit-mode-hardened-gateway-internal-fleet-proto-surface-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **kubernetes** · auth **federated** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

The worker pods are self-contained: no SSRF (`url`/`base_url`/`endpoint` params ignored or time out),
no IMDS/cloud-metadata reach, no `/v1/keys` mint, no RCE. Escalation to key-mint / org-admin / BYOK-secret
drain requires passing the auth wall (authenticated context). When the operator insists "there's
definitely a way past", re-probe the auth surface fresh; if genuinely hardened, record a **negative**
(`auth_wall_hardened_no_bypass`) and state the ceiling — never fabricate a forge or escalation.

## Probe adjustment (kubernetes × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
