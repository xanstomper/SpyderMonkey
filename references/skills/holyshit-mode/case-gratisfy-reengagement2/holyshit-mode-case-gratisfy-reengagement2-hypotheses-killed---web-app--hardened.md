# Hypotheses KILLED (honest negatives) — web-app / hardened

- source canon: `holyshit-mode/case-gratisfy-reengagement2.md`
- base technique: `holyshit-mode-case-gratisfy-reengagement2-hypotheses-killed-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **hardened** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- **Handoff code brute (55→dead):** live flow captured real code = 32-hex, 128-bit, one-time. Dead.
- **profiles RLS UPDATE bypass:** 204 was `content-range: */0`. RLS holds.
- **Realtime WS:** 101 + unauth heartbeat OK, but postgres_changes subscription on public tables errors (Realtime not enabled). No leak. Prior "401 = auth gate" was a curl false-negative.
- **/admin/users 200:** SPA ghost route (text/html).
- **handoff_code_entropy_unknown (55→negative):** resolved by live flow.

## Probe adjustment (web-app × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
