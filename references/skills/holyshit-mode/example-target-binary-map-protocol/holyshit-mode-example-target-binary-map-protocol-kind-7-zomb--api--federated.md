# Kind 7 — zombies (record size 37: `Ki=16` UUID, `Nd=37`) — api / federated

- source canon: `holyshit-mode/example-target-binary-map-protocol.md`
- base technique: `holyshit-mode-example-target-binary-map-protocol-kind-7-zomb.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **api** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- `o+0` u32 rosterSequence, `o+4` u32 slotsSequence, `o+8` f64 timeBase
- Per record: 16-byte UUID id, u16 ownerSlot, i32 expiresAtDelta (timeBase + v*100, gated by flag bit `$d`), f32 speedMps (gated `Wi`), u8 flags (top 3 bits reserved must be 0; `Ld`=guard), f32 leechIntervalSeconds, f32 leechRadiusM, u16 leechAmount.
- Roster ids must be strictly sorted (`Qu(a,b)<0`).

## Probe adjustment (api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
