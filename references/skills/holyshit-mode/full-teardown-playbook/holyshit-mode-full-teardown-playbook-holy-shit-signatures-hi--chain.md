# HOLY SHIT SIGNATURES — highest-yield quick checks (one probe each) — chain composition

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-holy-shit-signatures-hi.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. Dangling CNAME → takeover
2. Deployed .map sourcemap → full source
3. Ghost route with no auth (content-type verified)
4. ?token= / ?discord_token= URL param session fixation
5. Metadata endpoint SSRF (169.254.169.254)
6. Stateless claim/verification gate (no server callback anywhere)
7. Client-only payment/credits/permission gate
8. Zero-call-site auth scaffolding (unwired gate = lockout or bypass depending on direction)
9. Public bucket with creds/backups
10. Rate limiter keyed to a header you control (X-Forwarded-For honored = unlimited budget)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
