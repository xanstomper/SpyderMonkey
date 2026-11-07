# 4. RPC surface: HTTP-proxy pattern vs socket emits — windows / root

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-4-rpc-surface-http-p.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **windows** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- Some stacks proxy RPC over HTTP POST `/stream<ns>/rpc/<method>` (body `{"type":"rpc","arg":...}`) while the socket stays receive-only. Extract the method table from the bundle's `.rpc.<method>(` call sites; extract ARG SHAPES from the shared io-ts/zod schema library the client imports (validation enums ship inline — grab WalletUnit/currency enum literals to build valid shapes).
- Method-existence oracle: unknown method → `unknown rpc`; known method with wrong args → `Invalid parameters`; dead namespace → Express-style `Cannot POST`. Maps the server's method table with zero auth.
- Gate order: a VALID-shaped arg changes the response to a session error (`Not logged in`, generic, or `You are not connected...`) — the auth check is only reachable with correct shapes. The session check may bind to a server-issued token exchanged at page load: a bare engine sid + `io` cookie is NOT enough — expect the session error until the full bootstrap exists.

## Probe adjustment (windows × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
