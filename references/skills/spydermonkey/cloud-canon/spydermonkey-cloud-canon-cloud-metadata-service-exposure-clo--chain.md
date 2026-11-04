# Cloud Metadata Service Exposure (CLOUD-SSRF-01) — chain composition

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-metadata-service-exposure-clo.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- class: 169.254.169.254 reachable through an in-scope app — the SSRF crown
- probe: the SSRF battery's metadata targets — the differential proves the reach
- wall: proof-of-reach only; metadata contents beyond the marker are never dumped

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
