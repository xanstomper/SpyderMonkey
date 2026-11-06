# Apache .htaccess and directory-move classes — kubernetes / unauth

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-apache-htaccess-and-directory.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **kubernetes** · auth **unauth** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

.htaccess exposure itself (fetch it), Options +Indexes (already DIRECTORY canon), and mod_userdir legacy. Decisive test: direct fetch of .htaccess — the file content IS the harvest.

## Probe adjustment (kubernetes × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
