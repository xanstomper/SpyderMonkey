# XXE out-of-band and local-file — cloud / low-priv

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-xxe-out-of-band-and-local-file.md`
- bindings: **WSTG-INPV-07** · **CWE-611** · **ATT&CK T1190**
- context: **cloud** · auth **low-priv** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

DOCTYPE + external entity to your DNS/HTTP listener = OOB proof; file:///etc/hostname echoed = local-file proof. Decisive test: OOB marker arrival at your listener; file read limited to hostname/ident material.

## Probe adjustment (cloud × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
