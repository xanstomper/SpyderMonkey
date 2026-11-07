# 6b. CONFIRMED — Hidden-model catalog leak (prod + staging) (score 55) — gcp / high-priv

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-6b-confirmed-hidden-m.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **gcp** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- **Prod catalog (`/api/models`):** `gpt-6-astra-2026-09-03-private` (literally "private", azure_openai).
- **Staging catalog (`api.staging.../api/models`):** `ox-alpha` = provider `openrouter`, provider_model_id
  **`stealth/ox-alpha`** — a hidden/stealth model; plus `-latest` rolling aliases.
- **IMPACT:** Keyless disclosure of models an org cannot/should not access, and the stealth/private
  internal catalog naming. Recon/observation (maps the hidden tier), not direct compromise.
- **CONFIDENCE:** High (raw keyless JSON).

## Probe adjustment (gcp × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
