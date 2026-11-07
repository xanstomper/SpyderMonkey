# IIS short-name (8.3) enumeration — linux / service

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-iis-short-name-8-3-enumeratio.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **linux** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

`~1` short-name requests enumerate files/dirs despite listing denial. Decisive test: /~s/~1 style probes yielding distinct 404-vs-200 classes for the control vs candidate — the oracle is the finding (read-only inventory).

## Probe adjustment (linux × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
