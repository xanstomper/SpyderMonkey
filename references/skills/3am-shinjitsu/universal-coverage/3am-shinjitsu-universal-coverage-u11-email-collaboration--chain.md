# U11 Email & collaboration — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u11-email-collaboration.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- [ ] MX/SPF/DKIM/DMARC/MTA-STS/TLS-RPT checked and aligned
- [ ] Mailbox/SaaS sharing links, external guests, helpdesk/reset trust reviewed
- [ ] Anti-phishing controls and reporting paths validated (documentation only unless RoE)
- [ ] Domain spoofing/lookalike domains and tenant takeover risks documented
- [ ] Audit logs and retention for collaboration platforms reviewed

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
