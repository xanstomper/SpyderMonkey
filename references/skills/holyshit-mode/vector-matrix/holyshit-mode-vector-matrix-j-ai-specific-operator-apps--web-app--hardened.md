# J. AI-SPECIFIC (operator apps) — web-app / hardened

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-j-ai-specific-operator-apps.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **web-app** · auth **hardened** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (web-app × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
