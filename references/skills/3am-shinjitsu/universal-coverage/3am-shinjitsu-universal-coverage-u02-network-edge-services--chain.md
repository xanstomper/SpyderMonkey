# U02 Network edge & services — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u02-network-edge-services.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- [ ] Live services and versions inventoried from banners/config, not guesswork
- [ ] EOL/default/unpatched edge and admin planes identified
- [ ] Exposure of admin/DB/queue/cache/monitoring ports checked
- [ ] VPN/firewall/SSH/RDP policy and MFA coverage reviewed
- [ ] Segmentation and management-plane isolation verified

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
