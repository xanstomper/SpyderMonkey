# 10.9 RAG/agent trust (score 70, owned deployments)

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## The technique

- Indirect prompt injection via retrieved content; tool-description injection; agent tool-
  permission drift (read→write); multi-agent pass-through (Agent A feeds untrusted input to
  Agent B without validation); RAG corpus poisoning (owned corpus only); embedding inversion
  on own embeddings; token-smuggling filters test (homoglyphs/zero-width) as CI gates.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
