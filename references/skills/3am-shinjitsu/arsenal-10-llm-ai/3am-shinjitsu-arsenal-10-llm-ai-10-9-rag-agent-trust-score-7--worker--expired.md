# 10.9 RAG/agent trust (score 70, owned deployments) — worker / expired

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-9-rag-agent-trust-score-7.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **worker** · auth **expired** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

- Indirect prompt injection via retrieved content; tool-description injection; agent tool-
  permission drift (read→write); multi-agent pass-through (Agent A feeds untrusted input to
  Agent B without validation); RAG corpus poisoning (owned corpus only); embedding inversion
  on own embeddings; token-smuggling filters test (homoglyphs/zero-width) as CI gates.

## Probe adjustment (worker × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
