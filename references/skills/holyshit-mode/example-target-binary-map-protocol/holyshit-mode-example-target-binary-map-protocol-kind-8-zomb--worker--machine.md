# Kind 8 — zombie leech schedule (`Pd=20, Dd=9, Ud=6`) — worker / machine

- source canon: `holyshit-mode/example-target-binary-map-protocol.md`
- base technique: `holyshit-mode-example-target-binary-map-protocol-kind-8-zomb.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **worker** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- `o+0` u32 rosterSequence, `o+4` f64 timeBase, `o+12` i32 latBase, `o+16` i32 lngBase (scale 1e5)
- l× u8 count + l× u16 index; per zombie: u16 slot, i16 latDelta, i16 lngDelta, u16 targetSlot, then count× {u16 leechSlot, i32 nextHitAtDelta*100ms}.

## Probe adjustment (worker × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
