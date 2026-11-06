# CMS staging/debug artifacts — container / low-priv

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-cms-staging-debug-artifacts.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- context: **container** · auth **low-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

debug.log, install.php residual, backup SQL dumps under webroot. Decisive test: control-path differential (never trust a 200 shell) — distinct content = the harvest finding.

## Probe adjustment (container × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
