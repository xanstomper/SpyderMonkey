# PHASE 3 — CLIENT-SIDE DEEP MINE — grpc / machine

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-3-client-side-dee.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **grpc** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (grpc × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
