# 6. sid = bearer credential (attach test) — chain composition

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-6-sid-bearer-credent.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- A second websocket using an EXISTING sid attaches to that session (101 accepted, ping answered). The origin allowlist is client-asserted — it stops cross-site browser JS, NOT a scripted attacker who fakes the header.
- Mechanism test: obtain a live sid (page-context hook capturing socket OPEN frames, or your own session), attach a second socket from python, send `2` (v2 ping), expect pong. Do NOT emit application frames on an attached session.
- Impact gate: only AUTHED sockets carry personal events — the sid-attach is the mechanism finding; severity lives in what rides authed sessions.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
