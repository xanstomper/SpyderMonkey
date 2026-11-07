# Kind 7 — zombies (record size 37: `Ki=16` UUID, `Nd=37`) — web-app / service

- source canon: `holyshit-mode/example-target-binary-map-protocol.md`
- base technique: `holyshit-mode-example-target-binary-map-protocol-kind-7-zomb.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **web-app** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- `o+0` u32 rosterSequence, `o+4` u32 slotsSequence, `o+8` f64 timeBase
- Per record: 16-byte UUID id, u16 ownerSlot, i32 expiresAtDelta (timeBase + v*100, gated by flag bit `$d`), f32 speedMps (gated `Wi`), u8 flags (top 3 bits reserved must be 0; `Ld`=guard), f32 leechIntervalSeconds, f32 leechRadiusM, u16 leechAmount.
- Roster ids must be strictly sorted (`Qu(a,b)<0`).

## Probe adjustment (web-app × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
