# Verified negatives (sealed — do not re-probe without a code change) — cloud / unauth

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-verified-negatives-sealed-do-n.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **cloud** · auth **unauth** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Main authz: valid-shaped unauth POSTs to 7 gated `/client-api` endpoints → uniform
  `specific:unknown`. Gate order = validation→auth→nothing executes.
- CORS: no ACAO reflection. Sourcemaps 401. dashboard.gamdom.com = nginx 403 (IP-gated).
- CSWSH: websocket transport validates Origin (evil/null/absent → 400). Anon socket EMITS →
  server sends `41` disconnect. `/crypto` ns silent unauth.
- Registration: Fastly VCL blocks non-browser TLS on `POST /signup` (400 err 54113) + server
  demands a Turnstile token (`Captcha required` FAILED state in a real browser; widget never
  renders in harness). Bots dead at both layers.
- Exim 4.97.1 (patched range — no CVE-2019-10149). MariaDB default creds denied. No source
  disclosure (`.git`/`.env`/backups 404). No hidden prefixes (`/api`,`/v1`,`/graphql`,... =
  SPA-shell 404). `/admin/*` = 302→404 decoy. Blog = same custom stack (no CMS). No service
  workers. `/panic-block-account` = SPA route, not API.
- DNS: gamdom zone sealed (150-word sweep), all gamdom TLDs defensively registered, NS =
  Route53 (gamdom) / GoDaddy (perabet), recursion+AXFR refused on the fossil box. beta.perabet.com
  = same build as prod (alias). old/static.perabet.com = dead hosts, stale DNS.
- **crash_hash_chain_verifies (40, the anti-WhiteArmor weapon)**: `sha256(later-round-hash as
  ascii) == earlier-round-hash` EXACT across 3 chain links / 2 sessions. The documented 10M-hash
  chain EXISTS and is publicly verifiable — retroactively unforgeable. Rebuttal package for any
  "PF is fake" claim: two consecutive hashes + one sha256 call. The bustabit derivation does NOT
  match (gamdom uses its own curve — lives in the client math code).

## Probe adjustment (cloud × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
