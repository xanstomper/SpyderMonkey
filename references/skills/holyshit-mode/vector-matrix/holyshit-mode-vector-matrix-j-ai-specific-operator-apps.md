# J. AI-SPECIFIC (operator apps)

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-07

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
