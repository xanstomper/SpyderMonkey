# 3.5 PostgREST error oracles (score 70, RLS-safe recon) — mobile-api / federated

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-5-postgrest-error-oracles-sco.md`
- bindings: **WSTG-SESS-01** · **CWE-347** · **ATT&CK T1552**
- context: **mobile-api** · auth **federated** · chain role **entry**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- `PGRST205` table absent · `[]` table exists+RLS-gated · `42703` on `?select=<col>` = free
  column-name brute · `22P02` = column TYPE oracle · `PGRST301` = PostgREST uses a DIFFERENT
  JWT trust root than GoTrue (forge against both separately).
- Schema map from errors = coverage finding even when RLS holds.

## Probe adjustment (mobile-api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
