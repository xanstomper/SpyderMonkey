# 1. Find the production protocol version FIRST — chain composition

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-1-find-the-productio.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- The page's own socket URL carries it: `EIO=3` (socket.io v2) vs `EIO=4` (v4). A site can run BOTH on the same `/socket.io/` path — they are DIFFERENT server instances with DIFFERENT namespace registrations. Test BOTH. Evidence: gamdom ran EIO=3 in production (full namespace set incl. game namespaces) while EIO=4 was a secondary instance missing namespaces (`slotsArena` existed only on EIO=3). Testing one protocol = an incomplete engagement.
- Harvest namespace names from the client bundle (`socketioNamespaces.chat` literals; per-game `math.config.socketioNamespace`) before connecting.
- Per-store config objects (`socketioRoot`) can point at DIFFERENT hosts per namespace on multi-service stacks — if a namespace rejects on the main host, check the config source for alternate roots.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
