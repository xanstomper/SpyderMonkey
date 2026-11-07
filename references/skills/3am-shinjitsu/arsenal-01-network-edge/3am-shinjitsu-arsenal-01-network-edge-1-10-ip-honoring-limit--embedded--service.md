# 1.10 IP-honoring / limiter keying (score 60) — embedded / service

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-10-ip-honoring-limit.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **embedded** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: banner/identity reads only on in-scope industrial tiers — control writes are the absolute wall
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- DECISIVE: same request twice, `X-Forwarded-For: 1.2.3.4` vs without — diff response.
- DISCRIMINATOR: CF-fronted → XFF/CF-Connecting-IP from client = **403 error 1000** (they're
  stripped; spoofing impossible). A 1000 IS the finding that limiter is real-IP-keyed.
- CONFIRMED WHEN: non-CF origin honors XFF for rate-limit buckets → rotation bypass.

## Probe adjustment (embedded × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
