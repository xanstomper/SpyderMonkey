# Turnstile harvesting — aws / machine

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- base technique: `holyshit-mode-case-apimart-newapi-fork-turnstile-harvesting.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **aws** · auth **machine** · chain role **final**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Headless Playwright (firefox) often fails to render the widget:
`[Cloudflare Turnstile] Unable to find onload callback 'onloadTurnstileCallback'`. The target's own
integration can be half-broken — if the widget never mints tokens for real users either,
server-side enforcement may be flaky. Test `?turnstile=garbage` once the rate limit allows.

## Probe adjustment (aws × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
