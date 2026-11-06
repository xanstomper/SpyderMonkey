# 7. Cross-brand blast radius — api / machine

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-7-cross-brand-blast.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **api** · auth **machine** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Identical CDN IPs + verbatim-identical error envelopes across sister brands = shared
  backend user/session store hypothesis.
- Ledger a cross-brand session-replay hypothesis (one account on either brand tests it)
  and the credential-reuse angle: attacker leaks of ONE brand's `userid|email|password`
  records degrade the whole family.
- Sister-brand CT logs surface what the main brand's logs hide: staging servers (dead
  503 origin behind a live route) and dangling CDN routes ("unknown domain" errors).

## Probe adjustment (api × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
