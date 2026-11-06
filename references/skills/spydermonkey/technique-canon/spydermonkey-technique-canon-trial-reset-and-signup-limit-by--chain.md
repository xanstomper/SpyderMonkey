# Trial reset and signup-limit bypass — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-trial-reset-and-signup-limit-by.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Trial entitlement tied to a client-controllable identity fragment (device id, email alias) is a logic seam. Decisive test: second trial via email+1 alias on your OWN address — entitlement granted = the finding (the abuse class, not the grant).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
