# U03 Web application — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u03-web-application.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- [ ] Routes, methods, authn/authz states, and tenant boundaries mapped
- [ ] Session lifecycle, cookie flags, CSRF, CORS, CSP, and redirects reviewed
- [ ] Server-side authorization proven with two authorized test identities
- [ ] File upload/import/export and parser boundaries reviewed
- [ ] Business-logic invariants and abuse cases documented

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
