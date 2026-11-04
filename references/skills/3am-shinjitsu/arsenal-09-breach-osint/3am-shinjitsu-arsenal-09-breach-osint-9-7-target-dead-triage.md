# 9.7 Target-dead triage (score 60)

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## The technique

- Ladder: `dig +short <host> @1.1.1.1` AND `@8.8.8.8` (both empty = global no-record) →
  `getent hosts` apex/www/api spread → wayback availability API → whois against the TLD
  registry (`whois -h whois.nic.<tld>`) → split registered-but-DNS-stripped (registrar hold/
  takedown — re-check later, baseline moot) from dropped (expired — engagement closed).
- A baselined target going dark IS a finding — report it as one.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
