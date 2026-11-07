# Rate-limit measurement pattern — mobile / unauth

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-rate-limit-measurement.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **mobile** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: family probes cover the class
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Foreground shells refuse `&` backgrounding; use execute_code with
concurrent.futures.ThreadPoolExecutor spawning subprocess curl per worker, then
Counter() the status codes (e.g. 30 parallel → 21×200, 9 timeouts, zero 429 = no
effective limit). Log req/s, lockout presence, captcha presence.

## Probe adjustment (mobile × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
