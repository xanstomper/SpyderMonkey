# Turnstile harvesting — iac / unauth

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- base technique: `holyshit-mode-case-apimart-newapi-fork-turnstile-harvesting.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **iac** · auth **unauth** · chain role **final**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Headless Playwright (firefox) often fails to render the widget:
`[Cloudflare Turnstile] Unable to find onload callback 'onloadTurnstileCallback'`. The target's own
integration can be half-broken — if the widget never mints tokens for real users either,
server-side enforcement may be flaky. Test `?turnstile=garbage` once the rate limit allows.

## Probe adjustment (iac × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
