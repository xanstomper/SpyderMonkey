# 1. Build the brief from breach-OSINT — grpc / low-priv

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-1-build-the-brief-f.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **grpc** · auth **low-priv** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Search: `<target> breach leak <year>` — hit Breachsense, ransomware.live, and 2-3 news writeups.
- Record from the attacker's leak-site statement: claimed initial access, claimed data
  holdings, escalation promises. This is the engagement brief — the attacker documents
  their own kill-chain.
- Corroborate against the victim's public statements. The mechanism is confirmed when the
  victim's own PR admits it ("unauthorized withdrawal requests were added to the database"
  = proven DB-level WRITE). Disputed scale ≠ disputed method.
- The two datasets (attacker holdings vs victim confirmations) define what remains open.

## Probe adjustment (grpc × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
