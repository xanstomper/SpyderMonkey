# 9.7 Target-dead triage (score 60) — web-app / high-priv

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- base technique: `3am-shinjitsu-arsenal-09-breach-osint-9-7-target-dead-triage.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **web-app** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Ladder: `dig +short <host> @1.1.1.1` AND `@8.8.8.8` (both empty = global no-record) →
  `getent hosts` apex/www/api spread → wayback availability API → whois against the TLD
  registry (`whois -h whois.nic.<tld>`) → split registered-but-DNS-stripped (registrar hold/
  takedown — re-check later, baseline moot) from dropped (expired — engagement closed).
- A baselined target going dark IS a finding — report it as one.

## Probe adjustment (web-app × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
