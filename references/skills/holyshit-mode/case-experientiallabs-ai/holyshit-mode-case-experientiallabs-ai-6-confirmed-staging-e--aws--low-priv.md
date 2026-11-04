# 6. CONFIRMED — Staging environment fully exposed (score 60) — aws / low-priv

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-6-confirmed-staging-e.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **aws** · auth **low-priv** · chain role **pivot**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- `staging.experientiallabs.ai` + `api.staging.experientiallabs.ai` — a **parallel deployment** of the
  whole platform on **AWS-direct IPs** (16.146.222.180 / 54.214.13.115 / 184.33.83.9, no Cloudflare).
- Serves its **own 164KB `llms.txt`**, `/.well-known/api-catalog` → `api.staging.experientiallabs.ai`,
  keyless **`/api/models`** catalog (404 models), keyless `/openapi.json`, open `/health`+`/health/ready`.
- Auth is `staff_only` (staging login → `?error=staff_only`) — harder than prod, but the **whole
  surface is an independently-deployed estate** an attacker can target separately.
- **IMPACT:** Expanded attack surface — a second, AWS-direct instance with keyless catalog + openapi +
  hidden-model exposure. If staff-cred isolation or the staging gateway ever weakens, it's a pivot target.
- **CONFIDENCE:** High.

## Probe adjustment (aws × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
