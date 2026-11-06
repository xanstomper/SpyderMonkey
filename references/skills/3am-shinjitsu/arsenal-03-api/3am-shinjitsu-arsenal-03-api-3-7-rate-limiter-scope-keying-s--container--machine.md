# 3.7 Rate-limiter scope/keying (score 75, ceiling 15/endpoint, once) — container / machine

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-7-rate-limiter-scope-keying-s.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **container** · auth **machine** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Map: keying (IP/email/account/global), decay, window. Tests: 10-rapid sequential; HPP dup
  (`?a=1&a=1`); dual-stack (v6 pool vs v4); malformed-payload counting (do 400s consume?).
- Self-DoS law: 429'd attempts usually COUNT — a fast retry loop keeps the bucket drained
  forever. After a burst go FULL-COLD 2h, then ONE attempt. Read `retry-after` + margin.
- CF challenge pacing: IP-wide ~12-burst → 403/429 EVERY endpoint ~75s. Space 3-4s; re-read
  the SAME endpoint after decay before calling it gated.
- CONFIRMED: unthrottled code/token-exchange (zero 429 on 15-20 garbage inputs) + short
  entropy + long TTL = the Holy-Shit shape (entropy sizing: §4.5).

## Probe adjustment (container × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
