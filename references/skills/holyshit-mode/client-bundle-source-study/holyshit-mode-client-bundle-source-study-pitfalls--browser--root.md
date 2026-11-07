# Pitfalls — browser / root

- source canon: `holyshit-mode/client-bundle-source-study.md`
- base technique: `holyshit-mode-client-bundle-source-study-pitfalls.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **browser** · auth **root** · chain role **pivot**

## Route

- probes: `wpscan`, `cmseek`, `droopescan`, `cmsmap`, `nmap-wp-plugins`, `nmap-drupal-enum`
- chains: `cms-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

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

## Probe adjustment (browser × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
