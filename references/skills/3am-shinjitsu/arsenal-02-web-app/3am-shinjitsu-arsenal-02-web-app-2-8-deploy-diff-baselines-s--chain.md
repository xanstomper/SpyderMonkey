# 2.8 Deploy-diff baselines (score 70, mandatory on re-engage) — chain composition

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-8-deploy-diff-baselines-s.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Store per-bundle: sha256[:12], `?v=` param, Content-Length. Same hash = stale, skip to decay
  probes; new hash + `?v=` bump = full re-probe.
- SSR-rebuild discriminator: prior SPA now server-rendered (inline `<script>`, no hashed bundle)
  → diff `openapi.json` route lists instead of bundle hashes.
- Decayed findings re-verified BEFORE citing; wall SHAPES re-tested (403 can become 500).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
