# L1 — VANTAGE — host / machine

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-l1-vantage.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **host** · auth **machine** · chain role **pivot**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

| Audit | Synthesis |
|---|---|
| default route (residential iface = CRITICAL) | posture declares vm/vps/vpn/lab as THE sanctioned exit |
| proxy/VPN env + resolver config | engagement shells verify the route before firing |
| target-side logs will show the vantage — assume it's recorded forever | never mix personal browsing with engagement vantage |

## Probe adjustment (host × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
