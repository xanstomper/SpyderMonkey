# Handoff-code entropy — unbruteforceable to size blind — api / federated

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-handoff-code-en.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **federated** · chain role **final**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

A one-time handoff code exchanged at `/api/auth/platform-handoff/exchange` (code → Supabase access+refresh tokens) is a juicy target, but you CANNOT size its entropy without observing one real code. Uniform `401 invalid_handoff_code` on garbage gives no format/length oracle. The `/start` endpoint requires a valid refresh_token to mint a code — pre-auth you can't generate one.

Log it as "brute surface open, entropy unknown" and move on. Sizing needs one authenticated session to trigger a real handoff and observe the code format in the redirect URL.

## Probe adjustment (api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
