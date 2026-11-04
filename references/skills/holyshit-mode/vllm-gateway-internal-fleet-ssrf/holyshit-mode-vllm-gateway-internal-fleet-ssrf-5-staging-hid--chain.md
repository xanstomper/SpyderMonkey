# 5. Staging / hidden-infra discovery (keyless) — chain composition

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-5-staging-hid.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Subdomain brute common names** on BOTH `<d>` and the internal `<d>` root → found `staging.*` +
  `api.staging.*` on **AWS-direct IPs** (not Cloudflare) with its own 164KB `llms.txt`, keyless
  `/api/models` (404 models), `/openapi.json`, `/health`, and `staff_only` OAuth login.
- **`/.well-known/api-catalog`** (served by default on OpenRouter-style gateways) hands you both the
  `openapi.json` links and the `service-meta` `llms.txt`.
- **Hidden-model leak:** keyless `/api/models` listed models that are "private"/"stealth" by name:
  `gpt-6-astra-2026-09-03-private`, `stealth/ox-alpha`, plus `-latest` rolling aliases. Diff the
  keyless catalog against the documented public list to surface the hidden tier.
- **Modal/GPU infra leak:** catalog provider rows carried a real **Modal** function URL
  (`bespoke-ai-agents--<...>us-east.modal.direct/v1`) — internal serverless GPU endpoint disclosed
  in a public catalog. Scale-to-zero 503 currently; a potential free-GPU if it ever runs authless.
- **Free-AI reachability breadth:** an unauth `/invocations` accepts any catalog slug routed to the
  shared lane (`claude-opus-5`, `deepseek-r1`, glm/qwen/internvl all execute) — a **payment-gate
  bypass across the paid catalog** (`requires_payment:true` models served keyless). `stream:true`
  → SSE → drop-in OpenAI-compatible free endpoint for any SDK.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
