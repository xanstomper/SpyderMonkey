# Pivot & tunnel classes — edge-node / root

- source canon: `spydermonkey/c2-canon.md`
- base technique: `spydermonkey-c2-canon-pivot-tunnel-classes.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **edge-node** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Socks reverse | `chisel`/`ligolo-ng` lab pair | local socks reaches remote lan |
| SSH dynamic | `ssh -D` (own hosts) | socks proxy up |
| Frp/nps | `frp` lab pair | nat traversal works |
| RDP pivot | `rpivot` lab pair (own rdp) | socks over rdp |
| HTTP CONNECT | `proxytunnel` lab pair | meet-in-middle tunnel |
| Malleable profile | c2 profile test (own listener) | jitter/URI pattern applied |
| OPSEC hygiene | `macchanger` + fresh identity before lab c2 | listener not tied to op identity |

## Probe adjustment (edge-node × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
