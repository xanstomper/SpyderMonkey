# IPv6 /64 rotation — ios / unauth

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- base technique: `holyshit-mode-case-apimart-newapi-fork-ipv6-64-rotation.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **ios** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

`sudo ip -6 addr add <any-addr-in-block>/64 dev <iface>` then `curl --interface <addr>` = fresh
rate-limit bucket per address. NOTE: the sandbox security guard may block `curl --interface <addr>`
mid-session (approved-command gate) — scope-gate with the operator before IP-rotation testing.

## Probe adjustment (ios × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
