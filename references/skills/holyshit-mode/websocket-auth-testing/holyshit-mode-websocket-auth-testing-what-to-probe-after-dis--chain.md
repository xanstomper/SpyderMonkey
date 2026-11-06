# What to Probe After Discovering the Auth Pattern — chain composition

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-what-to-probe-after-dis.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Vector | Test |
|--------|------|
| Token reuse across users | Get token as user A, use on user B's resources |
| Token replay | Use the same token twice |
| Token expiry | Wait 5/30/60 min, retry |
| Token forgery | Guess the structure (UUID? JWT? random?) |
| Session-cookie substitute | Send session cookie in upgrade headers, skip token frame |
| Mass assignment on token source | POST `/api/.../session` with `{"unlimited":true,"isAdmin":true}` |
| Origin bypass | Strip Origin header from upgrade request |
| First-frame type confusion | Send `{"type":"ready"}` instead of `{"type":"authenticate",...}` |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
