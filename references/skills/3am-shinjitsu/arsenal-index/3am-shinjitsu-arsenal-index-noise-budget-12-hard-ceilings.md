# Noise budget (§12, hard ceilings)

- source canon: `3am-shinjitsu/arsenal-index.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
