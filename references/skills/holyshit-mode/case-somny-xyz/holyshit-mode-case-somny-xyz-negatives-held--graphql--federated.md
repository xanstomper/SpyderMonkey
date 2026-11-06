# Negatives (held) — graphql / federated

- source canon: `holyshit-mode/case-somny-xyz.md`
- base technique: `holyshit-mode-case-somny-xyz-negatives-held.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **graphql** · auth **federated** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- CORS: no ACAO reflection; CSP `connect-src 'self'`; cookies Lax.
- Paid-model gate: 403 `model_access` on claude/*; 9-variant bypass matrix (case/space/`:latest`/dot/#/array-type) all 404/400. Same gate on messages/responses/batch.
- PTOK constant → stateless, no shared buffer.
- Stripe checkout honors only server-side plan codes → legit `cs_live` session.
- No admin/internal/webhook surface (uniform 404 JSON). `/api/status` leaks only `{service, inference, billing, billingManagement, signup, google, mode}` — gate map enumerable unauth.
- `verify-email?callbackURL=` origin-locked (evil.com → 403). Userinfo-confusion `https://evil.com@somny.xyz` → 302 but host resolves to somny.xyz (browser-safe, low).

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
