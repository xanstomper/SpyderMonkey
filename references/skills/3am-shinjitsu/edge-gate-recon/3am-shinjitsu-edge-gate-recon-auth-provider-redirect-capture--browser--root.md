# Auth-provider redirect capture (before driving any login form) — browser / root

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- base technique: `3am-shinjitsu-edge-gate-recon-auth-provider-redirect-capture.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **browser** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- When a login button hops to an external IdP, capture the FULL redirect URL from the
  click (don't just follow it): `openid.realm`, `openid.return_to`, and ticket params
  (`e`/`h`/`s` style) reveal the trust anchor and whether return_to is pinned to a
  dedicated login host.
- Rotating login-infra domains (`loginN.<brand>.com` series) are CF-fronted API-only
  hosts — root returns an empty 404. DNS + banner ONE, then probe adjacent numbers to
  map the series; realm-pinning to the series is an anti-phishing control, not a flaw.
- Record the IdP form's field layout before invoking vault save (Steam:
  steamcommunity.com/openid/loginform/, username id `«r3»`, password `«r4»`, guard code
  `authcode` — the guard prompt arrives after password submit; have the enter_code path
  ready).

## Probe adjustment (browser × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
