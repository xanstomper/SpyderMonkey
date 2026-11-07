# PHASE 3 — CLIENT-SIDE DEEP MINE

- source canon: `holyshit-mode/full-teardown-playbook.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- **Bundle inventory**: every script tag (app.js AND giveaway.js/providers.js/membership.js
  etc.), size baseline saved (`~/.hermes/scripts/<target>_baseline.json`).
- **Endpoint extraction**: regex /api/ from ALL bundles; diff against Wayback old versions —
  ghost routes (removed-from-frontend, still-live-backend).
- **Secrets sweep**: hardcoded keys, tokens, internal URLs, debug flags, sourcemaps (map files
  often still deployed — HOLY SHIT: full original source).
- **Client-only trust checks**: window.* globals, client-side gates (console-call bypass),
  client-side validation of payments/rates/limits.
- Deliverable: endpoint list (live vs ghost), secret findings, client-trust violations.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
