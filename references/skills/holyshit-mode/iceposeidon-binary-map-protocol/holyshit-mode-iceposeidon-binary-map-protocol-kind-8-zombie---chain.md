# Kind 8 — zombie leech schedule (`Pd=20, Dd=9, Ud=6`) — chain composition

- source canon: `holyshit-mode/iceposeidon-binary-map-protocol.md`
- base technique: `holyshit-mode-iceposeidon-binary-map-protocol-kind-8-zombie-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `o+0` u32 rosterSequence, `o+4` f64 timeBase, `o+12` i32 latBase, `o+16` i32 lngBase (scale 1e5)
- l× u8 count + l× u16 index; per zombie: u16 slot, i16 latDelta, i16 lngDelta, u16 targetSlot, then count× {u16 leechSlot, i32 nextHitAtDelta*100ms}.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
