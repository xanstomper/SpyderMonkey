# WebAuthn/FIDO classes — chain composition

- source canon: `spydermonkey/technique-canon-6.md`
- base technique: `spydermonkey-technique-canon-6-webauthn-fido-classes.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Origin/RP-ID scoping gaps, challenge entropy, credential-id enumeration, the SPY-101 allowCredentials:[] mint class. Decisive test: ceremony parameters observed on your own enrollment — the scoping delta is the finding.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
