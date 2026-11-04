# Target shape — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-pg-bypass.md`
- base technique: `holyshit-mode-case-obsidian-y-api-pg-bypass-target-shape.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

"Obsidian Y API" — OpenAI-compatible multi-provider gateway on Render (Flask-class: 405s return
`<h1>Method Not Allowed</h1>` HTML, app-JSON 404s are `{"error":...}` 60-byte). Three hand-rolled
pages: `/docs`, `/playground`, `/status`. No openapi.json (not FastAPI). Docs advertise:
"Requests without a key still work but are rate-limited per IP address" (on /v1 — turned out
FALSE: 401 regardless of IP-based fallback), Bearer keys issued per user.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
