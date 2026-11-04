# Command and Control Application Layer Protocol (T1071) — dns / low-priv

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-command-and-control-application-la.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **dns** · auth **low-priv** · chain role **pivot**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: C2 over 443/dns/http
- probe: out of family walls entirely
- wall: REFUSED — no C2 infrastructure, ever

## Probe adjustment (dns × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
