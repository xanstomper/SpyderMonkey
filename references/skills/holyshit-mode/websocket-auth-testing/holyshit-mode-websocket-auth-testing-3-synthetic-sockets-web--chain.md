# 3. Synthetic sockets: websocket transport only — chain composition

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-3-synthetic-sockets-web.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Sequential HTTP polling from a script dies on CDN node affinity — each request lands
on a different backend and the in-memory session returns `"Session ID unknown"`.
One long-lived websocket connection is immune. And on EIO=3 the websocket-FIRST
handshake works with NO polling pre-step: `GET /socket.io/?EIO=3&transport=websocket`
(no sid) returns 101 and the server pushes `0{"sid":...}` as the first frame — own
session in one connection, no affinity problem. (Synthetic `io=<sid>` cookies do NOT
fix polling affinity — the cookie is not honored by the routing layer.)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
