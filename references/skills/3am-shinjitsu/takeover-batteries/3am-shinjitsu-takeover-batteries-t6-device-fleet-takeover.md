# T6 — Device/fleet takeover

- source canon: `3am-shinjitsu/takeover-batteries.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- Default/leaked device creds → management plane (one login); firmware creds → adjacent
  services; MQTT subscribe map (never publish) on owned brokers; OT register reads
  (read-only); shared VPN/config creds across fleet.
- **DECISIVE PROOF:** management-plane login success or authenticated service
  enumeration. Then STOP.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
