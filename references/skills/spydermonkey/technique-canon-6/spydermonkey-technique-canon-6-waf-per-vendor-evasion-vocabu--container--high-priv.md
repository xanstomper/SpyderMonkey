# WAF per-vendor evasion vocabulary (documented classes) — container / high-priv

- source canon: `spydermonkey/technique-canon-6.md`
- base technique: `spydermonkey-technique-canon-6-waf-per-vendor-evasion-vocabu.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **container** · auth **high-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

The encoding vocabulary exists FOR the WAF tier (canon-I hardened state): double-encode, unicode, case-split, comment-split — one variant per request, the differential must clear WITHOUT tripping. Decisive test: variant-acceptance vs WAF-flag delta on your own benign probe.

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
