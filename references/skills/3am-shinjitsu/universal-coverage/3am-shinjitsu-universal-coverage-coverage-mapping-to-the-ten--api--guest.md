# Coverage mapping to the ten surface classes — api / guest

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-coverage-mapping-to-the-ten.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

| Existing class | Universal domains |
|---|---|
| 1 Network/Edge | U01, U02 |
| 2 Web app | U03 |
| 3 API | U04 |
| 4 Auth/Identity | U05 |
| 5 Client-side | U06 |
| 6 Infra/Hosting | U07, U08, U09 |
| 7 Supply-chain/Deps | U10 |
| 8 Human/Identity | U11, U12, U16 |
| 9 Breach/OSINT | U01, U10, U11, U14, U15 |
| 10 LLM/AI | U13 |

The universal file expands coverage without weakening the ten-class contract. An
engagement may merge domains in its ledger, but all sixteen must be probed or N/A'd.

## Probe adjustment (api × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
