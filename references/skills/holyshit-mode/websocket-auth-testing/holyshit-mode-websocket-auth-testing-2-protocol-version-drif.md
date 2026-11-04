# 2. Protocol-version drift — test BOTH EIO versions

- source canon: `holyshit-mode/websocket-auth-testing.md`
- bindings: **WSTG-CLNT-05** · **CWE-345** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

Servers frequently expose socket.io v2 (`EIO=3`) AND v4 (`EIO=4`) simultaneously,
and the production client often speaks the OLDER one. Synthetic testing against the
wrong protocol version tests a surface the real app doesn't use. Grab the production
URL from page traffic (`wss://host/socket.io/?EIO=3&transport=websocket&sid=...`)
and mirror its version.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
