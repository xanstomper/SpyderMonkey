# Rule quality bar — worker / root

- source canon: `kage/mirror-playbook.md`
- base technique: `kage-mirror-playbook-rule-quality-bar.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **worker** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- One attack class per rule (no kitchen-sink detection).
- Match on BEHAVIOR (hash/window/diff), not indicators — rules survive tool swaps.
- Every rule carries a re-fire test: the family re-fires the attack read-only
  and the rule MUST fire; a rule that cannot fire is a hypothesis.

## Probe adjustment (worker × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
