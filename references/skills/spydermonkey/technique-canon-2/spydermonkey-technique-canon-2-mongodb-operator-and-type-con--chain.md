# MongoDB operator and type confusion — chain composition

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-mongodb-operator-and-type-con.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`$ne`/`$regex`/`$where` and array-typed params accepted server-side. Decisive test: operator body on your own login/owner field — acceptance without the secret = the class; `$where` acceptance is the JS-execution variant (reported, never weaponized).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
