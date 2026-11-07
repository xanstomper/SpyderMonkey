# Stack fingerprint — container / high-priv

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-stack-fingerprint.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **high-priv** · chain role **entry**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
