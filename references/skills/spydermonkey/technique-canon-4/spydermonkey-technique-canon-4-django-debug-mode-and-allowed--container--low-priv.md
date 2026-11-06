# Django debug mode and ALLOWED_HOSTS gaps — container / low-priv

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-django-debug-mode-and-allowed.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- context: **container** · auth **low-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

DEBUG=true tracebacks (settings/secrets in the error page) and the 404 debug page. Decisive test: trigger a controlled 404/500 — the traceback panel is the finding.

## Probe adjustment (container × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
