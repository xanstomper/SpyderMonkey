# Stored-XSS class — iot-edge / high-priv

- source canon: `spydermonkey/technique-canon-11.md`
- base technique: `spydermonkey-technique-canon-11-stored-xss-class.md`
- bindings: **WSTG-INPV-02** · **CWE-79** · **ATT&CK T1189**
- context: **iot-edge** · auth **high-priv** · chain role **pivot**

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Persistent payloads in your own objects rendering for OTHER principals — needs two principals (the two-role context rule). Decisive test: your own second account renders it = confirmed; single-principal = hypothesis.

## Probe adjustment (iot-edge × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
