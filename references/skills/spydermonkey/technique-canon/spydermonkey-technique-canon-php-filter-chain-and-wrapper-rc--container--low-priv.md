# PHP filter chain and wrapper rce-shape — container / low-priv

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-php-filter-chain-and-wrapper-rc.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **container** · auth **low-priv** · chain role **final**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

php://filter chains (convert.iconv) produce arithmetic-signed output for blind detection. Decisive test: chain produces the expected signature byte pattern — class confirmed read-only.

## Probe adjustment (container × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
