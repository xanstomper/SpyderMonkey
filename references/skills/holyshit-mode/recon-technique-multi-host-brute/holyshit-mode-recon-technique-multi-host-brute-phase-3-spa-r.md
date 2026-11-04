# Phase 3: SPA Route Discovery (Client-Side Secret Extraction)

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- doc.freeinference.org returned a Next.js SPA shell (21,395 bytes, identical for ALL paths — SPA fallback)
- Key technique: download and grep the JS bundle (`/_next/static/chunks/...`) instead of reading rendered HTML
- The JS bundle contained siteConfig and revealed `x-refresh-password`/`x-export-password` auth headers
- Also leaked: turnstile key, publicSignup flag, storageKeyPrefix — enough to understand the auth model

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
