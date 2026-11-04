# SSE base64 envelope parsing — chain composition

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-sse-base64-envelope-par.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Chat streams `data: <base64(json)>`. Decode with padding fix:
```python
b = line[6:].strip(); d = json.loads(base64.b64decode(b + '='*(-len(b)%4)))
```
- First chunk carries `usage` with prompt_tokens (empty completion_tokens); final `logfare_complete:true` chunk has totals.
- Parse ALL chunks, not just the last line — file tail can have corruption; use `errors='replace'`.
- `X-Conversation-Id` / `X-Message-Id` response headers; `/api/conversations` lists session history.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
