# The cycle — graphql / high-priv

- source canon: `dojo/range-playbook.md`
- base technique: `dojo-range-playbook-the-cycle.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **graphql** · auth **high-priv** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

1. catalog: what can be built (9 classes × flaw × seam × canon)
2. build: replica up on the lab port
3. strike: the family engines run their real probes against the replica
4. mirror: every confirmed strike becomes a kage rule — the lesson ends detected

## Probe adjustment (graphql × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
