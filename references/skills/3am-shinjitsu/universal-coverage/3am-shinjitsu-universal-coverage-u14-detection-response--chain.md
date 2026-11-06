# U14 Detection & response — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u14-detection-response.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- [ ] Asset coverage mapped against SIEM/EDR/NDR data sources
- [ ] High-value alerts tested through approved purple-team cases
- [ ] Log integrity, time sync, retention, and forensic readiness verified
- [ ] Incident runbooks, revocation, and rollback paths exercised
- [ ] Detection gaps and tuning backlog documented

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
