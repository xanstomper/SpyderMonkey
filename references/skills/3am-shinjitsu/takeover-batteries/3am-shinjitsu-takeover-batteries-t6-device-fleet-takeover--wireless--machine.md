# T6 — Device/fleet takeover — wireless / machine

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t6-device-fleet-takeover.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **wireless** · auth **machine** · chain role **final**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: LAB-ONLY — your own radios and stations; third-party airwaves are the absolute wall
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Default/leaked device creds → management plane (one login); firmware creds → adjacent
  services; MQTT subscribe map (never publish) on owned brokers; OT register reads
  (read-only); shared VPN/config creds across fleet.
- **DECISIVE PROOF:** management-plane login success or authenticated service
  enumeration. Then STOP.

## Probe adjustment (wireless × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
