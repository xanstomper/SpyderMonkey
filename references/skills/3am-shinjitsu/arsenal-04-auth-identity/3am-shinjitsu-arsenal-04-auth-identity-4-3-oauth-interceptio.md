# 4.3 OAuth interception harness (score 90 — the live decisive test)

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

- The 200/302 on the authorize page proves NOTHING (Discord validates at token-exchange,
  Google at render — provider split is the impact gate).
- DECISIVE: local listener (`oauth_callback_interceptor.py` pattern / webhook.site fallback)
  + `cloudflared tunnel --url http://localhost:8888` → grep the trycloudflare URL →
  `curl -s -o /dev/null -w '%{redirect_url}' '/auth/v1/authorize?provider=discord&redirect_uri=<tunnel>/cb'`
  → 302 Location carries attacker URI = GoTrue-side flaw (~8.1). Operator clicks the crafted
  authorize URL in a logged-in browser; `?code=` landing on listener = CONFIRMED takeover chain.
- Variant matrix: `http://evil.com/cb` (no HTTPS enforcement), `/callback/../../evil` (no
  normalization), `evil.com@legithost/cb` (userinfo confusion). `redirect_to` is a DIFFERENT
  benign param — dead provider query param (good false-positive discriminator).
- State tests: 2× /start → state A,B; `callback?state=A&code=fake` + cookie B → `bad_oauth_state`
  = hardened. No-cookie/no-state → 400. `redirect_uri=evil` on /start returning the HARDCODED
  callback verbatim = ignored (fast negative).
- Provider app pages rendering generic code-entry for bogus client_ids = no enumeration oracle.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
