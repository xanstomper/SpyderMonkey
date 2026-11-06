# Lambda/env and secrets-in-plaintext classes — container / low-priv

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-lambda-env-and-secrets-in-pla.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **container** · auth **low-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Config exposure revealing plaintext env/secrets (e.g. error pages, config endpoints, downloadable artifacts). Decisive test: the artifact's own content — a live secret in a fetched artifact is the crown.

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
