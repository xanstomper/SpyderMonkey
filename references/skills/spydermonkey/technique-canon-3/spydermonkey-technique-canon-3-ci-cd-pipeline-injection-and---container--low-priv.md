# CI/CD pipeline injection and artifact poisoning (documented classes) — container / low-priv

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-ci-cd-pipeline-injection-and-.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **container** · auth **low-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

PR-triggered workflows executing fork-controlled code (pull_request_target misuse) and artifact substitution. Decisive test: workflow YAML analysis — the misconfiguration IS the finding (the exploit is reported as the mechanism writeup).

## Probe adjustment (container × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
