# CDN-Specific Gotchas — iot-edge / expired

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-cdn-specific-gotchas.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iot-edge** · auth **expired** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

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

## Probe adjustment (iot-edge × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
