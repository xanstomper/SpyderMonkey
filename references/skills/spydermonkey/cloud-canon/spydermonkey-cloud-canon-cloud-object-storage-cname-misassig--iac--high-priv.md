# Cloud Object Storage CNAME Misassignment (CLOUD-OBJ-02) — iac / high-priv

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-object-storage-cname-misassig.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- context: **iac** · auth **high-priv** · chain role **pivot**

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- class: the service bucket still claimed — domtake's cloud cousin
- probe: the takeover engine's dangling-fingerprint class against cloud endpoints
- wall: NO-GAIN — claim status is proof; registration is never performed

## Probe adjustment (iac × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
