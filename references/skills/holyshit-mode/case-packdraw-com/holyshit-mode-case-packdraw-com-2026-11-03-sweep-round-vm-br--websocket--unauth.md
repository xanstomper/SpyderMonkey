# 2026-11-03 sweep round (VM + browser) — websocket / unauth

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-2026-11-03-sweep-round-vm-br.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (websocket × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
