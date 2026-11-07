# 4.5 MFA/OTP entropy sizing (score 70 — record the math, not "unthrottled")

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Throughput calibration: 100-thread curl ≈ 52 req/s effective. 6-digit space (1M): single-
  thread 5.4 req/s = 51h; 100 threads = 5.3h. TTL vs that = the verdict.
- Charset oracle: off-format tokens (`abcdefgh`, `12345`, `Z9Z9Z9`) — uniform `otp_expired`
  regardless = no charset oracle, error channel blind. Size entropy by triggering ONE live
  flow (§3.8 consumers) — one real code settles it; uniform errors tell nothing.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
