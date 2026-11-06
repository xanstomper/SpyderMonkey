# Remediation — graphql / machine

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-remediation.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **machine** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

1. **Rate-limit** `/api/export` and `/api/dashboard?refresh=1` — lockout after 5 failed password attempts
2. **Replace shared secret** `madsys` with per-user tokens or session-based auth
3. **Add MFA** for refresh/export operations
4. **Restrict unauthenticated `/api/dashboard`** (returns stale cache anyway — gate it)

## Probe adjustment (graphql × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
