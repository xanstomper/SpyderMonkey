# 6. Lesson: operator-owned LLM-gateway engagements — where the findings actually live — aws / unauth

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- base technique: `holyshit-mode-case-experientiallabs-xplabs-internal-fleet-6-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **aws** · auth **unauth** · chain role **pivot**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

On a well-built reseller gateway, do NOT judge the whole estate by the hardened public edge.
The high-value compromisable class is almost always: **the hidden self-hosted serving fleet
(`experiential_cloud`-style lane) disclosed via the keyless catalog `base_url`**, whose
control-plane/inference-routes share the inference binary but skip the auth middleware. Sweep the
internal hosts for `/openapi.json`, `/invocations`, `/scale_elastic_ep`, `/usage.json`, and
validate auth-asymmetry by contrast (same-route 401 on a sibling host = the finding is real).
Full ledger recorded at `~/.hermes/scripts/holyleadger/experientiallabs-ai.json` (12 confirmed).

## Probe adjustment (aws × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
