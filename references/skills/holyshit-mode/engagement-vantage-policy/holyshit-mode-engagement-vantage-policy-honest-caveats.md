# Honest caveats

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- Datacenter IPs get challenged harder by some WAFs (Fastly/Turnstile fingerprints ASN) —
  if a wall appears that the same probe never hit from home, diff the vantage before blaming
  the probe.
- Vermes holds keys (reverse-tunnel identity, hermes/mochi auth) — probe scripts stay
  read-only curl/socket work; never drop stored target credentials on the VM.
- Never re-probe g***REDACTED***.com from the home IP while the ban stands (and don't from the VM
  either without re-checking the case file first).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
