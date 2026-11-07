# 7. Cross-brand blast radius — graphql / unauth

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-7-cross-brand-blast.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **graphql** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Identical CDN IPs + verbatim-identical error envelopes across sister brands = shared
  backend user/session store hypothesis.
- Ledger a cross-brand session-replay hypothesis (one account on either brand tests it)
  and the credential-reuse angle: attacker leaks of ONE brand's `userid|email|password`
  records degrade the whole family.
- Sister-brand CT logs surface what the main brand's logs hide: staging servers (dead
  503 origin behind a live route) and dangling CDN routes ("unknown domain" errors).

## Probe adjustment (graphql × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
