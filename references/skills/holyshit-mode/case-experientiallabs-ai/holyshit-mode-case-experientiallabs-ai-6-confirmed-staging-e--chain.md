# 6. CONFIRMED — Staging environment fully exposed (score 60) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-6-confirmed-staging-e.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `staging.experientiallabs.ai` + `api.staging.experientiallabs.ai` — a **parallel deployment** of the
  whole platform on **AWS-direct IPs** (16.146.222.180 / 54.214.13.115 / 184.33.83.9, no Cloudflare).
- Serves its **own 164KB `llms.txt`**, `/.well-known/api-catalog` → `api.staging.experientiallabs.ai`,
  keyless **`/api/models`** catalog (404 models), keyless `/openapi.json`, open `/health`+`/health/ready`.
- Auth is `staff_only` (staging login → `?error=staff_only`) — harder than prod, but the **whole
  surface is an independently-deployed estate** an attacker can target separately.
- **IMPACT:** Expanded attack surface — a second, AWS-direct instance with keyless catalog + openapi +
  hidden-model exposure. If staff-cred isolation or the staging gateway ever weakens, it's a pivot target.
- **CONFIDENCE:** High.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
