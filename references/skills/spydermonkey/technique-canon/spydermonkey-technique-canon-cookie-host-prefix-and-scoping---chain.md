# Cookie __Host- prefix and scoping regressions — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-cookie-host-prefix-and-scoping-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Missing `__Host-`, missing Secure, or Domain=.parent leaves cookies portable across sibling hosts. Decisive test: set a cookie on sub.in-scope.host and read it from sibling.in-scope.host over HTTPS — cross-subdomain readability is the finding.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
