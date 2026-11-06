# Rule quality bar — host / low-priv

- source canon: `kage/mirror-playbook.md`
- base technique: `kage-mirror-playbook-rule-quality-bar.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **host** · auth **low-priv** · chain role **pivot**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- One attack class per rule (no kitchen-sink detection).
- Match on BEHAVIOR (hash/window/diff), not indicators — rules survive tool swaps.
- Every rule carries a re-fire test: the family re-fires the attack read-only
  and the rule MUST fire; a rule that cannot fire is a hypothesis.

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
