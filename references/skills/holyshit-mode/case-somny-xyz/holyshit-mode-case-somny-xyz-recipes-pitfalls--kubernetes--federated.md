# Recipes / pitfalls — kubernetes / federated

- source canon: `holyshit-mode/case-somny-xyz.md`
- base technique: `holyshit-mode-case-somny-xyz-recipes-pitfalls.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **kubernetes** · auth **federated** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- **Key-masking pattern:** key-create endpoints return masked keys; a `reveal`/`secret` sub-endpoint is the real primitive (same as gratisfy's `platform-keys/{id}/secret`). IDOR on reveal with foreign UUID → 400 body-validation (auth before existence).
- **mail.tm flow:** GET `/domains` (find active domain) → POST `/accounts` → POST `/token` → poll `/messages` (5s) → GET `/messages/{id}` for full body → regex `token=([a-zA-Z0-9._-]+)&callbackURL`. Consume ONCE via GET with no-redirect opener; capture 302 Location.
- **Verification token may be JWT-style (167 chars), not hex** — regex must allow dots: `[a-zA-Z0-9._-]+`.
- **Terminal `&` guard:** shell loops with `&` backgrounding rejected by terminal tool — serialize.
- **delete-user 404:** better-auth endpoint present in client bundle but plugin not enabled server-side — bundle lists endpoints the server doesn't have; always live-probe.
- Hygiene: revoked probe key via `DELETE /api/keys/{id}` (worked).

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
