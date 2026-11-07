# 5. Unauth emit fencing — container / service

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-5-unauth-emit-fencing.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

Gated namespaces usually kill anonymous emitters: send a `42<ns>,["event",...]`
frame unauth and watch for the server's `41` (namespace disconnect) — that IS the
fence working. Log it; don't retry the emit. Order matters: fire benign probes
(say/lastRain) BEFORE gate probes (join moderators) — the first gated emit kills
the namespace and everything after it reads as "no reply".

## Probe adjustment (container × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
