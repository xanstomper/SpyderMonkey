# Evidence & verdict rules — cloud / high-priv

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-evidence-verdict-rules.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **cloud** · auth **high-priv** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- **CONFIRMED** requires an authorized, minimal, non-destructive proof and a control check.
- **BLOCKED** means authorization, vantage, or tooling stopped the decisive test; name it.
- **HYPOTHESIS** means reasoned but unproven; include the exact gap and unlock condition.
- **N/A** requires a concrete reason (e.g. "no AI components deployed; inventory export
  dated 2026-11-03 confirms zero inference endpoints").
- Secrets are redacted in reports. Read-only access is used only to prove impact.
- Findings decay; record deployed version/build and re-verify before reuse.

## Probe adjustment (cloud × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
