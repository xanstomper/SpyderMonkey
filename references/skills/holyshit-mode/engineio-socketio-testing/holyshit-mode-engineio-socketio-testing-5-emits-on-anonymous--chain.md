# 5. Emits on anonymous sockets — chain composition

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-5-emits-on-anonymous.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Try socket events (`42/ns,["event",args]`) benign-first, gates LAST: many servers disconnect the namespace (`41`) on ANY unexpected emit, and the disconnect kills the rest of the probe queue.
- Receive-only anonymous sockets are a deliberate design on modern stacks — record as the fence, do not re-probe.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
