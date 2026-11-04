# Pitfalls — chain composition

- source canon: `undercroft/bundle-decode.md`
- base technique: `undercroft-bundle-decode-pitfalls.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Guessing API paths from docs alone misses the auth-gated surface — docs list
  public routes only; the client contract lists everything the app calls.
- A 404 with an EMPTY body on every guessed path means wrong base host or wrong
  prefix, not hidden routes — go back to the client's URL builder instead of
  brute-forcing prefixes.
- Vendor chunks (tone.js, zod, maplibre, react) are noise — grep for the app's own
  route vocabulary, not generic SDK strings.
- A string-table entry like `40IlQxWv` is a build-hash, not a route — filter
  entries to path/verb/host shapes before reading the table as an endpoint list.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
