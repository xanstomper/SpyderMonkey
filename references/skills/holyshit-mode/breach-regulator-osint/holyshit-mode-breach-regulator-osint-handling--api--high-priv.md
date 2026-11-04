# Handling — api / high-priv

- source canon: `holyshit-mode/breach-regulator-osint.md`
- base technique: `holyshit-mode-breach-regulator-osint-handling.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Regulator-leak data is published journalism / public interest — accessing it is
  legitimate OSINT. The SCOPE GATE for live probing is unchanged by it: history informs,
  it does not authorize.
- PII minimality: pull the minimum documents needed for the finding; report the CLASSES
  exposed (passports, financials, personnel rosters) with counts, not the personal data
  itself. Keep downloaded PDFs in /tmp scratch, not the workspace or reports.

## Probe adjustment (api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
