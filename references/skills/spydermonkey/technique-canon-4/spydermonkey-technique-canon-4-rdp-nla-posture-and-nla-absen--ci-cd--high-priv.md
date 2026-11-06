# RDP/NLA posture and NLA-absent classes — ci-cd / high-priv

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-rdp-nla-posture-and-nla-absen.md`
- bindings: **PTES-RA** · **CWE-287** · **ATT&CK T1078**
- context: **ci-cd** · auth **high-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

NLA required vs not (documented class), banner/tls posture. Decisive test: protocol handshake reaching the NLA stage — the stage reached IS the finding.

## Probe adjustment (ci-cd × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
