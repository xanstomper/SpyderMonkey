# Stack — chain composition

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-stack.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Static: Astro on Cloudflare Pages (iceposeidon.com), React islands `/_astro/*.js`, Stripe in CSP.
- API: `api.iceposeidon.com` — Caddy origin behind CF. Typed aspida-style client in `cx-client.zJQN-0cw.js`. Auth = Kick OAuth session cookie (`credentials:'include'`; login entry `api.iceposeidon.com/oauth/login/kick`). No Bearer anywhere.
- Event: `event-public.iceposeidon.com` — separate host: `/event/config`, `/event/contestants`, `/event/map-snapshot` — NOT origin-blocked (2026-10-20).
- Live event running: contestants (HP/sigils/inventory), viewer deliveries, prediction polls.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
