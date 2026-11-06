# Password reset token reuse and non-expiry — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-password-reset-token-reuse-and-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The reset flow that accepts the same token twice (or after password change) fails single-use semantics. Decisive test: request a reset, consume it, replay it — a second 200 (vs 400/410) is the class. Crown: token TTL and whether the OLD password still works after reset.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
