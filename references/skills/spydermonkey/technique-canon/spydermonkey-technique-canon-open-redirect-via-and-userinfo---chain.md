# Open redirect via //, \\, and userinfo tricks — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-open-redirect-via-and-userinfo-.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

//evil.example, https:evil.example, /\evil.example parser-differential confusion. Decisive test: each variant's browser navigation (headless, local) — one variant navigates off-host = the class. Crown: redirect chains into OAuth redirect_uri (pairs with the OAuth class).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
