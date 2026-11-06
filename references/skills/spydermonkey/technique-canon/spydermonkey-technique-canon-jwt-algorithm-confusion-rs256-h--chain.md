# JWT algorithm confusion (rs256 → hs256) — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-jwt-algorithm-confusion-rs256-h.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

If the verification library accepts `alg` from the token, an rs256-signed scheme falls to hs256 with the public key as HMAC secret. Decisive test: sign a token with alg=hs256 using the fetched public key PEM as the secret, send it, and require a measurable behavioral delta (accepted vs 401) — token acceptance without privilege movement is a hypothesis, not a finding. Validation-only: a forged token is PROVEN but never used for access.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
