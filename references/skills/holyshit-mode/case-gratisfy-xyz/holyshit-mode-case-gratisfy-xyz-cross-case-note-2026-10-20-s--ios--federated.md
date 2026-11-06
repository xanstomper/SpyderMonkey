# Cross-case note (2026-10-20, somny.xyz) — ios / federated

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-cross-case-note-2026-10-20-s.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **ios** · auth **federated** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Recurring reseller pattern (gratisfy, gonka, somny): **key-create endpoints return masked keys; a `reveal`/`secret` sub-endpoint is the real primitive** (somny: `POST /api/keys` → masked `sk-som...wle0`, `POST /api/keys/{id}/reveal` → full key). IDOR on reveal with foreign UUID → 400 body-validation (auth checked before existence). Also recurring: disposable-domain signup filters miss mail.tm's rotating domains — probe mail.tm `/domains` for newly-active ones first. See `references/case-somny-xyz.md`.

## Probe adjustment (ios × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
