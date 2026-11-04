# Stack

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- Static: Astro on Cloudflare Pages (iceposeidon.com), React islands `/_astro/*.js`, Stripe in CSP.
- API: `api.iceposeidon.com` — Caddy origin behind CF. Typed aspida-style client in `cx-client.zJQN-0cw.js`. Auth = Kick OAuth session cookie (`credentials:'include'`; login entry `api.iceposeidon.com/oauth/login/kick`). No Bearer anywhere.
- Event: `event-public.iceposeidon.com` — separate host: `/event/config`, `/event/contestants`, `/event/map-snapshot` — NOT origin-blocked (2026-10-20).
- Live event running: contestants (HP/sigils/inventory), viewer deliveries, prediction polls.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
