# L4 — TRAIL — api / unauth

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-l4-trail.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **unauth** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

| Audit | Synthesis |
|---|---|
| which upstream providers the engagement touches | sanctioned providers named in posture; personal accounts forbidden for engagement traffic |
| authorization paperwork | zero documents (family canon): nothing exists to subpoena/leak |
| payment trails for engagement infra | lab/free-tier only, or alias-separated accounts |

## Probe adjustment (api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
