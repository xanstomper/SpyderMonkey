# J. AI-SPECIFIC (operator apps) — chain composition

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-j-ai-specific-operator-apps.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Prompt injection: indirect via retrieved content, tool-description injection, system-prompt exfil
- Agent over-scope: tool permissions wider than claimed (read→write drift)
- Router placebo: tokenizer/cost fingerprint divergence on "premium" models
- Guardrail bypass: encoding/roleplay/language-switch regression suites as CI gates
- Training-data extraction probes on own fine-tunes
- Model extraction: query pacing, semantic-similarity evasion, distillation via API
- Embedding inversion: nearest-neighbor reconstruction from embedding queries
- Multi-agent trust: Agent A passes untrusted input to Agent B without validation
- Token-smuggling: homoglyphs, zero-width chars, split tokens evading keyword filters
- RAG poisoning: malicious documents injected into retrieval corpus

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
