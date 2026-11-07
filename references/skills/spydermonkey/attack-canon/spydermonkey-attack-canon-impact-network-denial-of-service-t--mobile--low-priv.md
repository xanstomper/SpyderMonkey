# Impact Network Denial of Service (T1498) — mobile / low-priv

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-impact-network-denial-of-service-t.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- context: **mobile** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: family probes cover the class
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: volumetric DoS
- probe: REFUSED — rate-limit bypass classes are proven with 2 requests, never a flood
- wall: proof = the differential, not the outage

## Probe adjustment (mobile × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
