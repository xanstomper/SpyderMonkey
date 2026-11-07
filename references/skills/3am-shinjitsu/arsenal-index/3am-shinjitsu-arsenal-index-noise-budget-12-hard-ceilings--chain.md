# Noise budget (§12, hard ceilings) — chain composition

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-noise-budget-12-hard-ceilings.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Class | Ceiling/burst | Cadence |
|---|---|---|
| Network/Edge | 10 req + banner grabs | 3-4s spacing; CF challenge → wait 75s, re-read SAME endpoint |
| Web app | 20 req | route maps once; never re-fetch unchanged bundle |
| API | 15 req/endpoint-class | bursts only on exchange endpoints, once |
| Auth/Identity | 15 req | NEVER leave a retry loop on a throttled auth plane — full-cold 2h |
| Client-side | passive | bundle fetches only |
| Infra/Hosting | 10 req | buckets/ping once |
| Supply-chain | passive | version matching offline |
| Breach/OSINT | zero target traffic | all third-party archives |
| LLM/AI | 5 req + 2×PTOK | PTOK off by default (`--ptok`) |

Bulk rule: >50 req total = chunk + read-only verify between batches. A probe that fails
twice is dead. Negatives are results.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
