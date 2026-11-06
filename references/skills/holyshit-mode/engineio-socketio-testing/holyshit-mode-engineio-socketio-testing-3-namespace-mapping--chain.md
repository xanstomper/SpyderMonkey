# 3. Namespace mapping — chain composition

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-3-namespace-mapping.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Send `40/nsp,` (v4; v2 accepts with/without trailing comma). The bare `40` = engine ack; the namespace ack FOLLOWS — wait 2-4s and read frames in order. `40/nsp,` = LIVE; `44/nsp,"Invalid namespace"` = rejected.
- Live namespaces push an initialize/state event on connect (leaderboards, players online, prize data) — capture it; it is often the most data-rich unauth feed on the platform.
- Fuzz extra names (`/admin`, `/mod`, `/staff`, `/internal`, `/prediction`, `/sports`) — expect `44` on hardened stacks; log as negative coverage.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
