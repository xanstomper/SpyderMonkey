# Where the wall is — chain composition

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-where-the-wall-is.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Everything interesting sits behind:
1. **Google session** — /api/chat plan-tier tampering, /api/usage IDOR, /api/apikey authz (can user A read user B's key?)
2. **Admin session** — admin API depth, session fixation, CSRF on state-changing admin POSTs, privilege escalation via mass assignment on /api/admin/users/:id

Pre-auth surface exhausted. The next decisive test REQUIRES credentials.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
