# Deserialization gadget DNS-ping — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-deserialization-gadget-dns-ping.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The safe proof of a deserialization class is a DNS-only gadget (no command execution). Decisive test: serialized payload whose gadget list ends in a DNS resolution to your domain — the lookup arrival is the finding. Execution gadgets are REPORTED as the class, never fired.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
