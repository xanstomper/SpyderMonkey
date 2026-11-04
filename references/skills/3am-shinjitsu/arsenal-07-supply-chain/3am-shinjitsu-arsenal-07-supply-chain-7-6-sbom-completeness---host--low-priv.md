# 7.6 SBOM completeness (score 55) — host / low-priv

- source canon: `3am-shinjitsu/arsenal-07-supply-chain.md`
- base technique: `3am-shinjitsu-arsenal-07-supply-chain-7-6-sbom-completeness-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **host** · auth **low-priv** · chain role **pivot**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Phantom deps (referenced, never shipped), license gaps as attack-surface indicators,
  reproducible-build validation on operator artifacts.

## Probe adjustment (host × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
