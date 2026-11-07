# The estate shape (where the weak underbelly hides on these gateways) — chain composition

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-the-estate-sh.md`
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

- **Public gateway + web platform = hardened** (server-side auth, keyless-recon-only). The
  compromisable surface on THIS class of product is the **internal serving fleet** the public
  gateway routes through — one misconfigured lane = whole crown.
- Fleet pattern: `*.x***REDACTED***.ai` with per-provider lanes. `gateway.<d>/{glm,qwen}/v1` were
  **properly keyed (401 Invalid API Key)** while `wm.<d>` (deepseek lane) left `/invocations` +
  `/scale_elastic_ep` + `/generative_scoring` + `/load` + `/detokenize` **completely unauth**.
  **Contrast = proof of misconfiguration**, not platform-wide behavior.
- Keyless `/api/models` **+ `/api/models/<slug>` catalog** leaked the internal `base_url`s and
  provider wiring (see below) — the recon gift that made everything else possible.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
