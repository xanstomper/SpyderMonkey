# BOUNDARY — HWFLASH — mobile / service

- source canon: `kairo/technique-classes.md`
- base technique: `kairo-technique-classes-boundary-hwflash.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **mobile** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the client is another principal — storage/permission surface, own device only
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- BOUNDARY
- HWFLASH
- scope-id trust on update/extract paths — swapped slot ids (lab, owned device)

## Probe adjustment (mobile × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
