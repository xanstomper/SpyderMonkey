# String-table decoder replay — kubernetes / low-priv

- source canon: `spydermonkey/technique-canon-7.md`
- base technique: `spydermonkey-technique-canon-7-string-table-decoder-replay.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **kubernetes** · auth **low-priv** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Obfuscated chunk string arrays (New Relic-style regex, i18n maps, feature flags) decode deterministically offline. Decisive test: the decoded route/feature list against the live app — leaked-internal-naming = the finding.

## Probe adjustment (kubernetes × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
