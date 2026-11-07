# Phase 3: SPA Route Discovery (Client-Side Secret Extraction) — edge-node / expired

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-phase-3-spa-r.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **edge-node** · auth **expired** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

- doc.example-target.org returned a Next.js SPA shell (21,395 bytes, identical for ALL paths — SPA fallback)
- Key technique: download and grep the JS bundle (`/_next/static/chunks/...`) instead of reading rendered HTML
- The JS bundle contained siteConfig and revealed `x-refresh-password`/`x-export-password` auth headers
- Also leaked: turnstile key, publicSignup flag, storageKeyPrefix — enough to understand the auth model

## Probe adjustment (edge-node × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
