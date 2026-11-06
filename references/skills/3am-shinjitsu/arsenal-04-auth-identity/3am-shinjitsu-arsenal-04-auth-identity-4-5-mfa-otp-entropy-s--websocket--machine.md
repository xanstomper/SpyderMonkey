# 4.5 MFA/OTP entropy sizing (score 70 — record the math, not "unthrottled") — websocket / machine

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- base technique: `3am-shinjitsu-arsenal-04-auth-identity-4-5-mfa-otp-entropy-s.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **websocket** · auth **machine** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Throughput calibration: 100-thread curl ≈ 52 req/s effective. 6-digit space (1M): single-
  thread 5.4 req/s = 51h; 100 threads = 5.3h. TTL vs that = the verdict.
- Charset oracle: off-format tokens (`abcdefgh`, `12345`, `Z9Z9Z9`) — uniform `otp_expired`
  regardless = no charset oracle, error channel blind. Size entropy by triggering ONE live
  flow (§3.8 consumers) — one real code settles it; uniform errors tell nothing.

## Probe adjustment (websocket × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
