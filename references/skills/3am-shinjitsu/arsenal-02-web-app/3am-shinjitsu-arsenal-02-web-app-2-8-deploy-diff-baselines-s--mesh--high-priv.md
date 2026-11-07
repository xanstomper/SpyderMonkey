# 2.8 Deploy-diff baselines (score 70, mandatory on re-engage) — mesh / high-priv

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-8-deploy-diff-baselines-s.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **mesh** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Store per-bundle: sha256[:12], `?v=` param, Content-Length. Same hash = stale, skip to decay
  probes; new hash + `?v=` bump = full re-probe.
- SSR-rebuild discriminator: prior SPA now server-rendered (inline `<script>`, no hashed bundle)
  → diff `openapi.json` route lists instead of bundle hashes.
- Decayed findings re-verified BEFORE citing; wall SHAPES re-tested (403 can become 500).

## Probe adjustment (mesh × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
