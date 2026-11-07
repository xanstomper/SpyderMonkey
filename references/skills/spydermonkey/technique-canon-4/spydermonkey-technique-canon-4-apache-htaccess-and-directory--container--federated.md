# Apache .htaccess and directory-move classes — container / federated

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-apache-htaccess-and-directory.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **container** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

.htaccess exposure itself (fetch it), Options +Indexes (already DIRECTORY canon), and mod_userdir legacy. Decisive test: direct fetch of .htaccess — the file content IS the harvest.

## Probe adjustment (container × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
