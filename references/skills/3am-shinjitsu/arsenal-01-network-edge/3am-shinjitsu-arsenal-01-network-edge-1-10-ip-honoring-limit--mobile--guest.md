# 1.10 IP-honoring / limiter keying (score 60) — mobile / guest

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-10-ip-honoring-limit.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **mobile** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the client is another principal — storage/permission surface, own device only
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- DECISIVE: same request twice, `X-Forwarded-For: 1.2.3.4` vs without — diff response.
- DISCRIMINATOR: CF-fronted → XFF/CF-Connecting-IP from client = **403 error 1000** (they're
  stripped; spoofing impossible). A 1000 IS the finding that limiter is real-IP-keyed.
- CONFIRMED WHEN: non-CF origin honors XFF for rate-limit buckets → rotation bypass.

## Probe adjustment (mobile × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
