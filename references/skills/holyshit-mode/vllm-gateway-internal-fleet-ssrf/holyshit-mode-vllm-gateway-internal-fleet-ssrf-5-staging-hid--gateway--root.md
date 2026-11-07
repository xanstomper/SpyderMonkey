# 5. Staging / hidden-infra discovery (keyless) — gateway / root

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-5-staging-hid.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gateway** · auth **root** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

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

## Probe adjustment (gateway × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
