# Ghost-route trap → real API discovery — chain composition

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-ghost-route-trap-real-api-disco.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `gonka-api.org/v1/*` returns the SPA HTML shell for every path (200
  text/html) — classic SPA fallback. Don't judge API existence by status.
- Real LLM API is a Supabase Edge Function, found via FAQ JSON-LD embedded in
  the main JS bundle: `https://<project>.supabase.co/functions/v1/gonka`
  ("Point any OpenAI-compatible client at ... and use your Easy GonkaAI key").
- Auth: `Authorization: Bearer sk_...`. Endpoints: `/v1/models` (3 models),
  `/v1/chat/completions` (real completions, `reasoning` field present),
  `/v1/credits` → leaks `{label, usage, limit, limit_remaining, balance}` per key.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
