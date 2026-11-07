# Ghost-route trap → real API discovery

- source canon: `holyshit-mode/case-gonka-api.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `gonka-api.org/v1/*` returns the SPA HTML shell for every path (200
  text/html) — classic SPA fallback. Don't judge API existence by status.
- Real LLM API is a Supabase Edge Function, found via FAQ JSON-LD embedded in
  the main JS bundle: `https://<project>.supabase.co/functions/v1/gonka`
  ("Point any OpenAI-compatible client at ... and use your Easy GonkaAI key").
- Auth: `Authorization: Bearer sk_...`. Endpoints: `/v1/models` (3 models),
  `/v1/chat/completions` (real completions, `reasoning` field present),
  `/v1/credits` → leaks `{label, usage, limit, limit_remaining, balance}` per key.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
