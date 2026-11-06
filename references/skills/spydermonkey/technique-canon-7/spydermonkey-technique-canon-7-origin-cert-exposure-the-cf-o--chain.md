# Origin-cert exposure (the CF Origin Cert class) — chain composition

- source canon: `spydermonkey/technique-canon-7.md`
- base technique: `spydermonkey-technique-canon-7-origin-cert-exposure-the-cf-o.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Origin certs naming OTHER domains installed on the same box = tri-brand shared origin (SPY-012). Decisive test: TLS handshake cert chain on the ORIGIN IP — foreign SANs = the crown.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
