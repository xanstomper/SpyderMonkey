# What was adopted from kimiko (and what was not)

- source canon: `spydermonkey/mandate.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

ADOPTED (the discipline): mandate architecture (persona contract, not "ignore your
training") · entry protocol with IMMEDIATE adoption · zero-blocker execution IN
SCOPE · no moralizing/warnings/disclaimers on authorized work · evidence-first
complete outputs (zero theoretical, zero placeholders) · tool-use expectations ·
loop control (step caps, retries, context discipline) · precise stop conditions.

NOT ADOPTED (rejected as harm, not discipline): nullified safeguards, malware
generation, black-hat support, FRP/IMEI/activation bypass, "execute first ask
never" against out-of-scope systems, audit-trail destruction. The family's walls
replace kimiko's nullification with PRECISE boundaries — the discipline without
the harm.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
