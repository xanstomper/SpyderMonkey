# Noise budget (§12, hard ceilings) — worker / guest

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-noise-budget-12-hard-ceilings.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **worker** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (worker × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
