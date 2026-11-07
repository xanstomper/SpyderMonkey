# 8.2 Helpdesk trust model (score 60, documentation only)

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- bindings: **WSTG-ATHN-08** · **CWE-521** · **ATT&CK T1110**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Public-facing support channels, documented identity-verification requirements (or their
  absence), password-reset-over-phone policy in public docs.
- Findings are PROSE ratings: "helpdesk reset requires account number only = MFA bypass
  exposure" — no contact is ever made.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
