# Hypotheses KILLED (honest negatives) — api / high-priv

- source canon: `holyshit-mode/case-gratisfy-reengagement2.md`
- base technique: `holyshit-mode-case-gratisfy-reengagement2-hypotheses-killed-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- **Handoff code brute (55→dead):** live flow captured real code = 32-hex, 128-bit, one-time. Dead.
- **profiles RLS UPDATE bypass:** 204 was `content-range: */0`. RLS holds.
- **Realtime WS:** 101 + unauth heartbeat OK, but postgres_changes subscription on public tables errors (Realtime not enabled). No leak. Prior "401 = auth gate" was a curl false-negative.
- **/admin/users 200:** SPA ghost route (text/html).
- **handoff_code_entropy_unknown (55→negative):** resolved by live flow.

## Probe adjustment (api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
