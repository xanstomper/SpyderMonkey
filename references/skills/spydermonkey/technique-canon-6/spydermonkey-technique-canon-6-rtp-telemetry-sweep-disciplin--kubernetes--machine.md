# RTP telemetry sweep discipline — kubernetes / machine

- source canon: `spydermonkey/technique-canon-6.md`
- base technique: `spydermonkey-technique-canon-6-rtp-telemetry-sweep-disciplin.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **kubernetes** · auth **machine** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Rolling-window liveRtp sweeps every session (fresh money-pump rows), DISTINCT leading words per title (dedupe discipline), mirror the exact POST verb+headers. Decisive test: liveRtp_24h from the public endpoint — the repricing pattern across sweeps is the crown class.

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
