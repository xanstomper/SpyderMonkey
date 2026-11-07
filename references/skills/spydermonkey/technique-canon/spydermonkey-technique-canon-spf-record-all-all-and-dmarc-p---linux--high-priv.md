# SPF record +all / ?all and DMARC p=none — linux / high-priv

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-spf-record-all-all-and-dmarc-p-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **linux** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Spoofability is record arithmetic: SPF ending +all (or ?all with no fallback), DMARC p=none with no rua = spoofable domain posture. Decisive test: TXT record parse — the arithmetic IS the finding (no spoofed mail sent).

## Probe adjustment (linux × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
