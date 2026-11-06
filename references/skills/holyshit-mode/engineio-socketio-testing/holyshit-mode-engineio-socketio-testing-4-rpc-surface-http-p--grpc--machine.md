# 4. RPC surface: HTTP-proxy pattern vs socket emits — grpc / machine

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-4-rpc-surface-http-p.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **grpc** · auth **machine** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Some stacks proxy RPC over HTTP POST `/stream<ns>/rpc/<method>` (body `{"type":"rpc","arg":...}`) while the socket stays receive-only. Extract the method table from the bundle's `.rpc.<method>(` call sites; extract ARG SHAPES from the shared io-ts/zod schema library the client imports (validation enums ship inline — grab WalletUnit/currency enum literals to build valid shapes).
- Method-existence oracle: unknown method → `unknown rpc`; known method with wrong args → `Invalid parameters`; dead namespace → Express-style `Cannot POST`. Maps the server's method table with zero auth.
- Gate order: a VALID-shaped arg changes the response to a session error (`Not logged in`, generic, or `You are not connected...`) — the auth check is only reachable with correct shapes. The session check may bind to a server-issued token exchanged at page load: a bare engine sid + `io` cookie is NOT enough — expect the session error until the full bootstrap exists.

## Probe adjustment (grpc × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
