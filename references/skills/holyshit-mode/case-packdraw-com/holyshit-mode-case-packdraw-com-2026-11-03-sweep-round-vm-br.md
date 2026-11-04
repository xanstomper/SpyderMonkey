# 2026-11-03 sweep round (VM + browser)

- source canon: `holyshit-mode/case-packdraw-com.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- **Checkpoint bypass verified:** Security Checkpoint binds ONLY to apex/www. All
  78 fuzzed `*.packdraw.com` names resolve (wildcard DNS) and answer WITHOUT 429 from
  the datacenter (404s = catch-all Vercel). `packdraw.vercel.app` serves the app shell
  (old build era, SPA-fallback 200 ghosts for EVERY path incl /.git/HEAD, /.env,
  swagger, graphql — ghost discrimination, none are real); `/api/pusher/auth` on the
  alias = 405 (route exists). `staging.packdraw.com` = Vercel Authentication 401
  (password off — v1 curl/MCP-gated). WAF coverage = branded host only; tool-based
  attackers re-point to the alias/subdomain plane.
- **Prod API surface (definitive):** ~140-path dict via in-page fetch: only
  `/api/pusher/auth` is a real route (GET 405, POST 403 for every channel class incl.
  public names — realtime authz holds). `tokenize/iframe/config` = 200-HTML ghost on
  GET AND POST. No demo/open/seed/user/admin routes. No $ACTION_ID_ public actions.
  App architecture = SSR/RSC + auth-gated server actions; unauth data rides RSC.
- **Full path fuzz of the alias:** 134/134 paths = 200 SPA shell (ghosts); verified the
  shell is byte-identical to prove ghost status before discounting.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
