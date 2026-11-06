# U12 Endpoint & devices — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u12-endpoint-devices.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- [ ] Managed fleet enrollment, patch level, EOL software, EDR and disk encryption audited
- [ ] Privileged local accounts, cached credentials, and remote access tooling reviewed
- [ ] Network device configs/secrets/firmware/AAA/TACACS/RADIUS reviewed
- [ ] IoT/OT inventory, segmentation, default credentials, and fail-safe behavior reviewed
- [ ] Physical access / RFID / badge systems are documentation only unless explicit RoE

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
