# 6. Lesson: operator-owned LLM-gateway engagements — where the findings actually live

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

On a well-built reseller gateway, do NOT judge the whole estate by the hardened public edge.
The high-value compromisable class is almost always: **the hidden self-hosted serving fleet
(`experiential_cloud`-style lane) disclosed via the keyless catalog `base_url`**, whose
control-plane/inference-routes share the inference binary but skip the auth middleware. Sweep the
internal hosts for `/openapi.json`, `/invocations`, `/scale_elastic_ep`, `/usage.json`, and
validate auth-asymmetry by contrast (same-route 401 on a sibling host = the finding is real).
Full ledger recorded at `~/.hermes/scripts/holyleadger/experientiallabs-ai.json` (12 confirmed).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
