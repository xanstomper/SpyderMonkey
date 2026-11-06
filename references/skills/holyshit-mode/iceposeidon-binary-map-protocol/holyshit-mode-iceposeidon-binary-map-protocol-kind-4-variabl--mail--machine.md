# Kind 4 — variable-length records (`en`-byte records, type table `Zd`) — mail / machine

- source canon: `holyshit-mode/i***REDACTED***-binary-map-protocol.md`
- base technique: `holyshit-mode-i***REDACTED***-binary-map-protocol-kind-4-variabl.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **mail** · auth **machine** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

`recordCount` from header; each record: first byte indexes table `Zd`, followed by typed fields via `Zd[r.getUint8(...)]` descriptor. (Not fully enumerated — event was quiet.)

## Probe adjustment (mail × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
