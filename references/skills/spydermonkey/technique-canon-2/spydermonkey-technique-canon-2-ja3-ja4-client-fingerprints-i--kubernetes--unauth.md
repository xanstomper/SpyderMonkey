# JA3/JA4 client fingerprints (infra intel) — kubernetes / unauth

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-ja3-ja4-client-fingerprints-i.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **kubernetes** · auth **unauth** · chain role **entry**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Fingerprint the EGRESS the service expects vs accepts — anomalies map bot-walls and API tiers. Decisive test: same request two fingerprints — differential handling = the intel (register as recon, not vuln).

## Probe adjustment (kubernetes × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
