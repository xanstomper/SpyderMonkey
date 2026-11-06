# 5.1 postMessage origin matrix (score 70) — kubernetes / machine

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-1-postmessage-origin-.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **kubernetes** · auth **machine** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- VULN: `postMessage(data, '*')` / attacker-origin targets; receive-side without origin check.
- CORRECT (no false alarm): `postMessage(data, window.location.origin)` on send; sender-origin
  validation on receive.
- DECISIVE: static grep every chunk for `postMessage(`; dynamic harness only on confirmed
  wildcards.

## Probe adjustment (kubernetes × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
