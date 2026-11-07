# Code-search dorking (github/gitlab/gist) — edge-node / service

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-code-search-dorking-github-gi.md`
- bindings: **WSTG-CONF-04** · **CWE-538** · **ATT&CK T1552**
- context: **edge-node** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

Org-attribution via user-id chains (the SPY-067 class family), deleted-file recovery, committed secrets in value="" attributes, committed CSVs as QA telemetry. Decisive test: the recovered artifact itself (file/blob path) — the artifact is the evidence.

## Probe adjustment (edge-node × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
