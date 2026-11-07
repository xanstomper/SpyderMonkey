# SvelteKit chunk walk (client-API call-site discovery) — chain composition

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-sveltekit-chunk-walk-cl.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`index.html` → `entry/start.<hash>.js` → `chunks/<hash>.js` → `nodes/<n>.<hash>.js`. The 358KB **node** chunk (not the tiny entry/app chunks) held ALL fetch call sites — including the correct `/api/conversations/${id}/messages` subresource that guessed paths missed (all wrong guesses 404'd). Don't guess subresource paths; read the framework's lazy-loaded page chunks.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
