# Key Vault posture — kubernetes / low-priv

- source canon: `spydermonkey/technique-canon-8.md`
- base technique: `spydermonkey-technique-canon-8-key-vault-posture.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **kubernetes** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Vaults with public network access + soft-delete absent. Decisive test: public reachability of the vault endpoint = the posture row.

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
