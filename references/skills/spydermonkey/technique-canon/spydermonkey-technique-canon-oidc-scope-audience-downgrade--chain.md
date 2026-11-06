# OIDC scope/audience downgrade — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-oidc-scope-audience-downgrade.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Resource servers trust the AS's audience tag; an attacker-controlled client registration (or a lax AS) can mint tokens for scopes the principal never granted. Decisive test: request scope=X with prompt=none from a fresh session and compare the minted token's scope/aud claims against the consent screen's promises — a delta is the finding.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
