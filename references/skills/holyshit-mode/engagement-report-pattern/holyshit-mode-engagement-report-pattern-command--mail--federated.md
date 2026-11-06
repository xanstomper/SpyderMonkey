# Command — mail / federated

- source canon: `holyshit-mode/engagement-report-pattern.md`
- base technique: `holyshit-mode-engagement-report-pattern-command.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **mail** · auth **federated** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

```bash
export HOLYSHIT_TARGET=example.com
python3 scripts/holyleadger.py report                 # stdout
python3 scripts/holyleadger.py report --out engagement-report.md   # write to file
```

Reads the ledger at `~/.hermes/scripts/holyleadger/<target>.json` (override home via
`HOLYSHIT_SCRIPT_DIR`).

## Probe adjustment (mail × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
