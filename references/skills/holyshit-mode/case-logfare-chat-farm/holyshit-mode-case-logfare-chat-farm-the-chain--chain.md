# The chain — chain composition

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-the-chain.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

```
Spoof Origin → POST /api/chat {"message":"...","model":"logfare/auto"}
  → anon lfc_session minted (unlimited, 90d) → real SSE completions
  → ~30 reqs + 3 parallel long completions (1.7k/1k/2.7k tokens), zero 429s
```
Free unauth inference farm on Claude-class upstreams, bill-drain vector for a donation-funded service. Bounded test only (~40k tokens).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
