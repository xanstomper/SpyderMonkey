# 10.8 Mint/signup chains (score 75)

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Free-tier automated signup → `sk_` key mint → `/v1/models` + `/v1/chat/completions` live +
  `/v1/credits` per-key `{usage, limit, balance}` leak (the only metadata endpoint). Signup
  on the TARGET with operator-authorized identities only (no third-party account fraud — §2).
- Reseller upstream = operator's supply-chain crown jewel: free-credit bleed on the reseller
  degrades the operator's own upstream — state the chain, never drain.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
