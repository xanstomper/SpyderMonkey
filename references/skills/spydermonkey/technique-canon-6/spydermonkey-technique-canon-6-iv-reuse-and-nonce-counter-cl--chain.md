# IV reuse and nonce-counter classes — chain composition

- source canon: `spydermonkey/technique-canon-6.md`
- base technique: `spydermonkey-technique-canon-6-iv-reuse-and-nonce-counter-cl.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Deterministic ciphertext prefixes across messages (ECB-class visual repetition) and IV/nonce reuse detectable from ciphertext pairs of YOUR OWN test material. Decisive test: two same-prefix plaintexts → ciphertext prefix delta (ECB) or equality (IV reuse).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
