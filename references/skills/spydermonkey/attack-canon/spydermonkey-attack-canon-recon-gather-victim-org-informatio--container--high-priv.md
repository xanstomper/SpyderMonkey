# Recon Gather Victim Org Information (T1591) — container / high-priv

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-recon-gather-victim-org-informatio.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **container** · auth **high-priv** · chain role **entry**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- class: org structure, locations, business rhythm — the social-engineering surface
- probe: public filings, job posts, status pages; crown the exposure classes
- wall: passive collection only, ledgered with source provenance

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
