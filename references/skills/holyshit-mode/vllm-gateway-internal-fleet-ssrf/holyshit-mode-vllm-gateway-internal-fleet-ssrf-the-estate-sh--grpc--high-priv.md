# The estate shape (where the weak underbelly hides on these gateways) — grpc / high-priv

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-the-estate-sh.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **grpc** · auth **high-priv** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- **Public gateway + web platform = hardened** (server-side auth, keyless-recon-only). The
  compromisable surface on THIS class of product is the **internal serving fleet** the public
  gateway routes through — one misconfigured lane = whole crown.
- Fleet pattern: `*.xplabs.ai` with per-provider lanes. `gateway.<d>/{glm,qwen}/v1` were
  **properly keyed (401 Invalid API Key)** while `wm.<d>` (deepseek lane) left `/invocations` +
  `/scale_elastic_ep` + `/generative_scoring` + `/load` + `/detokenize` **completely unauth**.
  **Contrast = proof of misconfiguration**, not platform-wide behavior.
- Keyless `/api/models` **+ `/api/models/<slug>` catalog** leaked the internal `base_url`s and
  provider wiring (see below) — the recon gift that made everything else possible.

## Probe adjustment (grpc × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
