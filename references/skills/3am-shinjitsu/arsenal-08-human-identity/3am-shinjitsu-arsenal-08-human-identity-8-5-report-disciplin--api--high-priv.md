# 8.5 Report discipline — api / high-priv

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- base technique: `3am-shinjitsu-arsenal-08-human-identity-8-5-report-disciplin.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **api** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Every §8 finding ships as an EXPOSURE rating with the remediation, never as an attempted
  op. Cross-persona note: social ops are out of scope family-wide (kimiko/holyshit/3am §2).

## Probe adjustment (api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
