# 5.1 postMessage origin matrix (score 70)

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-04

## The technique

- VULN: `postMessage(data, '*')` / attacker-origin targets; receive-side without origin check.
- CORRECT (no false alarm): `postMessage(data, window.location.origin)` on send; sender-origin
  validation on receive.
- DECISIVE: static grep every chunk for `postMessage(`; dynamic harness only on confirmed
  wildcards.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
