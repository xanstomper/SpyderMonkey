# Pitfalls — chain composition

- source canon: `holyshit-mode/client-bundle-source-study.md`
- base technique: `holyshit-mode-client-bundle-source-study-pitfalls.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Route sweeps MUST pass `allow_redirects=False`.** A followed 302 records the PROVIDER
  page (accounts.google.com) as the route status — 200-OPEN verdicts on OAuth starters are
  artifacts. Classify status + content-type from the no-redirect response; a 302 with a
  provider Location is itself the REAL route (read its return_to/redirect_uri params).
- **CF Access gates return 200 HTML "Sign in · Cloudflare Access" for every path** —
  detect by title/body string, not status; determinism tests run against Access pages
  produce garbage "rotating/identical" verdicts. Parse `Server:` + `content-type` before
  scoring any response.
- **Region gates are selective:** sweep the whole auth plane (200-JSON = OPEN,
  403-JSON = exists-gated, 404-JSON = absent). OAuth STARTERS often escape the gate their
  exchange sits behind — the starter side is testable from datacenter vantage even when
  the exchange is not.
- **Region-deny shapes drift:** a clean 403 on a route can become an unhandled 500 crash
  between sessions. Re-probe the wall each engagement session; never assume the old
  status class still holds.
- **Socket transport walls:** polling `400 Transport unknown` / `400 Bad handshake
  method` = websocket-only namespace; CF 403 on python WS upgrades = vantage limitation.
  Log both as coverage and move on.
- **CMS/deep-content regex sweeps false-positive massively** on Contentful-style link IDs
  (`SKLyX0GT...`, `pkY...`) matching sk-/pk-prefixed secret patterns — thousands of hits,
  zero secrets. Whack-list linkType/sys contexts before reporting counts.
- **Mint endpoints ignore bodies:** a scope-mint that returns a token for EVERY body
  (grant_type=password with credentials, empty {}, garbage) proves the mint has no
  credential oracle — the response SHAPE across bodies is the finding, not the tokens.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
