# 3. Synthetic sockets: websocket transport only

- source canon: `holyshit-mode/websocket-auth-testing.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

Sequential HTTP polling from a script dies on CDN node affinity — each request lands
on a different backend and the in-memory session returns `"Session ID unknown"`.
One long-lived websocket connection is immune. And on EIO=3 the websocket-FIRST
handshake works with NO polling pre-step: `GET /socket.io/?EIO=3&transport=websocket`
(no sid) returns 101 and the server pushes `0{"sid":...}` as the first frame — own
session in one connection, no affinity problem. (Synthetic `io=<sid>` cookies do NOT
fix polling affinity — the cookie is not honored by the routing layer.)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
