# Kind 2 — contestant status (record size 28, `qi=12, Sd=28`) — host / machine

- source canon: `holyshit-mode/iceposeidon-binary-map-protocol.md`
- base technique: `holyshit-mode-iceposeidon-binary-map-protocol-kind-2-contest.md`
- bindings: **WSTG-ADV-01** · **CWE-444** · **ATT&CK T1190**
- context: **host** · auth **machine** · chain role **pivot**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- `o+0` u32 definitionSequence, `o+4` f64 timeBase (ms grid 100)
- Per record: `M=o+12`: u16 slot (z*2), u8 statusFlags (z at M+l*2; bit6+ reserved, `Id`=self bit etc.), u8 status badges (bitfield over `yd`), u8 healthStatus (index into Yi), u8 hp, u8 maxHp (max `Gi`), then optional i32 fields gated by statusFlags bits — offsets `M+l*8, l*12, l*16, l*20, l*24` (z*4 stride): poison started/ends, droneLandsAt, outsideSince, nextDamageAt — each `timeBase + v*100` ms.

## Probe adjustment (host × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
