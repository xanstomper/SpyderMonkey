# The wall — aws / high-priv

- source canon: `holyshit-mode/case-gratisfy-reengagement2.md`
- base technique: `holyshit-mode-case-gratisfy-reengagement2-the-wall.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **aws** · auth **high-priv** · chain role **pivot**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Every remaining path needs either (a) an app endpoint that trusts `user_metadata.role`, or (b) OTP TTL >> brute time (needs ~10× throughput). GoTrue redirect_uri override remains confirmed-but-blocked at Discord (strict URI registration; live listener test = Discord "Invalid OAuth" rejection).

## Probe adjustment (aws × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
