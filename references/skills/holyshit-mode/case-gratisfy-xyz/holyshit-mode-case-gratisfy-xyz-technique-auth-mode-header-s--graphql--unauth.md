# Technique: auth-mode header split discovery — graphql / unauth

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-technique-auth-mode-header-s.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Multi-tenant SPA bundles carry an auth-mode selector header (`X-Chat-Auth-Mode: account|platform_key`). The error chain enumerates itself: endpoint bare → 400 naming the header → each value names the next required credential. Each branch validates DIFFERENT credentials against DIFFERENT backends — treat each branch as its own auth surface.

## Probe adjustment (graphql × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
