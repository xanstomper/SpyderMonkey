# Structure (each section's purpose) — azure / unauth

- source canon: `holyshit-mode/engagement-report-pattern.md`
- base technique: `holyshit-mode-engagement-report-pattern-structure-each-secti.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **azure** · auth **unauth** · chain role **pivot**

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- **Header** — target, generation timestamp, counts (classes tracked / confirmed /
  hypothesis / negative / chains). Compliance + scope-evidence at a glance.
- **`## Confirmed Holy Shits`** — the money section. Each confirmed class, ranked by score
  desc (then status tier), with score / technique / probe-count / last-probed. **Severity
  high first.** This is what clients read first.
- **`## Hypotheses (need proof)`** — unproven-but-higher-probability classes with score +
  probe-count. Not Holy Shits (mandate §29 strictness: a finding needs provable req+resp,
  kill-chain phase + ATT&CK id, one-sentence impact, non-destructive validation) — flagged
  as the highest-priority NEXT decisive tests.
- **`## Ruled Out (negative)`** — classes tested and cleared. Evidence of test coverage
  (valuable for scope/compliance), excluded from remediation.
- **`## Attack Paths`** — each recorded chain (crown jewel, steps joined with `→`, impact).
  Chains the isolated findings into exploit narratives.
- **`## Remediation Priority`** — the standing ordering: (1) confirmed holyshits first
  (RCE/admin-bypass/cross-tenant/cloud-cred), (2) confirmed chains (fix the base primitive
  step first), (3) hypotheses (prove or dismiss), (4) re-verify confirmed on every deploy
  (findings decay).

## Probe adjustment (azure × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
