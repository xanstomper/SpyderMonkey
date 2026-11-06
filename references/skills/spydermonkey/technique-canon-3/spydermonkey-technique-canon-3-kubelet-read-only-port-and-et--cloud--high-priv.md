# Kubelet read-only port and etcd exposure — cloud / high-priv

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-kubelet-read-only-port-and-et.md`
- bindings: **PTES-CON** · **CWE-250** · **ATT&CK T1610**
- context: **cloud** · auth **high-priv** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

10255 read-only /pods and etcd 2379 without client cert. Decisive test: GET /pods anonymous; etcd /version probe — read-only responses are the findings.

## Probe adjustment (cloud × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
