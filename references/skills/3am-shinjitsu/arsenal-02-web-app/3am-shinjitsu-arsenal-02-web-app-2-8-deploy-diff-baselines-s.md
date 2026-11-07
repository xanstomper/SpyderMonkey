# 2.8 Deploy-diff baselines (score 70, mandatory on re-engage)

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Store per-bundle: sha256[:12], `?v=` param, Content-Length. Same hash = stale, skip to decay
  probes; new hash + `?v=` bump = full re-probe.
- SSR-rebuild discriminator: prior SPA now server-rendered (inline `<script>`, no hashed bundle)
  → diff `openapi.json` route lists instead of bundle hashes.
- Decayed findings re-verified BEFORE citing; wall SHAPES re-tested (403 can become 500).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
