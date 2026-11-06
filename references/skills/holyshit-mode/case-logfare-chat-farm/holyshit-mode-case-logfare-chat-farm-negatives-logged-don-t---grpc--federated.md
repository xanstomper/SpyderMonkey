# Negatives (logged, don't re-probe) — grpc / federated

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-negatives-logged-don-t-.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **grpc** · auth **federated** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- Tier-2 consent gate holds: glm-5/grok-4.6 → 403 `consent_required` (real server gate; mass-assigned tier/role/can_use_premium/consent fields accepted `{"ok":true}` but stripped — verify by GET-back + retry, not the 200).
- Cross-session conversation IDOR → 404; client-supplied `conversation_id` ignored; no shared global buffer (PTOK constant 7-36/fresh session, cross-user probe → NONE).
- Model-field path traversal → clean 502 upstream-404 passthrough (no SSRF via model routing).
- SvelteKit escapes stored conversation titles; settings theme not reflected into HTML.

## Probe adjustment (grpc × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
