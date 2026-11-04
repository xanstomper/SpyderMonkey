# Disposable-email filter bypass (discovery recipe) — web-app / low-priv

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-disposable-email-filter-bypass-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **web-app** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Signup enforces a 23514 CHECK constraint on email domain.
- Blocked: tempmail, guerrillamail, yopmail, 10minutemail, maildrop, getnada,
  dispostable, fakeinbox, trashmail, sharklasers, grr.la.
- MISSED (200): harakirimail.com, pokemail.net, spam4.me, bccto.me, chammy.info.
- Discovery: batch-signup one probe account per candidate domain, read
  200 vs 23514. A filter-list gap = automate account creation at scale.

## Probe adjustment (web-app × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
