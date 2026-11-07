# Phase 4: Endpoint Fingerprinting — linux / machine

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-phase-4-endpo.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **linux** · auth **machine** · chain role **entry**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- `/api/dashboard` → 200 unauth, 55KB stale telemetry (aggregate node health — no client IP logs)
- JS bundle revealed password-gated endpoints:
  - `x-refresh-password` → `/api/dashboard?refresh=1` (cache-bust)
  - `x-export-password` → `/api/export?days=N` (full data export)
- Both are shared secrets stored in sessionStorage (NOT per-user tokens)

## Probe adjustment (linux × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
