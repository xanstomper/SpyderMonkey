# 1. Find the production protocol version FIRST

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-04

## The technique

- The page's own socket URL carries it: `EIO=3` (socket.io v2) vs `EIO=4` (v4). A site can run BOTH on the same `/socket.io/` path — they are DIFFERENT server instances with DIFFERENT namespace registrations. Test BOTH. Evidence: g***REDACTED*** ran EIO=3 in production (full namespace set incl. game namespaces) while EIO=4 was a secondary instance missing namespaces (`slotsArena` existed only on EIO=3). Testing one protocol = an incomplete engagement.
- Harvest namespace names from the client bundle (`socketioNamespaces.chat` literals; per-game `math.config.socketioNamespace`) before connecting.
- Per-store config objects (`socketioRoot`) can point at DIFFERENT hosts per namespace on multi-service stacks — if a namespace rejects on the main host, check the config source for alternate roots.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
