# Trust-anchor hygiene — host / service

- source canon: `spydermonkey/technique-canon-12.md`
- base technique: `spydermonkey-technique-canon-12-trust-anchor-hygiene.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **host** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

Custom CAs accepted in release builds. Decisive test: user-CA traffic readable = the row.

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
