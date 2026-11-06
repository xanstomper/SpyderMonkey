# OAuth code interception (redirect_uri looseness) — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-oauth-code-interception-redirec.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

A permissive redirect_uri validation (prefix match, wildcard subdomain, open redirect chained) makes the authorization code interceptable. Decisive test: redirect_uri=https://in-scope.host.evil.example — accepted or rejected by the AS; if accepted, the code arrives at your host. The finding is the validation looseness class, proven by one redirect.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
