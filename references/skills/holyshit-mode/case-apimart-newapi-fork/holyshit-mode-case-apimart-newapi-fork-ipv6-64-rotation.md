# IPv6 /64 rotation

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`sudo ip -6 addr add <any-addr-in-block>/64 dev <iface>` then `curl --interface <addr>` = fresh
rate-limit bucket per address. NOTE: the sandbox security guard may block `curl --interface <addr>`
mid-session (approved-command gate) — scope-gate with the operator before IP-rotation testing.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
