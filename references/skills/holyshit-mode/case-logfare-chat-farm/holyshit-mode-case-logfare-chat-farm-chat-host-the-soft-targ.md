# CHAT HOST — the soft target (the Holy Shit, score 75)

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

### Origin-header gate = string match, not security
`/api/*` on chat host returns 403 for evil/null/absent Origin. But:
1. `Origin: https://chat.logfare.ai` from curl bypasses entirely.
2. Discriminator: `GET /api/models` → 403 with evil Origin, 200 with allowed Origin — reveals the gate is header-only.
3. `POST /api/chat` with allowed Origin → server MINTS anon `lfc_session` cookie (HttpOnly; Secure; SameSite=Lax; **Max-Age 7776000 = 90 days**) and completes the request.
4. **Existing sessions work with NO Origin header at all** — Origin required only at MINT.

### The chain
```
Spoof Origin → POST /api/chat {"message":"...","model":"logfare/auto"}
  → anon lfc_session minted (unlimited, 90d) → real SSE completions
  → ~30 reqs + 3 parallel long completions (1.7k/1k/2.7k tokens), zero 429s
```
Free unauth inference farm on Claude-class upstreams, bill-drain vector for a donation-funded service. Bounded test only (~40k tokens).

### Stored system_prompt hijack (score 60)
`PUT /api/settings {"system_prompt": "You are AttackerBot..."}` → injected verbatim into model context on all subsequent completions (proof: reply began `[HIJACKED] I am AttackerBot`). Persistent persona control per session. Test with marker-prefixed directive.

### Zero server-side CSRF enforcement (score 45, hypothesis for browser-exploit)
`PUT /api/settings` returns 200 with `Origin: evil.com` AND no Origin. Only SameSite=Lax blocks browser exploitation — one flag from drive-by config hijack. Server does no verification.

### SSE base64 envelope parsing
Chat streams `data: <base64(json)>`. Decode with padding fix:
```python
b = line[6:].strip(); d = json.loads(base64.b64decode(b + '='*(-len(b)%4)))
```
- First chunk carries `usage` with prompt_tokens (empty completion_tokens); final `logfare_complete:true` chunk has totals.
- Parse ALL chunks, not just the last line — file tail can have corruption; use `errors='replace'`.
- `X-Conversation-Id` / `X-Message-Id` response headers; `/api/conversations` lists session history.

### Endpoints on chat host (all Origin-gated, all real JSON)
`/api/health {status,version}` · `/api/models` (full tier/visibility/premium intel; leaks hidden default `claude-sonnet-4.5` not in public list) · `/api/chat` · `/api/conversations` (GET list / PATCH / DELETE per-id) · `/api/settings` (GET/PUT) · `/api/consent` (GET: `{tier:"anonymous",can_use_premium:false,logged_in:false}`).

### Session-ID attacker-chosen acceptance (score 50, confirmed)
Server accepts ANY client-supplied `lfc_session` uuid **verbatim** — no entropy check, no re-mint: send `Cookie: lfc_session=11111111-2222-4333-8444-555566667777` and the server persists it via Set-Cookie, then creates conversations + settings on the chosen id. Cookie-fixation class; brute is closed (uuid v4, 122-bit) but issuance has zero integrity. Weaponization needs an injection vector or parent-domain cookie-toss (sibling subdomain setting cookies for `.logfare.ai`) — subdomain sweep is the open follow-up.

### SvelteKit chunk walk (client-API call-site discovery)
`index.html` → `entry/start.<hash>.js` → `chunks/<hash>.js` → `nodes/<n>.<hash>.js`. The 358KB **node** chunk (not the tiny entry/app chunks) held ALL fetch call sites — including the correct `/api/conversations/${id}/messages` subresource that guessed paths missed (all wrong guesses 404'd). Don't guess subresource paths; read the framework's lazy-loaded page chunks.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
