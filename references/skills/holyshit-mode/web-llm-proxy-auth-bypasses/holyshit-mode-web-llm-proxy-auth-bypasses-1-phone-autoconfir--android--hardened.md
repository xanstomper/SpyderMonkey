# 1. Phone autoconfirm = instant confirmed accounts — android / hardened

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- base technique: `holyshit-mode-web-llm-proxy-auth-bypasses-1-phone-autoconfir.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **android** · auth **hardened** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- `GET /auth/v1/settings` reveals `phone_autoconfirm: true`, `mailer_autoconfirm: false`.
- `POST /auth/v1/signup` with `{"phone":"+1...","password":"..."}` returns a FULL session
  (access_token + refresh_token) with NO SMS/OTP step. Accounts mint in ~2s.
- Rate limits on the AI proxy (~6 req/min) are defeated by minting fresh accounts and rotating.
- Pitfall: response shape differs by flow — email signup nests the session under `session`,
  phone signup may return access_token at top level. Parse both.

## Probe adjustment (android × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
