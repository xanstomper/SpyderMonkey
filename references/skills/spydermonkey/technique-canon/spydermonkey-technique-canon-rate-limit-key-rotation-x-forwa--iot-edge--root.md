# Rate-limit key rotation (X-Forwarded-For trust) — iot-edge / root

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-rate-limit-key-rotation-x-forwa.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **iot-edge** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

Limits keyed on a client-supplied header = limit-free access. Decisive test: same request 6× with rotating X-Forwarded-For — all 200 past the documented limit = the class (the arithmetic, not a brute).

## Probe adjustment (iot-edge × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
