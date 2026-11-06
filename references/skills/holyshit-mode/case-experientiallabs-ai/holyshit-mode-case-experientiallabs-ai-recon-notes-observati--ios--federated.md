# Recon Notes (observation class, not scored as compromise) — ios / federated

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-recon-notes-observati.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **ios** · auth **federated** · chain role **entry**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- `api.experientiallabs.ai` public gateway: all `/v1/*` + management routes properly 401/no-auth.
  Well-hardened.
- Full public model catalog (500 models) keyless via `/api/models` + `/api/models/<slug>`:
  internal provider wiring, billing fields, and 8 leaked internal `base_url`s:
  `gateway.xplabs.ai/glm|glm3|qwen`, `wm.xplabs.ai`, `clef.xplabs.ai(|/flash)`.
- Internal fleet DNS fully enumerated & publicly reachable (GCP 34.44.x, Azure 20.125.x).
- Next.js admin console routes exist (`/admin/*`) but are signin-gated.
- Signup/onboarding, MFA, BYOK, provisioning-key flows all behind session auth — not
  bootstrapped (doctrine: no credential bootstrapping on operator's own estate; operator to
  supply a session/key for management-API IDOR depth).

## Probe adjustment (ios × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
