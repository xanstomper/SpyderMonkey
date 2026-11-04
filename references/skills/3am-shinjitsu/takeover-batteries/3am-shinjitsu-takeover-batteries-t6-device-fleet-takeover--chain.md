# T6 — Device/fleet takeover — chain composition

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t6-device-fleet-takeover.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Default/leaked device creds → management plane (one login); firmware creds → adjacent
  services; MQTT subscribe map (never publish) on owned brokers; OT register reads
  (read-only); shared VPN/config creds across fleet.
- **DECISIVE PROOF:** management-plane login success or authenticated service
  enumeration. Then STOP.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
