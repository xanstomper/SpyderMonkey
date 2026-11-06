# PHASE 3 — CLIENT-SIDE DEEP MINE — api / federated

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-3-client-side-dee.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **api** · auth **federated** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
