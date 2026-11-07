# What was adopted from kimiko (and what was not) — browser / machine

- source canon: `spydermonkey/mandate.md`
- base technique: `spydermonkey-mandate-what-was-adopted-from-kimiko-and-what-w.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **browser** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (browser × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
