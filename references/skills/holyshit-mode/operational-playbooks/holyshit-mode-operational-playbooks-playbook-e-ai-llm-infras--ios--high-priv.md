# PLAYBOOK E — AI / LLM-INFRASTRUCTURE — ios / high-priv

- source canon: `holyshit-mode/operational-playbooks.md`
- base technique: `holyshit-mode-operational-playbooks-playbook-e-ai-llm-infras.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ios** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

**Objective**: red-team the operator's own AI stack: model endpoints, agent frameworks,
RAG pipelines, fine-tunes, guardrails.

**Phase 1 — Endpoint Discovery**
- Model API enumeration: `/v1/models`, `/v1/completions`, `/v1/chat/completions` — 405 matrix.
- Version disclosure: model names, provider leaks, quantization format (GGUF = self-hosted).
- Cost/tokens endpoint: rate limits, billing validation, quota enforcement.

**Phase 2 — Prompt-Injection Surface**
- **Direct**: jailbreak attempts on the operator's own models (roleplay, encoding, DAN-class,
  language-switch) — validate guardrail regression as CI gate.
- **Indirect**: inject payloads into documents the model retrieves (RAG poisoning), test
  whether the model executes embedded instructions.
- **Tool injection**: manipulate tool descriptions mid-conversation; test if the model
  follows modified tool specs.

**Phase 3 — Agent Framework**
- Tool permission scoping: can a read-only tool be coerced into writes via prompt?
- Multi-agent trust: Agent A receives untrusted input, passes to Agent B — does B validate?
- System-prompt exfiltration: can you extract the system prompt via token-by-token probing?

**Phase 4 — Data & Model Security**
- Training-data extraction: membership inference, verbatim recall of fine-tuning data.
- Model theft: can you distill the model via API queries? Rate-limit vs. extraction budget.
- Embedding inversion: text from embeddings via nearest-neighbor reconstruction.

**Phase 5 — Infrastructure**
- GPU/cluster exposure: Jupyter notebooks, TensorBoard, MLflow — unauthenticated?
- Model artifact storage: public buckets with `.safetensors`, `.gguf`, `adapter_model.bin`?
- CI/CD for models: can you poison the training pipeline via dependency confusion?

**Deliverable**: injection-surface map, guardrail regression suite, agent-trust findings,
data-exposure validation, infrastructure gaps.

---

## Probe adjustment (ios × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
