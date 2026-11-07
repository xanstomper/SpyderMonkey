# 3.8 Unauth token-mint (score 80) — mesh / low-priv

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-8-unauth-token-mint-score-80.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **mesh** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- PATTERN: `POST /auth/token?scope=X` mints RS256 JWTs unauth, signs ANY client scope.
- Map CONSUMERS first (bundle vocabulary: sub/admin/mod/internal/system + websocket identity);
  any-scope mint + proven privileged consumer = chain; inert HTTP plane + server-side room
  enforcement = ~45. Test EVERY implied sub value incl. a second mint on the OAuth-authority
  host (bare `/token` may mint `sub=websocket` with a GLOBAL constant id).
- Uniform 403 in bearer AND query delivery = mint inert on HTTP plane; state both planes.

## Probe adjustment (mesh × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
