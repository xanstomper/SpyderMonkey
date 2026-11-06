# HOLY SHIT (75): chat.logfare.ai anon inference farm — graphql / federated

- source canon: `holyshit-mode/case-logfare-reengagement2.md`
- base technique: `holyshit-mode-case-logfare-reengagement2-holy-shit-75-chat-l.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **graphql** · auth **federated** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Chain: `Origin: https://chat.logfare.ai` header (plain spoof) → `POST /api/chat {"message":...,
"model":"logfare/auto"}` → server mints `lfc_session` (90-day HttpOnly) with zero auth → real
SSE completions. ~30 reqs, zero 429s; 3 parallel long completions (1.7k/1k/2.7k tokens) served.

Key discriminators learned:
- **Origin gate is a header string-match, enforced only at SESSION MINT.** evil/null/absent →
  403 during mint; once a session cookie exists, the same POST works with **no Origin at all**.
  Test the gate separately for mint vs. use — one 403 does not mean the endpoint is gated.
- **Playground hosts hide the real API.** Ghost discrimination on chat host: `404 text/html` =
  ghost, `403 application/json` = real route. Found `/api/health`, `/api/models`,
  `/api/chat`, `/api/auth`, `/api/conversations`, `/api/settings`, `/api/consent`.
- **Error channel gives body shape:** bare POST → 400 "message required" (field is `message`,
  not OpenAI `messages`).
- **SSE is base64-wrapped JSON per `data:` line** (`eyJ...`) — decode with `+ '='*(-len%4)`;
  `logfare_complete:true` final chunk carries usage. First-chunk `usage.prompt_tokens` is the
  PTOK-drift oracle (constant ~7-36/fresh session here = isolated sessions, no shared buffer).
- **Anon `/api/settings` PUT accepts `system_prompt`/`default_model` (persisted) but mass-assigned
  `tier/role/premium/consent` fields are silently dropped** — server re-checks tier on every call
  (`consent_required` 403 on tier-2 models). `/api/consent` GET leaks `{"tier":"anonymous",
  "can_use_premium":false,"logged_in":false}`.
- **Conversation IDOR held** (cross-session read → 404). PATCH/DELETE own conversation 200.

## Probe adjustment (graphql × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
