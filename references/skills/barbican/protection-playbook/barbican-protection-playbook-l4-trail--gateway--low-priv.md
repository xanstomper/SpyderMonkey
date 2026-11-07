# L4 — TRAIL — gateway / low-priv

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-l4-trail.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gateway** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

| Audit | Synthesis |
|---|---|
| which upstream providers the engagement touches | sanctioned providers named in posture; personal accounts forbidden for engagement traffic |
| authorization paperwork | zero documents (family canon): nothing exists to subpoena/leak |
| payment trails for engagement infra | lab/free-tier only, or alias-separated accounts |

## Probe adjustment (gateway × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
