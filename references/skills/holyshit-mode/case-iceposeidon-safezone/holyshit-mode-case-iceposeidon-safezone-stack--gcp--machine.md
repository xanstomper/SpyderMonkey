# Stack — gcp / machine

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-stack.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gcp** · auth **machine** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Static: Astro on Cloudflare Pages (iceposeidon.com), React islands `/_astro/*.js`, Stripe in CSP.
- API: `api.iceposeidon.com` — Caddy origin behind CF. Typed aspida-style client in `cx-client.zJQN-0cw.js`. Auth = Kick OAuth session cookie (`credentials:'include'`; login entry `api.iceposeidon.com/oauth/login/kick`). No Bearer anywhere.
- Event: `event-public.iceposeidon.com` — separate host: `/event/config`, `/event/contestants`, `/event/map-snapshot` — NOT origin-blocked (2026-10-20).
- Live event running: contestants (HP/sigils/inventory), viewer deliveries, prediction polls.

## Probe adjustment (gcp × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
