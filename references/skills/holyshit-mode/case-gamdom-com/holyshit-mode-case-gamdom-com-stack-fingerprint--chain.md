# Stack fingerprint — chain composition

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-stack-fingerprint.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
