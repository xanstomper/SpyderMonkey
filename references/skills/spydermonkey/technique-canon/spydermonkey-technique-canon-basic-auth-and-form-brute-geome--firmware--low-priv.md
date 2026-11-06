# Basic-auth and form brute geometry — firmware / low-priv

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-basic-auth-and-form-brute-geome.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **firmware** · auth **low-priv** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

The brute class is a RATE problem before it is a CREDENTIAL problem: lockout windows, per-IP vs per-account throttling, and response-length uniformity decide feasibility. Decisive test: 5 wrong-password requests on one account, one on the next — a lockout on the first and none on the second means per-account throttling with per-IP rotation potential. Register the geometry (window, scope, response delta), never a harvested credential.

## Probe adjustment (firmware × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
