# Keychain-keystore inventory — embedded / service

- source canon: `spydermonkey/technique-canon-12.md`
- base technique: `spydermonkey-technique-canon-12-keychain-keystore-inventory.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- context: **embedded** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: banner/identity reads only on in-scope industrial tiers — control writes are the absolute wall
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

Secrets outside hardware-backed keystores. Decisive test: software-backed key material on your build = the row.

## Probe adjustment (embedded × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
