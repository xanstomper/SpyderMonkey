# GCP metadata and service-account surface — linux / high-priv

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-gcp-metadata-and-service-acco.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- context: **linux** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

metadata.google.internal classes + service-account key exposure in artifacts. Decisive test: metadata header requirement (Metadata-Flavor) honored/refused — the delta is the posture.

## Probe adjustment (linux × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
