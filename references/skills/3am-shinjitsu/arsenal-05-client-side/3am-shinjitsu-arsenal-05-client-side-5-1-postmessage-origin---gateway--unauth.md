# 5.1 postMessage origin matrix (score 70) — gateway / unauth

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-1-postmessage-origin-.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **gateway** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- VULN: `postMessage(data, '*')` / attacker-origin targets; receive-side without origin check.
- CORRECT (no false alarm): `postMessage(data, window.location.origin)` on send; sender-origin
  validation on receive.
- DECISIVE: static grep every chunk for `postMessage(`; dynamic harness only on confirmed
  wildcards.

## Probe adjustment (gateway × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
