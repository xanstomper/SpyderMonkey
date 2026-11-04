# Phase 4: Endpoint Fingerprinting — chain composition

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-phase-4-endpo.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `/api/dashboard` → 200 unauth, 55KB stale telemetry (aggregate node health — no client IP logs)
- JS bundle revealed password-gated endpoints:
  - `x-refresh-password` → `/api/dashboard?refresh=1` (cache-bust)
  - `x-export-password` → `/api/export?days=N` (full data export)
- Both are shared secrets stored in sessionStorage (NOT per-user tokens)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
