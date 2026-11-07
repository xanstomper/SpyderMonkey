# 4.5 MFA/OTP entropy sizing (score 70 — record the math, not "unthrottled") — chain composition

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- base technique: `3am-shinjitsu-arsenal-04-auth-identity-4-5-mfa-otp-entropy-s.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Throughput calibration: 100-thread curl ≈ 52 req/s effective. 6-digit space (1M): single-
  thread 5.4 req/s = 51h; 100 threads = 5.3h. TTL vs that = the verdict.
- Charset oracle: off-format tokens (`abcdefgh`, `12345`, `Z9Z9Z9`) — uniform `otp_expired`
  regardless = no charset oracle, error channel blind. Size entropy by triggering ONE live
  flow (§3.8 consumers) — one real code settles it; uniform errors tell nothing.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
