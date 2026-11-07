# Stack fingerprint

- source canon: `holyshit-mode/case-gamdom-com.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- **gamdom.com**: Fastly (151.101.x) → nginx (`x-nginx-limit-req` header) → custom app. CSP nonce
  + `strict-dynamic`, HSTS. Sourcemaps **401 "Not authorized"** (protected — good). Vite SSR,
  612 code-split chunks; the full chunk map lives in the main `client.HASH.js` route table.
- **Auth**: Dynamic.xyz embedded-wallet SDK (email/passkey/social) + site account layer.
- **API prefixes**: `/client-api/*` (typed magic-Proxy client: `Bt("/client-api")` — every
  property chain = a POST endpoint), `/stream/<ns>/rpc/<method>` (RPC-over-HTTP for chat+dice
  only), `/user-api/*` (softblock-details, change-pp). Error envelope:
  `{message,name:GamdomMessage,_tag,type,info}`.
- **Production socket: `wss://gamdom.com/socket.io/?EIO=3&transport=websocket`** (socket.io v2,
  all namespaces multiplexed on ONE engine connection). An EIO=4 instance ALSO answers with a
  DIFFERENT namespace set — protocol-instance drift; test the instance the real app uses.
- **Family**: perabet.com = IDENTICAL stack (same Fastly IPs, verbatim error envelopes, smaller
  game suite). Turkish entrance funnel: `tr.perabet.com` + `giris.perabet.com` → 217.23.12.109
  (LeaseWeb, VestaCP box).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
