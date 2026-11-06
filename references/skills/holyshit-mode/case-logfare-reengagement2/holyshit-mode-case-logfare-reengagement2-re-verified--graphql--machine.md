# Re-verified — graphql / machine

- source canon: `holyshit-mode/case-logfare-reengagement2.md`
- base technique: `holyshit-mode-case-logfare-reengagement2-re-verified.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **graphql** · auth **machine** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- **CORS arbitrary-origin + credentials reflection** (score 72) on every endpoint including
  state-changers (`/v1/auth/regenerate-key`, `/v1/me/delete`). BUT: auth is now cookie-based and
  observed cookies ship `SameSite=Lax; HttpOnly; Secure` + path scoping → cross-site POSTs don't
  carry the session. **Exploitability downgraded 9.1 → ~7.1.** Lesson: the SAME finding changes
  severity when the auth model changes — re-rate exploitability, not just presence, on re-engage.
- `/openapi.json` full exposure (60+ routes, no security schemes).

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
