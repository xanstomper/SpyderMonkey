# PLAYBOOK E — AI / LLM-INFRASTRUCTURE — chain composition

- source canon: `holyshit-mode/operational-playbooks.md`
- base technique: `holyshit-mode-operational-playbooks-playbook-e-ai-llm-infras.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
