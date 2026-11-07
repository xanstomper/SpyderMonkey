# Region-wall discriminator (auth-plane 403 ≠ IP-quality) — iot-edge / unauth

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- base technique: `holyshit-mode-engagement-vantage-policy-region-wall-discrimi.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iot-edge** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Datacenter vantage + `403 general.Forbidden` on auth endpoints while READ surfaces (feeds,
sockets, configs) answer 200 = a RESTRICTED-MARKET geo block on the vantage, not IP-quality.
Confirm via the target's own signal: the realtime socket pushes `blocked:{reason:"region_page",
location:"de"}` naming the geolocated country. Never churn request variants on ONE route
(signing modes, address casings, claimed country params) — they fail identically and the
churn burns the vantage. DO sweep route BREADTH once per route: the region gate is
PER-ROUTE, not per-host — one host answered `/auth/token` 201, `/auth/blockCheck` 200,
`/auth/web3` 403, and `/auth/steam` + `/auth/google` 302 in the same engagement. The 302
OAuth login starters (steam/google/discord) are the likeliest exemptions, so probe every
login-method starter BEFORE declaring the auth plane walled. Gated routes need a
residential unrestricted vantage; open starters do not — say once which is which.

## Probe adjustment (iot-edge × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
