# Operator note — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-operator-note.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Free-AI/bill-drain and cross-user poisoning were the prior session's highest-scoring items
(scores 85/95), already reported. This pass adds supply-chain recon + data-plane leak surface.
No host RCE, no admin panel, no secrets — target remains hardened on the data plane; the "holy
shit" is unauthorized resource usage + full infrastructure disclosure, not root.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
