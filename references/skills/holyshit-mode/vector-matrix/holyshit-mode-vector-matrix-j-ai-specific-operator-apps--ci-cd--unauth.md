# J. AI-SPECIFIC (operator apps) — ci-cd / unauth

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-j-ai-specific-operator-apps.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **ci-cd** · auth **unauth** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

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

## Probe adjustment (ci-cd × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
