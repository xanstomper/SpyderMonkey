# ASN/BGP/WHOIS netblock intel — cloud / low-priv

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-asn-bgp-whois-netblock-intel.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **cloud** · auth **low-priv** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Estate netblocks via ASN, rDNS sweep across the range, WHOIS org pivots — the netblock map extends the scope estate (scope add is the operator's call). Decisive test: rDNS inventory rows for in-scope ranges.

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
