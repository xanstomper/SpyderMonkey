# 1. Phone autoconfirm = instant confirmed accounts — android / unauth

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- base technique: `holyshit-mode-web-llm-proxy-auth-bypasses-1-phone-autoconfir.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **android** · auth **unauth** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- `GET /auth/v1/settings` reveals `phone_autoconfirm: true`, `mailer_autoconfirm: false`.
- `POST /auth/v1/signup` with `{"phone":"+1...","password":"..."}` returns a FULL session
  (access_token + refresh_token) with NO SMS/OTP step. Accounts mint in ~2s.
- Rate limits on the AI proxy (~6 req/min) are defeated by minting fresh accounts and rotating.
- Pitfall: response shape differs by flow — email signup nests the session under `session`,
  phone signup may return access_token at top level. Parse both.

## Probe adjustment (android × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
