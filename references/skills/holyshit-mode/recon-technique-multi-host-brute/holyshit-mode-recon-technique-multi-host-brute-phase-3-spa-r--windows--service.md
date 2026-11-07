# Phase 3: SPA Route Discovery (Client-Side Secret Extraction) — windows / service

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-phase-3-spa-r.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **windows** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- doc.f***REDACTED***.org returned a Next.js SPA shell (21,395 bytes, identical for ALL paths — SPA fallback)
- Key technique: download and grep the JS bundle (`/_next/static/chunks/...`) instead of reading rendered HTML
- The JS bundle contained siteConfig and revealed `x-refresh-password`/`x-export-password` auth headers
- Also leaked: turnstile key, publicSignup flag, storageKeyPrefix — enough to understand the auth model

## Probe adjustment (windows × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
