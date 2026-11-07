# Verified negatives (sealed — do not re-probe without a code change)

- source canon: `holyshit-mode/case-gamdom-com.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
