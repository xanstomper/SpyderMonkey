# CDN-Specific Gotchas — ios / high-priv

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-cdn-specific-gotchas.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ios** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- **Cloudflare**: forwards the 101 upgrade transparently. The origin server sees
  the upgrade as a normal WebSocket. Spoofing `X-Forwarded-For`/`CF-Connecting-IP`
  on the upgrade returns `403 error 1000` — Cloudflare strips client-supplied IPs
  before proxying. IP rotation to bypass rate limits is NOT possible.

- **AWS CloudFront**: similar passthrough behavior. Check `via:` header to confirm
  CDN presence.

- **Origin behind multiple proxies**: the upgrade may pass through 2+ hops; auth
  may be enforced at any hop. If frames are rejected with no clear pattern,
  check whether the CDN itself is doing auth (e.g. Cloudflare Access).

## Probe adjustment (ios × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
