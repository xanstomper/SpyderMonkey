# Rate-limit measurement pattern

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-04

## The technique

Foreground shells refuse `&` backgrounding; use execute_code with
concurrent.futures.ThreadPoolExecutor spawning subprocess curl per worker, then
Counter() the status codes (e.g. 30 parallel → 21×200, 9 timeouts, zero 429 = no
effective limit). Log req/s, lockout presence, captcha presence.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
