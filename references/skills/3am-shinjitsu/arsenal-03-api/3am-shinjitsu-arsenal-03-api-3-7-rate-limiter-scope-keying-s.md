# 3.7 Rate-limiter scope/keying (score 75, ceiling 15/endpoint, once)

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Map: keying (IP/email/account/global), decay, window. Tests: 10-rapid sequential; HPP dup
  (`?a=1&a=1`); dual-stack (v6 pool vs v4); malformed-payload counting (do 400s consume?).
- Self-DoS law: 429'd attempts usually COUNT — a fast retry loop keeps the bucket drained
  forever. After a burst go FULL-COLD 2h, then ONE attempt. Read `retry-after` + margin.
- CF challenge pacing: IP-wide ~12-burst → 403/429 EVERY endpoint ~75s. Space 3-4s; re-read
  the SAME endpoint after decay before calling it gated.
- CONFIRMED: unthrottled code/token-exchange (zero 429 on 15-20 garbage inputs) + short
  entropy + long TTL = the Holy-Shit shape (entropy sizing: §4.5).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
