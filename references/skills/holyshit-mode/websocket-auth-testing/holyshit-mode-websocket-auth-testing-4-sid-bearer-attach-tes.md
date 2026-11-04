# 4. Sid bearer-attach test

- source canon: `holyshit-mode/websocket-auth-testing.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

engine.io sessions authenticate by sid alone unless the app binds them server-side:
open a SECOND websocket against a LIVE session's sid (`?...&sid=<victim sid>`).
`101 Switching Protocols` + answered pings = the sid is a single-secret bearer
credential. The websocket Origin allowlist is client-asserted (header VALUE
comparison at handshake) — trivially faked from non-browser clients, so it does not
protect the session. A leaked sid (access logs, any reflection) on an AUTHED socket
= full event-stream takeover. Remediation to state: bind socket sessions to the HTTP
session cookie server-side (reject connections whose cookie doesn't match the
handshake session).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
