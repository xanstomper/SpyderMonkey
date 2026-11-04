# 1. Namespace discovery — wait for the rejection frame — mobile / low-priv

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-1-namespace-discovery-w.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- context: **mobile** · auth **low-priv** · chain role **pivot**

## Context

- platform: family probes cover the class
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Unknown namespaces STILL ack `40` (connected) immediately; the server sends
`44<ns>,"Invalid namespace"` only after ~1-2 seconds. A recv window shorter than
that misreads EVERY namespace as live. Connect, then listen ≥2s per namespace and
classify: `40<ns>,` kept = real, `44` follows = rejected.

Then map the RPC layer — socket.io apps often route RPCs over HTTP as a SEPARATE
surface (`POST /stream<ns>/rpc/<method>` with body `{"type":"rpc","arg":...}`).
Existence oracle: unknown method → literal `unknown rpc`; live method, bad args →
`Invalid parameters`; dead namespace path → Express `Cannot POST`. Cross the two
axes for a full method×namespace map with zero credentials.

## Probe adjustment (mobile × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
