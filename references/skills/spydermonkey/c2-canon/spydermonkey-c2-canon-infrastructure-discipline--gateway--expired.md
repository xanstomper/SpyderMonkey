# Infrastructure discipline — gateway / expired

- source canon: `spydermonkey/c2-canon.md`
- base technique: `spydermonkey-c2-canon-infrastructure-discipline.md`
- bindings: **WSTG-INPV-06** · **CWE-601** · **ATT&CK T1190**
- context: **gateway** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Listener red-flag scan | verify own listener banners match decoy (own) | banner/tls profile clean |
| Redirector | `socat`/`haproxy` stager in lab | redirector forwards |
| Log checks | `relay exec` ls on own node | no third-party touch |
| Takedown drill | stop + verify listener dead (own) | clean kill switch |
| Backup channel | second listener pair (own lab) | resilience confirmed |

Walls: C2/Tunnels run against operator-OWNED endpoints exclusively —
anything else is a network-level violation (scope gate refuses, rc=1). A
confirmed channel is proof in the ledger, never an operation: no data
exfiltration, no persistence on owned hosts.

## Probe adjustment (gateway × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
