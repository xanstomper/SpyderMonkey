# 1. Namespace discovery — wait for the rejection frame — chain composition

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-1-namespace-discovery-w.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Unknown namespaces STILL ack `40` (connected) immediately; the server sends
`44<ns>,"Invalid namespace"` only after ~1-2 seconds. A recv window shorter than
that misreads EVERY namespace as live. Connect, then listen ≥2s per namespace and
classify: `40<ns>,` kept = real, `44` follows = rejected.

Then map the RPC layer — socket.io apps often route RPCs over HTTP as a SEPARATE
surface (`POST /stream<ns>/rpc/<method>` with body `{"type":"rpc","arg":...}`).
Existence oracle: unknown method → literal `unknown rpc`; live method, bad args →
`Invalid parameters`; dead namespace path → Express `Cannot POST`. Cross the two
axes for a full method×namespace map with zero credentials.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
