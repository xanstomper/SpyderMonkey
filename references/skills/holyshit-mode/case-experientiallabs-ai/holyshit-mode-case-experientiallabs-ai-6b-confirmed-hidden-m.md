# 6b. CONFIRMED — Hidden-model catalog leak (prod + staging) (score 55)

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- **Prod catalog (`/api/models`):** `gpt-6-astra-2026-09-03-private` (literally "private", azure_openai).
- **Staging catalog (`api.staging.../api/models`):** `ox-alpha` = provider `openrouter`, provider_model_id
  **`stealth/ox-alpha`** — a hidden/stealth model; plus `-latest` rolling aliases.
- **IMPACT:** Keyless disclosure of models an org cannot/should not access, and the stealth/private
  internal catalog naming. Recon/observation (maps the hidden tier), not direct compromise.
- **CONFIDENCE:** High (raw keyless JSON).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
