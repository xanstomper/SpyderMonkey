# 6. Capture: reassemble continuation frames, sanitize binaries

- source canon: `holyshit-mode/websocket-auth-testing.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Large socket.io events fragment across websocket frames (continuations, opcode 0).
A recv loop that treats one frame per message splices JSON at ~4KB boundaries and
"Unterminated string" parse errors. Read one FULL message per recv: loop until the
FIN bit, merging opcode-0 payloads into the opcode-1 message. Pongs and other
binary frames arrive as 2-byte opcodes mid-stream — strip `\x00-\x1f` control
bytes from captured text before any JSON parse. A mis-reassembled capture will make
a 90KB `initialize` event parse as a 4KB stub — size-check messages before
trusting field counts.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
