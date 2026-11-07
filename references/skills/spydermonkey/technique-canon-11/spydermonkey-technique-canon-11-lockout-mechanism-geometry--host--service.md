# Lockout-mechanism geometry — host / service

- source canon: `spydermonkey/technique-canon-11.md`
- base technique: `spydermonkey-technique-canon-11-lockout-mechanism-geometry.md`
- bindings: **WSTG-ATHN-08** · **CWE-521** · **ATT&CK T1110**
- context: **host** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

Wrong-password counters, lock TTL, and reset behavior mapped. Decisive test: 5+1 attempts measuring the geometry = the row (the arithmetic, not a crack).

## Probe adjustment (host × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
