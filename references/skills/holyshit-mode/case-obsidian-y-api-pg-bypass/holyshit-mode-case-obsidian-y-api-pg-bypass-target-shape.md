# Target shape

- source canon: `holyshit-mode/case-obsidian-y-api-pg-bypass.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

"Obsidian Y API" — OpenAI-compatible multi-provider gateway on Render (Flask-class: 405s return
`<h1>Method Not Allowed</h1>` HTML, app-JSON 404s are `{"error":...}` 60-byte). Three hand-rolled
pages: `/docs`, `/playground`, `/status`. No openapi.json (not FastAPI). Docs advertise:
"Requests without a key still work but are rate-limited per IP address" (on /v1 — turned out
FALSE: 401 regardless of IP-based fallback), Bearer keys issued per user.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
