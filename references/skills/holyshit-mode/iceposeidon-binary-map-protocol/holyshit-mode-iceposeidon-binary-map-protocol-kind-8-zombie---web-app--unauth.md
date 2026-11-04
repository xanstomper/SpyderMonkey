# Kind 8 — zombie leech schedule (`Pd=20, Dd=9, Ud=6`) — web-app / unauth

- source canon: `holyshit-mode/i***REDACTED***-binary-map-protocol.md`
- base technique: `holyshit-mode-i***REDACTED***-binary-map-protocol-kind-8-zombie-.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **web-app** · auth **unauth** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- `o+0` u32 rosterSequence, `o+4` f64 timeBase, `o+12` i32 latBase, `o+16` i32 lngBase (scale 1e5)
- l× u8 count + l× u16 index; per zombie: u16 slot, i16 latDelta, i16 lngDelta, u16 targetSlot, then count× {u16 leechSlot, i32 nextHitAtDelta*100ms}.

## Probe adjustment (web-app × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
