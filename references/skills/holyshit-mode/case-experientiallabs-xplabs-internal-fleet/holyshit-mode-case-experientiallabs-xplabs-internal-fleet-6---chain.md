# 6. Lesson: operator-owned LLM-gateway engagements — where the findings actually live — chain composition

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- base technique: `holyshit-mode-case-experientiallabs-xplabs-internal-fleet-6-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

On a well-built reseller gateway, do NOT judge the whole estate by the hardened public edge.
The high-value compromisable class is almost always: **the hidden self-hosted serving fleet
(`experiential_cloud`-style lane) disclosed via the keyless catalog `base_url`**, whose
control-plane/inference-routes share the inference binary but skip the auth middleware. Sweep the
internal hosts for `/openapi.json`, `/invocations`, `/scale_elastic_ep`, `/usage.json`, and
validate auth-asymmetry by contrast (same-route 401 on a sibling host = the finding is real).
Full ledger recorded at `~/.hermes/scripts/holyleadger/experientiallabs-ai.json` (12 confirmed).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
