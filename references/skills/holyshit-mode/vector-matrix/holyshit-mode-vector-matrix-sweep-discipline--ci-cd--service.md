# SWEEP DISCIPLINE — ci-cd / service

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-sweep-discipline.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ci-cd** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- One decisive probe per cell. A negative result IS a result — log it as coverage evidence.
- Escalate only on signal. No blind CVE spam, no spray-and-pray.
- HOLY SHIT = confirmed cell with impact narrative + kill-chain position. Everything else
  is documented coverage.
- All probes respect the mandate scope gate: scoped targets only, non-destructive, revert
  map before any state change, disclosure path for anything outside own infrastructure.

## Probe adjustment (ci-cd × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
