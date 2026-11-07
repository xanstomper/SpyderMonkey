# The TRANSPOSE domain map (web → metal) — chain composition

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-the-transpose-domain-map-web-metal.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Web class | Metal analogue | The transposed probe |
|---|---|---|
| BOUNDARY | HWFLASH | scope-id trust on update/extract paths — swapped slot ids (lab, owned device) |
| REPLAY | HDRADIO | pairing/replay window — capture + replay ack frames (lab spectrum) |
| STATEBYPASS | HWFLASH | out-of-order OTA/bootloader stages — N+2 before N+1 |
| MATH | HDRADIO | precision drift in radio counters — worst values ×N |
| ENTITLEMENT | HWFLASH | provisioning order — entitlement flag before its check |
| AUTHBYPASS | HDRADIO | pairing-material entropy — effective bits from captures |

`kairo crossdomain --target T --from web --to hardware|radio` registers each as a
PROBED plane-ledger plan — lab-first, owned devices, never auto-CONFIRMED, never
distributed.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
