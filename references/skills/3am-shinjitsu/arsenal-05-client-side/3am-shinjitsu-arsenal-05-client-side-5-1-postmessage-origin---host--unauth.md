# 5.1 postMessage origin matrix (score 70) — host / unauth

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-1-postmessage-origin-.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **host** · auth **unauth** · chain role **pivot**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- VULN: `postMessage(data, '*')` / attacker-origin targets; receive-side without origin check.
- CORRECT (no false alarm): `postMessage(data, window.location.origin)` on send; sender-origin
  validation on receive.
- DECISIVE: static grep every chunk for `postMessage(`; dynamic harness only on confirmed
  wildcards.

## Probe adjustment (host × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
