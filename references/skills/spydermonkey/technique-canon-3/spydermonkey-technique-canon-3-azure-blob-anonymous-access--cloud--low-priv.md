# Azure blob anonymous access — cloud / low-priv

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-azure-blob-anonymous-access.md`
- bindings: **PTES-CON** · **CWE-250** · **ATT&CK T1611**
- context: **cloud** · auth **low-priv** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Container-level public access (list/get). Decisive test: anonymous LIST on the container endpoint — the listing is the finding.

## Probe adjustment (cloud × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
