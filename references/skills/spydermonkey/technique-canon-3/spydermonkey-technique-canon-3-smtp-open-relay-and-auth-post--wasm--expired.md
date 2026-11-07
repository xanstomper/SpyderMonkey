# SMTP open-relay and auth-posture classes — wasm / expired

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-smtp-open-relay-and-auth-post.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **wasm** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

Open relay (characterized with ONE test mail to YOURSELF), STARTTLS downgrade posture, VRFY/EXPN disclosure. Decisive test: banner + the single self-addressed relay test — the acceptance is the finding.

## Probe adjustment (wasm × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
