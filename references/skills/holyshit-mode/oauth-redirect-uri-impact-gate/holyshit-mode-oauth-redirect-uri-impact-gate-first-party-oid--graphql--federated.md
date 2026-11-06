# First-party OIDC (separate from GoTrue external OAuth) — graphql / federated

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-first-party-oid.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **graphql** · auth **federated** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Platforms that offer "Login with X" via their own OIDC provider (`/oauth/authorize` + `/api/oauth/token`) are a SEPARATE auth surface from the Supabase GoTrue external OAuth (Discord/Google). On g***REDACTED***.xyz the first-party flow used:

- PKCE S256 with `crypto.getRandomValues(48)` verifier — proper, not bruteable
- `code_challenge_method: S256`, nonce, sessionStorage state binding
- Server rejects garbage codes with uniform `invalid_grant`

Treat first-party OIDC as hardened unless the verifier is `Math.random()`-based or the challenge method is `plain`. Mine the SPA bundle for the PKCE generation function to confirm — `grep -oE 'crypto\.getRandomValues|Math\.random' firstPartyOidc*.js`.

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
