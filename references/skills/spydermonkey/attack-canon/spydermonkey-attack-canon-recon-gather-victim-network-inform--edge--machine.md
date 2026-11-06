# Recon Gather Victim Network Information (T1590) — edge / machine

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-recon-gather-victim-network-inform.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **edge** · auth **machine** · chain role **entry**

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- class: IP blocks, DNS topology, routing, trust relationships from public records
- probe: whois/rdap/dns walking; netblock mapping against the scope file
- wall: read-only; everything stays in the estate ledger

## Probe adjustment (edge × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
