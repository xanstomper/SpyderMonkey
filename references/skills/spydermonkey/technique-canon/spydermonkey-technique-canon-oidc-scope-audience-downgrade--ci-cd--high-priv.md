# OIDC scope/audience downgrade — ci-cd / high-priv

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-oidc-scope-audience-downgrade.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **ci-cd** · auth **high-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Resource servers trust the AS's audience tag; an attacker-controlled client registration (or a lax AS) can mint tokens for scopes the principal never granted. Decisive test: request scope=X with prompt=none from a fresh session and compare the minted token's scope/aud claims against the consent screen's promises — a delta is the finding.

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
