# 7.4 Dependency confusion (score 80, OWNED namespace only) — kubernetes / high-priv

- source canon: `3am-shinjitsu/arsenal-07-supply-chain.md`
- base technique: `3am-shinjitsu-arsenal-07-supply-chain-7-4-dependency-confusi.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **kubernetes** · auth **high-priv** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Operator's private package names probed on public registries (npm/PyPI) — availability =
  confusion primitive. Typosquat detection on the operator's brand names.
- Workflow: query registry, never publish/register anything.

## Probe adjustment (kubernetes × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
