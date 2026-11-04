# 1.9 Host-header injection (score 65) [ONE request, off-peak]

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-04

## The technique

- DECISIVE: `curl -s -H 'Host: evil.com' https://<target>/password-reset -d 'email=x@y.z'`
  → inspect reset link host in any response body / downstream email (operator-supplied box).
- CONFIRMED WHEN: reset URL carries attacker host (reset poisoning / cache poisoning).
- FP: absolute-URL builders that re-derive host server-side.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
