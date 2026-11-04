# 5. Staging / hidden-infra discovery (keyless)

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
