# 2026-11-03 sweep round (VM + browser) — chain composition

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-2026-11-03-sweep-round-vm-br.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
