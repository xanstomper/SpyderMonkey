# 5. Unauth emit fencing — chain composition

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-5-unauth-emit-fencing.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Gated namespaces usually kill anonymous emitters: send a `42<ns>,["event",...]`
frame unauth and watch for the server's `41` (namespace disconnect) — that IS the
fence working. Log it; don't retry the emit. Order matters: fire benign probes
(say/lastRain) BEFORE gate probes (join moderators) — the first gated emit kills
the namespace and everything after it reads as "no reply".

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
