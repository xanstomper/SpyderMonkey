# Zero server-side CSRF enforcement (score 45, hypothesis for browser-exploit) — chain composition

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-zero-server-side-csrf-e.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`PUT /api/settings` returns 200 with `Origin: evil.com` AND no Origin. Only SameSite=Lax blocks browser exploitation — one flag from drive-by config hijack. Server does no verification.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
