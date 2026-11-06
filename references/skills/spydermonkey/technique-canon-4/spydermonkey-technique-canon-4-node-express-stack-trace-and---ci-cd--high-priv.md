# Node/Express stack-trace and source disclosure — ci-cd / high-priv

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-node-express-stack-trace-and-.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **ci-cd** · auth **high-priv** · chain role **final**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Error handlers dumping stack + cwd, sourcemaps (already canon-I), .map on chunk files. Decisive test: forced error on a non-route — stack text with paths = the finding.

## Probe adjustment (ci-cd × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
