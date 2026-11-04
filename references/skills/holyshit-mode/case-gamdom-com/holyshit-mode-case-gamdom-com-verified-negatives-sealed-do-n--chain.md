# Verified negatives (sealed — do not re-probe without a code change) — chain composition

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-verified-negatives-sealed-do-n.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
