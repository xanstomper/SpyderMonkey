# Phase 2 — Valuation (the extortion-economy ladder) — mesh / guest

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-phase-2-valuation-the-extortion-eco.md`
- bindings: **WSTG-BUSL-01** · **CWE-1336** · **ATT&CK T1565**
- context: **mesh** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

ESTIMATE ranges per record/asset, labeled with basis. Prices are ranges, never false
precision:

| Class | Basis (observed market) | Range (ESTIMATE) |
|---|---|---|
| PII — US consumer | ~$5–15/record street, breach-class aggregation multipliers | per 1k rows |
| PII — EU (GDPR-class) | higher penalty-weight, lower street | per 1k rows |
| FIN (cards/banking) | $20–50/record class | per record |
| CRED (secrets/keys) | credential-market tiers by privilege | per credential |
| BACKUP (unencrypted dump) | lump: % of org revenue-class (ransom demand logic) | per artifact |
| SRC (exclusive repo) | private repo market + IP class | per repo |
| SASS (tenant export) | SaaS-resale/takeover ladder | per tenant |

Valuation MUST be labeled: `$ESTIMATE (basis: <market-ladder | disclosed demand |
industry benchmark>)`. No invented precision; a single-number price without basis
is a violation.

## Probe adjustment (mesh × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
