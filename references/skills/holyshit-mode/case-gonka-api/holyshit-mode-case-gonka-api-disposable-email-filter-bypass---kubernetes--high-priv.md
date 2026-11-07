# Disposable-email filter bypass (discovery recipe) — kubernetes / high-priv

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-disposable-email-filter-bypass-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **kubernetes** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Signup enforces a 23514 CHECK constraint on email domain.
- Blocked: tempmail, guerrillamail, yopmail, 10minutemail, maildrop, getnada,
  dispostable, fakeinbox, trashmail, sharklasers, grr.la.
- MISSED (200): harakirimail.com, pokemail.net, spam4.me, bccto.me, chammy.info.
- Discovery: batch-signup one probe account per candidate domain, read
  200 vs 23514. A filter-list gap = automate account creation at scale.

## Probe adjustment (kubernetes × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
