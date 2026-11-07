# Ghost-route trap → real API discovery — websocket / high-priv

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-ghost-route-trap-real-api-disco.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- `gonka-api.org/v1/*` returns the SPA HTML shell for every path (200
  text/html) — classic SPA fallback. Don't judge API existence by status.
- Real LLM API is a Supabase Edge Function, found via FAQ JSON-LD embedded in
  the main JS bundle: `https://<project>.supabase.co/functions/v1/gonka`
  ("Point any OpenAI-compatible client at ... and use your Easy GonkaAI key").
- Auth: `Authorization: Bearer sk_...`. Endpoints: `/v1/models` (3 models),
  `/v1/chat/completions` (real completions, `reasoning` field present),
  `/v1/credits` → leaks `{label, usage, limit, limit_remaining, balance}` per key.

## Probe adjustment (websocket × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
