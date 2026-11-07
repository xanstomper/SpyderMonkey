# 1. Find the production protocol version FIRST — browser / federated

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-1-find-the-productio.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **browser** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- The page's own socket URL carries it: `EIO=3` (socket.io v2) vs `EIO=4` (v4). A site can run BOTH on the same `/socket.io/` path — they are DIFFERENT server instances with DIFFERENT namespace registrations. Test BOTH. Evidence: g***REDACTED*** ran EIO=3 in production (full namespace set incl. game namespaces) while EIO=4 was a secondary instance missing namespaces (`slotsArena` existed only on EIO=3). Testing one protocol = an incomplete engagement.
- Harvest namespace names from the client bundle (`socketioNamespaces.chat` literals; per-game `math.config.socketioNamespace`) before connecting.
- Per-store config objects (`socketioRoot`) can point at DIFFERENT hosts per namespace on multi-service stacks — if a namespace rejects on the main host, check the config source for alternate roots.

## Probe adjustment (browser × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
