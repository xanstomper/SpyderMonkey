# Pivot & tunnel classes

- source canon: `spydermonkey/c2-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
