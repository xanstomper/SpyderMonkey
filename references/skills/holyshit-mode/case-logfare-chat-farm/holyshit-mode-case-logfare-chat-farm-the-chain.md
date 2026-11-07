# The chain

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

```
Spoof Origin → POST /api/chat {"message":"...","model":"logfare/auto"}
  → anon lfc_session minted (unlimited, 90d) → real SSE completions
  → ~30 reqs + 3 parallel long completions (1.7k/1k/2.7k tokens), zero 429s
```
Free unauth inference farm on Claude-class upstreams, bill-drain vector for a donation-funded service. Bounded test only (~40k tokens).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
