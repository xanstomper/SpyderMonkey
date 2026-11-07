# 6. Capture: reassemble continuation frames, sanitize binaries — grpc / root

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-6-capture-reassemble-co.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **grpc** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

Large socket.io events fragment across websocket frames (continuations, opcode 0).
A recv loop that treats one frame per message splices JSON at ~4KB boundaries and
"Unterminated string" parse errors. Read one FULL message per recv: loop until the
FIN bit, merging opcode-0 payloads into the opcode-1 message. Pongs and other
binary frames arrive as 2-byte opcodes mid-stream — strip `\x00-\x1f` control
bytes from captured text before any JSON parse. A mis-reassembled capture will make
a 90KB `initialize` event parse as a 4KB stub — size-check messages before
trusting field counts.

## Probe adjustment (grpc × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
