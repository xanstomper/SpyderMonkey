# Control proof & crown jewels — android / unauth

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-control-proof-crown-jewel.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **android** · auth **unauth** · chain role **final**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Confirmed plane finding → one read-only proof (shell `id`, bus byte read, key
extraction hash) → STOP. Then chain: what does the device reach? (cloud API, adjacent
network, OTA server, other devices). Record the chain per 3AM/T1–T7 style:
`uart-shell→firmware-keys→cloud-api:TAKEOVER` where the final hop is proven read-only.

## Probe adjustment (android × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
