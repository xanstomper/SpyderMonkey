# 10.8 Mint/signup chains (score 75) — chain composition

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-8-mint-signup-chains-scor.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Free-tier automated signup → `sk_` key mint → `/v1/models` + `/v1/chat/completions` live +
  `/v1/credits` per-key `{usage, limit, balance}` leak (the only metadata endpoint). Signup
  on the TARGET with operator-authorized identities only (no third-party account fraud — §2).
- Reseller upstream = operator's supply-chain crown jewel: free-credit bleed on the reseller
  degrades the operator's own upstream — state the chain, never drain.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
